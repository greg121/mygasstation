import mechanize
from lxml import html



br = mechanize.Browser()
br.open("www.tanken.t-online.de")
br.select_form(nr=0)
br.form["location-search-input"] = "Darmstadt"
br.submit()

print br.title()
print response1.geturl()
print response1.info()  # headers
print response1.read()  # body
