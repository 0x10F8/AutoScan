#!/bin/bash

nmap -sT -p 80 --script="http-vuln*" $1 | tee $2/httpscan.txt