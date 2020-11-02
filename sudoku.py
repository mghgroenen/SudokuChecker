from time import sleep

def rowinput(row):      # Inputting rows. Invoked in sudinput().
    try:
        rowlist = [int(i) for i in str(row)]
        assert len(rowlist) == 9
        return rowlist
    except:
        rowinput(input("Invalid input. Try again: "))

def sudinput():     # Creation of 9 rows and a matrix
    global row1, row2, row3, row4, row5, row6, row7, row8, row9, megarow
    row1 = rowinput(input("Enter row 1: "))
    row2 = rowinput(input("Enter row 2: "))
    row3 = rowinput(input("Enter row 3: "))
    row4 = rowinput(input("Enter row 4: "))
    row5 = rowinput(input("Enter row 5: "))
    row6 = rowinput(input("Enter row 6: "))
    row7 = rowinput(input("Enter row 7: "))
    row8 = rowinput(input("Enter row 8: "))
    row9 = rowinput(input("Enter row 9: "))
    megarow = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

def checkrows(row):     # Checking a row
    for i in range(1,10):
        if i not in row:
            return False
    return True

def checkcols():        #Checking columns
    column = []
    for i in range(9):
        for row in megarow:
            column.append(row[i])
        for i in range(1,10):
            if i not in column:
                return False
        column = []
    return True

def checksqrs():        #Checking squares
    sqr1 = row1[:3] + row2[:3] + row3[:3]
    sqr2 = row1[3:6] + row2[3:6] + row3[3:6]
    sqr3 = row1[6:] + row2[6:] + row3[6:]
    sqr4 = row4[:3] + row5[:3] + row6[:3]
    sqr5 = row4[3:6] + row5[3:6] + row6[3:6]
    sqr6 = row4[6:] + row5[6:] + row6[6:]
    sqr7 = row7[:3] + row8[:3] + row9[:3]
    sqr8 = row7[3:6] + row8[3:6] + row9[3:6]
    sqr9 = row7[6:] + row8[6:] + row9[6:]
    megalist = [sqr1, sqr2, sqr3, sqr4, sqr5, sqr6, sqr7, sqr8, sqr9]
    for sqr in megalist:
        for i in range(1, 10):
            if i not in sqr:
                return False
    return True

###########Start of the actual script###########
sudinput()

for row in megarow:
    if checkrows(row) == False:
        row_check = False
        break
    row_check = True
col_check = checkcols()
sqr_check = checksqrs()

if row_check == True and col_check == True and sqr_check == True:
    print("Yes")
else:
    print("No")
    if row_check == False:
        print("Row check failed.")
    if col_check == False:
        print("Column check failed.")
    if sqr_check == False:
        print("Square check failed.")

close = input("Press any key to exit.")
