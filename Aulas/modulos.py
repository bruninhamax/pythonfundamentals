# from aula07 import Pai
# joao = Pai()

# import aula07

# print(dir(aula07))
# print(aula07.__name__)
# print(__name__)

# alex = aula07.Pai()
# alex.trabalhar()

import os
import pwd
import sys
import datetime

# os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
# user = os.getlogin()

# print(user)

# print(os.listdir('/home/developer'))
# os.rename('./base.py', 'pandas.py')

# os.system('echo $USER')

# print(sys.platform)
# print(sys.builtin_module_names)

print(sys.argv)

#sys.exit()

for i in range(len(sys.argv)):

    if i == 0:
        print(f'Function name: {sys.argv[0]}')

    else:

        print(f'{i}. argument: {sys.argv[i]}')

print(datetime.datetime.now())
print(datetime.timedelta(7))
print(datetime.time(14, 0, 0))
print(datetime.date(2017, 1, 11))

import csv

with open('../Arquivos/novo.csv','w', newline='') as csvfile:

    arquivo = csv.writer(csvfile, delimiter=',')
    arquivo.writerow(['Teste']*5)
    arquivo.writerow(['4linux','Python'])