class VaccineError(Exception):
    print ("Error vaccine!")


class NotVaccinatedError(VaccineError):
    print ("Vaccine not found!")


class OutdatedVaccineError(VaccineError):
    print ("Vaccine has been expired!")


class NotWearingMaskError(Exception):
    print ("Mask not weared!")
