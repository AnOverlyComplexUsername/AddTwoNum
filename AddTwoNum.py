a,b = '51900000000000000000000020', '51900000000000000000000020'


def add(a,b):
     
     result = ''
     maxLength = 0
     carry = 0
     #difference = 0
     #this is a change
     if len(a) > len(b):
         maxLength = len(a)
         b = b.zfill(len(a))
     else:
         maxLength = len(b)
         a = a.zfill(len(b))
         
     for i in range(maxLength-1, -1, -1):
         tempNum = int(a[i]) + int(b[i]) + carry
         if(tempNum > 9 and i != 0):
             tempNum = tempNum - 10
             carry = 1
         else:
            carry = 0
         
         result = str(tempNum) + result
            
            
     return result
sum = add(a,b)
print(a, '+', b, '=', sum)