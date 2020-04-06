from xml.dom.minidom import parse
import xml.dom.minidom
import os.path

list_of_ids = []

#test list
file_path_to_ids = "sample_list_of_ids.txt"

#full list (comment out this variable assignment if only testing)
#file_path_to_ids = "list_of_eads.txt"

with open(file_path_to_ids, "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))

#print (list_of_ids)

def create_path(id):
    base_path = os.path.join("EAD Files","ead_file_")
    end_path = ".xml"
    pathdir = base_path + id + end_path
    return pathdir

list_sys_ids = []
list_titles = []

for i in list_of_ids:
    ead_id = i[0]
    #print(create_path(ead_id))
    dom = xml.dom.minidom.parse(create_path(ead_id))
    file = dom.documentElement
    #system id
    list_sys_ids.append(ead_id)
    #unititle
    unittitle = dom.getElementsByTagName("unittitle")
    list_titles.append(unittitle)

#create the file if it doesn't exist, append if it does
try:
    file = open(r"ead_titles.txt","x")
except:
    file = open(r"ead_titles.txt","a")

for item in list_titles:
    sent = item[0].firstChild.data.strip()
    sent+="\n"
    #print(sent, sep='')
    file.write(sent)
file.close()
