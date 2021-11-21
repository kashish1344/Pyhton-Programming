try:
    file = open('file_1.txt','w')
    file.write("Hello User")
    data = file.read()
    print(data)
except BaseException as exc:
    print('Finally always Execute')
    print(exc)
finally:
    file.close()