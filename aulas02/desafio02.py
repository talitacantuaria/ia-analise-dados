notas= []
n1= float(input("digite sua nota1:"))
n2= float(input("digite sua nota2:"))
n3= float(input("digite sua nota3:"))
n4= float(input("digite sua nota4:"))

notas= [n1,n2,n3,n4]
print (f"a maior nota foi {max( notas)}")
print (f"a maior nota foi {min(notas)}")
print(f"a soma de todas as notas é igual a {sum(notas)}")


media= sum(notas)/len(notas)
print(media)


if media >= 6:
    print("aprovado")
else:
    print("reprovado")




