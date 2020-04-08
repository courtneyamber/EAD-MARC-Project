from xml.dom.minidom import parse
import xml.dom.minidom
import os.path
import pandas as pd

list_of_ids = ['9000']

#test list
file_path_to_ids = "short_sample_ids.txt"

#full list (comment out this variable assignment if only testing)
#file_path_to_ids = "list_of_eads.txt"

# Read the input file of ids and put these into a list
with open(file_path_to_ids, "r") as inputfile:
    for line in inputfile:
        list_of_ids.append(line.strip().split(','))

# Form the path to the EAD file when given a system id
def create_path(id):
    base_path = os.path.join("EAD Files","ead_file_")
    end_path = ".xml"
    pathdir = base_path + id + end_path
    return pathdir

# Initialize lists for grabbing data from the EADs
list_titles = []

# Iterate through the lists of ids to parse each EAD for metadata needed
for i in list_of_ids:
    ead_id = i[0]

    #for debugging
    #print(create_path(ead_id))

    #try to get the dom associated with the EAD and then get metadata elements from the dom
    #if it doesn't exist, then remove that id from the list to maintain the right order
    try:
        dom = xml.dom.minidom.parse(create_path(ead_id))
        file = dom.documentElement

        #get the unititle
        unittitle = dom.getElementsByTagName("unittitle")
        list_titles.append(unittitle)

    except:
        list_of_ids.remove(i)

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

# print statements for testing and debugging (comment out when final)
print(pd_list_ids)
print(pd_list_titles)
print("\n")

# Put the lists for the pandas into a dataframe, also specifying the correct column labels
spreadsheet = pd.DataFrame(list(zip(pd_list_ids, pd_list_titles)), columns=['System ID', 'Title'])
print(spreadsheet)

# Export dataframe to a csv file
path_csv_file = os.path.join("output","spreadsheet_example.csv")
spreadsheet.to_csv(path_csv_file, encoding='UTF-8')
