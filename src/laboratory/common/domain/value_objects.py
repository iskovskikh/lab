from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    pass

@dataclass(frozen=True)
class GenderVO(ValueObject):
    value: str

@dataclass(frozen=True)
class PhoneVO(ValueObject):
    value: str

