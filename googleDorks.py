#!/usr/bin/python
# -*- coding: utf-8 -*

from googlesearch import search
import requests
import optparse

def searchGoogleDork(domain, number):
	# Array of searchs
	searchs = []
	# Define the google dorks to search for
	gd_open_redirect = "site:"+domain+"  inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http"
	searchs.append(gd_open_redirect)
	gd_passwd_files = "site:"+domain+"  'password' filetype:doc | filetype:pdf | filetype:docx | filetype:xls | filetype:dat | filetype:log"
	searchs.append(gd_passwd_files)
	gd_dir_listing = "site:"+domain+"  intitle:index.of  | 'parent directory'"
	searchs.append(gd_dir_listing)
	gd_database = "site:"+domain+"  intext:'sql syntax near' | intext:'syntax error has occurred' | intext:'incorrect syntax near' | intext:'unexpected end of SQL command' | intext:'Warning: mysql_connect()' | intext:'Warning: mysql_query() | intext:'Warning: pg_connect()' | filetype:sqlext:sql | ext:dbf | ext:mdb"
	searchs.append(gd_database)
	gd_config_log_files = "site:"+domain+"  ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:log"
	searchs.append(gd_config_log_files)
	gd_backup_files = "site:"+domain+"  ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
	searchs.append(gd_backup_files)
	gd_login_pages = "site:"+domain+"  inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth"
	searchs.append(gd_login_pages)
	gd_phpinfo = "site:"+domain+"  ext:php intitle:phpinfo 'published by the PHP Group'"
	searchs.append(gd_phpinfo)
	gd_subdomains = "site:*."+domain
	searchs.append(gd_subdomains)
	gd_aws = "site:.s3.amazonaws.com '"+domain+"'"
	searchs.append(gd_aws)
	gd_stackoverflow = "site:stackoverflow.com '"+domain+"'"
	searchs.append(gd_stackoverflow)
	gd_paste_sites = "site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com '"+domain+"'"
	searchs.append(gd_paste_sites)
	gd_wordpress_content = "site:"+domain+"  inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"
	searchs.append(gd_wordpress_content)
	gd_vulnerable_site = "site:"+domain+"  inurl:php?=id1 | inurl:index.php?id= | inurl:pageid= | inurl:.php?"
	searchs.append(gd_vulnerable_site)

	# Insert into array to for every search
	f = open("googleDorks.txt", 'w+')
	logs = open("logs.txt", 'a+')
	n = 0
	for query in searchs:
		for i in search(query, num_results=number):
			try:
				print(i)
				n += 1
				f.write(i + "\n")
			except e:
				logs.write(e)
				continue
	f.close()
	print("There are " + str(n) + " positive GoogleDorks")

def main():
	parser = optparse.OptionParser("%prog -d domain [-n number] ")
	parser.add_option("-d", dest='domain', type='string',\
			help='specify the domain to search google dorks')
	parser.add_option("-n", dest='number', type='int',\
			help='specify the maximun number of pages to search')

	(options, args) = parser.parse_args()
	if(options.domain == None):
		print(parser.print_help())
		exit(0)
	else:
		domain = options.domain
	if(options.number == None):
		number = 100
	else:
		number = options.number

	print("Searching your goolgle dorks, be patient...")
	searchGoogleDork(str(domain), number)
	print("Search done, check the results in googleDorks.txt")

if __name__ == '__main__':
	main()

