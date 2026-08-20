from app.cafe import Cafe
from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    counter = 0
    friends_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            friends_counter += 1
        except OutdatedVaccineError as error:
            return f"{error}"
        except NotVaccinatedError as error:
            return f"{error}"
        except NotWearingMaskError:
            counter += 1

    if friends_counter == len(friends):
        return "Friends can go to KFC"

    if counter > 0:
        return f"Friends should buy {counter} masks"
