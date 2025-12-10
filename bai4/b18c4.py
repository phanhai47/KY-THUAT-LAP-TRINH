print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def tao_list_fibonacci(n):
    if n <= 0:
        return []
    a,b=0,1
    ds_fib=[]
    while a<n:
        ds_fib.append(a)
        a,b=b,a+b
    return ds_fib
try :
    n=int(input("Nhap so nguyen duong n: "))
    list_fib=tao_list_fibonacci(n)
    print("Danh sach Fibonacci nho hon",n,":",list_fib)
except ValueError:
    print("Vui long nhap so nguyen duong!")
