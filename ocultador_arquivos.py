import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultador_arquivos.txt", atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Não deu certo")