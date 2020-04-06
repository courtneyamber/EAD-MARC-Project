from lxml import etree

infile = open('C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/EAD Files/ead_file_2.xml', 'rb')
xml = infile.read()
infile.close() # don't forget to close the file

tree = etree.fromstring(xml)


title_proper = tree.xpath('//ead:titleproper/text()', namespaces={'ead': "urn:isbn:1-931666-22-9"})

# the /text() grabs the actual text so don't forget that part of the xpath query
# make

print(title_proper)
# this returns a list
print(title_proper[0])
# this returns the first item in that list, ideally you'll have more specific xpath queries so that you only have
# one item in each list

print('Done')