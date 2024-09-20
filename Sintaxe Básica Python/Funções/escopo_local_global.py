salario = 2000 # Essa variável é global

def salario_bonus(bonus, lista):
    global salario # Se não fosse estipulado "global", daria erro porque você não declarou essa variável dentro do escopo da função.
    salario += bonus
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista auxiliar = {lista_aux}")
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)