#!/usr/bin/env python
"""Nagios module for monitoring available updates via slackpkg."""

import subprocess
import sys
import os

# pylint: disable=invalid-name

# run check-updates to poll mirror for changes
result = []
try:
    result = subprocess.check_output("myslackpkg check-updates", shell=True).split("\n")
except (OSError, subprocess.CalledProcessError) as error:
    print "Failed to check for updates: %s" % error
    sys.exit(3)

updates = "idk"
for line in result:
    if "good news" in line:
        updates = "no"
    elif "News on" in line:
        updates = "yes"
if updates == "idk":
    print "Error parsing slackpkg check-updates status"
    sys.exit(3)
elif updates == "yes":
    # fetch updated package list
    devnull = open(os.devnull, 'w')
    try:
        subprocess.check_call("myslackpkg update", stdout=devnull, shell=True)
    except (OSError, subprocess.CalledProcessError) as error:
        print "Failed to update package list: %s" % error
        sys.exit(3)

# Now the packages list is up to date, check if we need to upgrade anything
result = []
devnull = open(os.devnull, 'w')
try:
    result = subprocess.check_output([
        "myslackpkg",
        "upgrade-all"], stderr=devnull).split("\n")
except (OSError, subprocess.CalledProcessError) as error:
    print "Failed to check for upgrades: %s" % error
    sys.exit(3)

packages = []
for line in result:
    if ".txz" in line:
        packages.append(line.strip())
    if "update gpg" in line:
        print "Error: need up-to-date gpg key!"
        sys.exit(3)

if len(packages) == 0:
    print "OK: everything up-to-date"
    sys.exit(0)
else:
    print "Updates available: " + " ".join(packages)
    sys.exit(2)
