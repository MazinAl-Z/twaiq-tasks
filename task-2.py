#makeing a list
list = []
#seting the int
x = 0
#makeing the loop , it adds a 1 to the int x , and if that nuper (x+1) can be divaided by 2 then it is good 2 go in the list!
while (x<100) :
    x = x+1 
    if x%2 == 0:
        list.append(x)
# 2 make sure we did it right we print the list
print (list)
