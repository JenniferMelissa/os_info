import os
import platform 

#pega qual o nome de usuario que voce esta usando e colocar na variavel criada
usuario = os.environ.get('USERNAME')
#nt = windows 

print(f'Sistema Operacional: {platform.system()} {platform.release()}.')
print(f'Nome do usuário: {usuario}.')