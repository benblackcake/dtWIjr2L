from BasePhone import phone

class taiwanPhone(phone):

    def special_freature(self,n):
        return self.fib(n)

    def fib(self,n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)