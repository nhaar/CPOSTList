# Welcome to the Club Penguin OST List!

This project aims to document the Club Penguin OST as much as it is possible. This repository is for those who are interested in contributing to the project, if you want to see the data, you should check out the [google sheets page](https://docs.google.com/spreadsheets/d/140Kui6g27N4FXXKX844JWxprgJ6xwbSBso8AGXaLYLM/edit#gid=1754104519). The main goal is to list basic information and information about the high quality sources, in-depth information of each song can be found in the [Club Penguin Music Wiki](https://clubpenguinmusic.miraheze.org/wiki/Main_Page).

# What needs doing

The list is a work in progress. This is how you can help:
- Add more data to the songs, or adding more songs.
- Issue wrong data.
- Particularly, the App and CPI soundtracks are a work in progress. Club Penguin Youtube and TV Special soundtrack is also in the plans.
- Improving the python code (remove unnecessary parts and making it easier to change).

# The repository

This repository is composed of 3 parts: The song data, which is available in JSON formats (details below), the sources notes (WIP), and the scripts that create the notes, and the spreadsheet.

# Data template

This is the data template to be used, comments written after the # symbol.
```
{
    "name": "", # One name is picked to be the main one
    "truename": 0, # 0 if the name is NOT official, 1 if the name IS official
    "artists": "", # "?" if unknown, can list multiple, like "Someone1, Someone2"
    "altnames": "", # Any other names go in here.
    "link": "", # Youtube link. Apart from licensed music, uses the Club Penguin High Quality OST channel.
    "versions": [ # This refers to the google drive files.
        {
            "name": "", # Name and extension
            "info": "", #Description
            "source": "" #Source of File,
            "sourcelinks": "" # Optional, if there is a link
        }
    ],
    "media": { # Replace media with the correspondent code, eg "gd". The list of media are written below.
        "date": "", # The earliest date that the song appeared in this particular media. The date formatting details are given below
        "truedate": 0, # 0 if the date given is true, 1 if it is not, details are discussed below
        "uses": "", # A string with the details of where/how it was used.
    }
}
```
About the dates: The date format must be written in the format YYYY/MM/DD, all in numbers, eg. 2022/02/02. This is what the scrip uses to define the order of things. However, if multiple music show up in the same date, one can add an extra value, which can be a floating point or just integer and that sets the priority, for example:
1. 2022/02/02/2
2. 2022/02/02/1.5
If the script sees these two values, it will give priority to the lowest value, so first it will use the 1.5 one, and then the 2 one. It is recommended using floating points only when changing order when there are many songs already for example, you can change the order of:
* 2022/02/02/1
* 2022/02/02/2
* 2022/02/02/3
By using a floating point:
* 2022/02/02/1
* 2022/02/02/0.9 -> This will now come first
* 2022/02/02/3
Please keep on mind that python is accurate up to 16 decimal places.

There are a handful of media codes you can use:
- cp (=Club Penguin Flash)
- cpu (=Unused Flash Music)
- pc (=Penguin Chat (1 & 3))
- gd (=Game Day)
- cpi (=Club Penguin Island)
- app (=Mobile App)
- cpyt (=Club Penguin Youtube)

Thus, if you want to create info for Penguin Chat, you'd create "pc", and so on. Planned medias for the future:
- cptv

As always, check out the data and notes for examples.

# Transforming the data into a spreadsheet

This repository was built having in mind that this data is better visualized as a spreadsheet. The python script generates a .xslx file with all the data. It uses openpyxl to create the spreadsheet, and separates all the songs in a few lists. One list for each media (like the Flash music) and a final list for every song combined together.

# The source notes

This is a planed future, which will transform the "versions" into tables in a Markdown format for it to be easier to read.