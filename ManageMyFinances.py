import fileinput
import csv
import pygsheets
import pandas as pd
#authorization

Month_Number_Str = '01'

Month = 'January'

Input_File_Name = 'TD_' + Month + '.csv'

path = '/Users/callum/PycharmProjects/ManageMyFinances'

gc = pygsheets.authorize(service_file='/Users/callum/PycharmProjects/ManageMyFinances/managemyfinances-a5cb52b968f8.json')
# Create empty dataframe
nf = pd.DataFrame()
af = pd.DataFrame()
df = pd.DataFrame()

# Create a column
def csv_file_editor(fileinput):
    myfile = open('data/' + fileinput)
    type(myfile)
    csvreader = csv.reader(myfile)
    header = []
    header = next(csvreader)
    Name = []
    Amount = []
    Date = []
    for row in csvreader:
        if row[0][:2] == Month_Number_Str:
            if row[3] == "":
                Name.append(row[1])
                Amount.append(row[2])
                Date.append(row[0])
    nf['name'] = Name
    af['amount'] = Amount
    df['date'] = Date
    sh = gc.open(Month)
    wks = sh[0]
    wks.set_dataframe(nf, (1, 1))
    wks.set_dataframe(af, (1, 2))
    wks.set_dataframe(df, (1, 3))

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)


#select the first sheet

#update the first sheet with df, starting at cell B2.
csv_file_editor('TD_January.csv')

