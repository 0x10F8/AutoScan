from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import SMB_PORT, SMB_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class SMBScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, SMB_PORT)

    def scan(self):
        aslog.log("Found smb server - starting scans")
        launch_terminal(SMB_SCRIPT, format_script_args(
            self.ip, self.output_dir))
