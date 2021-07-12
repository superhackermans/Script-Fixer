from os import listdir
from os.path import isfile, join
from words import *
from pdb import set_trace as st
#
INPUT = "./"

def newfilename(filename):
    dotIndex = filename.rfind(".")
    return filename[:dotIndex]+" FIXED.txt"

files = [f for f in listdir(INPUT) if isfile(join(INPUT, f))]
try:
    files.remove('main.py')
    files.remove('words.py')
    files.remove('.DS_Store')
except:
    ValueError

for file in files:
    print(f'Processing "{file}"')

    fileloc = INPUT+file
    newfileloc = newfilename(file)

    #input file
    fin = open(fileloc, "rt")
    #output file to write the result to
    fout = open(newfileloc, "wt")

    for line in fin:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        fout.write(line)
    fin.close()
    fout.close()

