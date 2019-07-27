#!/bin/bash

nikto -h http://$1 | tee $2/niktoscan.txt