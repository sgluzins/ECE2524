# Sasha Gluzinski
# 905380453
# Intro to Unix - ECE 2524

import sys
import argparse
import fileinput
import shlex
import array
import pprint
from sys import argv


parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='*', type=str, default=sys.stdin)
parser.add_argument('-f','--data-file', nargs='*', help='path to the data file to read at startup')
parser.parse_args()


def printEntry(argm):
    i = 0
    for line in group[i]:
        print '\t'.join(line)        
        i = i + 1
   
def remove(arg):
    TermRemove = arg[0].split('=')
    i = 0
    j = 0
    a = []
    count = 0
    headCount = 0
    index = 0
    infoIndex = 0#counts which group its in
    aIndex = 0#counts which line it is in
    
    for line in info:
        if((TermRemove[1] == group[i][j][0])):
            if(TermRemove[0] == heading[index][0]):            
                a.append(i) 

        j = j + 1
        index +=1   
        if(j == len(heading)):
            j = 0
            i = i + 1
            
            if(index == len(heading)):
                index = 0
    
    for line in xrange(len(a)):
        del group[a[count]-count]
        count += 1
        
    for item in heading:
        openFile.write("%s\t" %item)        

    openFile.write("%s" %'\n')           

    for item in group:
        openFile.write("%s\n" %item)        

def list_all(arg):   
    i = 0
    j= 0
    a = []
    index = 0
    count = 0
    if len(arg) > 1 and arg[0] == 'with':
        listTerms = arg[1].split('=')
        if(len(arg) > 1 and arg[0] == 'with'):
            for line in xrange(len(info)):  
                if((listTerms[0] == heading[index][0]) and (listTerms[1] == group[i][j][0])):               
                    a.append(i)
                j = j+1
                index = index + 1
                if(j == len(heading)):
                    j = 0
                    i = i + 1
                    #index = index + 1
                    if (index == len(heading)):
                        index = 0                   
        for item in heading:
            openFile.write("%s\t" %item)
            
        openFile.write("%s" %'\n')       

        for line in xrange(len(a)):
            openFile.write("%s\n" %group[a[count]])
            count += 1  
              
    elif len(arg) == 0:
        for item in heading:
            openFile.write("%s\t" %item)
        openFile.write("%s" %'\n')       
        for item in group:
            openFile.write("%s\n" %item)    


 

toDo = {'remove': remove,'list_all': list_all, 'printEntry': printEntry}
openFile = open(argv[1], 'r+')

heading = []
info = []
fp = []
quan = []



i = 0
count = 0


for line in openFile:
    if(line != '\n'):
        heading.append(line.strip().split()) 
    else:        
        break
        
for line in openFile:
    if(line != '\n'):
        if line.isdigit():
            info.append(int(line.strip().splitlines()))
        else:
            info.append(line.strip().splitlines())
        count += 1
    elif(line == '\n'):
        continue 

#print info
######################################        
num = len(info)/len(heading)     
#print num 

######################################  
index = 0
index1 = 0



group1 = []     
group = []
a = []

index1 = 0
group.append([])
for line in info:
    if(index1 < len(heading)):
        group[index].append(line)
        index1 = index1 + 1
    else:
        index1 = 0
        index = index + 1
        group.append([])
        group[index].append(line)
        index1 = index1 + 1

index = 0
index1 = 0
outPrint = ''
b = 0


while True:
    try:
        inputCom = sys.stdin.readline()
        if inputCom.strip(): #try it later
            arguments = shlex.split(inputCom)
            command = arguments[0]
            arguments.pop(0)
        else:
            continue
    except KeyboardInterrupt:
        sys.exit(0)



    try:
        toDo[command](arguments)
    except KeyError as e:
        sys.stderr.write("command is invalid.")
