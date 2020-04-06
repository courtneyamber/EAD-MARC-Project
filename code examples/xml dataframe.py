from lxml import etree
import os
import fileinput
import sys

# print(os.getcwd())

directory = ("C:/Users/Hailey/OneDrive/Documents/Senior year/EAD-MARC Project/EAD-MARC Project/EAD Files")
# os.path.exists(("G:\ILHistSurvey\Manuscript Processing\Catalog record project\EAD-MARC Project\EAD Files"))

# with os.scandir(directory) as entries:
#     for entry in entries:
#         print(entry.name)

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()

# for file in os.listdir(directory):
#      filename = os.fsdecode(file)
#      print(filename)
#      if filename.endswith(".xml"):
#          # print(os.path.join(directory, filename))
#          continue
#      else:
#          continue
# filename = []
# infile = open("G:\ILHistSurvey\Manuscript Processing\Catalog record project\EAD-MARC Project\EAD Files", "rb")
#
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     print(filename)
#     if filename.endswith(".xml"):
#         with open(os.path.join(directory, filename)):
#             xml = infile.read()
#             infile.close()
#     else:
#         continue

# infile = open("G:\ILHistSurvey\Manuscript Processing\Catalog record project\EAD-MARC Project\EAD Files", "rb")
# # infile =  open(filename, "rb")
# xml = infile.read()
# infile.close()

### Code that I need below, DO NOT DELETE ####
#
#
tree = etree.fromstring(xml)

title_proper = tree.xpath('//ead:titleproper/text()', namespaces={'ead': "urn:isbn:1-931666-22-9"})

print(title_proper)

print(title_proper[0])

print('Done')
