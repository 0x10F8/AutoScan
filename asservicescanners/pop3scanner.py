from asservicescanners.abstractscanner import AbstractBannerScrapeScanner
from asservicescanners.serviceutils import POP3_PORT, POP3_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class POP3Scanner(AbstractBannerScrapeScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, POP3_PORT)

    def scan(self):
        aslog.log("Found pop3 server - starting scans")
        launch_terminal(POP3_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        aslog.log("Trying to scrape POP3 banner")
        self.scrape_banner("pop3banner.txt")
