#from modulename import filename
from bs4 import BeautifulSoup
html_doc = """

"""

#print(html page)
soup = BeautifulSoup(html_doc, 'html.parser')

#print(htmlpage)
link1=soup.find_all(id='link1')
print(link1[0].get_text())