#!/bin/bash

nmap -sT -p 25 --script="smtp* and not brute" $1 | tee $2/smtpscan.txt