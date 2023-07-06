import hashlib

arquivo_1 = "hash_1.txt"
arquivo_2 = "hash_2.txt"

hash_1 = hashlib.new("ripemd160")
hash_1.update(open(arquivo_1, "rb").read())

hash_2 = hashlib.new("ripemd160")
hash_2.update(open(arquivo_2, "rb").read())

if hash_1.digest() != hash_2.digest():
    print(f"O arquivo:{arquivo_1} é diferente do arquivo: {arquivo_2}")
    print("O hash_1 é: ", hash_1.hexdigest())
    print("O hash_2 é: ", hash_2.hexdigest())
else:
    print(f"{arquivo_1} é igual ao arquivo:{arquivo_2}")
    print("O hash_1 é: ", hash_1.hexdigest())
    print("O hash_2 é: ", hash_2.hexdigest())