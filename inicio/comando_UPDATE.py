sqlite3.connect('Meu_zoologico.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('''UPDATE zoologico
          SET estado_emocional = 'Alegre'
          WHERE nome = 'Dragon'
    ''')
    conexao.commit()
