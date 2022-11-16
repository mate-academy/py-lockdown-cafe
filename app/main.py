from app.cafe import Cafe
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_mask = 0
    friends_without_vaccine = 0
    for person in friends:
        try:
            Cafe.visit_cafe(cafe, person)
        except NotWearingMaskError:
            friends_without_mask += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            friends_without_vaccine += 1
            return "All friends should be vaccinated"

    if friends_without_mask == 0 and friends_without_vaccine == 0:
        return "Friends can go to KFC"
    else:
        return f"Friends should buy {friends_without_mask} masks"
