# Welcome to the Club Penguin OST List!

This project aims to document the Club Penguin OST as much as it is possible. This repository is for those who are interested in contributing to the project, if you want to see the data, you should check out the [google sheets page](https://docs.google.com/spreadsheets/d/140Kui6g27N4FXXKX844JWxprgJ6xwbSBso8AGXaLYLM/edit#gid=1754104519), or read the [notes](https://github.com/nhaar/CPOSTList/blob/main/notes.md).

# What needs doing

The list is a work in progress. This is how you can help:
- Add more data to the songs, or adding more songs.
- Issue wrong data.
- Particularly, the App and CPI soundtracks are a work in progress. Club Penguin Youtube and TV Special soundtrack is also in the plans.
- Improving the python code.

# The repository

This repository is composed of 3 parts: The song data, which is available in JSON formats (details below), the notes (WIP), and the scripts that create the notes, and the spreadsheet.

# Data template

This is the data template to be used, comments written after the # symbol.
```
{
    "name": "", # One name is picked to be the main one
    "truename": 0, # 0 if the name is NOT official, 1 if the name IS official
    "artists": "", # "?" if unknown, can list multiple, like "Someone1, Someone2"
    "altnames": "", # Any other names go in here.
    "sources": "", # If multiple, then list as "Source1 + Source2"
    "sourcelinks": "", # Optional, if the source is available on the internet, link it.
    "order": 0, # Order in the series (more details below).
    "link": "", # Youtube link. Apart from licensed music, uses the Club Penguin High Quality OST channel.
    "versions": [ # This refers to the google drive files.
        {
            "name": "", # Name and extension
            "info": "", #Description
            "source": "" #Source of File
        }
    ],
    "media": { # Replace media with the correspondent code, eg "gd". The list of media are written below.
        "order": 0, # Order in this media (more details below)
        "files": [ # List all the files, ordered by a string number, from oldest to newest.
            {
                "name": "", # Name of the file in the code/media.
                "info": "" # Any comments that may exist for it.
            }
        ],
        "uses": [ # List all the usages, from oldest to newest.
            {
                "date": "", # Date it was used, in "YYYY/MM/DD" format, or "?" if unknown
                "end: "", # Date it stopped being used, in same format, optional
                "use": "", # Where/How it was used, keep it brief.
                "files": "", # Use file names from the "files" dictionary.
                "info": "" # If any extra info exists, may detail which rooms in a party it was used, for example.
            }
        ]
    }
}
```
About "Order": This is an arbitrary attempt at ordering songs in a chronological way. If you are creating a song you can set this to whatever, it will be sorted in the future. This is meant to be used with floats, and it it's later sorted into integers. For example, if two songs have orders 0.5 and 0.6, they'll be sorted from least to biggest, and then an integer count will follow. This is to avoid having to rewrite every song when changing a single song out of order. It is not very elegant, but it works.

There are a handful of media codes you can use:
- cp (=Club Penguin Flash)
- cpu (=Unused Flash Music)
- pc (=Penguin Chat (1 & 3))
- gd (=Game Day)
- cpi (=Club Penguin Island)
- app (=Mobile App)

Thus, if you want to create info for Penguin Chat, you'd create "pc", and so on. Planned medias for the future:
- cpyt
- cptv

As always, check out the data and notes for examples.

# Transforming the data into a spreadsheet

This repository was built having in mind that this data is better visualized as a spreadsheet. The python script generates a .xslx file with all the data. It uses openpyxl to create the spreadsheet, and separates all the songs in a few lists. One list for each media (like the Flash music) and a final list for every song combined together.