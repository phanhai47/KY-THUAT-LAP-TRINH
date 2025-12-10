print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def sang_eratosthenes(gioi_han):
    is_prime = [True] * (gioi_han+1)
    is_prime[0] = is_prime[1] = False 

    p=2
    while(p*p <= gioi_han):
        if is_prime[p]:
            for i in range(p*p, gioi_han, p):
                is_prime[i] = False
        p += 1
    so_nguyen_to = [i for i in range(gioi_han) if is_prime[i]]
    return so_nguyen_to

GIOI_HAN = 1000000

ds_nguyen_to = sang_eratosthenes(GIOI_HAN-1)
P = tuple(ds_nguyen_to)
print(f"Số lượng số nguyên tố nhỏ hơn {GIOI_HAN}: {len(P)}")
    
