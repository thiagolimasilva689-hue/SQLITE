# order by
visitar =cursor.execute('''Select*from zoologico
ORDER BY idade desc
''').fetchall()
for nome, estado_emocional, idade, nome_da_especie in visitar:
    print(f"{nome} | {estado_emocional} | {idade} | {nome_da_especie}")
