#!/bin/bash

nmap -p 22 --script="ssh* and not brute" $1 | tee $2/sshscan.txt