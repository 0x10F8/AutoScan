#/bin/bash

nmap -sT -p 110 --script="pop3* and not brute" $1 | tee $2/pop3scan.txt