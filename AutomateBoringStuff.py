def collatz(number):
    if number%2 == 0:
        return(number//2)
    else:
        return(3*number+1)

if __name__=="__main__":
    print("enter number: ")
    try:
        number = int(input())
        while True:
            if number != 1:
                number = collatz(number)
                print(number)
            else:
                break
    except:
        print("Error: Invalid Value. You did ot enter an integer")