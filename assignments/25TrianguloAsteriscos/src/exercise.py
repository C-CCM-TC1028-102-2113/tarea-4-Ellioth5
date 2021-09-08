
def main():
    #Escribe tu código debajo de esta línea
x=int(input())
a="*"
b=0
e=" "
p=0
while x!=0:    
    b=b+1
    x=x-1
    e=" "*x
    a="*"*b
    print(e+a)


if __name__=='__main__':
    main()
