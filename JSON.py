facts =  {
         "inventory": {
             "device": [
                 {
                     "name": "csr1kv1",
                     "version": "16.09",
                     "vendor": "cisco",
                     "uptime": "2 days",
                     "serial": "XB96861",
                     "snmp": [
                         {"name": "public", "permission": "ro"},
                         {"name": "private", "permission": "rw"}
                     ]
                 }
             ]
         }
     }

print(type(facts))
print(facts['inventory']['device'][0]['uptime'])