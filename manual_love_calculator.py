string1 = "soubhik Roy" 
string2 = "Chandrani Bhattacharjee" 
string3 = "True" 
string4 = "Love" 

string1 = string1.lower().replace(' ','')
string2 = string2.replace(' ','').lower()
string3 = string3.replace(' ','').lower() 
string4 = string4.replace(' ','').lower() 

list1 = []
list2 = []
list3 = []

for l in string1:
    list1.append(l)

for l in string2:
    list1.append(l)

for l in string3:
    list2.append(l)

for l in string4:
    list3.append(l)

print(list1, "\n", list2,"\n", list3)

sum1 = 0
for j in list2:
    counter = 0
    for i in list1: 
        if(j == i):
            counter += 1
    print(j, counter)
    sum1 = counter + sum1
print(sum1)


sum2 = 0
for j in list3:
    counter = 0 
    for i in list1: 
        if(j == i):
            counter += 1
    print(j, counter)
    sum2 = counter + sum2
print(sum2)

tot = str(sum1) + str(sum2)
#print("Your score is", tot)

if(int(tot) < 10 or int(tot) > 90):
    print(f"Your score is {tot}, you go together like coke and mentos.")

elif(int(tot) >= 40 and int(tot) <= 50):
    print(f"Your score is {tot}, you are alright together.")

else:
    print("Your score is", tot)


