def temp_convert(c):return 9/5*c+32

def min_to_sec(m):return m*60

def km_to_m(k):return k*1000

temp=[34.5,56,24.5,76.4,55.5]
mins=[5,4,7,8,3,44]
km=[4,6,7,22,44]


print(list(map(temp_convert,temp)))
print(list(map(min_to_sec,mins)))
print(list(map(km_to_m,km)))