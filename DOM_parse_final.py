from xml.dom.minidom import parse
import xml.dom.minidom

list_of_ids = []

#test list
file_path_to_ids = "sample_list_of_ids.txt"

#full list (comment out this variable assignment if only testing)
#file_path_to_ids = "list_of_eads.txt"

with open(file_path_to_ids, "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
print (list_of_ids)

def create_path(id):
    base_path = "EAD Files\ead_file_"
    end_path = ".xml"
    pathdir = base_path + id + end_path
    return pathdir

list_titles = []

for i in list_of_ids:
    ead_id = i[0]
    print(create_path(ead_id))
    dom = xml.dom.minidom.parse(create_path(ead_id))
    file = dom.documentElement
    unittitle = dom.getElementsByTagName("unittitle")
    list_titles.append(unittitle)

try:
    file = open(r"ead_titles.txt","x")
except:
    file = open(r"ead_titles.txt","a") #ead_titles.txt needs to exist first, this line simply appends the text to the file#

for item in list_titles:
    sent = item[0].firstChild.data
    print(sent, sep='')
    file.write(sent)
file.close()
