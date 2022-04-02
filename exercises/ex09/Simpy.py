"""Utility class for numerical operations."""

from __future__ import annotations


from typing import Union


__author__ = "YOUR PID HERE"


class Simpy():
    values: list[float]

    def __init__(self, values):
        """A constructor method."""
        self.values = values
    
    def __str__(self) -> str:
        """A method that returns a string representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, rep_value: float, num_rep: int) -> None:
        """A method that mutates object to add repeats of float for a specified number of times."""
        value: list[float] = []
        for i in range(0, num_rep):
            value.append(rep_value)
        self.values = value
        
    def arange(self, start: float, stop: float, step: float = 1.0):
        """A range method for floats."""
        value: list[float] = []
        value.append(start)
        if step > 0:
            i: int = 0
            while value[i] < (stop - step):
                value.append(value[i] + step)
                i += 1
        else:
            i: int = 0
            while value[i] > (stop - step):
                value.append(value[i] + step) 
                i += 1
        self.values = value

    def sum(self) -> float:
        """A method that returns the sum."""
        total: float = sum(self.values)
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """A method that overloads addition operator to apply to both Simpy and float."""
        value: list[float] = []
        if isinstance(rhs, float):
            for items in self.values:
                value.append(items + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                value.append(self.values[i] + rhs.values[i])

        return Simpy(value)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """A method that overloads exponential operater to apply to Simpy."""
        result: list[float] = []
        if isinstance(rhs, float):
            for items in self.values:
                result.append(items ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])

        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """A method that creates a mask based on if self is equal to rhs."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """A method that creates a mask based on if self is grater than rhs."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """A method that allows for subscription operator with Simpy."""
        if isinstance(rhs, int):
            value: float = 0.0
            for item in self.values:
                value = self.values[rhs]
            return value
        else:
            result: list[float] = []
            for i in range(0, len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
