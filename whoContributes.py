#title			:whoContributes.py
#description	:run through a list of wiki pages (listed in a text file) and gather the list of contributors
#author			:Chris Koerner & Paul Boal
#date			:20150907
#version		:0.1
#usage			:python whoContributes.py
#notes			:Make sure you change the script to point to your wiki's URL!
#prerequisites	:This script also assumes you have Python installed :)

import json
import urllib
 
 
f = open('page-titles.txt', 'r')
w = open('output.txt', 'w')
for line in f.readlines():
    id = line.strip('\n')
    url = "https://yourwiki.address.here/w/api.php?action=query&titles={0}&prop=contributors&format=json&rawcontinue=".format(id)
    urlobj = urllib.urlopen(url)
 
    sock = urllib.urlopen(url)
    content = sock.read()
    sock.close()
 
    contentObj = json.loads(content)
    query = contentObj['query']
    if query.has_key('pages'):
        pages = query['pages']
 
        for (pid, page) in pages.iteritems():
            title = page['title']
            if page.has_key('contributors'):
                contributors = page['contributors']
                for c in contributors:
                    out = title + '|' + c['name'] + '\n'
                    print out
                    w.write(out)