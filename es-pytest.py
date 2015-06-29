import requests
import json

query_starts_with = "http://ec2-54-164-33-1.compute-1.amazonaws.com:9200/_search"

query_params = [
	"?q=content:collecting&size=1",
	"?q=content:collecting&size=4",
	"?q=content:collecting&size=16",
	"?q=content:collecting&size=64",
	"?q=content:collecting&size=256",

	"?q=sense_id:EE2349F25AF33D11&size=1",
	"?q=sense_id:EE2349F25AF33D11&size=4",
	"?q=sense_id:EE2349F25AF33D11&size=16",
	"?q=sense_id:EE2349F25AF33D11&size=64",
	"?q=sense_id:EE2349F25AF33D11&size=256",

	"?q=timestamp:[1435282800000+TO+1435369249143]",
	"?q=timestamp:[1435282800000+TO+1435369249143]%20AND%20content:Ouya",
	"?q=sense_id:DBCCFD2D1368BCC9%20OR%2009EA5FA90F9FE48E",
	"?q=sense_id:8AA455AB97CE1CD8%20NOT%20content:Ouya"
]

print "\nQuery\tSuccess\tTakeTime"


sorting_order = {"sort": {"timestamp": "desc"}}
for p in query_params:
	r = requests.post(url=query_starts_with + p, data=json.dumps(sorting_order))
	print "{}\t{}\t{}".format(p, r.ok, r.json()['took'] or "timed out")
