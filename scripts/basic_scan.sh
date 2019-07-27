#!/bin/bash

nmap $1 | tee $2/basicscan.txt