#!/bin/bash

nmap -p 80 --script="http-vuln*" $1 | tee $2/httpscan.txt