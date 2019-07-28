from asservicescanners.abstractscanner import AbstractBannerScrapeScanner
from asservicescanners.serviceutils import SSH_PORT, SSH_SCRIPT, launch_script_without_terminal, format_script_args
from aslogging import aslog


class SSHScanner(AbstractBannerScrapeScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, SSH_PORT)

    def scan(self):
        aslog.log("Found ssh server - starting scans")
        launch_script_without_terminal(SSH_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        aslog.log("Trying to scrape ssh banner")
        self.scrape_banner("sshbanner.txt")
