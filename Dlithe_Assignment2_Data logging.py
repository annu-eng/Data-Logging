import xlwt  #used to perform operations on spreadsheets
from xlwt import Workbook #The Workbook class represents the entire spreadsheet 
                         #as you see it in Excel and internally it represents the Excel file as it is written on disk.

# To create some space for next entry.

def spacer():
    for l in range(5):
        print(" ")

# funtion which enters user data into Excel file
def entriez(i):

    # input data
    name=input("Name: ")
    place=input("Place: ")
    contact_no=input("Contact no: ")
    body_temp=input('Body temperature:')

    # Entering details of a particular input to the file.
    sheet1.write(i, 0, name)
    sheet1.write(i, 1, place)
    sheet1.write(i, 2, contact_no)
    sheet1.write(i, 3, body_temp)

# main program.

# Workbook is created
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

# creating the columns required.
sheet1.write(0, 0, 'Name')
sheet1.write(0, 1, 'Place')
sheet1.write(0, 2, 'Contact number')
sheet1.write(0, 3, 'Body temperature')

# creating a customized file name.
n=input('enter the name of the file you want to create')
g=n+'.xls'

i=1                                                    # initial value being declared.

while(1):                                              # loop to keep the process ongoing.
    f=''

    entriez(i)                                         # function call.
    spacer()
    f=input("Enter 'yes' to get the final sheet. Else to continue, enter any key")
    if f=='yes':
        wb.save(g)                                     # saving the file.
        print(f'''
        your file is saved as '{g}'
               '''  )
        break
    i+=1                                               # incrementing the counter for next entry.

