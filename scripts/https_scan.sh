#!/bin/bash

nmap -sT -p 443 --script="http-vuln*" $1 | tee $2/httpsscan.txt