from xml.dom.minidom import parse
import xml.dom.minidom
import os.path
import pandas as pd

list_of_ids = []

#to test error handing
list_of_ids.append(['9000'])

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
list_sys_ids = list(list_of_ids)  #so that it will be a copy and not a reference
list_titles = []
list_persnames = []
list_coll_id = []
list_physdesc = []
list_date = []

# Iterate through the lists of ids to parse each EAD for metadata needed
for i in list_of_ids:
    ead_id = i[0]

    #try to get the dom associated with the EAD and then get metadata elements from the dom
    #if it doesn't exist, then remove that id from the list to maintain the right order
    try:
        dom = xml.dom.minidom.parse(create_path(ead_id))
        file = dom.documentElement

        #get the unititle
        unittitle = dom.getElementsByTagName("unittitle")
        if len(unittitle)>0:
            list_titles.append(unittitle)
        else:
            list_titles.append(['title not found'])

        #get the persname
        persname = dom.getElementsByTagName("persname")
        if len(persname)>0:
            list_persnames.append(persname)
        else:
            list_persnames.append(['personal name not found'])

        #get the unitid
        unitid = dom.getElementsByTagName("unitid")
        if len(unitid)>0:
            list_coll_id.append(unitid)
        else:
            list_coll_id.append(['collection id not found'])

        #get the physical description
        physdesc = dom.getElementsByTagName("extent")
        for extent in physdesc:
            if extent.hasAttribute("type"):
                if len(physdesc)>0:
                    list_physdesc.append(physdesc)
            # for extent in physdesc:
            #     list_physdesc.append(extent.getAttribute("type"))
        else:
            list_physdesc.append(['physical description not found'])

        #get the date
        date = dom.getElementsByTagName("unitdate")
        if len(date)>0:
            list_date.append(date)
        else:
            list_date.append(['date not found'])

    except:
        list_sys_ids.remove(i)

#create lists for pandas
def createPdList(list_to_convert):
    converted_list = []
    for item in list_to_convert:
        print(item)  #for debugging
        try:
            converted_list.append(item[0].firstChild.data.strip())
        except:
            converted_list.append(item[0].strip())
    return converted_list

pd_list_ids = createPdList(list_sys_ids)
pd_list_titles = createPdList(list_titles)
pd_list_persnames = createPdList(list_persnames)
pd_list_coll_id = createPdList(list_coll_id)
pd_list_physdesc = createPdList(list_physdesc)
pd_list_date = createPdList(list_date)

# print statements for testing and debugging (comment out when final)
print(pd_list_ids)
print('Length: '+str(len(pd_list_ids)))
print(pd_list_titles)
print('Length: '+str(len(pd_list_titles)))
print(pd_list_persnames)
print('Length: '+str(len(pd_list_persnames)))
print("\n")

# Put the lists for the pandas into a dataframe, also specifying the correct column labels
spreadsheet = pd.DataFrame(list(zip(pd_list_ids, pd_list_titles,pd_list_date, pd_list_persnames, pd_list_coll_id, pd_list_physdesc)), columns=['System ID', 'Title','Date', 'PersonalName', 'Collection ID', 'Physical Description'])
print(spreadsheet)

# Export dataframe to a csv file
path_csv_file = os.path.join("output","spreadsheet_example.csv")
spreadsheet.to_csv(path_csv_file, encoding='UTF-8')
