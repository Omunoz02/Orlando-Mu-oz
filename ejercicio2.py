
def num_primos():
    num = int(input("Digite un numero: "))
    cont=0
    for i in range(1,num+1):
        if num % 1 ==0:
            cont +=1
    if cont == 2:
        print("El numero: "+str(num)+" es primo" )
        return True
    else:
         print("El numero: "+str(num)+" no es primo" )
    return False 
def main():
        num_primos()

if __name__ == "__main__":
    pass
    main()