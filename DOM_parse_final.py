from xml.dom.minidom import parse
import xml.dom.minidom

list_of_ids = []

with open(#insert file path# , "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
print (list_of_ids)

def create_path(id):
    base_path = #insert path including file name#
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


file = open(r"ead_titles.txt","a") #ead_titles.txt needs to exist first, this line simply appends the text to the file#

for item in list_titles:
    sent = item[0].firstChild.data
    print(sent, sep='')
    file.write(sent)
file.close()
