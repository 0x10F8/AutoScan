#!/bin/bash

nmap -sT $1 | tee $2/basicscan.txt