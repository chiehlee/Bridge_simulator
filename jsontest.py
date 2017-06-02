#!/usr/bin/env python
import json

data = json.loads('{"source":"d5b5","dest":"0aa8","message":{"id":3},"type":"data"}')

print data
print data['dest']
print data['message']
id = data['message']
print id['id']
print type(data)
s = "d5b5"
d = "0aa83"
bpdu = {"source":"02a1", "dest":"ffff", "type": "bpdu", 
		"message":{"id":"92b4", "root":"02a1", "cost":3}}

print "bpdu:", bpdu
print "type(bpdu): ", type(bpdu)
print "bpdu['message']['id']: ", bpdu['message']['id']

tt = json.dumps(bpdu)
print tt
print type(tt)






