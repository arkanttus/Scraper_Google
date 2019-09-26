from bs4 import BeautifulSoup as Bs

html_doc = """
<html><head><title>Imperial</title></head>
<body>
<p class="title"><b>Atletica Imperial</b></p>

<p class="story">Atletica de S.I criada em 2017. Temos:
<a href="www.imperial.com/blusas" class="prod" id="link1">Blusas</a>,
<a href="www.imperial.com/canecas" class="prod" id="link2">Canecas</a> e
<a href="www.imperial.com/bones" class="prod" id="link3">Bones</a>;
Filie-se.</p>

<p class="story">...</p>
"""

soup = Bs(html_doc, 'html.parser')

print(soup.prettify())

print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent.name)

print(soup.p)

print(soup.p['class'])

print(soup.a)

print(soup.a['href'])

print(soup.a['id'])

print(soup.a.text)

print(soup.find_all('a'))

print(soup('a'))

print(soup.find(id="link3"))

print(soup.find_all('a', attrs={'class': 'prod'}))

print(soup.find_all('a', attrs={'class': 'prod', 'id': 'link2'}))

print(soup.find_all('a', class_='prod'))

print(soup.find_all('a', limit=2))

print(soup.find_all(id=True)

print(soup.find_all(class_=True)

a = soup.a
a['id'] = 'link01'

soup.b.append(" Ufac")

print(soup.p)

nova_tag = soup.new_tag('a', href='www.imperial.com.br')

print(nova_tag)

nova_tag.append("Site Imperial")

soup.p.append(nova_tag)

def custom_class(tag):
...    if tag.has_attr('class') and tag.has_attr('id'):
...       return 'prod' in tag['class'] and not 'link2' in tag['id']

print(soup.find_all(custom_class))

def 
