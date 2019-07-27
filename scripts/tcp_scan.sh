#!/bin/bash

nmap -A -sC -sV -p- $1 | tee $2/portscan.txt