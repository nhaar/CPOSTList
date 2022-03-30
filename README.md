# Welcome to the Club Penguin OST List!

This project aims to document the Club Penguin OST as much as it is possible. This repository is for those who are interested in contributing to the project, if you want to see the data, you should check out the [google sheets page](https://docs.google.com/spreadsheets/d/140Kui6g27N4FXXKX844JWxprgJ6xwbSBso8AGXaLYLM/edit#gid=1754104519).

# The repository

This repository is composed of 3 parts: The song data, which is available in JSON formats (details below), a script that writes all the data into table separated values, and two Visual Basic macros that format it as it is in the spreadsheet.

# Data template

Each song has the following keys (Some of these may be ignored):

"Name" : The main name adopted in this spreadsheet. This may differ from the names some might use, but one name is chosen for each song, preferrably an official one if it exists.
"Name_official" : This is a "boolean". It's 1 if the name listed in "Name" is official, or 0 if it's not.
"HQ Source(s)" : A simple string for all the Highest Quality sources. It may be a single name like "App" or multiples like "App + Youtube"
"Source Links": If the source comes from an accessible link, it is listed. Sometimes, multiple links are listed, but always in the same string! So this leads to broken links in the spreadsheet
"Composers": A string listing all the artists involved
"Link": A link to Youtube of the song.
"Alternate Names": A string listing alternate names
"Earliest Date": A date, if it is known, in the format YYYY/MM/DD. This formatting is importat so that it's exportable to the spreadsheet. If it's unknown, it's written as "?".
"Medias": All Club Penguin media where the song is found. EG. Club Penguin Island, Club Penguin: Game Day!
"Order": This is an arbitrary attempt at ordering songs in a chronological way. This is meant to be used with floats, and it it's later sorted into integers. For example, if two songs have orders 0.5 and 0.6, they'll be sorted from least to biggest, and then an integer count will follow. This is to avoid having to rewrite every song when changing a single song out of order.

Aditionally, there are some keys containing dictionary of the form "Media name Info". For example:

"CP Flash Info": {...}

The list of media currently listed are:

CP Flash, CP Flash Unused, Penguin Chat

The final goal of this list is to also contain the following media as complete as possible:

CPEPF, CPEPF Unused, CPEPFHR, Game Day, Game Day Unused, App, CPI

The data inside the media info is divided in the following keys:

"Order": This is named the same as the other one, but this is the ordering in the context of this specific media, while the other one is in the context of the whole series.
"Earliest Date": Likewise, this is the earliest data in this particular media.
"Related To": A string listing everything that links this song to the game. For example, in Club Penguin Flash it would be listing the rooms, the parties or minigames it played on.

And others to be defined

# Transforming the data into a spreadsheet

This repository was built having in mind that this data is better visualized as a spreadsheet. The python script uses Pandas and generates .tsvs, which are meant to be imported into Microsoft Excel, and the Visual Basic macros will clean the formatting.
