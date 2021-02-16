from bs4 import BeautifulSoup

#with open('html_doc.html') as html_doc:
#    soup = BeautifulSoup(html_doc, 'html.parser')

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')

tag = soup.b
type(tag)