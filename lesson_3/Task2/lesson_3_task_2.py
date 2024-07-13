from smartphone import Smartphone 
    
catalog = []

phone1 = Smartphone("Apple", "Iphone 15", "+37256432123") 
phone2 = Smartphone("Samsung", "Galaxy5", "+79109886921") 
phone3 = Smartphone("Xiaomi", "11T Pro", "+79145622456")
phone4 = Smartphone("Nokia", "3110", "+37134256732")
phone5 = Smartphone("OnePlus", "9PRO","+78956723443")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)   

for phone in catalog:
    print (f"{phone.brand} - {phone.model}. {phone.phone_number}") 
    