from array import *
import random
import time

List_size = 8
List = [['o']*List_size for i in range(List_size)]
start_time = time.time()
points = 15
Lost = 0

def StartingCommunication():
    print("Author:Anastasiya Beliashchuk")
    print("Tic-tac-toe game ")

def EndingCommunication():
    print("WIN")

def ListOutput():
    print(" ", end=" ")
    for l in range(List_size):
        print(l+1, end=" ")
    print()
    rownumber = 1
    for i in List:
        print(rownumber, end=" ")
        for j in i:
            print(j, end=" ")
        print()
        rownumber = rownumber + 1

def RowColumnInput():
    global Row, Column 
    Row = int(input("Row number: "))-1
    Column = int(input("Column number: "))-1

def ListModification():
    if List[Row][Column] == '#':
        return 0
    List[Row][Column] = 'x'
    if Row != 7: 
        if List[Row+1][Column] == 'x':
            List[Row+1][Column] = 'o' 
        if List[Row+1][Column] == 'o':
            List[Row+1][Column] = 'x'        
    if Row != 0:
        if List[Row-1][Column] == 'x':
            List[Row-1][Column] = 'o' 
        if List[Row-1][Column] == 'o':
            List[Row-1][Column] = 'x'
    if Column !=7: 
        if List[Row][Column+1] == 'x':
            List[Row][Column+1] = 'o' 
        if List[Row][Column+1] == 'o':
            List[Row][Column+1] = 'x'
    if Column !=0: 
        if List[Row][Column-1] == 'x':
            List[Row][Column-1] = 'o' 
        if List[Row][Column-1] == 'o':
            List[Row][Column-1] = 'x'

def WinorNot():
    if Lost == 1:
        return 0 
    for i in List:
        for j in i:
            if j == 'o' : return 1
    return 0

def UnusedField():
    NumberofUnusedFields = random.randint(0, List_size)
    print(" Number of unused fields -", NumberofUnusedFields)
    k = 0
    while k < NumberofUnusedFields : 
        RandomRow = random.randint(0, List_size-1)
        RandomColumn = random.randint(0, List_size-1)
        List[RandomRow][RandomColumn] = '#'
        k = k + 1

def TimeGame():
    seconds = time.time() - start_time
    print("You play for %s seconds " % (seconds))
    minutes = seconds // 60
    print("Remaining points - %s" %(points - minutes))
    if (points - minutes) == 0: 
        Lost = 1



StartingCommunication()
UnusedField()
a = WinorNot()
while a>0:
    ListOutput()
    RowColumnInput()
    ListModification()
    a = WinorNot()
    TimeGame()

EndingCommunication()