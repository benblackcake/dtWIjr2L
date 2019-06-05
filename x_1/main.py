from googlePhone import googlePhone
from taiwanPhone import taiwanPhone
from applePhone import applePhone

if __name__=='__main__':
    ######
    li=[3,5,7]
    google=googlePhone(10,3,5)
    print(google.special_freature(li))
    ######
    taiwan=taiwanPhone(20,1,3)
    print(taiwan.special_freature(33))
    ######
    apple=applePhone(30,2,10)
    print(apple.special_freature(5,3))