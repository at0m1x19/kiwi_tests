from enum import Enum


class SearchFormType(str, Enum):
    RETURN = 'return'
    ONE_WAY = 'oneWay'
    MULTI_CITY = 'multicity'
    NOMAD = 'nomad'


class Airport(Enum):
    RTM = 'Rotterdam'
    MAD = 'Madrid'

    @property
    def code(self):
        return self.name

    @property
    def city(self):
        return self.value


class CheckBoxState(Enum):
    CHECKED = True
    UNCHECKED = False
