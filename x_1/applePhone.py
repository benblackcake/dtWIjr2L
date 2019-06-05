from BasePhone import phone
from math import factorial

class applePhone(phone):
    def special_freature(self,n,m):
        return self.calc_arrangement(n,m)


    def calc_arrangement(self,n, m):
        return factorial(n)/factorial(n-m)


