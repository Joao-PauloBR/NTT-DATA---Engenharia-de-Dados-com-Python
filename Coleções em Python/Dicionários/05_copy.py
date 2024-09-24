contatos = {"João@gmail.com": {"nome": "João", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["João@gmail.com"] = {"nome": "Jão"}

print(contatos["João@gmail.com"])  # {"nome": "João", "telefone": "3333-2221"}

print(copia["João@gmail.com"])  # {"nome": "Jão"}
