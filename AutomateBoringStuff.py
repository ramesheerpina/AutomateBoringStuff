#priint statment prints the input given to it where as the return statment stores the value
#in the function where can be used later. If a print statment is used in the function it
#will print the value either the function is called or not where as the return will print
#only if the function is called.
def number(num):
    print(num)
    print("last "+ str(num) + " came from print statement")
    return(num)

number(9)

print("lets see what is printed")

print(number(10))