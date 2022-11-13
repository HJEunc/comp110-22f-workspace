"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730566282"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, inputlist: list[float]):
        """Constructor, initialized values."""
        self.values = inputlist
    
    def __repr__(self) -> str:
        """Returns a string representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, amount: int) -> None:
        """Fills a Simpy values list."""
        result: list[float] = []
        for i in range(amount):
            result.append(value)
        self.values = result
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a Simpy value list with step count."""
        result: list[float] = [start]
        i: int = 1
        while i < (int(stop - start) / step):
            result.append(start + (step * i))
            i += 1
        self.values = result
    
    def sum(self) -> float:
        """Returns total sum of Simpy values list."""
        result: float = 0.0
        for i in range(len(self.values)):
            result += self.values[i]
        return result
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for additon with Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for power with Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Operator overload for is equal with Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.values.append(True)
                else:
                    result.values.append(False)
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] == rhs:
                    result.values.append(True)
                else:
                    result.values.append(False)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Operator overload of greater than with Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.values.append(True)
                else:
                    result.values.append(False)
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] > rhs:
                    result.values.append(True)
                else:
                    result.values.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows iteration of Simpy value list."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs.values[i]:
                    result.values.append(self.values[i])
            return result