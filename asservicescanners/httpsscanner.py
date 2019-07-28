from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import HTTPS_PORT, HTTPS_SCRIPT, HTTPS_DIRSEARCH_SCRIPT, HTTPS_NIKTO_SCRIPT, launch_script_without_terminal, launch_terminal, format_script_args
from aslogging import aslog


class HTTPSScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, HTTPS_PORT)

    def scan(self):
        aslog.log("Found https server - starting scans")
        launch_script_without_terminal(HTTPS_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(HTTPS_NIKTO_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(HTTPS_DIRSEARCH_SCRIPT, format_script_args(
            self.ip, self.output_dir), keep_open=True)
