
# Creating a dataframe from lists

import pandas as pd

test_titles = ['This', 'Is', 'A', 'Test']
test_authors = ['Also', 'Is', 'A', 'Test']

spreadsheet = pd.DataFrame(list(zip(test_titles, test_authors)), columns=['Title', 'Author'])

print(spreadsheet)

print(' ' + '\n' + ' ' + '\n' + ' ')

# Iterate through the dataframe

for index, row in spreadsheet.iterrows():
    print(row['Title'])

print(' ' + '\n' + ' ' + '\n' + ' ')

# Edit content in the dataframe

for index, row in spreadsheet.iterrows():
    row['Title'] = row['Title'].replace("T", "X")
    row['Author'] = row['Author'] + '.....'

print(spreadsheet)

# Export dataframe to a csv file

spreadsheet.to_csv('spreadsheet_example.csv', encoding='UTF-8')



