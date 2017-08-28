#! /usr/bin/python3

"""
	Devrant.io API. Written by Rohan Burke (coolq).
"""

import requests, json

class Devrant:

	API = 'https://www.devrant.io/api/'

	"""
		get_profile(id):
			Return JSON object with all information about that user.
	"""
	def get_profile(self, id_):
		url = self.API + 'users/' + str(id_)
		params = {
			'app': 3,
		}

		r = requests.get(url, params)
		obj = json.loads(r.text)
		return obj

	"""
		get_search(term):
			Return JSON object containing all results of that search. Index ['rants'] for rants.
	"""
	def get_search(self, term):
		url = self.API + 'devrant/search'
		params = {
			'app': 3,
			'term': term
		}
		
		r = requests.get(url, params)
		obj = json.loads(r.text)
		return obj

	"""
		get_rant(sort, index):
			Return JSON object of that rant.
	"""
	def get_rant(self, sort, index):
		rants = self.get_rants(sort, 1, index)['rants']
		if rants:
			return rants[0]

	"""
		get_rants(sort, limit, skip):
			Return JSON object with range skip-limit. Max limit is 50, increase the skip to get rants further down.
	"""
	def get_rants(self, sort, limit, skip):
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

	"""
		get_user_id(name):
			Return JSON with containing the id for that user, E.g. if `coolq` is inputted, it shall return `{'success': True, 'user_id': 703149}`.
	"""
	def get_user_id(self, name):
		url = self.API + 'get-user-id'
		params = {
			'app': 3,
			'username': name
		}

		r = requests.get(url, params)
		obj = json.loads(r.text)
		return obj

if __name__ == '__main__':
	# Simple demo, runs through rants sorted by most recent.
	dr = Devrant()
	i = 0
	while True:
		result = dr.get_rant('recent', i)
		print('\n'*50)
		name = result['user_username']
		tags = ', '.join(result['tags'])
		print('-' + name + '-'*(50 - (len(name) + 1)))
		print(result['text'])
		print('-' + tags + '-'*(50 - (len(tags) + 1)))
		i += 1
