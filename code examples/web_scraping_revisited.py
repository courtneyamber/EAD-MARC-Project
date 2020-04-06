import requests
import time

# list_of_ids = ["418", "964", "935"]
# url_id = str(list_of_ids)

list_of_ids = []
url_id= str(list_of_ids)

with open("C:/Users/hvasqu3/PycharmProjects/catalog_project/archon-id-list-12.txt", "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
    print (list_of_ids)

def create_link(id):
    base_url = "https://www.library.illinois.edu/ihx/archon/?p=collections/ead&id="
    ending_url = "&templateset=ead&disabletheme=1"
    url_link = base_url + id + ending_url
    # print(url_link)
    return url_link

print(len(list_of_ids))


for i in list_of_ids:
    ead_id = i[0]
    page = requests.get(create_link(ead_id))
    ead_file_name = "ead_file_" + ead_id + ".xml"
    with open(ead_file_name, 'w') as ead_file:
        ead_file.write(page.text)
        print("downloading ", ead_file_name)
        if ead_file_name == '':
            print("failed")

print("Finished downloading.")