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

# Finding every file name

directory = 'Song Data'

all_files = []
files = []
for x in os.walk(directory):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

# Iterating through every song and adding to all_data

all_data = []
for x in files:
    print(x)
    newsong = json.load(open('Song Data/' + x, 'r'))
    all_data.append(newsong)
