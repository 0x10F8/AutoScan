#!/bin/bash

nmap -sT -p 143 --script="imap* and not brute" $1 | tee $2/imapscan.txt