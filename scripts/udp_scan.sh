#!/bin/bash

nmap -sU $1 | tee $2/udpscan.txt