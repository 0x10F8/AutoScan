#!/bin/bash

nmap -p 3389 --script="rdp*" $1 | tee $2/rdpscan.txt