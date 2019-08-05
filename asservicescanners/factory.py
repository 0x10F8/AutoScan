from asservicescanners.smtpscanner import SMTPScanner
from asservicescanners.httpscanner import HTTPScanner
from asservicescanners.smbscanner import SMBScanner
from asservicescanners.pop3scanner import POP3Scanner
from asservicescanners.vncscanner import VNCScanner
from asservicescanners.imapscanner import IMAPScanner
from asservicescanners.sshscanner import SSHScanner
from asservicescanners.ftpscanner import FTPScanner
from asservicescanners.httpsscanner import HTTPSScanner
from asservicescanners.rdpscanner import RDPScanner
from asservicescanners.ldapscanner import LDAPScanner

def build_service_factory(ip, output_dir):
    # Mapping of NMAP token to the relevant scanner
    return {
        "21/tcp": FTPScanner(ip, output_dir),
        "22/tcp": SSHScanner(ip, output_dir),
        "25/tcp": SMTPScanner(ip, output_dir),
        "80/tcp": HTTPScanner(ip, output_dir),
        "110/tcp": POP3Scanner(ip, output_dir),
        "143/tcp": IMAPScanner(ip, output_dir),
        "389/tcp": LDAPScanner(ip, output_dir),
        "443/tcp": HTTPSScanner(ip, output_dir),
        "445/tcp": SMBScanner(ip, output_dir),
        "3389/tcp": RDPScanner(ip, output_dir),
        "5900/tcp": VNCScanner(ip, output_dir)
    }
