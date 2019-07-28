from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import HTTP_PORT, HTTP_SCRIPT, HTTP_DIRSEARCH_SCRIPT, HTTP_NIKTO_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class HTTPScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, HTTP_PORT)

    def scan(self):
        aslog.log("Found http server - starting scans")
        launch_terminal(HTTP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(HTTP_NIKTO_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        launch_terminal(HTTP_DIRSEARCH_SCRIPT, format_script_args(
            self.ip, self.output_dir), keep_open=True)
