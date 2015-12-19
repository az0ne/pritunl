COUNT = 15000
MONGO_URI = 'mongodb://localhost:27017/pritunl'
ORG_ID = '5674466ab0e7305d8bd57657'

import pymongo
import bson

client = pymongo.MongoClient(MONGO_URI)
db = client.get_default_database()
collection = db.users

for i in xrange(COUNT):
    doc = {
        "_id" : bson.ObjectId(),
        "private_key" : "-----BEGIN PRIVATE KEY-----\n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\npNBX3ac4OuXtNS650auhfydt22/7\n-----END PRIVATE KEY-----",
        "otp_secret" : "EV7QKZJHHPDOP4VB",
        "name" : "user_" + str(i).zfill(6),
        "certificate" : "Certificate:\n    Data:\n        Version: 3 (0x2)\n        Serial Number: 1 (0x1)\n    Signature Algorithm: sha256WithRSAEncryption\n        Issuer: O=5514297db0e7302d926f7a43, CN=5514297db0e7302d926f7a47\n        Validity\n            Not Before: May 15 07:38:33 2015 GMT\n            Not After : May 14 07:38:33 2025 GMT\n        Subject: O=5514297db0e7302d926f7a43, CN=5555a2770640fd63fbbf47f7\n        Subject Public Key Info:\n            Public Key Algorithm: rsaEncryption\n                Public-Key: (4096 bit)\n                Modulus:\n                    00:de:3b:50:af:87:ef:f8:92:bb:b9:c3:85:c6:08:\n                    40:15:12:0a:5c:91:e1:f1:f5:cd:79:21:10:92:a3:\n                    84:da:fd:8b:2d:e4:ec:ef:e1:43:6f:2b:8c:de:be:\n                    30:21:27:02:87:2d:f9:67:48:2b:a5:c1:9f:b8:8a:\n                    e2:65:c4:33:22:75:3c:e4:65:23:c8:65:ef:ce:13:\n                    a1:18:94:1e:ac:0e:7d:63:5c:78:51:c2:7b:73:94:\n                    25:69:a2:b5:73:36:1e:93:25:dc:60:81:1a:92:12:\n                    9c:20:20:ef:0f:e8:41:3d:cb:73:36:4d:75:c0:db:\n                    ab:cb:93:60:9c:aa:4a:50:77:d6:86:68:26:c3:d0:\n                    68:3f:d1:01:c1:b3:6e:a5:c1:de:df:5f:cc:d9:b9:\n                    6e:fa:8d:aa:5d:7a:e5:0d:40:89:30:46:e1:b6:25:\n                    65:7f:ba:f6:28:8d:9c:13:c6:2a:c2:e2:e2:ab:f4:\n                    ac:70:e0:19:49:a3:37:84:c2:bd:62:a4:55:c6:43:\n                    47:ad:47:b9:89:53:38:68:b3:35:92:73:1b:4d:3e:\n                    cf:e0:11:a0:65:d9:bd:24:fa:27:7e:67:74:d1:08:\n                    75:e2:d8:88:24:bb:ba:99:ce:28:7a:29:37:b5:d4:\n                    26:d5:e2:0b:74:24:12:44:ff:d9:e4:62:e9:36:40:\n                    bc:cc:1b:cb:48:0f:ca:a1:87:37:da:55:b3:9d:54:\n                    ac:06:ad:1f:fb:e4:d8:0c:e5:dc:ea:91:c0:19:fb:\n                    11:fd:b6:6a:f3:7e:44:1b:d5:b9:64:5c:4c:ef:9c:\n                    5b:22:85:09:61:15:70:7b:49:f2:52:bd:fa:4c:2d:\n                    eb:45:f3:2f:5e:90:a0:89:05:78:0f:be:8e:d9:37:\n                    39:60:ea:43:4a:3a:57:84:63:de:36:b8:dd:ac:f8:\n                    81:e7:67:9c:41:ce:c6:5c:5c:77:1b:21:56:e8:02:\n                    6e:89:f9:a4:df:3d:36:ba:69:ca:65:72:34:ab:09:\n                    c1:77:0e:b7:52:ef:3b:f9:a8:ae:64:12:75:6d:65:\n                    1d:3f:db:c5:65:8d:b1:80:66:51:1f:b2:0f:db:6d:\n                    a2:96:18:fe:f9:06:27:78:15:d8:14:6c:65:59:e3:\n                    63:e1:c5:97:74:93:a1:9c:57:0f:45:02:a0:3b:0c:\n                    46:aa:b2:b3:c9:f8:b8:c7:49:ef:ef:86:3b:2d:d7:\n                    c9:66:20:53:5d:d3:a6:f5:25:46:bf:55:bb:eb:f8:\n                    3b:9d:a1:7a:57:50:35:ce:8d:a3:3f:5e:1c:55:6b:\n                    40:06:85:ad:5b:1f:cf:7f:dc:65:76:46:18:c2:de:\n                    b7:a5:6d:fe:3a:37:25:19:5e:81:43:f0:be:47:b2:\n                    95:80:dd\n                Exponent: 65537 (0x10001)\n        X509v3 extensions:\n            X509v3 Key Usage: critical\n                Digital Signature, Key Encipherment\n            X509v3 Basic Constraints: \n                CA:FALSE\n            X509v3 Extended Key Usage: \n                TLS Web Client Authentication\n            X509v3 Subject Key Identifier: \n                A4:75:2F:C7:A7:E0:AA:B1:AE:05:20:86:86:23:1F:D1:1A:AB:73:F0\n            X509v3 Authority Key Identifier: \n                keyid:13:E4:E8:5F:D7:E8:BD:84:74:3A:A3:AD:46:22:DF:B5:64:58:25:F2\n\n    Signature Algorithm: sha256WithRSAEncryption\n         a4:0f:fc:07:4d:f7:a7:50:3f:a6:aa:2e:a1:ab:32:51:64:20:\n         c1:32:b5:b8:12:63:77:e9:16:d1:c7:a4:42:1a:e6:4b:79:bf:\n         16:9b:d7:ab:66:3b:44:d4:1a:7d:01:75:e1:c7:e6:5f:09:97:\n         8d:42:60:e6:8f:a1:2a:79:0b:16:e2:32:e6:cc:25:eb:df:72:\n         f0:e5:ed:4f:24:7e:4d:d1:5a:50:e9:c0:54:e5:4d:68:e9:14:\n         61:e3:03:74:55:35:55:f5:4b:96:21:04:c7:db:8a:60:ce:87:\n         13:62:a0:1d:e2:98:8e:74:3d:93:20:11:ef:c9:93:71:c1:3e:\n         62:75:a6:93:f3:5a:02:92:a8:43:4a:77:44:c8:47:2f:a4:4d:\n         6c:02:09:f8:a9:05:d9:bc:11:59:bc:ca:40:f5:22:90:82:38:\n         3a:ef:79:18:8c:b3:a3:d5:d2:ae:14:bf:62:7d:9b:47:8a:b2:\n         19:1b:fd:ae:55:67:92:0b:fe:75:1b:b1:07:7c:89:a5:1a:ab:\n         c9:55:66:00:3a:df:0b:ed:82:f2:42:78:9e:45:0f:14:7e:ec:\n         04:9a:ed:93:e9:82:92:6f:a0:d1:da:92:af:7c:8c:e8:9e:05:\n         98:34:be:12:e7:bc:16:d2:fb:2a:a4:ad:c1:f8:ae:b9:f1:20:\n         74:76:d8:39:80:74:fb:e8:69:00:b3:d6:03:2c:84:48:85:aa:\n         0d:0f:51:d0:b4:99:20:08:bc:9b:1f:a0:e4:94:bd:9d:e3:9c:\n         0c:fb:5c:61:6a:f4:fc:a2:81:da:19:64:f7:d4:5b:a1:63:eb:\n         c6:13:19:b7:ff:bc:0f:63:93:32:69:1c:89:d8:54:ea:52:e8:\n         b2:27:15:f2:0d:d8:8a:58:55:1f:92:6d:b4:d5:f5:2b:d5:2a:\n         28:2d:82:d6:22:19:b4:fe:d8:a5:b7:a4:7a:16:c5:e4:21:b1:\n         a4:21:8d:fa:1e:ce:89:68:17:ad:84:c1:68:e2:56:d8:5c:06:\n         1a:ee:ad:61:f3:a8:d1:a2:f1:21:a8:b0:38:18:f9:1d:39:9c:\n         83:e0:d3:55:80:18:8f:34:b9:12:1c:d8:63:2b:9d:ec:53:e7:\n         e9:41:c3:30:d1:42:5d:bd:65:66:0c:f2:14:51:b3:19:48:2e:\n         7a:19:78:db:6f:49:73:0d:04:e9:58:09:73:58:51:bf:a2:50:\n         15:05:ca:2f:58:46:ac:6f:bf:cd:41:b3:71:4c:11:28:b0:9a:\n         c5:12:d6:2b:5a:20:e0:50:6c:c2:62:c7:b1:98:02:bd:f2:52:\n         56:d7:60:d6:f5:54:40:a3:61:69:bf:cb:fd:6b:52:0c:e3:1f:\n         35:48:4d:b2:8f:99:77:ec\n-----BEGIN CERTIFICATE-----\nMIIFeTCCA2GgAwIBAgIBATANBgkqhkiG9w0BAQsFADBGMSEwHwYDVQQKDBg1NTE0\nMjk3ZGIwZTczMDJkOTI2ZjdhNDMxITAfBgNVBAMMGDU1MTQyOTdkYjBlNzMwMmQ5\nMjZmN2E0NzAeFw0xNTA1MTUwNzM4MzNaFw0yNTA1MTQwNzM4MzNaMEYxITAfBgNV\nBAoMGDU1MTQyOTdkYjBlNzMwMmQ5MjZmN2E0MzEhMB8GA1UEAwwYNTU1NWEyNzcw\nNjQwZmQ2M2ZiYmY0N2Y3MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA\n3jtQr4fv+JK7ucOFxghAFRIKXJHh8fXNeSEQkqOE2v2LLeTs7+FDbyuM3r4wIScC\nhy35Z0grpcGfuIriZcQzInU85GUjyGXvzhOhGJQerA59Y1x4UcJ7c5QlaaK1czYe\nkyXcYIEakhKcICDvD+hBPctzNk11wNury5NgnKpKUHfWhmgmw9BoP9EBwbNupcHe\n31/M2blu+o2qXXrlDUCJMEbhtiVlf7r2KI2cE8YqwuLiq/SscOAZSaM3hMK9YqRV\nxkNHrUe5iVM4aLM1knMbTT7P4BGgZdm9JPonfmd00Qh14tiIJLu6mc4oeik3tdQm\n1eILdCQSRP/Z5GLpNkC8zBvLSA/KoYc32lWznVSsBq0f++TYDOXc6pHAGfsR/bZq\n835EG9W5ZFxM75xbIoUJYRVwe0nyUr36TC3rRfMvXpCgiQV4D76O2Tc5YOpDSjpX\nhGPeNrjdrPiB52ecQc7GXFx3GyFW6AJuifmk3z02umnKZXI0qwnBdw63Uu87+aiu\nZBJ1bWUdP9vFZY2xgGZRH7IP222ilhj++QYneBXYFGxlWeNj4cWXdJOhnFcPRQKg\nOwxGqrKzyfi4x0nv74Y7LdfJZiBTXdOm9SVGv1W76/g7naF6V1A1zo2jP14cVWtA\nBoWtWx/Pf9xldkYYwt63pW3+OjclGV6BQ/C+R7KVgN0CAwEAAaNyMHAwDgYDVR0P\nAQH/BAQDAgWgMAkGA1UdEwQCMAAwEwYDVR0lBAwwCgYIKwYBBQUHAwIwHQYDVR0O\nBBYEFKR1L8en4KqxrgUghoYjH9Eaq3PwMB8GA1UdIwQYMBaAFBPk6F/X6L2EdDqj\nrUYi37VkWCXyMA0GCSqGSIb3DQEBCwUAA4ICAQCkD/wHTfenUD+mqi6hqzJRZCDB\nMrW4EmN36RbRx6RCGuZLeb8Wm9erZjtE1Bp9AXXhx+ZfCZeNQmDmj6EqeQsW4jLm\nzCXr33Lw5e1PJH5N0VpQ6cBU5U1o6RRh4wN0VTVV9UuWIQTH24pgzocTYqAd4piO\ndD2TIBHvyZNxwT5idaaT81oCkqhDSndEyEcvpE1sAgn4qQXZvBFZvMpA9SKQgjg6\n73kYjLOj1dKuFL9ifZtHirIZG/2uVWeSC/51G7EHfImlGqvJVWYAOt8L7YLyQnie\nRQ8UfuwEmu2T6YKSb6DR2pKvfIzongWYNL4S57wW0vsqpK3B+K658SB0dtg5gHT7\n6GkAs9YDLIRIhaoND1HQtJkgCLybH6DklL2d45wM+1xhavT8ooHaGWT31FuhY+vG\nExm3/7wPY5MyaRyJ2FTqUuiyJxXyDdiKWFUfkm201fUr1SooLYLWIhm0/tilt6R6\nFsXkIbGkIY36Hs6JaBethMFo4lbYXAYa7q1h86jRovEhqLA4GPkdOZyD4NNVgBiP\nNLkSHNhjK53sU+fpQcMw0UJdvWVmDPIUUbMZSC56GXjbb0lzDQTpWAlzWFG/olAV\nBcovWEasb7/NQbNxTBEosJrFEtYrWiDgUGzCYsexmAK98lJW12DW9VRAo2Fpv8v9\na1IM4x81SE2yj5l37A==\n-----END CERTIFICATE-----",
        "resource_id" : None,
        "link_server_id" : None,
        "dns_suffix": None,
        "sync_secret" : "livSR5Ved0DTeK6yrtC7hWv2fI5w2gf3",
        "org_id" : bson.ObjectId(ORG_ID),
        "disabled" : False,
        "bypass_secondary": False,
        "sync_token" : "kVd5DKrRne30vJXhbh0LVWSHphigbGuF",
        "type" : "client",
        "email" : None,
    }

    collection.insert_one(doc)