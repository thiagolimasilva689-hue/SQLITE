visitar =cursor.execute('Select*from zoologico').fetchall()
for visto in visitar:
  print(visto)
