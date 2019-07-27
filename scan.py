#!/usr/bin/python3
import sys
import os
import subprocess
import shlex
import time

END_OF_NMAP_SCAN = "Nmap done:"

# Format string for shell spawning, argument 0 is the script and 1 is the args
spawn_shell_frmt = 'gnome-terminal -q -- /bin/bash -c "{0} {1}"'

# The scripts resources dir
scripts_dir = "{0}/scripts".format(os.getcwd())


def get_script(script_name):
    return "{0}/{1}".format(scripts_dir, script_name)


# Some basic initial scans that will be started for everyone
basic_scan_script = get_script("basic_scan.sh")
tcp_scan_script = get_script("tcp_scan.sh")
udp_scan_script = get_script("udp_scan.sh")
initial_scans = [basic_scan_script, tcp_scan_script, udp_scan_script]

# HTTP scan scripts
nikto_script = get_script("nikto_scan.sh")
dirsearch_script = get_script("dirsearch.sh")

# SMB scan scripts
smb_script = get_script("smb_scan.sh")

# SMTP scan scripts
smtp_script = get_script("smtp_scan.sh")

# POP3 scan scripts
pop3_script = get_script("pop3_scan.sh")

def log(string):
    print("[+] {0}".format(string))


def format_script_args(ip, dir):
    return "{0} {1}".format(ip, dir)


def launch_terminal(script, script_args, keep_open=False):
    if keep_open:
        script_args += " && /bin/bash"
    args = shlex.split(spawn_shell_frmt.format(script, script_args))
    subprocess.Popen(args)

def scrape_banner(ip_address, port, timeout=10):
    try:
        with(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.settimeout(timeout)
            s.connect((ip_address, port))
            banner = s.recv(1024)
            return banner.decode('ascii')
    except:
        log("Unable to scrape banner from {0}:{1}".format(ip_address, port))
        pass

def do_smtp_scans(ip, dir):
    log("Found smtp server - starting scans")
    launch_terminal(smtp_script, format_script_args(ip, dir))
    log("Trying to scrape SMTP banner")
    banner = scrape_banner(ip, 25)
    with open("{0}/smtpbanner.txt".format(dir), "w") as banner_output:
        banner_output.write(banner)

def do_pop3_scans(ip, dir):
    log("Found pop3 server - starting scans")
    launch_terminal(pop3_script, format_script_args(ip, dir))
    log("Trying to scrape POP3 banner")
    banner = scrape_banner(ip, 110)
    with open("{0}/pop3banner.txt".format(dir), "w") as banner_output:
        banner_output.write(banner)


def do_http_scans(ip, dir):
    log("Found http server - starting nikto and dirsearch")
    launch_terminal(nikto_script, format_script_args(ip, dir))
    launch_terminal(dirsearch_script, ip, keep_open=True)


def do_smb_scans(ip, dir):
    log("Found smb server - starting enumeration")
    launch_terminal(smb_script, format_script_args(ip, dir))


def start_initial_scans(ip, dir):
    log("Launching initial port scans")
    for scan_script in initial_scans:
        launch_terminal(scan_script, format_script_args(ip, dir))


def get_basic_scan(dir):
    # Wait for the basic scan to complete to kick off other scans
    basic_scan_output = "{0}/basicscan.txt".format(dir)
    log("Waiting for basic scan to complete")
    scan_complete = False
    while not scan_complete:
        scan_lines = []
        if os.path.isfile(basic_scan_output):
            with open(basic_scan_output, "r") as scan_output:
                scan_lines = scan_output.readlines()
                for line in scan_lines:
                    if line.startswith(END_OF_NMAP_SCAN):
                        scan_complete = True
        else:
            time.sleep(1)
    return scan_lines


# Scan result to extra scans
service_map = {
    "25/tcp": do_smtp_scans,
    "80/tcp": do_http_scans,
    "110/tcp": do_pop3_scans,
    "445/tcp": do_smb_scans
}

# Parse arguments
if len(sys.argv) < 2:
    print("Usage: {0} [target_ip]".format(sys.argv[0]))
    exit(1)

# Get the target ip
target_ip = sys.argv[1]
output_dir = "{0}/{1}/".format(os.getcwd(), target_ip)

# Create a directory for this ip address
os.mkdir(output_dir)

log("Scanning {0} and sending output to {1}".format(target_ip, output_dir))

# Start the initial scans
start_initial_scans(target_ip, output_dir)

# Get the initial basic scan content
basic_scan_lines = get_basic_scan(output_dir)

log("Basic scan complete, checking for common ports")

# Run extra scripts if something is found
for line in basic_scan_lines:
    for service_key in service_map.keys():
        if line.startswith(service_key):
            service_map[service_key](target_ip, output_dir)
