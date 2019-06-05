from BasePhone import phone

class googlePhone(phone):

    def special_freature(self,li):
        sum=1;
        for i in range(0,len(li)):
            sum*=li[i]
        return sum