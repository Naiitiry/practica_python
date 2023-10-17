#Concatenación avanzada
#método JOIN
"""
p = "programación"
f = "facil"

print(" ".join([p,f,p,f,f]))#se puede concatenar con espacio o caracteres. ej.: * / -, etc.
"""
#método COMODIN
"""
p = "programación"
f = "facil"

print("%s %s"%(p,f))
"""
#método FORMAT
"""
p = "programación"
f = "facil"

print("{} {}".format(p,f))
"""
#método
# con comillas de comentarios """ lo que sea que vaya dentro se puede hacer enters para que no sobrepase la pantalla """
'''
texto = """iahbdishd sdifhwfh ihufid 
lorem ipusinaisfwidfnwidfb 
djbfiwdbfisjdbfisd nwidfnjwidjfn"""
print(texto)
'''
#método
#multiplicar strings
'''
p = "programación"
f = "facil"
print(p*5)
'''
#método
#iteración
'''
pf = 'programacion facil'
for letra in pf:
    print(letra, end=" ")
'''
#método
#