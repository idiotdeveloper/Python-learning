alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()

def encode (t, s):
    list = []
    list_2 = []

    for i in t:
        list = list + [i]
    print(list)

    position = 0 

    for i in list:
        counter1 = 0
        for j in alphabet:
            counter1 += 1
            if j == i:
                position = counter1 + s
                if position > 26 : 
                    position = position - 26
                    print("position ::", position)
                    list_2 += alphabet[position-1]
                else:
                    print(position)
                    list_2 += alphabet[position-1]
                print(list_2)
            
        if i == " ":
            list_2 += " "
        print(f"the final cipher list :: {list_2}")

    strn = ""
    for i in list_2:
        strn += i
    print (f"the final cipher string/text :: {strn}")



def decode(t,s):

    list = []
    list_2 = []

    for i in t:
        list = list + [i]
    print(list)

    position = 0 

    for i in list:
        counter1 = 0
        for j in alphabet:
            counter1 += 1
            if j == i:
                position = counter1 - s
                if position < 0 : 
                    position = position + 26
                    print("position ::", position)
                    list_2 += alphabet[position-1]
                else:
                    print(position)
                    list_2 += alphabet[position-1]
                print(list_2)
            
        if i == " ":
            list_2 += " "
        print(f"the final cipher list :: {list_2}")

    strn = ""
    for i in list_2:
        strn += i
    print (f"the final cipher string/text :: {strn}")


if direction == "e": 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encode(t=text, s=shift)
    
    
if direction == "d": 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decode(t=text, s=shift)
    