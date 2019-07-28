from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import BASIC_SCAN_SCRIPT, TCP_SCAN_SCRIPT, UDP_SCAN_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog
from os import path
from time import sleep


class InitialScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, 0)
        # Token which occurs in the last line of an NMAP scan
        self.END_OF_NMAP_SCAN = "Nmap done:"

    def scan(self):
        aslog.log("Launching initial port scans")
        launch_terminal(BASIC_SCAN_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(TCP_SCAN_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(UDP_SCAN_SCRIPT, format_script_args(
            self.ip, self.output_dir))

    def get_basic_scan_output(self):
        # Wait for the basic scan to complete to kick off other scans
        basic_scan_output = "{0}/basicscan.txt".format(self.output_dir)
        aslog.warning_log("Waiting for basic scan to complete...")
        scan_complete = False
        while not scan_complete:
            scan_lines = []
            if path.isfile(basic_scan_output):
                with open(basic_scan_output, "r") as scan_output:
                    scan_lines = scan_output.readlines()
                    for line in scan_lines:
                        if line.startswith(self.END_OF_NMAP_SCAN):
                            scan_complete = True
            else:
                sleep(1)
        return scan_lines
