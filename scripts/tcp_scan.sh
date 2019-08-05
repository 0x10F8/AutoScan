#!/bin/bash

nmap -sT -A -sC -sV -p- $1 | tee $2/portscan.txt