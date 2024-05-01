import abc
import typing
from typing import Generic

# Create your models here.
from django.db import models

from laboratory.common.domain.types import EntityType, ValueObjectType

# class GenericBase(Generic[Entity],abc.ABC):
#     @abc.abstractmethod
#     def to_domain(self) -> Entity:
#         raise NotImplementedError
#
#     @staticmethod
#     @abc.abstractmethod
#     def from_domain(entity: Entity) -> 'BaseModel':
#         raise NotImplementedError

# """
# https://code.djangoproject.com/ticket/33174
# """
if typing.TYPE_CHECKING:
    class GenericEntityBase(Generic[EntityType]):
        pass
else:
    class GenericEntityBase:
        def __class_getitem__(cls, _):
            return cls


class BaseEntityModel(GenericEntityBase[EntityType], models.Model):

    @abc.abstractmethod
    def to_domain(self) -> EntityType:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def from_domain(entity: EntityType) -> 'BaseEntityModel':
        raise NotImplementedError

    class Meta:
        abstract = True


if typing.TYPE_CHECKING:
    class GenericValueObjectBase(Generic[ValueObjectType]):
        pass
else:
    class GenericValueObjectBase:
        def __class_getitem__(cls, _):
            return cls


class BaseValueObjectModel(GenericValueObjectBase[ValueObjectType], models.Model):

    @abc.abstractmethod
    def to_domain(self) -> ValueObjectType:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def from_domain(value_object: ValueObjectType) -> 'BaseValueObjectModel':
        raise NotImplementedError

    class Meta:
        abstract = True
