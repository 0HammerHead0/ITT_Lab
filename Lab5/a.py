while(True):
    print("1.Sum")
    print("2.Multiply")
    print("3.Divide")
    print("4.Subtract")
    print("-1.Exit")
    inp = int(input("Enter operation"))
    [m,n]=[int(i) for i in input("Enter two numbers by space ").split(" ")]
    if( inp == 1):
        print(m+n)
    elif(inp == 2):
        print(m*n)
    elif(inp == 3):
        print(m/n)
    elif(inp==4):
        print(m-n)
    elif(inp==-1):
        print("bye bye")
    else:
        print("sahi likho be")