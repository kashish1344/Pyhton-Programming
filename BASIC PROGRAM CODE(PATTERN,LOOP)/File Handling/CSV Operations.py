import csv
#data = [
#    ['First Name', 'Last Name'],
#    ['Sachin', ' Tandulkar'],
#   ['Virat', 'Kohli'],
#    ['MS' ,' Dhoni']

#]

#with open('data.csv','w',newline='') as file:
 #   obj= csv.writer(file)
  #  for item in data:
   #     obj.writerow(item)

with open ('data.csv') as file:
    obj= csv.reader(file)
    for row in obj:
        print(row)