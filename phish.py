#!/usr/bin/env python3
import sys
import os
import time
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action", type = str, choices = ["clone", "enable"])
parser.add_argument("website", help = "website of login page you want to steal OR website of your own site")
args = parser.parse_args()

def main():
    website = args.website
    print("Attempting to contact website...")
    if website_test(website) == 0:
        print("ERROR: Could not contact website. Exiting...")
    else:
        print("Successfully contacted website")
        if args.action == "clone":
            return clone(website)
        elif args.action == "enable":
            return enable(website)
        else:
            return 0

def clone(website):
    print("Stealing login page from website...")
    subprocess.run(["wget", "--mirror", "--convert-links", "--adjust-extension", "--page-requisites", "--no-parent", website])
    print("Successfully stole website!")
def enable(website):
    print("Uploading stolen website to personal website...")

def website_test(website):
    status = subprocess.run(
    ['ping', '-q', '-c', '3', website],
    stdout=subprocess.DEVNULL)
    if status == 0:
        return 0
    else:
        return -1

if __name__ == "__main__":
    main()
