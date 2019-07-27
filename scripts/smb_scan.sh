#!/bin/bash

nmap --script=smb-enum* $1 | tee $2/smbnmap.txt