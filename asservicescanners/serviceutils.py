from os import getcwd
from shlex import split
from subprocess import Popen, DEVNULL


def get_script(script_name):
    '''
    Get the script within the scripts resources directory
    '''
    return "{0}/{1}".format(SCRIPTS_DIR, script_name)


# The scripts resources dir
SCRIPTS_DIR = "{0}/scripts".format(getcwd())

# Format string for shell spawning, argument 0 is the script and 1 is the args
SPAWN_SHELL_FRMT = 'gnome-terminal -q -- /bin/bash -c "bash {0} {1}"'

# Format string for running scripts without terminal, argument 0 is the script and 1 is the args
RUN_SCRIPT_FRMT = '/bin/bash {0} {1}'

# -------------------------
# Service scripts and ports
# -------------------------

# Initial scan scripts
BASIC_SCAN_SCRIPT = get_script("basic_scan.sh")
TCP_SCAN_SCRIPT = get_script("tcp_scan.sh")
UDP_SCAN_SCRIPT = get_script("udp_scan.sh")

# FTP Info
FTP_PORT = 21
FTP_SCRIPT = get_script("ftp_scan.sh")

# SSH Info
SSH_PORT = 22
SSH_SCRIPT = get_script("ssh_scan.sh")

# SMTP Info
SMTP_PORT = 25
SMTP_SCRIPT = get_script("smtp_scan.sh")


# IMAP Info
IMAP_PORT = 143
IMAP_SCRIPT = get_script("imap_scan.sh")

# HTTP Info
HTTP_PORT = 80
HTTP_SCRIPT = get_script("http_scan.sh")
HTTP_NIKTO_SCRIPT = get_script("nikto_scan.sh")
HTTP_DIRSEARCH_SCRIPT = get_script("dirsearch.sh")

# HTTPS Info
HTTPS_PORT = 443
HTTPS_SCRIPT = get_script("https_scan.sh")
HTTPS_NIKTO_SCRIPT = get_script("nikto_scan_https.sh")
HTTPS_DIRSEARCH_SCRIPT = get_script("dirsearch_https.sh")

# SMB Info
SMB_PORT = 445
SMB_SCRIPT = get_script("smb_scan.sh")

# POP3 Info
POP3_PORT = 110
POP3_SCRIPT = get_script("pop3_scan.sh")

# VNC Info
VNC_PORT = 5900
VNC_SCRIPT = get_script("vnc_scan.sh")


def format_script_args(ip, dir):
    return "{0} {1}".format(ip, dir)


def launch_terminal(script, script_args, keep_open=False):
    if keep_open:
        script_args += " && /bin/bash"
    args = split(SPAWN_SHELL_FRMT.format(script, script_args))
    Popen(args)


def launch_script_without_terminal(script, script_args, wait=True):
    args = split(RUN_SCRIPT_FRMT.format(script, script_args))
    process = Popen(args, stdout=DEVNULL, stderr=DEVNULL)
    if wait:
        process.wait()
