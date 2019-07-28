from asservicescanners.abstractscanner import AbstractBannerScrapeScanner
from asservicescanners.serviceutils import IMAP_PORT, IMAP_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class IMAPScanner(AbstractBannerScrapeScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, IMAP_PORT)

    def scan(self):
        aslog.log("Found imap server - starting scans")
        launch_terminal(IMAP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        aslog.log("Trying to scrape IMAP banner")
        self.scrape_banner("imapbanner.txt")