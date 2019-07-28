from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import VNC_PORT, VNC_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class VNCScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, VNC_PORT)

    def scan(self):
        aslog.log("Found vnc server - starting scans")
        launch_terminal(VNC_SCRIPT, format_script_args(
            self.ip, self.output_dir))
