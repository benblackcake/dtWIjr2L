from BasePhone import phone

class taiwanPhone(phone):

    def special_freature(self,n):
        return self._fib(n)

    def _fib(self,n):
        if n == 0 or n == 1:
            return n
        else:
            return self._fib(n-1)+self._fib(n-2)