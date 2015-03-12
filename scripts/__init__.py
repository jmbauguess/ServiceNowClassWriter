#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ServiceNowClassWriter import ServiceNowClassWriter
import sys

def main():
	if (len(sys.argv) < 2):
		print "Please enter arguments with this script: serviceNow.py username password instance type (model or selenium)"
		sys.exit(2)
	serviceNow = ServiceNowClassWriter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	data = serviceNow.getDataFromServiceNow()
	serviceNow.writeFile(data)

if __name__ == "__main__":
   main()