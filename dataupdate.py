from json import loads, dumps
import os

def IsValidDate(x):
    year = 0
    day = 0
    month = 0
    foundFirst = False
    foundSecond = False
    for i in x:
        if foundFirst:
            if foundSecond:
                day += 1
            else:
                if i == '/':
                    foundSecond = True
                else:
                    month += 1
        else:
            if i == '/':
                foundFirst = True
            else:
                year += 1
    return (year == 4) and (day == 2) and (month == 2) and foundFirst and foundSecond

def DateStrToVal(x):
    val = ''
    for y in x:
        if y != '/':
            val += y
    return int(val)

path = 'Song Data'

all_files = []
files = []
for x in os.walk(path):
    all_files.append(x)

for x in all_files[0][2]:
    files.append(x)

default_date = '2018/12/20'

for thing in files:
    test = 'Song Data/' + thing

    medias = ['cp', 'cpu', 'pc', 'gd', 'cpi', 'app']

    original = loads(open(test, 'r').read())

    try:
        del original['order']
    except:
        pass

    for x in medias:
        try:
            target = original[x]
            del target['order']
            uses = target['uses']
            dates = []
            relateds = []
            for x in uses:
                date = x['date']
                if IsValidDate(date):
                    dates.append(x['date'])
                else:
                    dates.append(default_date)
                usage = x['use']
                if usage != '' and usage != '?':
                    relateds.append(usage)
            lowestvalue = 30000000
            lowpos = 0
            i = 0
            for x in dates:
                this_date = DateStrToVal(x)
                if this_date < lowestvalue:
                    lowestvalue = this_date
                    lowpos = i
                i += 1
            target['date'] = dates[lowpos]
            related_to = ''
            first = True
            for x in uses:
                usage = x['use']
                if first:
                    related_to += usage
                    first = False
                else:
                    related_to += ', ' + usage
            target['uses'] = related_to
            if target['date'] == default_date:
                target['truedate'] = 0
            else:
                target['truedate'] = 1
        except:
            pass

    new = open(test, 'w')
    new.write(dumps(original, indent=4))
    new.close()
