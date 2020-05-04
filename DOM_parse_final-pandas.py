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
list_persnames_source = []
list_coll_id = []
list_physdesc = []
list_physdesc_unit = []
list_date = []
list_genre_terms = []
list_gt_source = []
list_geogname = []
list_gn_source = []
list_topterm = []
list_topterm_source = []
list_corpname = []
list_corpname_source = []


# def get_text(element):
#     return " ".join(t.nodeValue for t in element[0].childNodes if t.nodeType == t.TEXT_NODE)


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
        persname_elements = dom.getElementsByTagName("persname")
        persname_source = file.getAttribute("source")

        # collect all top terms (and their sources) into a list
        # later, join() is used to transform the list into a single piece of text
        persname_text_list = []
        persname_source_list = []

        for persname_element in persname_elements:
            persname_text_list.append(persname_element.firstChild.data)
            persname_source_list.append(persname_element.getAttribute("source"))

            if persname_element.getAttribute('encodinganalog') == '600':

                if len(persname_text_list) > 0:
                    list_persnames.append([', '.join(persname_text_list)])
                    list_persnames_source.append([', '.join(persname_source_list)])
            else:
                list_persnames.append(['subject not found'])
                list_persnames_source.append(['subject source not found'])

        #get the unitid
        unitid = dom.getElementsByTagName("unitid")
        if len(unitid)>0:
            list_coll_id.append(unitid)
        else:
            list_coll_id.append(['collection id not found'])

        #get the physical description
        physdesc = dom.getElementsByTagName("extent")
        extent_type = file.getAttribute("type")

        for extent in physdesc:
            # print (extent.getAttribute("type"))
            if extent.hasAttribute("type"):
                if len(physdesc)>0:
                    list_physdesc.append(physdesc)
                    list_physdesc_unit.append([extent.getAttribute("type")])
            else:
                list_physdesc.append(['physical description not found'])
                list_physdesc_unit.append(['physical description unit not found'])

        #get the date
        date = dom.getElementsByTagName("unitdate")
        if len(date)>0:
            list_date.append(date)
        else:
            list_date.append(['date not found'])

        #get genre/form
        genre_elements = dom.getElementsByTagName("genreform")
        genre_source = file.getAttribute("source")

        genre_text_list = []
        genre_source_list = []

        for genre_element in genre_elements:
            genre_text_list.append(genre_element.firstChild.data)
            genre_source_list.append(genre_element.getAttribute("source"))

            if genre_element.getAttribute('encodinganalog') == '655':

                if len(genre_text_list) > 0:
                    list_genre_terms.append([', '.join(genre_text_list)])
                    list_gt_source.append([', '.join(genre_source_list)])
            else:
                list_genre_terms.append(['subject not found'])
                list_gt_source.append(['subject source not found'])

        #get geographic names
        geogname_elements = dom.getElementsByTagName("geogname")
        geog_source = file.getAttribute("source")

        geog_text_list = []
        geog_source_list = []

        for geog_element in geogname_elements:
            geog_text_list.append(geog_element.firstChild.data)
            geog_source_list.append(geog_element.getAttribute("source"))

            if geog_element.getAttribute('encodinganalog') == '651':

                if len(geog_text_list) > 0:
                    list_geogname.append([', '.join(geog_text_list)])
                    list_gn_source.append([', '.join(geog_source_list)])
            else:
                list_geogname.append(['subject not found'])
                list_gn_source.append(['subject source not found'])

        #get subject/topical terms
        topterm_elements = dom.getElementsByTagName("subject")
        topterm_source = file.getAttribute("source")

        # collect all top terms (and their sources) into a list
        # later, join() is used to transform the list into a single piece of text
        topterm_text_list = []
        topterm_source_list = []
        for topterm_element in topterm_elements:
            topterm_text_list.append(topterm_element.firstChild.data)
            topterm_source_list.append(topterm_element.getAttribute("source"))

            if topterm_element.getAttribute('encodinganalog') == '650':

                if len(topterm_text_list) > 0:
                    list_topterm.append([', '.join(topterm_text_list)])
                    # list_topterm.append(['{}\n'.format(text) for text in topterm_text_list])
                    list_topterm_source.append([', '.join(topterm_source_list)])
            else:
                list_topterm.append(['subject not found'])
                list_topterm_source.append(['subject source not found'])

        # get the corpname (610)
        corpname_elements = dom.getElementsByTagName('corpname')
        corpname_source = file.getAttribute('source')

        corpname_text_list = []
        corpname_source_list = []

        for corpname_element in corpname_elements:
            corpname_text_list.append(corpname_element.firstChild.data)
            corpname_source_list.append(corpname_element.getAttribute('source'))

            if corpname_element.getAttribute('encodinganalog') == '610':
                if len(corpname_text_list) > 0:
                    list_corpname.append([', '.join(corpname_text_list)])
                    list_corpname_source.append([', '.join(corpname_source_list)])

        # NOTE ON THE ABOVE COMMENTED-OUT CODE:
        # I think we actually want to get the element by tag name for:
        # genreform (where encodinganalog is 655),
        # geogname (where encodinganalog is 651), and
        # subject (where encodinganalog is 650)
        # All these should have their own list and column in the dataframe, too. We will also want to pull out
        # the source from the tags, and (for now) put these in their own column (like with the extent field).
        # You might start by just pulling out the first subject, but eventually we will want to figure out how
        # to get all the subjects (that is, in cases where there are multiple 650 fields, for instance)

    except:
        list_sys_ids.remove(i)

#create lists for pandas
def createPdList(list_to_convert):
    converted_list = []
    for item in list_to_convert:
        #print(item)  #for debugging
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
pd_list_physdesc_unit = createPdList(list_physdesc_unit)
pd_list_date = createPdList(list_date)
pd_list_genre_terms = createPdList(list_genre_terms)
pd_list_gt_source = createPdList(list_gt_source)
pd_list_geognames = createPdList(list_geogname)
pd_list_gn_source = createPdList(list_gn_source)
pd_list_topterm = createPdList(list_topterm)
pd_list_tt_source = createPdList(list_topterm_source)

# add each new list variable to this list of lists for easier debugging
pd_all_lists = [pd_list_ids,pd_list_titles,pd_list_persnames,pd_list_coll_id,pd_list_physdesc, pd_list_physdesc_unit,pd_list_date, pd_list_genre_terms, pd_list_gt_source, pd_list_geognames, pd_list_gn_source, pd_list_topterm, pd_list_tt_source]

# print statements for testing and debugging (comment out when final)
def print_list_info(list_to_print):
    print(list_to_print)
    print('Length: '+str(len(list_to_print)))

for pd_list in pd_all_lists:
    print_list_info(pd_list)

print("\n")

# Put the lists for the pandas into a dataframe, also specifying the correct column labels
data_columns=['System ID', 'Title','Date', 'PersonalName', 'Collection ID', 'Extent','Extent unit', 'Subject Terms-Genre/Form', 'Subject Source-Genre/Form', 'Subject Terms-Geog. Names', 'Subject Source-Geog. Names', 'Subject Terms-Topical term', 'Subject Source-Topical term']
spreadsheet = pd.DataFrame(list(zip(pd_list_ids, pd_list_titles,pd_list_date, pd_list_persnames, pd_list_coll_id, pd_list_physdesc,pd_list_physdesc_unit, pd_list_genre_terms, pd_list_gt_source, pd_list_geognames, pd_list_gn_source, pd_list_topterm, pd_list_tt_source)), columns=data_columns)
print(spreadsheet)

# Export dataframe to a csv file
path_csv_file = os.path.join("output","spreadsheet_example.csv")
spreadsheet.to_csv(path_csv_file, encoding='UTF-8')
