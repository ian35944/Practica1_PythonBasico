print("ingrese un numero positivo")
n=int(input())

if n<0:
    print("“Los números negativos no son permitidos")
elif n>0:
    for i in range(n,-1,-1):
        print (i)
elif n==0:
    print("el numero es 0")
