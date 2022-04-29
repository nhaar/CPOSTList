# Welcome to the Club Penguin OST List!

This project aims to document the Club Penguin OST as much as it is possible. This repository is for those who are interested in contributing to the project, if you want to see the data, you should check out the [google sheets page](https://docs.google.com/spreadsheets/d/140Kui6g27N4FXXKX844JWxprgJ6xwbSBso8AGXaLYLM/edit#gid=1754104519), or read the [notes](https://github.com/nhaar/CPOSTList/blob/main/notes.md).

# What needs doing

The list is a work in progress. This is how you can help:
- Add more data to the songs, or adding more songs.
- Issue wrong data.
- Particularly, the App and CPI soundtracks are a work in progress. Club Penguin Youtube and TV Special soundtrack is also in the plans.
- Improving the python code.

# The repository

This repository is composed of 3 parts: The song data, which is available in JSON formats (details below), the notes, and the scripts that create the notes, and the spreadsheet.

# Data template

This is the data template to be used, comments written after the # symbol.
´´´
{
    "Name": "The Name", # One name is picked to be the main one.
    "Name_official": 0, # 0 if the name is NOT official, 1 if the name IS official.
    "Alternate Names" : "Za Namae" # Any other names go in here.
    "Composers" : "Someone" # "?" if unknown, can list multiple, like "Someone1, Someone2"
    "HQ Source(s)": "The Source", # If multiple, then list as "Source1 + Source2"
    "Source Links" "www.alink.com" # Optional, if the source is available on the internet, link it.
    "Order": 0, # Order in the series (more details below).
    "Link": "Youtube Link", # Youtube link. Apart from licensed music, uses the Club Penguin High Quality OST channel.
    "Earliest Date": "YYYY/MM/DD", # Earliest Date seen in the whole series. "?" if unknown.
    "Media Info": { # For example, "Game Day Info". The list of media are written below.
        "Order": 0, # Order in this media (more details below)
        "Earliest Date": "YYYY/MM/DD", # Earliest date seen in this media. "?" if unknown.
        "Related To": "Coffee Shop, Book Room", # Places or ways it was used in this media.
        "files": { # List all the files, ordered by a string number, from oldest to newest.
            "1": { # Keep the order the same as this: name, info.
                "name" : "1st file name", # Name of the file in the code/media.
                "info" : "A description of the file" # Any comments that may exist for it.
            }
        },
        "uses": { # List all the usages, ordered by a string number, from oldest to newest.
            "1": { # Keep the order the same as this: date, use, files, info
                "date" :"Date it was used", # No strict standard, preference to style 2000/Jan/01, may have start and end, like 2005/Jan/01-2005/Jan/05. "?" if unknown.
                "use": "Where/How it was used", # Keep it brief.
                "files": "The files that were used", # Use file names from the "files" dictionary.
                "info" : "Detailed comments" # If any exist, may detail which rooms in a party it was used, for example.
            }
        }
    },
	"stock": { # Only for stock songs
		"info" : {"origin": "Website the stock song is from", "link": ""}, # Origin website and link.
		"sale" : ["Buying option 1", "Buying option 2"] # A list of the versions one can buy.
	},
    "versions": { # This refers to the google drive files.
        "1": { # First file
            "name" : "music.mp3", # Name and extension
            "info" : "Description",
            "source" : "Source of file"
        }
    }
}
´´´
About "Order": This is an arbitrary attempt at ordering songs in a chronological way. If you are creating a song you can set this to whatever, it will be sorted in the future. This is meant to be used with floats, and it it's later sorted into integers. For example, if two songs have orders 0.5 and 0.6, they'll be sorted from least to biggest, and then an integer count will follow. This is to avoid having to rewrite every song when changing a single song out of order. It is not very elegant, but it works.

There are a handful of medias you can use:
- CP Flash
- CP Flash Unused
- Penguin Chat
- Game Day
- CPI, App
Thus, if you want to create info for Penguin Chat, you'd create "Penguin Chat Info", and so on. Planned medias for the future:
- CPYT
- CPTV

As always, check out the data and notes for examples.

# Transforming the data into a spreadsheet

This repository was built having in mind that this data is better visualized as a spreadsheet. The python script generates a .xslx file with all the data. It uses openpyxl to create the spreadsheet, and separates all the songs in a few lists. One list for each media (like the Flash music) and a final list for every song combined together.

# Transforming the data into the notes doc

Alongside the spreadsheet, the data is also converted into a long markdown file with small remarks, tables and descriptions about the songs, that wouldn't normally fit in a spreadsheet.
