import pyfiglet
rhcrypto_banner= pyfiglet.figlet_format("RHCrypto")
print(rhcrypto_banner)
print("Note:Decrypting script\n")
cypher = list(input("Enter your secret ONC(one time cypher) HERE :").lower())
encmsg = list(input(f"Enter your {len(cypher)} encrypted msg here : ").lower())
cypher2 = []
encmsg2 =[]

def c2N
():## this function convert chr to number for further conversion
    for key in cypher[0:len(cypher)]:
        a =ord(key) -96
        cypher2.append(a)
    for key in encmsg[0:len(cypher)]:
        a =ord(key) -96
        encmsg2.append(a)
c2N()
sumdec =[]## converted enc msg
def reverse():##this function add 26 to the number which were sub 26 while encrypting
    for i in range(len(encmsg2)):
        if encmsg2[i]<=cypher2[i]:
            encmsg2[i]+=26
reverse()
         
def sumlist():##this function perform sub from encmsg to cypher , main function
    for key in range(0,len(cypher)):
        sumdec.append(encmsg2[key]-cypher2[key])
sumlist()
out = []
def conversion():##converting numbers into chrs in a list
    for key in sumdec:
        out.append(chr(key+96))
conversion()
output = "".join(str(x) for x in out)
print ("here is the output:",output)
print("\nthanx!! for using...cooked by rockyhandsm2k")











    

