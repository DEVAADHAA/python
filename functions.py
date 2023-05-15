#function dep to define a function
                   #name is argument
def greet(name):   #we should definre the function other wise it shows error
    print("hello" +' '+ name)
    print ("how are you")
greet("ram")    # ram is argument
greet("hari")   # it call the function
print("*******")
greet("kavi")




def sum(num):
    sum_result=num*(num+1)/2
    return sum_result
result=sum(11)
print(result)
print(sum(20))

#variable scope
def welcome(name):
    print("welcome"+name)
welcome("Radha")
#print(name)


