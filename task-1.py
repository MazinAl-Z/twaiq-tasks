#sets a vaul 4 the wither
tmp = ""
#takes input from the user and it will ask for it untill the user dose
while tmp == "" :
     tmp = input("in what derice is the wither outside ? : ")
#savinig the inpute as an int just 2 work with it 
tmp = int(tmp)
#now we will tell the user if it is how out side or not
if  tmp < 35 :
    print ("it is cold out side !")
elif tmp > 35 :
    print("it is hot out side !")
else :
    print("the wither out side is good !")#now we will tell the user if it is how out side or not