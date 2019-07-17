#news get common modul.py
# Usage import nc_common_module.py as ncm| ncm.foo(bar) | from ng_common_modul.py import foo()
# Basics: 
# 1
# 
# 
# 



#import libs
import urllib
import os
import time
from datetime import datetime
import os.path
#ssl support and context
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#Bautiful Parser load
from bs4 import BeautifulSoup
#Word counter load and init
from collections import Counter
Text_Counter = Counter()

is_news_ok_banlist = ("megöl","elhunyt","meghalt","ölt meg","halálra","Gruevszki","megöltek")




def get_prev_file_content(filename):
	#Check file exists and if it is
	#read content, and write it out to log purposes
	#Else eturn Flase

	if os.path.exists(filename):
		print("Previous file exists.")
		#lets read to object
		pftemp = open(filename,"r")
		prevdata = pftemp.read()
		print("File readed.")
		pftemp.close()
		print("Create old file.")
		pftemp = open("old"+filename,"w")
		pftemp.write(prevdata)
		pftemp.close()
		#print(prevdata)
		return(prevdata)
	else:
		print("No preivous file exists.")
		return(False)


# timer
def get_process_start_time():
	process_start_time = int(time.time())
	process_start_timestr =  datetime.strftime(datetime.fromtimestamp(process_start_time),"%H:%M:%S")
	print(process_start_timestr)	
	return(process_start_timestr)


def get_http_content(urllocal):
	#urllocal = URL call with this
	#import urllib 
	req = urllib.request.Request(urllocal)
	req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36')
	try: 
		resp = urllib.request.urlopen(req)
		cs = resp.headers.get_content_charset()
		if not cs:
			cs = charset
			#it is UTF 8 do not handle :)
		data = resp.read()
		print ("-------------------------------------------------------")
		html = data.decode("UTF-8")
		#extract to soup
		soup = BeautifulSoup(html,"html.parser")
		return(soup)



		#else: exit("Exit: wrong response code!")
	except (URLError,HTTPError) as e:
		print("Dowload error:",e.reason)
		html = None
		return(false)
	



def get_prev_wrapper(localftempName):
	prev_data_local = get_prev_file_content(localftempName)
	if prev_data_local:
		#only when it is valid
		psoup = BeautifulSoup(prev_data_local,"html.parser")
		if psoup.find_all(id='pst'):
			print("Previous check time: "+psoup.find_all(id = 'pst')[0].string)
			return(psoup)
	return(False)

def write_news_file_header(localftempName,process_start_timestr_local):
	ftemp = open(localftempName,"w")

	ftemp.write('''
	<!DOCTYPE html>
	<html lang='en'>
	<head>
  		<title>lenI scraper</title>
  		<meta charset='utf-8'>
  		<meta name='viewport' content='width=device-width, initial-scale=1'>
  		<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'>
  		<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js'></script>
  		<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script>
	</head>

	<style> 
		body {font-size:1.8rem; font-family: 'Helvetica Neue', HelveticaNeue, Helvetica, Arial, sans-serif; background-color:#11; color:rgba(22,22,22,0.7)}
		li { list-style-type: decimal-leading-zero; line-height:1.8em; } 
		a:link {color:black; text-decoration:none; } 
		a:visited:hover {color:red} a:link:hover {color:green} a:visited{color:gray; background-color:#dbffd6;}
		.btn{margin-bottom:5px;}
	</style>
	<body class="container">

	''')

	ftemp.write('<section><h1> hlcombinator.hu '+'<span id="pst">' + process_start_timestr_local + '</span></h1>')
	ftemp.write('<ul class="list-group">')
	return(ftemp)

def is_news_ok(text):
	#Article checker
	banned = is_news_ok_banlist
	for i in banned:
		if i in text.lower():
			return False
	return True

def is_href_ok(text,banneds,banned_endings):
	#Href checker
	#banneds = ("_stamp","sport","mindekozben","banner","Fzene","joautok")
	#banned_endings = ("blog.hu%2F","index.hu%2F")
	if banneds:
		for i in banneds:
			if i in text:
				return False
	if banned_endings:
		for i in banned_endings:
			if text.endswith(i):
				return False
	return True

	
def is_class_ok(text,allowed):
	#positive list
	#allowed = ("inxcl","inxinx2","inxtc","inxpfb","inxngb","inxport")
	if allowed :
		for i in allowed:
				if i in text:
					return True
		return False
	else: 
		return True 

def get_class_pref(text,thisdict):
	#igazából a classal majd össze kell vonni
	

	for i in thisdict:
			if i in text:
				return thisdict[i] 
	return ""
	

def bs4_checker(new_href,bs4_object):
	for link in bs4_object.find_all('a'):
		if link.get('href') == new_href:
			return(True)		
	return(False) 
	
#word cloud generator
def word_cloud(link_texts):
	print('------ words start ---------')
	#reset counter!
	Text_Counter = Counter()
	count_banned_words = ("az","a","meg","be","hogy","nem","itt","ha","ez","-","mi","van","így","el","ezek","le","ha","már","egy","is","és","ki","is","amit")
	if link_texts:
		link_texts = link_texts.lower()
	Text_Counter.update(link_texts.split())
	

	Words = Counter()
	for key,value in Text_Counter.most_common(500):
		if (value > 1) and (key not in count_banned_words):
			print(key,value,end = ' ')
			Words[key] = value
	print(' ')
	print('------ words end   ---------')
	return Words

def print_wc(cloud,ftemp):
	#word cloud generator
	ftemp.write('<section><h2>Word cloud:</h2><h4>')
	for key,value in cloud.items():
		ftemp.write('<button type="button" class="btn btn-primary">'+key+' <span class="badge badge-primary">'+str(value)+'</span></button> ')	
	ftemp.write('</h4></section>')
	return(True)

def print_news(soup,psoup,ftemp,prefix_dict,allowed,banned_href_snipets,banned_href_endings,ico_url):
	c=0
	link_texts = ""
	prev_href = ""
	old_counter = 0
	new_counter = 0
	li_class=""
	#chunks collect to a set to be able to detect duplicates
	hrefs = set()
	if ico_url:
		icon_snipet = "<img src='"+ico_url+"'style='margin-right:5px;width:16px;height:16px;'>"
	else:
		icon_snipet = ""


	for link in soup.find_all('a'):
		if is_class_ok(link.get('href'),allowed)  and link.string and is_href_ok(link.get('href'),banned_href_snipets,banned_href_endings) and is_news_ok(str(link.string)):
			#print( link.get('href') )
			li_id = str(c+1)
			if psoup:
				if bs4_checker(link.get('href'),psoup):
					li_class = "list-group-item-info"
					old_counter+=1
				else:
					li_class = ""
					new_counter+=1

			chunk = "<a class='list-group-item "+li_class+"' href=" + link.get('href') + ">" + icon_snipet+li_id +". "+ get_class_pref(link.get('href'),prefix_dict) +" " + str(link.string) + "</a>" + os.linesep

			#print(chunk)
			if link.get('href') not in hrefs:
				c+=1
				ftemp.write(chunk)
				hrefs.add(link.get('href'))
				#link_text collects all link string words for counting
				link_texts = link_texts +' '+ str(link.string)

	ftemp.write('</ul></section>')
	return(link_texts,c,old_counter,new_counter);


def close_file(ftemp):
	ftemp.write('</body></html>')
	ftemp.close()

def write_final(ftemp,c,old_counter,new_counter):
	print("Interesting articles: " + str(c))
	print("New/Old articles:" + str(new_counter) + "/" + str(old_counter))
	print ("Let's go to read!")
	print ("-------------------------------------------------------")




