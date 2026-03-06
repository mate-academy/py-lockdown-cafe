from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(
    friends: list[dict],
    cafe: Cafe
) -> str:
    # primeiro verificar vacinação
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    # se todos têm vacina, verificar máscaras
    masks_to_buy = sum(
        not friend.get("wearing_a_mask", False)
        for friend in friends
    )

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
