#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# html getter and pharser
# - get content to file
# - pharse the important elements
# - print out to html template
# - if there wehre older file compare and mark old elements



print ("---- News generator python modular revision - v3 beta -----")
print ("Import modules")

#common modul import
import ng_common_module as ngc
import os

ftempName = "index-2.save.py.html" # Output file name
url = "https://index.hu" # Major read source
ico_url = "https://index.hu/assets/images/favicons/favicon-16x16.png"
thisdict_var = {
	"napirajz":"NRAJZ-",
	"inxcl":"index-",
	"inxinx2":"I2-",
	"inxtc":"TC-" ,
	"inxpfb":"PRTFL-" ,
	"inxngb":"NAPI-",
	"inxport":"PORT-"
	}

allowed_html_class = ("inxcl","inxinx2","inxtc","inxpfb","inxngb","inxport")
banned_href_snipets =("_stamp","sport","mindekozben","banner","Fzene","joautok","markandmore")
banned_href_endings =("blog.hu%2F","index.hu%2F","szemlelek.net/")


# Setting timer
ngc.get_process_start_time()
# request hadnling 
soup_var = ngc.get_http_content(url)
psoup_var=ngc.get_prev_wrapper(ftempName);
#prepare file operations
filehandler = ngc.write_news_file_header(ftempName,ngc.get_process_start_time());
#iterate data
link_texts_var,c,old_counter,new_counter = ngc.print_news(soup_var,psoup_var,filehandler,thisdict_var,allowed_html_class,banned_href_snipets,banned_href_endings,ico_url)
#word cloud generator split html 
ngc.print_wc(ngc.word_cloud(link_texts_var),filehandler)
ngc.write_final(filehandler,c,old_counter,new_counter)
ngc.close_file(filehandler)

#24 ----




ftempName = "24-2.save.py.html" # Output file name
url = "https://24.hu" # Major read source
ico_url = "https://24.p3k.hu/apple-touch-icon.png"

thisdict = {
	"kozelet":"KÖZ -",
	"tudomany":"TUD -",
	"kulfold":"KÜLPOL -",
	"kultura":"KULT -" ,
	"belfold":"BELPOL -" ,
	"szorakozas":"lol -",
	"video":"VIDEO -",
	"gazdasag":"GAZD -",
	"tech":"TECH -",
	"sokszinuvidek":"VIDEK -",
	"g7":"G7 -"
 	}

allowed_html_class = False
banned_href_snipets  = ("tag","sport","rangado","hirlevel","impresszum","startlap","nlcafe","adatkezelesi","citromail","lap.hu","hirstart","vezess.hu","startapro.hu","hazipatika.com","noemi","elet-stilus","bringakaland","/tag/")
banned_href_endings = ("24.hu/","belfold/","szorakozas/","sport/","kultura/","kulfold/","techtud/","kozelet/","gazdasag/","uzleti-tippek/","tudomany/","tech/","elet-stilus/","otthon/","velemeny/","video/","kistotal/","#","video","hirfolyam/","kultura","ep-valasztas/","kritika/",".24.hu","szorakozas","gazdasag","tudomany","kulfold","tech","/gyorssegely/","utitars/","vivovb2019/","-titkok/")


# Setting timer
ngc.get_process_start_time()
# request hadnling 
soup_var = ngc.get_http_content(url)
psoup_var=ngc.get_prev_wrapper(ftempName);
#prepare file operations
filehandler = ngc.write_news_file_header(ftempName,ngc.get_process_start_time());
#iterate data
link_texts_var,c,old_counter,new_counter = ngc.print_news(soup_var,psoup_var,filehandler,thisdict_var,allowed_html_class,banned_href_snipets,banned_href_endings,ico_url)
#word cloud generator split html 
ngc.print_wc(ngc.word_cloud(link_texts_var),filehandler)
ngc.write_final(filehandler,c,old_counter,new_counter)
ngc.close_file(filehandler)






ftempName = "444-2.save.py.html" # Output file name
url = "https://444.hu" # Major read source
ico_url = "https://444.hu/assets/blog/static/favicon.ico"

allowed_html_class = False
banned_href_snipets = ("/author/","/category/","4cdn.hu","twitter.com/444hu","plus.google.com/b","44NEGY4","yqA3L","ask.fm/negynegynegy","instagram.com/negynegynegy","mailto:","/tag/")
banned_href_endings = ("/szolgalati-kozlemeny","/szerzoi-jogok","/mediaajanlat","/negyednegy","/tamogatas","/kereses","/archivum","/impresszum","/adatvedelmi-nyilatkozat","/feed","/tamogatas-altalanos-szerzodesi-feltetelek",".hu","user/jetivideo")

thisdict = {
		
		"vilag":"KÜLPOL -",
		"geekz":"GEEKZ -",
		"qubit":"QBIT -"	
	}


# Setting timer
ngc.get_process_start_time()
# request hadnling 
soup_var = ngc.get_http_content(url)
psoup_var=ngc.get_prev_wrapper(ftempName);
#prepare file operations
filehandler = ngc.write_news_file_header(ftempName,ngc.get_process_start_time());
#iterate data
link_texts_var,c,old_counter,new_counter = ngc.print_news(soup_var,psoup_var,filehandler,thisdict_var,allowed_html_class,banned_href_snipets,banned_href_endings,ico_url)
#word cloud generator split html 
ngc.print_wc(ngc.word_cloud(link_texts_var),filehandler)
ngc.write_final(filehandler,c,old_counter,new_counter)
ngc.close_file(filehandler)





exit()





