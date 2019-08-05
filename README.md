# AutoScan
Python script which will do some useful nmap scans, and trigger additional scans depending on which ports it finds open.

This script is designed to work within Kali linux but theoretically it will work in any Linux using gnome-terminal.

The HTTP scripts rely on dirsearch being available in the location specified in the script, you will need to check this out into the correct directory or update the ./scripts/dirsearch.sh script.

The script should work with proxy chains except the UDP based scan.
