import requests

def naming_files(id):
    base_url = 'https://www.library.illinois.edu/ihx/archon/index.php?p=collections/ead&id='
    url_id =


page = requests.get('https://www.library.illinois.edu/ihx/archon/index.php?p=collections/ead&id=2&templateset=ead&disabletheme=1')

with open('ead_file_.xml', 'w') as ead_file:
    ead_file.write(page.text)


