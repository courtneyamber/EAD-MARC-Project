# Web Scraping

# this is the only part of the code you actually need now.
# and the only variable that should change is the id's in the url and the file name


import requests

#urls = [('https://www.library.illinois.edu/ihx/archon/index.php?p=collections/ead&id=2&templateset=ead&disabletheme=1'),
#        ('https://www.library.illinois.edu/ihx/archon/index.php?p=collections/ead&id=778&templateset=ead&disabletheme=1')]

page = requests.get('https://www.library.illinois.edu/ihx/archon/index.php?p=collections/ead&id=778&templateset=ead&disabletheme=1')

with open('ead_file_778.xml', 'w') as ead_file:
    ead_file.write(page.text)


