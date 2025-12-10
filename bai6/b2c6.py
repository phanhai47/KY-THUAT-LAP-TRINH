print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

class HinhChunhat(object):
    def __init__(self, chieu_dai, chieu_rong):
            self.chieu_dai =chieu_dai
            self.chieu_rong=chieu_rong
    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    
hcn=HinhChunhat(8,5)
print(hcn.dien_tich())