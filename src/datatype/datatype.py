from abc import ABC
from ..ast import ASTNode
from dataclasses import dataclass


class DataType(ASTNode, ABC):
    def __bool__(self) -> bool: ...


@dataclass
class Number(DataType):
    value: float
    
    def __repr__(self):
        return f"Number({repr(self.value)})"
    
    def __bool__(self) -> bool:
        return self.value != 0
    
    def __add__(self, other: DataType) -> DataType:
        if isinstance(other, Number):
            return Number(self.value + other.value)
        raise NotImplementedError

    def __sub__(self, other: DataType) -> DataType:
        if isinstance(other, Number):
            return Number(self.value - other.value)
        raise NotImplementedError

    def __mul__(self, other: DataType) -> DataType:
        if isinstance(other, Number):
            return Number(self.value * other.value)
        raise NotImplementedError

    def __truediv__(self, other: DataType) -> DataType:
        if isinstance(other, Number):
            return Number(self.value / other.value)
        raise NotImplementedError


@dataclass
class Integer(Number):
    value: int # pyright: ignore[reportIncompatibleVariableOverride]

    def __repr__(self):
        return f"Integer({repr(self.value)})"
    def __bool__(self) -> bool:
        return self.value != 0

    def __add__(self, other: DataType) -> DataType:
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        elif isinstance(other, Number):
            return Number(self.value + other.value)
        raise NotImplementedError

    def __sub__(self, other: DataType) -> DataType:
        if isinstance(other, Integer):
            return Integer(self.value - other.value)
        elif isinstance(other, Number):
            return Number(self.value - other.value)
        raise NotImplementedError

    def __mul__(self, other: DataType) -> DataType:
        if isinstance(other, Integer):
            return Integer(self.value * other.value)
        elif isinstance(other, Number):
            return Number(self.value * other.value)
        raise NotImplementedError

    def __truediv__(self, other: DataType) -> DataType:
        if isinstance(other, Number): # division always returns a Number
            return Number(self.value / other.value)
        raise NotImplementedError


@dataclass
class String(DataType):
    value: str
    
    def __repr__(self):
        return f"String({repr(self.value)})"
    
    def __bool__(self) -> bool:
        return len(self.value) != 0
    
    def __add__(self, other: DataType) -> DataType:
        if isinstance(other, (String, Number)):
            return String(self.value + str(other.value))
        raise NotImplementedError

    def __sub__(self, other: DataType) -> DataType:
        raise NotImplementedError

    def __mul__(self, other: DataType) -> DataType:
        if isinstance(other, Integer):
            return String(self.value * other.value)
        raise NotImplementedError

    def __truediv__(self, other: DataType) -> DataType:
        raise NotImplementedError