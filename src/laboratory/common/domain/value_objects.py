from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class ValueObject:
    pass


@dataclass(frozen=True, kw_only=True)
class GenderVO(ValueObject):
    value: str


@dataclass(frozen=True, kw_only=True)
class PhoneVO(ValueObject):
    value: str
