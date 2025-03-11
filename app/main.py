from app import cafe as c
from app import errors as er


def go_to_cafe(friends: list, cafe: c.Cafe) -> str:
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except er.VaccineError:
            return "All friends should be vaccinated"
        except er.NotWearingMaskError:
            count += 1
    if count != 0:
        return f"Friends should buy {count} masks"
    else:
        return f"Friends can go to {cafe.name}"
