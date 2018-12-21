# netconf-looper
Python/PyEz loop to retrieve junos.facts from a selection of Juniper routers indefinitely during Type Approval Testing for customers

## Dependencies
- pprint
- jnpr.junos (PyEZ)
- datetime
- time


## Overview
This script is for lab testing only because it contains usernames and passwords.

It connects to port 22 using Netconf and retrieves the facts about a Junos device.  It is a pretty basic script that could use refining, but does what it needs.  When the facts are retrieved successfully, a message is appended to a log file.  This log file can be given to the customer to prove that multiple Netconf connections were made throughout the testing cycle without any exhaustion of memory on the target Junos devices etc.
