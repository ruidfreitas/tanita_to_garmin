import csv
import shutil
import sys

# Open file from tanita ds Card and read all content
print ('*****************************************\n')
print ('* Welcome to Tanita BC-601 to Garmin.csv*\n')
print ('*****************************************\n')


drive = input ('Please insert the drive letter of the Sdcard :\n')
path = (drive + ':\\TANITA\\GRAPHV1\\DATA\\DATA1.CSV')


with open(path, 'rt')as inf:
    reader = csv.reader(inf, delimiter=",")
    allcolumns = list(zip(*reader))

    # Date Colunm
    tab = 'Date'
    date = (list(allcolumns[13]))
    date[0] = tab

    # Weight Colunm
    tab = 'Weight'
    weight = (list(allcolumns[27]))
    weight[0] = tab

    # BMI Colunm
    tab = 'BMI'
    bmi = (list(allcolumns[29]))
    bmi[0] = tab

    # Fat Colunm
    tab = 'Fat'
    fat = (list(allcolumns[41]))
    fat[0] = tab


rows = zip(date,weight,bmi,fat)

out_put = csv.writer(open("garmin.csv",'w'))

for row in rows:
    out_put.writerow(row)





# for val in weight:
#   out_put.writerow([val])

# garmin = tanita

# shutil.copyfileobj(weight, sys.stdout)
    print(date)
