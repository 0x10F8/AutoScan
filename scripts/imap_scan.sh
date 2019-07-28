#!/bin/bash

nmap --script="imap* and not brute" $1 | tee $2