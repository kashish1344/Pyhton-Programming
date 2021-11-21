file= open('file_1.txt','w')
#data ='hello Data'

data =['hello\n','hi\n','hey\n']
#file.write(data)
file.writelines(data)
file.close()