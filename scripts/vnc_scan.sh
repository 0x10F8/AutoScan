#!/bin/bash

nmap --script="vnc* and not brute" $1 | tee $2