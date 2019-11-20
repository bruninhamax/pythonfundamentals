import pandas as pd

# df = pd.read_csv('/home/developer/pythonfundamentals/Arquivos/salarios.csv', encoding='UTF-8')
# df = pd.read_csv('/home/developer/pythonfundamentals/Arquivos/salarios.csv', usecols=['Name','Employee Annual Salary'])
df = pd.read_csv('/home/developer/pythonfundamentals/Arquivos/salarios.csv', nrows=30)

# Criando um novo arquivo com apenas as colunas Name e Salary numa única coluna
var = df['nome e salario'] = df['Name'] + ' ' + df['Employee Annual Salary']
var.to_csv('name_salario.csv', header=0)

# print(df)
# print(df.tail())

# var = df['Name']
# var.to_csv('Arquivos/name.csv', header=0)

# Parâmetros do loc: número da linha, nome da coluna
# var2 = df.loc[20, ['Name', 'Employee Annual Salary']]

# Parâmetros do iloc: número da linha, index da coluna
# print(df.iloc[20, 2])

# Cria um novo arquivo CSV com o separador ';'
# df.to_csv('novo_salarios.csv', header=0, sep=';')