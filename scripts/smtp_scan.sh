#!/bin/bash

nmap --script="smtp* and not brute" $1 | tee $2