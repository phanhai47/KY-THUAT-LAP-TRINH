print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

def squae(n):
    return n * n

def cube(n):
    return n * n * n

def aveage(values):
    nvals = len(values)
    sum_val =0.0
    for v in values:
        sum_val += v
    return float(sum_val) / nvals