# 1
a = "Aayush Khanna"
a = a.replace('a','$')
a = a.replace('A','$')
print(a)

# 2
a = input("Enter string")
def remove_char(a,n):
    b = a[:n]
    c = a[n+1:]
    return b+c
print(remove_char(a,0))
print(remove_char(a,3))
print(remove_char(a,5))

# 3
from pip._vendor.distlib.compat import raw_input
a = raw_input("Enter a string")
b = raw_input("Enter another string")
if(sorted(a) == sorted(b)):
  print("Anagram")
else:
   print("Not Anagram")

# 4
str = "aayush"
def change(str):
   return str[-1:] + str[1:-1] + str[:1]
print(change(str))

#5
a = input("Enter a string")
vowel = 0
consonent = 0
for i in a:
    if(i =='a'or i =='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
        vowel = vowel+1
    else:
       consonent = consonent+1
print(vowel)
print(consonent)

#6
a = input("Enter a string")
a = a.replace(" ","-")
print(a)

#7
a = input("Enter a string")
count = 0
for i in a:
    count = count+1

print(count)

#8
str = input("Enter a string")
result = " "
for i in range(len(str)):
   if i % 2 == 0:
      result = result + str[i]

print(result)

#9
str = input("Enter string")
char = 0
word = 0
for i in str:
    char = char +1
    if(i == ' '):
        word = word+1
print(word)
print(char)

#10
str1 = input("Enter string1")
str2 = input("Enter string2")
count1 =0
count2 =0
for i in str1:
    count1= count1+1
for i in str2:
    count2=count2+1
if(count1<count2):
    print("Str2 is larger")
elif (count2<count1):
    print("Str1 is larger")
else:
    print("Both strings are equal")

#11
str = input("Enter string")
count = 0
for i in str:
    if(i.islower()):
       count = count+1
    else:
       continue
print(count)

#13
str = input("Enter string")
count_upper = 0
count_lower = 0
for i in str:
    if(i.islower()):
       count_lower = count_lower+1
    else:
       count_upper = count_upper+1
print(count_upper)
print(co0unt_lower)

#12
b = input("Enter a string")
a = b[::-1]
if b == a:
   print("Palindrome")
else:
    print("Not a Palindrome")