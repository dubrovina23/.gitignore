from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991112233"),
    Smartphone("Samsung", "Galaxy S24", "+79992223344"),
    Smartphone("Xiaomi", "14 Pro", "+79993334455"),
    Smartphone("Google", "Pixel 8", "+79994445566"),
    Smartphone("Nothing", "Phone 2", "+79995556677"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
