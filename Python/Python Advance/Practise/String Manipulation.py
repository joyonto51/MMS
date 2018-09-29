a="Bangladesh"
a1="bangla"
b="Digital"
c= "Bangla"
d="English"
e="Hindi"

print(type(a))                  #to know the varriable type

print("Number of letter :",a.count('a'))             #tow know how much this  letter there

print('index is:',a.find('l'))              #to find a letter index
print("index is:",a.index('d'))
print("Lenth of index:",len(a))              # to know the string lenth

print(a1.capitalize())          #to capitalise a string a word

print(a.lower())                #to convert a String Upper to Lower
print('BANgLA'.casefold())

print(a.upper())                #to convert a string Lower to Upper

print('Bangla'.swapcase())      #to do reverse of letters

print("myfather is a farmer and school teacher.".title())     #to do capitalization each Word of a string

print(b+" "+a)                            #to add two string with each other

print("My favourite country is:%s"%a)    #to show a a string with another string
print("My favourite country is:",a)

print("My favourite language are",c,'and',d)    #to show a string with another strig on another way
print("My favourite language are %s and %s"%(c,d))

print(c+'-'+d+'-'+e)       # To join the sting with Hyphen(-)
print('-'.join((c,d,e)))


f="My name is Jayanta and i am a student"      #TO replace a letter
print(f.replace('i','b'))

g="My name is Jayanta and i am a student?"     #to remove the last keyword of a sentence or word
print(g.strip('?'))


x="My name is Jayanta and i am a student"
print(x.split(' '))

