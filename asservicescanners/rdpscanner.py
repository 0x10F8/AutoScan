from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import RDP_PORT, RDP_SCRIPT, launch_script_without_terminal, launch_terminal, format_script_args
from aslogging import aslog


class RDPScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, RDP_PORT)

    def scan(self):
        aslog.log("Found rdp server - starting scans")
        launch_script_without_terminal(RDP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
