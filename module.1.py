#1.Printing a pattern                                                 sample input:  pattern(5)                          no. of columns
#2.printing reverse,sum and even or odd of a number                   sample input:  rse(511)                            number
#3.given string is an anagram or not                                  sample input:  anagram("listen","silent")          string,string
#4.calculating current bill                                           sample input:  current(55)                         number of units
#5.printing fibonacci series                                          sample input:  fab(5)                              number
#6.next prime number                                                  sample input:  prime(5)                            number
#7.excpetion handling                                                 sample input:  fun1(77)                            number
#8.reversing the string without changing the special char index       sample input:  sep("py@t^hon%")                    string including special characters
#9.Encryption                                                         sample input:  encode("input",4)                   string and key value
#10.Decryption                                                        sample input:  decode("khoor",3)                   string and key value
def pattern(a):
    n=65
    for i in range(0,a):
        for j in range(0,i+1):
            print(chr(n),end=' ')
            n=n+1
        print()

def rse(a):
    sum=0
    rem=0
    rev=0
    while(a>0):
        rem=a%10
        rev=(rev*10)+rem
        sum=sum+rem
        a=a//10
    print("reverse=",rev)
    print("sum=",sum)    
    if(sum%2==0):
        print("Even")
    else:
        print("Odd")

def anagram(a,b):
    if(sorted(a)==sorted(b)):
        print("Anagram")
    else:
        print("Not")

def current(units):
    bill=0
    if(units<=50):
        bill=units*1.40
    elif(units<=100):
        bill=(50*1.40)+(units-50)*2.80
    elif(units<=200):
        bill=(50*1.40)+(50*2.80)+(units-100)*3.20
    elif(units<=300):
        bill=(50*1.40)+(50*2.80)+(100*3.20)+(units-200)*4
    else:
        bill=(50*1.40)+(50*2.80)+(100*3.20)+(100*4)+(units-300)*5
    print(bill)

def fab(x):
    if(x==1):
        return 1
    elif(x==2):
        return 2
    return fab(x-1)+fab(x-2)
for i in range(1,10):
    print(fab(i),end=' ')

def prime(n):
    while(1):
        c=0
        for i in range(2,n):
            if(n%i==0):
                c=c+1
            if(c==0):
                print(n,"prime")
                break
            else:
                n=n+1

def fun1(a):
    try:
        c=0
        for i in a:
            c=c+1
        print(c)
    except ValueError:
        print("Invalid")
    finally:
        if(c%2==0):
            print("even")
        else:
            print("odd")
 
def sep(a):
    b=[]
    for i in a:
        if(i.isalpha()):
            b.insert(0,i)
    for i in range(len(a)):
        if(not a[i].isalnum()):
            b.insert(i,a[i])
    print(''.join(b))

def encode(a,n):
    b=''
    for i in a:
        if(ord(i)+n>122):
            b=b+chr(ord(i)+n-26)
        else:
            b=b+chr(ord(i)+n)
    print(b)

def decode(a,n):
    b=''
    for i in a:
        if(ord(i)-n<97):
            b=b+chr(ord(i)-n+26)
        else:
            b=b+chr(ord(i)-n)
    print(b)


