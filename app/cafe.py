import datetime

import app.errors as errors


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if 'vaccine' not in visitor:
            raise errors.NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )
        if not visitor['vaccine']['expiration_date'] >= datetime.date.today():
            raise errors.OutdatedVaccineError(
                f"Visitor {visitor['name']} has outdated vaccine"
            )
        if not ('wearing_a_mask' in visitor and visitor['wearing_a_mask']):
            raise errors.NotWearingMaskError(
                f"Visitor {visitor['name']} has no mask"
            )
        return f"Welcome to {self.name}"
