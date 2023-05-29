lista=[1,5,25,100,500]

print("inicial: ",lista)

lista.append(250)
print("append: ",lista)

lista2=[75, 125]
lista.extend(lista2)
print("Extend: ",lista)

lista.insert(2,400)
print("Insert: ",lista)

lista.remove(400)
print("Remove ",lista)

lista.pop()
print("Pop: ",lista)
lista.pop(2)
print("Pop(2)",lista)

lista.reverse()
print("Reverse: ",lista)