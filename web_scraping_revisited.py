import requests

list_of_ids = []
url_id= str(list_of_ids)

with open("G:/ILHistSurvey/Manuscript Processing/Catalog record project/EAD-MARC Project/catalog_project/RBML lists/rbml_ead_list_0.txt", "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
    print (list_of_ids)

def create_link(id):
    base_url = "https://apache-ns-dev.library.illinois.edu/ihx/rbml_archon-3-21r3_modified/?p=collections/ead&id="
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