
def main():
    print("ingrese un numero positivo")
    n=int(input())
    if n<0:
        print("“Los números negativos no son permitidos")
        return main()
    elif n>0:
        for i in range(n,-1,-1):
                print (i, end=",")
    elif n==0:
            print("el numero es 0")

main()