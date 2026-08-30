from address import Address
from mailing import Mailing


from_address = Address("123456", "Москва", "Ленина", 10, 25)
to_address = Address("654321", "Санкт-Петербург", "Невский", 20, 15)

mailing = Mailing(
    to_address,
    from_address,
    500,
    "AB123456789RU"
)


print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
