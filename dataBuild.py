import json
import os

medias = { #tab: name of the tab on the spreadsheet
           #media: name of the media for notes and series tab
    'cp' : {
        'tab': 'Flash OST',
        'media': 'Club Penguin'
    },
    'pc' : {
        'tab': 'Penguin Chat OST',
        'media': 'Penguin Chat'
    },
    'gd' : {
        'tab': 'Game Day OST',
        'media': 'Club Penguin: Game Day!'
    },
    'cpu' : {
        'tab': 'Unused Flash OST',
        'media': 'Club Penguin (Unused)'
    },
    'app' : {
        'tab': 'App OST',
        'media': 'Club Penguin App'
    },
    'cpi' : {
        'tab': 'CPI OST',
        'media': 'Club Penguin Island'
    }
}

# Finding every directory name

directory = 'Song Data'
folders = []
for root, directories, files in os.walk(directory):
    for folder in directories:
        folders.append(os.path.join(root, folder))

# Iterating through every song and adding to all_data

all_data = []
for x in folders:
    print(x)
    newsong = json.load(open(x+'/data.json', 'r'))
    all_data.append(newsong)
