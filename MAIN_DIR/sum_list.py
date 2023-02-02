my_list = []

lista_none = None



def sum_list(lista):
    
    risultato = 0
    if len(my_list) == 0:
        return None
    for pippo in lista:
        risultato = risultato + pippo
        
    return risultato

    

print(sum_list(my_list))


print(sum_list(lista_none))

