## Get the data

exec(open('dataBuild.py').read())

#Creating the doc

def dicTableFormat(x):
    newdict = {'id' : []}
    for key in x:
        for header in x[key]:
            newdict[header] = []
        break
    for key in x:
        newdict['id'].append(key)
        for header in x[key]:
            newdict[header].append(x[key][header])
    return newdict

def tableCreate(headers, dict):
    dict = dicTableFormat(dict)
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

stock_composers = ["Paul Sumpter",
"Doug Brown, Harmonious Wail",
"Bjorn Lynne"
]
original_composers = ["Chris Hendricks", "Friction Music", "Norrie Henderson", "Rory", "Michael Campitelli"]
licensed_composers = ["John Williams"]

doc = open('notes.md', 'w')
doc_text = ''

order_assist = {}
for x in all_data:
    order_assist[all_data[x]['Order']] = all_data[x]['Name']
order_assist = dict(sorted(order_assist.items()))

ordered_data = {}
for x in order_assist:
    for y in all_data:
        if all_data[y]['Name'] == order_assist[x]:
            ordered_data[y] = all_data[y]
            break

for x in ordered_data: #all_data is from dataBuild.py
    song = all_data[x]
    song_text = ''
    composer = song['Composers']
    if composer in original_composers:
        songtype = 0
    elif composer in stock_composers:
        songtype = 1
    elif composer in licensed_composers:
        songtype = 3
    elif composer == '?':
        songtype = 2
    else:
        songtype = None
    if songtype != None:
        song_text += '\nThis song is'
    if songtype == 0:
        song_text += ' an original song.'
    elif songtype == 1:
        try:
            stockinfo = song['stock']['info']
            song_text += ' a stock song from [' + stockinfo['origin'] + '](' + stockinfo['link'] + ').'
        except:
            song_text += ' a stock song.'
        try:
            sale = song['stock']['sale']
            song_text += '\n## Stock Information\n The following versions were for sale:\n'
            for x in sale:
                song_text += '- ' + x + '\n'
        except:
            pass
    elif songtype == 2:
        song_text += ' of unknown origins.'
    elif songtype == 3:
        song_text += ' a licensed song.'
    try:
        versions = song['versions']
        if versions != None:
            song_text += '\n## Versions'
            song_text += '\n' + tableCreate(('Name', 'Info', 'Source'), versions)
    except:
        pass
    for y in medias:
        media_text = ''
        y = y
        try:
            mediainfo = song[y + ' Info']
            files = mediainfo['files']
            media_text +='\n## Files'
            media_text += '\n' + tableCreate(('Name', 'Info'), files)
        except:
            pass
        if media_text != '':
            song_text += '\n## ' + medias[y]['media'] + ' Information'
            song_text += media_text
    song_text += '\n'
    if song_text != '\n':
        doc_text += '\n# ' + song['Name']
        doc_text += song_text

doc.write(doc_text)
doc.close()