from address import Address
from mailing import Mailing

to_addr = Address("443001", "Самара", "Ленинская", "15", "42")
from_addr = Address("101000", "Москва", "Тверская", "10", "5")

mail = Mailing(to_addr, from_addr, 350, "TRK123456789")

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
