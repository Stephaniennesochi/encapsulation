class exam:
    def __init__(self,name,regno, score):
        self.name = name
        self.__regno = regno
        self.score = score
    def check_score(self):
        pass
exam1 = exam ("Sonia", "GOU/U22/CSC/850", "99")
print(f'My name is: {exam1.name}' )
print(f'My regno is: {exam1._exam__regno}')
print(f'My score is:{exam1.score}')



class exam:
    def __init__(self, name, regno, score):
        self.name = name
        self.__regno = regno
        self.score = score
    def check_score(self):
        print(f'Name: {self.name}')
        print(f'Regno: {self._exam__regno}')
        print (f'Score: {self.score}')
exam2 = exam ("Bethel", "GOU/U22/BTH/027", "65")
exam2.check_score()



