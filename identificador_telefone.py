import phonenumbers
from phonenumbers import geocoder,carrier

phone = input("Digite o telefone no formato: (+55 ddd celular)")

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, "pt"))
print(carrier.name_for_number(phone_numbers , "pt"))

              