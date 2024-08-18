from Address import Address
from mailing import Mailing

to_address = Address ("12345", "London", "Bond street", "10", "16")
from_address = Address ("11516", "Tallinn", "Vedru", "34", "19")
mailing = Mailing (to_address, from_address, 500, "133BTK")

print( f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street},{mailing.from_address.house} - {mailing.from_address.apartment} "
      f" в {mailing.to_address.index},{mailing.to_address.city},{mailing.to_address.street} "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей ")

   