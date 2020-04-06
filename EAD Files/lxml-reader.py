from lxml import etree

list_of_ids = []
url_id= str(list_of_ids)

with open("C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/list_of_eads.txt", "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))
    print (list_of_ids)

def print_list(list_of_eads):
    for i in list_of_ids:
        ead_id = i[0]
        ead_file = "ead_file_" + ead_id + ".xml"
        for title_proper in item:
            infile = open(ead_file, 'r')
            xml = infile.read()
            infile.close() # don't forget to close the file
            tree = etree.fromstring(xml)
            title_proper = tree.xpath('//ead:titleproper/text()', namespaces={'ead': "urn:isbn:1-931666-22-9"})
            print(title_proper)

# output = print_list()
# file = open("ead_titles.txt", "a")
# file.write()
# file.close()
