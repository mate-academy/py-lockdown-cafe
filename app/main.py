from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    error = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            print(e)
            error = True
        except NotWearingMaskError as e:
            print(e)
            error = True
    if error is False:
        return f"Friends can go to {cafe.name}"
