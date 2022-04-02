import json
import pandas as pd
import os
from openpyxl import Workbook

Data_division = {
    'General': {
        'Name' : [],
        'Name_official' : [],
        'Composers' : [],
        'Order' : [],
        'Link' : [],
        'HQ Source(s)' : [],
        'Source Links' : [],
        'Alternate Names' : [],
        'Medias' : [],
        'Earliest Date' : [],
    }
}

Order = {'General': {}}

Medias = ['CP Flash', 'CP Flash Unused', 'CPEPF', 'Unused CPEPF', 'CPEPFHR', 'Game Day', 'Unused Game Day', 'CPI', 'Penguin Chat']
Variables = ['Name', 'Name_official', 'HQ Source(s)', 'Source Links', 'Composers', 'Link', 'Alternate Names', 'Earliest Date', 'Medias']
for i in Medias:
    Data_division[i + ' Info'] = {'Name' : [], 'Name_official' : [], 'Composers' : [], 'Order' : [], 'Link' : [], 'Related To' : [], 'Alternate Names' : [], 'HQ Source(s)': [], 'Source Links' : [], 'Earliest Date' : []}
    Order[i + ' Info'] = {}

directory = 'Song Data'

# Finding every file name

all_files = []
files = []
for x in os.walk(directory):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

# Iterating through every song

for x in files:
    newsong = json.load(open(directory+'/' +x, 'r'))
    for y in Medias:
        try:
            dummy = newsong[y + ' Info']
            Data_division[y + ' Info']['Earliest Date'].append(newsong[y + ' Info']['Earliest Date'])
            Data_division[y + ' Info']['Related To'].append(newsong[y + ' Info']['Related To'])
            for z in ['Name', 'Composers', 'Alternate Names', 'HQ Source(s)', 'Source Links', 'Name_official', 'Link']:
                try:
                    Data_division[y + ' Info'][z].append(newsong[z])
                except:
                    Data_division[y + ' Info'][z].append(None)
            Order[y + ' Info'][newsong['Name']] = newsong[y + ' Info']['Order']
        except:
            pass
    for y in Variables:
        try:
            Data_division['General'][y].append(newsong[y])
        except:
            Data_division['General'][y].append(None)
    Order['General'][newsong['Name']] = newsong['Order']

# Fixing The Order Numbering

neworder = {}

for x in Order:
    neworder[x] = {}
    Order[x] = dict(sorted(Order[x].items(), key=lambda z:z[1]))
    i = 0
    for y in Order[x]:
        i += 1
        neworder[x][y] = i
    for y in Data_division[x]['Name']:
        Data_division[x]['Order'].append(neworder[x][y])

#Getting the Series tab .tsv

series = pd.DataFrame(Data_division['General'])
series.to_csv(r'series.tsv', index = False, sep = '\t')

#Getting each media tab .tsv

for x in Medias:
    series = pd.DataFrame(Data_division[x + ' Info'])
    series.to_csv(r'' + x + '.tsv', index = False, sep = '\t')

#sort data_division by order

newdata = {}

for x in Data_division:
    newdata[x] = {}
    for y in Data_division[x]:
        newdata[x][y] = []
    for i in range(1,len(Data_division[x]['Order'])+1):
        songno = Data_division[x]['Order'].index(i)
        for y in newdata[x]:
            newdata[x][y].append(Data_division[x][y][songno])


### Creating the spreadsheet

wb = Workbook()

# Configure base sheets

wb['Sheet'].title = 'Welcome'
wb.create_sheet('Downloads')

#Create Series OST's

#names
flash = 'Flash OST'
pc = 'Penguin Chast OST'
gd = 'Game Day OST'
flashU = 'Unused Flash OST'

#data correlations

sheetIs = {flash: 'CP Flash', pc : 'Penguin Chat', gd : 'Game Day', flashU : 'CP Flash Unused'}

wb.create_sheet(flash)
wb.create_sheet(pc)
wb.create_sheet(gd)
wb.create_sheet(flashU)

#Extra sheets

wb.create_sheet('to-do')

#Fill data to sheets

letters = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}

for k in sheetIs:
    i = 0
    for x in newdata[sheetIs[k] + ' Info']:
        j = 0
        i += 1
        for y in newdata[sheetIs[k] + ' Info'][x]:
            j += 1
            wb[k][letters[i] + str(j+1)] = y

wb.save('sheet.xlsx')