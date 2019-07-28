import socket
from aslogging import aslog


def scrape_banner(ip_address, port, output_file, timeout=10):
    try:
        with(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.settimeout(timeout)
            s.connect((ip_address, port))
            banner = s.recv(1024)
            if banner is not None:
                with open("{0}".format(output_file), "w") as banner_output:
                    banner_output.write(banner.decode("ascii"))
            else:
                aslog.warning_log("No banner was found")
    except Exception as e:
        aslog.warning_log(
            "Unable to scrape banner from {0}:{1} - {2}".format(ip_address, port, e))
        pass
