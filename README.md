# HTML-scraper-fastly-tutorial
Scrape links from a site fastly and print out a file for local read.

This repo contains simple code for tutorial purposes to scrape a web content, get anchors and print out to local file for reading - so it is a HTML.

Python3 was chosen for implementation, because I thought it was in a few hours - and I'm going to translate it from bash.

# Focus
1. Open HTTP/HTTPS request - do not check cert validity in case of HTTPS
2. Handle a local HTML file for print out
3. Parse content and write out links - read the headlines only

# Dependecies
* os modul for line endings 
* request modul -» pip urrlib install
* ssl modul -» pip ssl install
* parser modul (BeautifulSoup) -» pip bs4 install

  
