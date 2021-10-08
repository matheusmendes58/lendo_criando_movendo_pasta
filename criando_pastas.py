import glob
import os
import shutil

nomes_dos_arquivos = glob.glob('*.png')  # vai ler todos os arquivos e passar para uma lista
print(nomes_dos_arquivos)   # verificação se o glob está fazendo corretamente e retornando uma lista

os.makedirs(r'C:\Users\centm\Desktop\lendo_criando_movendo_pasta\captchas')  # criara pasta captchas

for arquivo in nomes_dos_arquivos:
    x = arquivo.replace('.png', '')  # ira arrumar todos os arquivos sem o .png

    os.mkdir(rf'C:\Users\centm\Desktop\lendo_criando_movendo_pasta\captchas\{x}')      # criara pastas com mesmo nome dos captchas

    original = fr'C:\Users\centm\Desktop\lendo_criando_movendo_pasta\{arquivo}' # caminho onde está as pastas criadas

    target = rf'C:\Users\centm\Desktop\lendo_criando_movendo_pasta\captchas\{x}'        # caminho para onde os arquivos ira ficar

    shutil.move(original, target)       # comando para mover os arquivos para a pasta correta


    # Resultado final esta na pasta captcha