#from modulename import filename
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<title>THE EASYLEARN ACADEMY</title>
</head>
<body>
<p class="title"><b>Page Heading</b></p>

<p class="story">Once upon a time there were three little brother; and their names were
<a href="http://example.com/Ram" class="brother" id="link1">Ram</a>
<a href="http://example.com/lakshman" class="brother" id="link2">lakshman</a> 
<a href="http://example.com/bharat" class="brother" id="link3">bharat</a>
<a href="http://example.com/shatrugna" class="brother" id="link3">shatrugna</a>
and they lived at the ayodhaya
</p>

<p class="story">they were very good people</p>
"""

#print(html page)
soup = BeautifulSoup(html_doc, 'html.parser')

#get all paragrapahs
paragraphs=soup.find_all("p")#find all it will return all paragraphs

print(paragraphs)
for paragraph in paragraphs:
        print(paragraph.get_text())
        print("_"*80)