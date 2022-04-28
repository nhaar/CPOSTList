import json
import os

def tableCreate(headers, dict):
    newdict = {}
    i = 0
    for x in headers:
        i += 1
        j = 0
        for y in dict:
            j += 1
            if j == i:
                newdict[x] = dict[y]
    table = '| '
    lenght = 0
    for x in  newdict:
        table += x + ' | '
        length = len(newdict[x])
    table += '\n|'
    for x in newdict:
        table += ' - |'
    for x in range(length):
        table += '\n| '
        for y in newdict:
            table += newdict[y][x] + ' | '
    table += '\n\n'
    return table

Data_division = { ##If decide to change these names, must change in every JSON
                #If adding anything, make sure to add to Variables, and if needed, add exception when creating spreadsheet
    'General': {
        'Name' : [],
        'Name_official' : [],
        'Composers' : [],
        'Order' : [],
        'Link' : [],
        'HQ Source(s)' : [],
        'Source Links' : [],
        'Alternate Names' : [],
        'versions': [],
        'stock': []
    }
}

Order = {'General': {}}


##This dictionary is important, keys are the sheet names related to the name in the jsons. Order is order of sheet
sheetIs = {'Flash OST': 'CP Flash', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST' : 'Game Day', 'Unused Flash OST' : 'CP Flash Unused', 'App OST' : 'App', 'CPI Ost': 'CPI'}
mediasIs = {'Flash OST': 'Club Penguin', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST': 'Club Penguin: Game Day!', 'Unused Flash OST': 'Club Penguin Unused', 'App OST': 'Club Penguin App', 'CPI Ost': 'Club Penguin Island'}

#Old medias list Medias = ['CP Flash', 'CP Flash Unused', 'CPEPF', 'Unused CPEPF', 'CPEPFHR', 'Game Day', 'Unused Game Day', 'CPI', 'Penguin Chat']
Medias = [sheetIs[k] for k in sheetIs]

#Variables = []
#for x in Data_division['General']:
#    Variables.append(x)
Variables = ['Name', 'Name_official', 'HQ Source(s)', 'Source Links', 'Composers', 'Link', 'Alternate Names', 'versions', 'stock']
for i in Medias:
    Data_division[i + ' Info'] = {'Name' : [], 'Name_official' : [], 'Composers' : [], 'Order' : [], 'Link' : [], 'Related To' : [], 'Alternate Names' : [], 'HQ Source(s)': [], 'Source Links' : [], 'Earliest Date' : [], 'files': [], 'uses': []}
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
    print(x)
    newsong = json.load(open(directory+'/' +x, 'r'))
    for y in Medias:
        try:
            print(y)
            dummy = newsong[y + ' Info']
            for z in ['Earliest Date', 'Related To', 'files', 'uses']:
                try:
                    Data_division[y + ' Info'][z].append(newsong[y + ' Info'][z])
                except:
                    Data_division[y + ' Info'][z].append(None)
            for z in ['Name', 'Composers', 'Alternate Names', 'HQ Source(s)', 'Source Links', 'Name_official', 'Link']:
                print(z)
                try:
                    print('Hello')
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