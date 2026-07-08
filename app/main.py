import datetime
from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    masks_to_buy = 0
    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    meu_cafe = Cafe("Barba Café")
    lista_de_amigos = [
        {
            "name": "Anderson",
            "vaccine": {"expiration_date": datetime.date(2027, 12, 31)},
            "wearing_a_mask": True
        },
        {
            "name": "Thiago",
            "vaccine": {"expiration_date": datetime.date(2027, 5, 20)},
            "wearing_a_mask": False
        }
    ]
    resultado_da_entrada = go_to_cafe(lista_de_amigos, meu_cafe)
    print(resultado_da_entrada)
