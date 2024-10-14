from enum import Enum, StrEnum


class SearchFormType(StrEnum):
    RETURN = 'return'
    ONE_WAY = 'oneWay'
    MULTI_CITY = 'multicity'
    NOMAD = 'nomad'


class Airport(StrEnum):
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
