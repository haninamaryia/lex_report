#!/usr/bin/env python

import csv
from anytree import Node, RenderTree, NodeMixin


#choice=input("Choose action: 1:Tree, 2: Medication, 3: Unique Topics")


def Tree():
    print('\n\n\n')
    print('# '*50)
    print("This is a tree oftop 5 topics discussed in the particular dataset.")
    print("The children of each node are top 5 subjects discussed at the same time as the parent subject.")
    print('# '*50)
    print('\n\n\n')

    answer=input('choose dataset (news/abstracts/reddit/blog): ')
    answer=answer.lower()
    if answer.startswith('n'):
        answer="news"
    elif answer.startswith('a'):
        answer="abstracts"
    elif answer.startswith('r'):
        answer="reddit"
    elif answer.startswith('b'):
        answer="blog"
    else:
        print("invalid input")
        answer=None


    with open ("tree.csv") as f:

    #create a list of topic objects

        reader = csv.reader(f)
        mylist=list(reader)
        mylist.pop(0)

        source = Node(answer)


        #while the parent is the source node, add to the tree
        for line in mylist:
            if source.name == line[2]:
                temp = Node(line[1], parent=source)

                for otherline in mylist:
                    if temp.name == otherline[2] and otherline[0] == source.name:
                        othertemp = Node(otherline[1], parent=temp)

        f.close()
        for pre,fill, node in RenderTree(source):
            print("%s%s" % (pre, node.name))
def Topics(file):
    print('\n')
    print('# ' * 32)
    print('\n')
    print("This is the list of unique ADHD Topics discussed in the datasets.")
    print('\n')
    print('# ' * 32)
    print('\n')

    with open(file) as f:

        reader = csv.reader(f)
        mylist = list(reader)
        mylist.pop(0)

        return mylist

def Medication(file):
    print('\n')
    print('# '*32)
    print('\n')
    print("This is the list of all ADHD drugs discussed in the datasets.")
    print('\n')
    print('# '*32)
    print('\n')

    with open(file) as f:

        reader = csv.reader(f)
        mylist = list(reader)
        mylist.pop(0)

        i = 0

        while i<(len(mylist)-1):

            source = mylist[i][0]
            print("\n\n")
            print("ADHD medication mentionned in "+source.upper()+" :\n")

            while mylist[i][0]==source and i<(len(mylist)-1):
                print(mylist[i][1]+", sentiment: "+mylist[i][2])
                i=i+1

        return mylist

def noMatch(a, b, c, d):
    return [[x for x in a if ((x not in b) and (x not in c) and (x not in d))],
    [x for x in b if ((x not in a) and (x not in c) and (x not in d))],
    [x for x in c if ((x not in a) and (x not in b) and (x not in d))],
    [x for x in d if ((x not in b) and (x not in c) and (x not in a))]]


def Unique(mylist):
#mylist has to be
    sources=[[]]
    i=0
    for line in mylist:
        if i==0:
            sources[i].append(line[0])
            i=i+1
        else:
            if line[0] not in sources[i-1]:
                sources.append([])
                sources[i].append(line[0])
                i=i+1

    temp=sources[0][0]
    i=0
    for line in mylist:
        if temp==line[0]:
            sources[i].append(line[1])
        else:
            i=i+1
            temp=line[0]

    a,b,c,d=noMatch(sources[0],sources[1],sources[2],sources[3])
    lol=[a,b,c,d]
    print('\n')
    for i in range(4):

        print('unique elements in '+sources[i].pop(0).upper() + '\n')
        lol[i].pop(0)
        for el in lol[i]:
            print(el)
        print('\n')
        print('#' * 47)
        print('\n')



command=-1
print("\n")
print("----------------------------------------------------------------------------------------------------")
print(""" Welcome. This is a simple program showing my findings comparing discussions about ADHD scraped from 
news articles, research articles, reddit and blogs.""")
print("----------------------------------------------------------------------------------------------------")


while command!=0:
    print("\n")
    answer=input("Here are your choices: 1: Topics Tree, 2: Medication, 3: Unique Topics, 0: Quit")

    try:
        command=int(answer)
    except:
        print("you need to answer 1,2 or 0.")
        continue
    #topics tree
    if command==1:
        Tree()
        print("\n")
        lol=input("4 : go back, 0 : quit")
        try:
            command=int(lol)
        except:
            print("invalid input.")

        continue
    #medication/unique medication
    if command==2: 
        Medication("meds.csv")
        print("\n")
        lol = input("3 : unique medication, , 4 : go back, 0 : quit ")
        try:
            command=int(lol)
        except:
            print("invalid input.")

    #unique topics
    if command == 3:
        ok = Topics("topics.csv")
        Unique(ok)

        lol = input("4 : go back, 0 : quit ")
        try:
            command = int(lol)
        except:
            print("invalid input.")

        continue
    

