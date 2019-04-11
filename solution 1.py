#print the second element from array
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
____________________________________________________
#print multiple 5 till 10 by using range
#do same as I have done by printing multiple of 2 using range(2,10,2)
for i in range(2,10,2):
    print(i)
_________________________________________________ 
#Change the value from "apple" to "kiwi", in the x.
#fill the dotted missing logic
#HINT --> use assignment operator

x=["apple","orange","banana","grapes"]

x[0]="kiwi"
_________________________________________
#Question-3
x=['f','g','t','h','l','w','k','p']
for i in x:
    if(i=='j'):
        c=1
        break
    else:
        c=0
if(c==1):
    print("YES Found It")
elif(c==0):
    print("NOT Found")
