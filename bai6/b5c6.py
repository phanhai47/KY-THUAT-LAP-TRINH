print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

class py_solution:
    #dao nguoc tu trong chuoi
    def reversed_word(self, s):
        #1.Tach chuoi thanh danh sach cac tu
        word = s.split()
        #2.Dao nguoc thu tu
        reversed_word =word[::-1]
        return ' '.join(reversed_word)
    
solution=py_solution()
print(solution.reversed_word('hello .py'))