def nperfect():
    
    num = int(input("Ingrese un numero: "))
    suma=0
    for i in range(1, num):
        if num % i == 0:
            suma +=i 
    if suma == num:
        print("El numero : " + str(num)+" es perfecto" )
    else:
        print("El numero : " + str(num)+" no es perfecto" )
    
        return 0

def main():
     nperfect()


if __name__ == "__main__":
    pass
    main()