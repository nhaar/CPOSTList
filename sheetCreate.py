import json
import os
from openpyxl import Workbook
from openpyxl.styles import Font

def tableCreate(headers, dict):
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
    for x in range(length-1):
        table += '\n| '
        for y in newdict:
            table += newdict[y][x] + ' | '
    return table

Data_division = { ##If decide to change these names, must change in every JSON
                #If adding anything, make sure to add to Variables, and if needed, add exception when creating spreadsheet
    'General': {
        'Name' : [],
        'Name_official' : [],
        'Composers' : [],
        'Order' : [],
        'Link' : [],
        'HQ Source(s)' : [],
        'Source Links' : [],
        'Alternate Names' : [],
        'versions': [],
        'stock': []
    }
}

Order = {'General': {}}


##This dictionary is important, keys are the sheet names related to the name in the jsons. Order is order of sheet
sheetIs = {'Flash OST': 'CP Flash', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST' : 'Game Day', 'Unused Flash OST' : 'CP Flash Unused', 'App OST' : 'App', 'CPI Ost': 'CPI'}
mediasIs = {'Flash OST': 'Club Penguin', 'Penguin Chast OST' : 'Penguin Chat', 'Game Day OST': 'Club Penguin: Game Day!', 'Unused Flash OST': 'Club Penguin Unused', 'App OST': 'Club Penguin App', 'CPI Ost': 'Club Penguin Island'}

#Old medias list Medias = ['CP Flash', 'CP Flash Unused', 'CPEPF', 'Unused CPEPF', 'CPEPFHR', 'Game Day', 'Unused Game Day', 'CPI', 'Penguin Chat']
Medias = [sheetIs[k] for k in sheetIs]

#Variables = []
#for x in Data_division['General']:
#    Variables.append(x)
Variables = ['Name', 'Name_official', 'HQ Source(s)', 'Source Links', 'Composers', 'Link', 'Alternate Names', 'versions', 'stock']
for i in Medias:
    Data_division[i + ' Info'] = {'Name' : [], 'Name_official' : [], 'Composers' : [], 'Order' : [], 'Link' : [], 'Related To' : [], 'Alternate Names' : [], 'HQ Source(s)': [], 'Source Links' : [], 'Earliest Date' : [], 'files': [], 'uses': []}
    Order[i + ' Info'] = {}

directory = 'Song Data'

# Finding every file name

all_files = []
files = []
for x in os.walk(directory):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

# Iterating through every song

for x in files:
    print(x)
    newsong = json.load(open(directory+'/' +x, 'r'))
    for y in Medias:
        try:
            print(y)
            dummy = newsong[y + ' Info']
            for z in ['Earliest Date', 'Related To', 'files', 'uses']:
                try:
                    Data_division[y + ' Info'][z].append(newsong[y + ' Info'][z])
                except:
                    Data_division[y + ' Info'][z].append(None)
            for z in ['Name', 'Composers', 'Alternate Names', 'HQ Source(s)', 'Source Links', 'Name_official', 'Link']:
                print(z)
                try:
                    print('Hello')
                    Data_division[y + ' Info'][z].append(newsong[z])
                except:
                    Data_division[y + ' Info'][z].append(None)
            Order[y + ' Info'][newsong['Name']] = newsong[y + ' Info']['Order']
        except:
            pass
    for y in Variables:
        try:
            Data_division['General'][y].append(newsong[y])
        except:
            Data_division['General'][y].append(None)
    Order['General'][newsong['Name']] = newsong['Order']

# Fixing The Order Numbering

neworder = {}

for x in Order:
    neworder[x] = {}
    Order[x] = dict(sorted(Order[x].items(), key=lambda z:z[1]))
    i = 0
    for y in Order[x]:
        i += 1
        neworder[x][y] = i
    for y in Data_division[x]['Name']:
        Data_division[x]['Order'].append(neworder[x][y])

#sort data_division by order

newdata = {}

for x in Data_division:
    newdata[x] = {}
    for y in Data_division[x]:
        newdata[x][y] = []
    for i in range(1,len(Data_division[x]['Order'])+1):
        songno = Data_division[x]['Order'].index(i)
        for y in newdata[x]:
            newdata[x][y].append(Data_division[x][y][songno])


### Creating the spreadsheet

wb = Workbook()

# Configure base sheets

wb['Sheet'].title = 'Welcome'
wb.create_sheet('Downloads')

#Create Series OST's

#names

#data correlations

for k in sheetIs:
    wb.create_sheet(k)

#Extra sheets

cpseries = 'Series OST'

wb.create_sheet(cpseries)
wb.create_sheet('to-do')

#Fill data to media sheets

letters = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}

for k in sheetIs:
    i = 0
    for x in newdata[sheetIs[k] + ' Info']:
        j = 0
        if x != 'Source Links' and x != 'Name_official':
            i += 1
        for y in newdata[sheetIs[k] + ' Info'][x]:
            if x == 'Source Links':
                pass
            elif x == 'HQ Source(s)':
                j += 1
                wb[k][letters[i] + str(j)] = y
                if newdata[sheetIs[k] + ' Info']['Source Links'][j-1] != None:
                    wb[k][letters[i] + str(j)].hyperlink = newdata[sheetIs[k] + ' Info']['Source Links'][j-1]
                    wb[k][letters[i] + str(j)].style = "Hyperlink"
            elif x == 'uses':
                pass
            elif x == 'files':
                pass
            elif x == 'Name_official':
                j += 1
                if y:
                    wb[k][letters[i] + str(j)].font = Font(color='2E47AA')
                else:
                    wb[k][letters[i] + str(j)].font = Font(color='CC0000')
            elif x == 'Link':
                j += 1
                wb[k][letters[i] + str(j)] = y
                if y != None and y != '':
                    wb[k][letters[i] + str(j)].hyperlink = y
                    wb[k][letters[i] + str(j)].value = 'Link'
                    wb[k][letters[i] + str(j)].style = 'Hyperlink'
            else:
                j += 1
                wb[k][letters[i] + str(j)] = y

#Fill data to series sheet

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

i = 0
for k in newdata['General']:
    j = 0
    if k != 'Source Links' and k != 'Name_official':
        i += 1
    for x in newdata['General'][k]:
        if k == 'Source Links':
            pass
        elif k == 'versions':
            pass
        elif k == 'stock':
            pass
        elif k == 'HQ Source(s)':
            j += 1
            wb[cpseries][letters[i] + str(j)] = x
            if newdata['General']['Source Links'][j-1] != None:
                wb[cpseries][letters[i] + str(j)].hyperlink = newdata['General']['Source Links'][j-1]
                wb[cpseries][letters[i] + str(j)].style = "Hyperlink"
        elif k == 'Name_official':
            j += 1
            if x:
                wb[cpseries][letters[i] + str(j)].font = Font(color='2E47AA')
            else:
                wb[cpseries][letters[i] + str(j)].font = Font(color='CC0000')
        elif k == 'Link':
            j += 1
            wb[cpseries][letters[i] + str(j)] = x
            if x != None and x != '':
                wb[cpseries][letters[i] + str(j)].hyperlink = x
                wb[cpseries][letters[i] + str(j)].value = 'Link'
                wb[cpseries][letters[i] + str(j)].style = 'Hyperlink'
        else:
            j += 1
            wb[cpseries][letters[i]+str(j)] = x
    for x in newdata['General']['Name']:
        overall_order = newdata['General']['Name'].index(x)
        all_medias = []
        all_dates = []
        for y in sheetIs:
            if x in newdata[sheetIs[y] + ' Info']['Name']:
                order = newdata[sheetIs[y] + ' Info']['Name'].index(x)
                all_medias.append(mediasIs[y])
                all_dates.append(newdata[sheetIs[y] + ' Info']['Earliest Date'][order])
        medias_str = ''
        medias_str += all_medias[0]
        for media in range(1,len(all_medias)):
            medias_str += ', ' + all_medias[media]
        the_date = ''
        lowestdate = 3000000000000000000
        for date in all_dates:
            date_number = dateToNumber(date)
            if lowestdate > date_number and date_number != False:
                lowestdate = date_number
                the_date = date
        if lowestdate == 3000000000000000000:
            the_date = '?'
        wb[cpseries]['G' + str(overall_order+1)] = medias_str
        wb[cpseries]['H' + str(overall_order+1)] = the_date
        
wb.save('sheet.xlsx')

#Creating the doc

stock_composers = ["Paul Sumpter"]
original_composers = ["Chris Hendricks", "Friction Music", "Norrie Henderson", "Rory", "Michael Campitelli"]
licensed_composers = ["John Williams"]

doc = open('WIPnotes.md', 'w')
doc_text = ''

gen = newdata['General']

for x in gen['Order']:
    doc_text += '\n# ' + gen['Name'][x-1]
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
        doc_text += '\nThis song is'
    if songtype == 0:
        doc_text += ' an original song.'
    elif songtype == 1:
        try:
            stockinfo = gen['stock'][x-1]['info']
            doc_text += ' a stock song from [' + stockinfo['origin'] + '](' + stockinfo['link'] + ')'
        except:
            pass
    elif songtype == 2:
        doc_text += ' of unknown origins.'
    elif songtype == 3:
        doc_text += ' a licensed song.'
    versions = gen['versions'][x-1]
    if versions != None:
        doc_text += '\n## Versions'
        doc_text += '\n' + tableCreate(('Name', 'Info', 'Source'), versions)
    for y in Medias:
        y = y + ' Info'
        if gen["Name"][x-1] in newdata[y]["Name"]:
            mediaorder = newdata[y]["Name"].index(gen["Name"][x-1])
            doc_text += '\n##' + y
            try:
                files = newdata[y]['files'][mediaorder]
                doc_text += '\n' + tableCreate(('Name', 'Info'), files)
            except:
                pass
    doc_text += '\n'

doc.write(doc_text)
doc.close()