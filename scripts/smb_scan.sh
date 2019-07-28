#!/bin/bash

nmap -p 445 --script=smb-enum* $1 | tee $2/smbnmap.txt