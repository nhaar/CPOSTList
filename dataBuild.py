import json
import os

all_data = {}
medias = { #tab: name of the tab on the spreadsheet
           #media: name of the media for notes and series tab
    'CP Flash' : {
        'tab': 'Flash OST',
        'media': 'Club Penguin'
    },
    'Penguin Chat' : {
        'tab': 'Penguin Chat OST',
        'media': 'Penguin Chat'
    },
    'Game Day' : {
        'tab': 'Game Day OST',
        'media': 'Club Penguin: Game Day!'
    },
    'CP Flash Unused' : {
        'tab': 'Unused Flash OST',
        'media': 'Club Penguin (Unused)'
    },
    'App' : {
        'tab': 'App OST',
        'media': 'Club Penguin App'
    },
    'CPI' : {
        'tab': 'CPI OST',
        'media': 'Club Penguin Island'
    }
}


##This dictionary is important, keys are the sheet names related to the name in the jsons. Order is order of sheet
#sheetIs = {'Flash OST': 'CP Flash', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST' : 'Game Day', 'Unused Flash OST' : 'CP Flash Unused', 'App OST' : 'App', 'CPI Ost': 'CPI'}
#mediasIs = {'Flash OST': 'Club Penguin', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST': 'Club Penguin: Game Day!', 'Unused Flash OST': 'Club Penguin Unused', 'App OST': 'Club Penguin App', 'CPI Ost': 'Club Penguin Island'}

#Variables = []
#for x in Data_division['General']:
#    Variables.append(x)
#Variables = ['Name', 'Name_official', 'HQ Source(s)', 'Source Links', 'Composers', 'Link', 'Alternate Names', 'versions', 'stock']
#for i in Medias:
#    Data_division[i + ' Info'] = {'Name' : [], 'Name_official' : [], 'Composers' : [], 'Order' : [], 'Link' : [], 'Related To' : [], 'Alternate Names' : [], 'HQ Source(s)': [], 'Source Links' : [], 'Earliest Date' : [], 'files': [], 'uses': []}
#    Order[i + ' Info'] = {}

directory = 'Song Data'

# Finding every file name

all_files = []
files = []
for x in os.walk(directory):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

# Iterating through every song and adding to all_data

i = 0
for x in files:
    i += 1
    print(x)
    newsong = json.load(open(directory+'/' +x, 'r'))
    all_data[i] = newsong
