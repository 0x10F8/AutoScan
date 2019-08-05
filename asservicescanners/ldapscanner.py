from asservicescanners.abstractscanner import AbstractScanner
from asservicescanners.serviceutils import LDAP_PORT, LDAP_SCRIPT, launch_script_without_terminal, launch_terminal, format_script_args
from aslogging import aslog


class LDAPScanner(AbstractScanner):

    def __init__(self, ip, output_dir):
        super().__init__(ip, output_dir, LDAP_PORT)

    def scan(self):
        aslog.log("Found ldap server - starting scans")
        launch_script_without_terminal(LDAP_SCRIPT, format_script_args(
            self.ip, self.output_dir))
