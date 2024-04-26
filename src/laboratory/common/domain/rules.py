import abc
from abc import abstractmethod
from dataclasses import dataclass


class BusinessRule:

    __message: str = "Business rule is broken"

    def get_message(self) -> str:
        return self.__message

    @abstractmethod
    def is_broken(self) -> bool:
        raise NotImplemented
