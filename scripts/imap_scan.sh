#!/bin/bash

nmap -p 143 --script="imap* and not brute" $1 | tee $2