import json
import pandas as pd
import os

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
