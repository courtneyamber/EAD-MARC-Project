from xml.dom.minidom import parse
import xml.dom.minidom
import os.path
import pandas as pd

list_of_ids = []

#test list
file_path_to_ids = "short_sample_ids.txt"

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

    #unititle
    unittitle = dom.getElementsByTagName("unittitle")
    list_titles.append(unittitle)

# #create the file if it doesn't exist, append if it does
# try:
#     file = open(r"ead_titles.txt","x")
# except:
#     file = open(r"ead_titles.txt","a")
#
# for item in list_titles:
#     sent = item[0].firstChild.data.strip()
#     sent+="\n"
#     #print(sent, sep='')
#     file.write(sent)
# file.close()

#create lists for pandas
def createPdList(list_to_convert):
    converted_list = []
    for item in list_to_convert:
        try:
            converted_list.append(item[0].firstChild.data.strip())
        except:
            converted_list.append(item[0].strip())
    return converted_list

pd_list_ids = createPdList(list_of_ids)
pd_list_titles = createPdList(list_titles)

print(pd_list_ids)
print(pd_list_titles)
print("\n")

spreadsheet = pd.DataFrame(list(zip(pd_list_ids, pd_list_titles)), columns=['System ID', 'Title'])
print(spreadsheet)

# Export dataframe to a csv file
path_csv_file = os.path.join("output","spreadsheet_example.csv")
spreadsheet.to_csv(path_csv_file, encoding='UTF-8')
