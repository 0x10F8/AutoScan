#!/bin/bash

nmap -sT -p 5900 --script="vnc* and not brute" $1 | tee $2/vncscan.txt