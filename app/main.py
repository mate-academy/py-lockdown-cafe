from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # Se encontrar qualquer problema de vacina, a regra é clara:
            # Retornar imediatamente a mensagem de vacinação.
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Se o problema for máscara, contabilizamos para o relatório final
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
