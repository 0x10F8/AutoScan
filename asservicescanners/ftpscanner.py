from asservicescanners.abstractscanner import AbstractBannerScrapeScanner
from asservicescanners.serviceutils import FTP_PORT, FTP_SCRIPT, launch_terminal, format_script_args
from aslogging import aslog


class FTPScanner(AbstractBannerScrapeScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, FTP_PORT)

    def scan(self):
        aslog.log("Found ftp server - starting scans")
        launch_terminal(FTP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
        aslog.log("Trying to scrape FTP banner")
        self.scrape_banner("ftpbanner.txt")
