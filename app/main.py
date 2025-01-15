from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    result = []
    count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count += 1
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError as e:
            if friend == friends[-1]:
                return str(e)
            else:
                result.append(str(e))
    if count == len(friends):
        return f"Friends can go to {cafe.name}"
    else:
        return result[-1]
