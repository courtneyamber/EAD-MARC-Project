# import xml.etree.ElementTree as ET

# def parseXML(xmlfile):
#     tree = ET.parse('ead_file_10.xml')
#     root = tree.getroot()
#     print(root.tag) #this should print the root of the tree
#     for item in root.findall('/ead/archdesc/did/unittitle'):
#         print(item)

## THIS WORKS but gives every bit of text for only one file ##

# from lxml import etree
#
# infile = open('C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/EAD Files/ead_file_2.xml', 'rb')
# xml = infile.read()
# infile.close() # don't forget to close the file
#
# tree = etree.fromstring(xml)
#
# print(tree.xpath("//text()")
#
# print(tree.xpath("//text[0]"))

##NEW##

#### THIS PART OF THE CODE CREATES THE DIRECTORY PATH ####

# list_of_ids = []
# url_id= str(list_of_ids)
#
# with open("C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/list_of_eads.txt", "r") as inputfile:
#     for line in inputfile:
#         list_of_ids.append(line.strip().split(','))
#     # print (list_of_ids)
#
# def create_file_name(id):
#     base_dir = "C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/EAD Files/ead_file_"
#     end_dir = ".xml"
#     path_dir = base_dir + id + end_dir
#     print (path_dir)
#
# for i in list_of_ids:
#     ead_id = i[0]



#### THIS PART OF THE CODE PULLS THE TEXT FROM THE XML WITHOUT XPATH ####
from xml.dom.minidom import parse
import xml.dom.minidom

list_of_ids = []

with open("C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/list_of_eads_1.txt", "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
print (list_of_ids)

def create_path(id):
    base_path = "C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/EAD Files/ead_file_"
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


file = open(r"ead_titles.txt","w")

for item in list_titles:
    sent = item[0].firstChild.data
    print(sent, sep='')
    file.write(sent)
file.close()
