from abc import ABC, abstractmethod
from asservicescanners.bannerscraper import scrape_banner


class AbstractScanner(ABC):

    def __init__(self, ip, output_dir, port):
        self.ip = ip
        self.output_dir = output_dir
        self.port = port
    
    @abstractmethod
    def scan(self):
        return NotImplemented

class AbstractBannerScrapeScanner(AbstractScanner):
    
    def __init__(self, ip, output_dir, port):
        super().__init__(ip, output_dir, port)
        
    def scrape_banner(self, output_file):
        scrape_banner(self.ip, self.port, "{0}/{1}".format(self.output_dir, output_file))
