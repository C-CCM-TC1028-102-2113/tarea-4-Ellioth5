
def main():
    #escribe tu código abajo de esta línea
a=0
b=1
c=0
x=int(input())
while c<x:
    c=c+1
    a, b=b, a+b
print(a)

if __name__=='__main__':
    main()
