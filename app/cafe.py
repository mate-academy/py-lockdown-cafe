import datetime

import app.errors as errors


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' in visitor:
            if visitor['vaccine']['expiration_date'] >= datetime.date.today():
                if 'wearing_a_mask' in visitor and visitor['wearing_a_mask']:
                    return f"Welcome to {self.name}"
                else:
                    raise errors.NotWearingMaskError(
                        f"Visitor {visitor['name']} has no mask"
                    )
            else:
                raise errors.OutdatedVaccineError(
                    f"Visitor {visitor['name']} has outdated vaccine"
                )
        else:
            raise errors.NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )
