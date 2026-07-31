import pandas as pd

df = pd.read_csv('C:/Users/Thiago/OneDrive/Desktop/teiu/csv/dieta_ultima.csv')

df.to_excel('Dieta.xlsx')
print("ARQUIVANDO COM SUCESSO!")