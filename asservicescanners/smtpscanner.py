from asservicescanners.abstractscanner import AbstractBannerScrapeScanner
from asservicescanners.serviceutils import SMTP_PORT, SMTP_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class SMTPScanner(AbstractBannerScrapeScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, SMTP_PORT)

    def scan(self):
        aslog.log("Found smtp server - starting scans")
        launch_terminal(SMTP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        aslog.log("Trying to scrape SMTP banner")
        self.scrape_banner("smtpbanner.txt")
