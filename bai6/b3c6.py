print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")
class Nguoi(object):
    def getGender(self):
        return "Unkonw"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nu"
    
#tao doi tuong
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())