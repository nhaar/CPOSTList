import json
import os

all_files = []
files = []
for x in os.walk('Song Data'):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

basic_features = {'Name' : 'name', "Name_official" :  'truename', 'Composers': 'artists', 'Alternate Names' : 'altnames',
'HQ Source(s)': 'sources', 'Source Links': 'sourcelinks', "Order" : 'order', "Link": 'link', 'versions' : 'versions'}

medias = ['pc', 'cp', 'cpu', 'gd', 'app', 'cpi']

media_features = {
'Order' : 'order',
'files' : 'files',
'uses' : 'uses',
}

for x in files:
    oldjson = json.load(open('Song Data/' + x, 'r'))
    newjson = {}
    for y in basic_features:
        try:
            newjson[basic_features[y]] = oldjson[y]
        except:
            pass
    for y in medias:
        try:
            media_dict = oldjson[y]
            newjson[y] = {}
            for z in media_features:
                try:
                    newjson[y][media_features[z]] = media_dict[z]
                except:
                    pass
        except:
            pass
    jsonwrite = open('Song Data/' + x, 'w')
    jsonwrite.write(json.dumps(newjson, indent=4))
    jsonwrite.close()