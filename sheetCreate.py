from openpyxl import Workbook
from openpyxl.styles import Font

## Get the data

exec(open('dataBuild.py').read())

## Define what data is important for the tabs

headers = {
    'all': [ #Headers for both media and series
    'Name',
    'Name_official',
    'Composers',
    'Link',
    'Source Links',
    'HQ Source(s)',
    'Alternate Names'
    ],
    'media': [ #Headers only for medias
    'Related To',
    'Order',
    'Earliest Date'
    ],
    'series': [ #Headers only for series (all medias tab)
        'Order',
        'Earliest Date',
        'Medias'
    ]
}

series_order = { #to-do: Merge these two order dicts with the one above later
    1 : 'Name',
    2 : 'Composers',
    3 : 'Order',
    4 : 'Link',
    5 : 'HQ Source(s)',
    6 : 'Alternate Names',
    7 : 'Medias',
    8 : 'Earliest Date'
}

tabs_order = {
    1 : 'Name',
    2 : 'Composers',
    3: 'Order',
    4: 'Link',
    5: 'Related To',
    6: 'Alternate Names',
    7 : 'HQ Source(s)',
    8 : 'Earliest Date'
}

## Format data into tab styles

tabs = {'series': {}}

for x in medias: #medias is from dataBuild.py
    tabs[x] = {}

for x in headers['all']:
    for y in tabs:
        tabs[y][x] = []
for x in headers['media']:
    for y in medias:
        tabs[y][x] = []
for x in headers['series']:
    tabs['series'][x] = []

ordering = {} #To fix order later
for x in tabs:
    ordering[x] = {}

# Iterate through every song to populate the tabs

for x in all_data: #all_data is form dataBuild.py
    song = all_data[x]
    present_medias = []
    for media in medias:
        try:
            dummy = song[media + ' Info']
            present_medias.append(media)
            usages = dummy['uses']
            use_str = ''
            for thing in usages:
                use_str += usages[thing]['use']
            if use_str[len(use_str)-1] == ' ':
                all_data[x][media + ' Info']['Related To'] = use_str[:-1]
            else:
                all_data[x][media + ' Info']['Related To'] = use_str
        except:
            pass
    for media in present_medias:
        ordering[media][song['Name']] = song[media + ' Info']['Order']
        for header in headers['media']:
            if header != 'Order':
                try:
                    tabs[media][header].append(song[media + ' Info'][header])
                except:
                    tabs[media][header].append(None)
    for header in headers['all']:
        try:
            tabs['series'][header].append(song[header])
        except:
            tabs['series'][header].append(None)
        for media in present_medias:
            try:
                tabs[media][header].append(song[header])
            except:
                tabs[media][header].append(None)
    for header in ['Earliest Date']:
        try:
            tabs['series'][header].append(song[header])
        except:
            tabs['series'][header].append(None)
    present_medias = [medias[l]['media'] for l in present_medias]
    media_str = ''
    for x in present_medias:
        media_str += ', ' + x
    tabs['series']['Medias'].append(media_str[2:len(media_str)])
    ordering['series'][song['Name']] = song['Order']


# Fix the non intenger orders

neworder = {}

for x in ordering:
    neworder[x] = {}
    ordering[x] = dict(sorted(ordering[x].items(), key=lambda z:z[1]))
    i = 0
    for y in ordering[x]:
        i += 1
        neworder[x][y] = i
    for y in tabs[x]['Name']:
        tabs[x]['Order'].append(neworder[x][y])

# Sort tabs by order

orderedtabs = {}

for x in tabs:
    orderedtabs[x] = {}
    for y in tabs[x]:
        orderedtabs[x][y] = []
    for i in range(1,len(tabs[x]['Order'])+1):
        songno = tabs[x]['Order'].index(i)
        for y in orderedtabs[x]:
            orderedtabs[x][y].append(tabs[x][y][songno])

### Creating the spreadsheet

wb = Workbook()

# Configure base sheets

wb['Sheet'].title = 'Welcome'
wb.create_sheet('Downloads')

#Create Series OST's

for k in medias:
    wb.create_sheet(medias[k]['tab'])

#Extra sheets

cpseries = 'Series OST'

wb.create_sheet(cpseries)
wb.create_sheet('to-do')

#Fill data to media sheets

letters = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}

for k in medias:
    tab = medias[k]['tab']
    for i in range(1, len(tabs_order)+1):
        column = orderedtabs[k][tabs_order[i]]
        for j in range(1,len(column)+1):
            cell = letters[i] + str(j)
            if tabs_order[i] == 'Name':
                wb[tab][cell].value = column[j-1]
                if orderedtabs[k]['Name_official'][j-1] == 1:
                    wb[tab][cell].font = Font(color='2E47AA')
                else:
                    wb[tab][cell].font = Font(color='CC0000')
            elif tabs_order[i] == 'HQ Source(s)':
                wb[tab][cell] = column[j-1]
                if orderedtabs[k]['Source Links'][j-1] != None:
                    wb[tab][cell].hyperlink = orderedtabs[k]['Source Links'][j-1]
                    wb[tab][cell].style = "Hyperlink"
            elif tabs_order[i] == 'Link':
                if column[j-1] != "" and column[j-1] != None:
                    wb[tab][cell].hyperlink = column[j-1]
                    wb[tab][cell].value = 'Link'
                    wb[tab][cell].style = "Hyperlink"
            else:
                wb[tab][cell] = column[j-1]

#Fill data to series sheet
k = 'series'
tab = cpseries
for i in range(1, len(series_order)+1):
    column = orderedtabs[k][series_order[i]]
    for j in range(1,len(column)+1):
        cell = letters[i] + str(j)
        if series_order[i] == 'Name':
            wb[tab][cell].value = column[j-1]
            if orderedtabs[k]['Name_official'][j-1] == 1:
                wb[tab][cell].font = Font(color='2E47AA')
            else:
                wb[tab][cell].font = Font(color='CC0000')
        elif series_order[i] == 'HQ Source(s)':
            wb[tab][cell] = column[j-1]
            if orderedtabs[k]['Source Links'][j-1] != None:
                wb[tab][cell].hyperlink = orderedtabs[k]['Source Links'][j-1]
                wb[tab][cell].style = "Hyperlink"
        elif series_order[i] == 'Link':
            wb[tab][cell].hyperlink = column[j-1]
            wb[tab][cell].value = 'Link'
            wb[tab][cell].style = "Hyperlink"
        else:
            wb[tab][cell] = column[j-1]

def dateToNumber(x):
    if x == "?":
        return False
    year = 0
    month = 0
    day = 0
    foundYear = False
    foundMonth = False
    for char in x:
        if char == "/":
            if foundYear:
                foundMonth = True
            else:
                foundYear = True
        else:
            if foundYear:
                if foundMonth:
                    day = day * 10 + int(char)
                else:
                    month = month * 10 + int(char)
            else:
                year = year * 10 + int(char)
    return day + month * 100 + year * 10000
        
wb.save('sheet.xlsx')