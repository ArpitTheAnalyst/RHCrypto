import pyfiglet

rhcrypto_banner = pyfiglet.figlet_format("RHCrypto")
print(rhcrypto_banner)
print("Note: encrypting script\n")
print("space or symbols on you keywboard like (_,!,|,etc) won't work. ")
cypher= list(input("Enter your secret ONC(once time cypher) HERE :").lower())
msg = list(input(f"Enter your {len(cypher)} encrypted msg here : ").lower()) 
alphamsg=[] 
alphacypher=[]
def conversion():##this function convert alphabets to numbers
    for key in msg:
        num1= ord(key)-96
        alphamsg.append(num1) 
    
    for key in cypher:
        num2= ord(key) -96
        alphacypher.append(num2) 
conversion()

sumenc =[]
def sumlist():#defining a function for adding the lists to make a single list with added value
    for key in range(0,len(alphacypher)):
        sumenc.append(alphamsg[key]+alphacypher[key])
sumlist()
for key in sumenc:#for converting items >26 to start from 1 again
    if key>26:
        sumenc1=sumenc.index(key)#index of the element
        sumenc2=sumenc.insert(sumenc1,key-26)
        sumenc.remove(key)
out = [] # last outcome including final text
def converting():
    for key in sumenc:
        out.append(chr(key+96))
converting()
final = "".join(str(x) for x in out) # conversion from list to string
print(F"SO YOUR ENCRYPTED TEXT IS {final}")






