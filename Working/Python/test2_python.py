# coding: utf-8
#Here’s a python script that will fill two kinds of records into a test set:
#Half with a -1 ttl or also known as a ‘never expire’ ttl.
#Half with a 1 hour(3600 seconds) ttl.

from __future__ import print_function
import aerospike

config = { 'hosts': [('127.0.0.1', 3000)] }
client = aerospike.client(config).connect()

i = 1
while i < 100:
        client.put(('test','foo',i), {'i':i}, meta={'ttl':-1}, policy={'exists': aerospike.POLICY_EXISTS_CREATE_OR_REPLACE})
        i = i + 1

        i = 101
while i < 200:
        client.put(('test','foo',i), {'i':i, 'x':i}, meta={'ttl':3600})
        i = i + 1
