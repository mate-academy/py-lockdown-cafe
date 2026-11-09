# main.py
from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # Captura tanto NotVaccinatedError quanto OutdatedVaccineError
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Conta quantos amigos estão sem máscara
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
