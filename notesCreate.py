## Get the data

exec(open('dataBuild.py').read())

#Creating the doc

stock_composers = ["Paul Sumpter"]
original_composers = ["Chris Hendricks", "Friction Music", "Norrie Henderson", "Rory", "Michael Campitelli"]
licensed_composers = ["John Williams"]

doc = open('WIPnotes.md', 'w')
doc_text = ''

gen = newdata['General']

for x in gen['Order']:
    song_text = ''
    if gen['Composers'][x-1] in original_composers:
        songtype = 0
    elif gen['Composers'][x-1] in stock_composers:
        songtype = 1
    elif gen['Composers'][x-1] in licensed_composers:
        songtype = 3
    elif gen['Composers'][x-1] == '?':
        songtype = 2
    else:
        songtype = None
    if songtype != None:
        song_text += '\nThis song is'
    if songtype == 0:
        song_text += ' an original song.'
    elif songtype == 1:
        try:
            stockinfo = gen['stock'][x-1]['info']
            song_text += ' a stock song from [' + stockinfo['origin'] + '](' + stockinfo['link'] + ')'
        except:
            song_text += ' a stock song.'
    elif songtype == 2:
        song_text += ' of unknown origins.'
    elif songtype == 3:
        song_text += ' a licensed song.'
    versions = gen['versions'][x-1]
    if versions != None:
        song_text += '\n## Versions'
        song_text += '\n' + tableCreate(('Name', 'Info', 'Source'), versions)
    for y in Medias:
        media_text = ''
        y = y + ' Info'
        if gen["Name"][x-1] in newdata[y]["Name"]:
            mediaorder = newdata[y]["Name"].index(gen["Name"][x-1])
            try:
                files = newdata[y]['files'][mediaorder]
                media_text += '\n' + tableCreate(('Name', 'Info'), files)
            except:
                pass
        if media_text != '':
            song_text += '\n## ' + y
            song_text += media_text
    song_text += '\n'
    if song_text != '\n':
        doc_text += '\n# ' + gen['Name'][x-1]
        doc_text += song_text

doc.write(doc_text)
doc.close()