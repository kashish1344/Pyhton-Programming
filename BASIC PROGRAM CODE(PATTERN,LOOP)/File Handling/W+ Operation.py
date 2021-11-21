file=open("file_2.txt",'r+')
data = file.read()
print(data)

file.write('Hello user 2')
file.close()