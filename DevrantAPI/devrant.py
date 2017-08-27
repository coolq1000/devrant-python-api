#! /usr/bin/python3

"""
	Devrant.io API.
	Has a way to go, only allows getting rants and userID's.
"""

import requests, json

class Devrant:

	API = 'https://www.devrant.io/api/'

	"""
		getRant(): Seems to only work to ~788.
	"""
	def getRant(self, sort, index):
		rants = self.getRants(sort, 1, index)['rants']
		if rants:
			return rants[0]

	def getRants(self, sort, limit, skip):
		url = self.API + 'devrant/rants'
		params = {
			'app': 3,
			'sort': sort,
			'limit': limit,
			'skip': skip
		}
		
		r = requests.get(url, params)
		obj = json.loads(r.text)
		return obj

	def getUserID(self, name):
		url = self.API + 'get-user-id'
		params = {
			'app': 3,
			'username': name
		}

		r = requests.get(url, params)
		return r.text
