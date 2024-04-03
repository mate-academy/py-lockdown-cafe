from __future__ import annotations
from datetime import date
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masked_friends = 0

    for friend in friends:
        try:
            if "vaccine" not in friend:
                raise NotVaccinatedError(
                    f"{friend['name']} "
                    f"is not vaccinated"
                )

            elif "expiration_date" in friend["vaccine"]:
                expiration_date = friend["vaccine"]["expiration_date"]
                if expiration_date < date.today():
                    raise OutdatedVaccineError(
                        f"{friend['name']}'s "
                        f"vaccine has expired"
                    )

            else:
                raise OutdatedVaccineError(
                    f"Incompletevaccine "
                    f"information for {friend['name']}"
                )

            if not friend.get("wearing_a_mask", False):
                masked_friends += 1

        except (NotVaccinatedError, OutdatedVaccineError) as e:
            return str(e)

    if masked_friends > 0:
        return f"Friends should buy {masked_friends} masks"
    else:
        return f"Friends can go to {cafe.name}"
