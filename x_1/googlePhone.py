from BasePhone import phone

class googlePhone(phone):

    def special_freature(self,list):
        sum=1;
        for i in range(0,len(list)):
            sum*=list[i]
        return sum