class VaccineError(Exception):
    '''An error with the vaccine'''


class NotVaccinatedError(VaccineError):
    '''The client is not vaccinated'''


class OutdatedVaccineError(VaccineError):
    '''The vaccine is outdated'''


class NotWearingMaskError(Exception):
    '''Somebody is not wearing a mask'''
