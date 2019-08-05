#!/bin/bash
nmap -p 389 --script="ldap* and not brute" $1 | tee $2