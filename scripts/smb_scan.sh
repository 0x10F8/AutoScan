#!/bin/bash

nmap -sT -p 445 --script=smb-enum* $1 | tee $2/smbnmap.txt
nmap -sT --script=smb-vuln* $1 | tee $2/smbvuln.txt