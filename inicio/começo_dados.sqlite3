   import sqlite3 
  conexao = sqlite3.connect('Meu_zoologico') cursor = conexao.cursor() 
  cursor.execute('CREATE TABLE zoologico(nome text,estado_emocional text,idade int, nome_da_especie text)') 
  conexao.commit() 
  cursor.execute('Insert into zoologico values("Dragon","Feliz",8,"Teiu(salvator merianae)")') cursor.execute('Insert into zoologico values("Lindinha","Animada",7,"Anta( Tapirus terrestris)")') cursor.execute('Insert into zoologico values("Rainha","Entediada",4,"Tigre(Panthera tigris)")') 
  cursor.execute('Insert into zoologico values("Brutus","rabugento",12,"Jacaré-Açu(Melanosuchus niger)")')
