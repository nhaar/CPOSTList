from shutil import move
import os.path

path = 'Song Data/'

dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

test = '8bit'

for x in dirs:
    move(path + x + '/data.json', path + x + '.json')
