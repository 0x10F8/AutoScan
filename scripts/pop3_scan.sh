#/bin/bash

nmap --script="pop3* and not brute" $1 | tee $2