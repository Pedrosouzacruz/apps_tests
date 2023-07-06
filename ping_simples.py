import os # importa o modulo ou biblioteca do OS (integra a biblioteca do sistema S.O)
print("#"*60) #imprimindo 60 vezes
ip_ou_host = input("Digite IP ou Host a ser verificado:") #criamos uma varialvel para receber o IP
print("-"*60)
os.system("ping -n 6 {}".format(ip_ou_host)) #imprimindo o IP recebido
print("-"*60)

