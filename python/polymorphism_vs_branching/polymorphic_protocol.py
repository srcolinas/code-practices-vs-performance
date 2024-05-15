import dis
import math
from typing import Iterable, Protocol

import pyperf


class Shape(Protocol):
    def area(self) -> float:
        ...


class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    def area(self) -> float:
        return (self._base * self._height) / 2
    

class Square:
    def __init__(self, side: float) -> None:
        self._side = side

    def area(self) -> float:
        return self._side * 2
    

class Circle:
    def __init__(self, radious: float) -> None:
        self._radious = radious

    def area(self) -> float:
        return self._radious * self._radious * math.pi
    


def sum_areas(shapes: Iterable[Shape]) -> float:
    total = 0
    for s in shapes:
        total += s.area()
    return total


def main():
    shapes = [Triangle(3, 4), Square(5), Circle(5)] * 1_000_000
    sum_areas(shapes)
    

if __name__ == "__main__":
    # runner = pyperf.Runner()
    # benchmark = runner.bench_func("main", main)
    # # benchmark.dump("polymorphic_protocol_main.json")
    # dis.dis(main, file=open("polymorphic_protocol_main.txt", "w"))
    
    objs = [Triangle(3, 4), Square(5), Circle(5)] * 1_000_000
    runner = pyperf.Runner()
    benchmark = runner.bench_func("sum_areas", sum_areas, objs)
    # benchmark.dump("polymorphic_protocol_sum_areas.json")
    dis.dis(sum_areas, file=open("polymorphic_protocol_sum_areas.txt", "w"))

