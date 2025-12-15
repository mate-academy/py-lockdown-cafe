from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

def test_errors_hierarchy():
    assert NotVaccinatedError.__bases__ == (
        VaccineError,
    ), "NotVaccinatedError should inherit only VaccineError class"

    assert OutdatedVaccineError.__bases__ == (
        VaccineError,
    ), "OutdatedVaccineError should inherit only VaccineError class"

    assert NotWearingMaskError.__bases__ == (
        Exception,
    ), "NotWearingMaskError should inherit only Exception class"
