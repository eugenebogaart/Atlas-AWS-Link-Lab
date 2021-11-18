#!/usr/bin/env python3

import srvlookup  # pip install srvlookup
import sys
import dns.resolver  # pip install dnspython

host = None

if len(sys.argv) > 1:
    host = sys.argv[1]

if host:
    services = srvlookup.lookup("mongodb", domain=host)
    for i in services:
        print("%s:%i" % (i.hostname, i.port))
    for txtRecord in dns.resolver.query(host, 'TXT'):
        print("%s: %s" % (host, txtRecord))

else:
    print("No host specified")
