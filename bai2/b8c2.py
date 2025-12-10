print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

a,b=1,2
total = 0

print("fibonace nho hon 4000000")
while b < 4000000:
    print (b, end = ', ')
    if b % 2 == 0:
        total += b
    a,b = b, a + b
print ("tong cac so chan trong day fibonace nho hon 4000000 la: ", total)