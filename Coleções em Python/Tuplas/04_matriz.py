matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

print("=================")

minha_matriz = (
    (2, 4, 6, 8),
    ("a", "c", "e", "g"),
    (1, 3, "b", "d"),
)

print(minha_matriz)
print(minha_matriz[0])
print(minha_matriz[1])
print(minha_matriz[2])
print(minha_matriz[0][1])
print(minha_matriz[1][2])
print(minha_matriz[2][3])