from smartphone import Smartphone


catalog = []

catalog.append(Smartphone("Apple", "iPhone 17", "+79000000001"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79000000002"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79000000003"))
catalog.append(Smartphone("Huawei", "P60", "+79000000004"))
catalog.append(Smartphone("Google", "Pixel 8", "+79000000005"))


for s in catalog:
    print(f"{s.brand} - {s.model}. {s.phone_number}")
