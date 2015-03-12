#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, re, os, sys

class ServiceNowClassWriter():	
	"""Searches through ServiceNow to get script data"""
	def __init__(self, username, password, instance, buildType):
		self.username = username
		self.password = password
		self.instance = instance
		self.type = buildType
		print 'Hello from ServiceNow Instance ' + instance

	def getDataFromServiceNow(self):
		if self.type == 'model':
			tableName = 'u_model_class_generator'
		elif self.type == 'selenium':
			tableName = 'class_generator'
		r = requests.get('https://' + self.instance + '.service-now.com/' + tableName + '.do?JSON', auth=(self.username, self.password))
		if r.status_code == 200:
			data = (r.json()['records'])		
			return data
		else:
			print "Server returned a status code of: " + str(r.status_code) + ".  Please ensure you entered the correct data." + "\n" + "usage: scriptname username password instance"
			sys.exit(2)


	def writeFile(self, data):
		if not os.path.exists(self.type):
			os.mkdir(self.type)
		for x in range(0, len(data)):
			filename = re.sub(r"_", "", data[x]['u_tablename'].title())
			if self.type == 'model':
				filename = re.sub(r"collection", "Collection", filename)
			with open(self.type + "\\" + filename + '.java', 'w+') as writer:				
				self.handleWriting(data[x], writer)
			
	def handleWriting(self, data, writer):		
		text = data['u_class_body']		
		text = text.encode('utf-8')
		writer.write(text)