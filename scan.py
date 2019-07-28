#!/usr/bin/python3

from aslogging import aslog
from sys import argv
from os import getcwd, mkdir, rmdir, path
from asservicescanners import factory, initialscan
from shutil import rmtree

# Parse arguments
if len(argv) < 2:
    print("Usage: {0} [target_ip]".format(argv[0]))
    exit(1)

# Get the target ip
TARGET_IP = argv[1]

# The target dir is just the IP address of the target
OUTPUT_DIR = "{0}/{1}/".format(getcwd(), TARGET_IP)

# Check if directory exists and offer to delete it
if path.isdir(OUTPUT_DIR):
    aslog.error_log("Output directory {0} already exists".format(OUTPUT_DIR))
    aslog.warning_log(
        "Do you want to remove the current directory and continue? (Y/N): ")
    answer = input()

    if answer is not None and str(answer).lower() == 'y':
        aslog.log("Removing existing directory")
        rmtree(OUTPUT_DIR)
    else:
        aslog.error_log("Unable to continue as directory already exists.")
        exit(1)

# Create a directory for this ip address
mkdir(OUTPUT_DIR)

aslog.log("Scanning {0} and sending output to {1}".format(
    TARGET_IP, OUTPUT_DIR))

# Build the service scanner factory
SERVICE_FACTORY = factory.build_service_factory(TARGET_IP, OUTPUT_DIR)

# Start the initial scans
initial_scanner = initialscan.InitialScanner(TARGET_IP, OUTPUT_DIR)
initial_scanner.scan()

# Get the initial basic scan content
basic_scan_lines = initial_scanner.get_basic_scan_output()
aslog.log("Basic scan complete, checking for common ports")

# Check the factory for any services with scanners
for line in basic_scan_lines:
    for service_token in SERVICE_FACTORY.keys():
        if line.startswith(service_token):
            SERVICE_FACTORY[service_token].scan()
