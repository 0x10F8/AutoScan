#!/bin/bash

nikto -h https://$1 | tee $2/niktoscan_https.txt