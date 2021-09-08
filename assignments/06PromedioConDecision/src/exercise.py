def main():
    #escribe tu código abajo de esta línea
   suma=0
cantidad=0
p=0
while p>=0:       
    p=float(input())
    if p>=0:
        suma=(suma+p)
        cantidad=cantidad+1
prom=suma/cantidad
print("Promedio: %f " %prom)
if __name__=='__main__':
    main()
