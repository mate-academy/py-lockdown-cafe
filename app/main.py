from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    # Primeiro verifica vaccines (ignorando erros de máscara)
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                pass  # ignora máscara nesta etapa
    except VaccineError:
        return "All friends should be vaccinated"
    masks_to_buy = sum(1 for f in friends if not f.get(
                       "wearing_a_mask", False))

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
