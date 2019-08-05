#!/bin/bash

nmap -sT -p 21 --script="ftp* and not brute" $1 | tee $2/ftpscan.txt