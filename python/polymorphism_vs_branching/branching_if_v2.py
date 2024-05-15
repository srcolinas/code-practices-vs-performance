import dis
import math
from typing import Iterable

import pyperf


class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height


class Square:
    def __init__(self, side: float) -> None:
        self.side = side
    

class Circle:
    def __init__(self, radious: float) -> None:
        self.radious = radious

    
def sum_areas(shapes: Iterable[Triangle | Square | Circle]) -> float:
    total = 0
    for s in shapes:
        if isinstance(s, Triangle):
            total += s.base * s.height / 2
        elif isinstance(s, Square):
            total += s.side * s.side
        elif isinstance(s, Circle):
            total += s.radious * s.radious * math.pi
    return total
        


def main():
    shapes = [Triangle(3, 4), Square(5), Circle(5)] * 1_000_000
    sum_areas(shapes)

    

if __name__ == "__main__":
    runner = pyperf.Runner()
    benchmark = runner.bench_func("main", main)
    # benchmark.dump("polymorphic_protocol_main.json")
    dis.dis(main, file=open("branching_if_v2_main.txt", "w"))
    
    # objs = [Triangle(3, 4), Square(5), Circle(5)] * 1_000_000
    # runner = pyperf.Runner()
    # benchmark = runner.bench_func("sum_areas", sum_areas, objs)
    # # benchmark.dump("polymorphic_protocol_sum_areas.json")
    # dis.dis(sum_areas, file=open("branching_if_v2_sum_areas.txt", "w"))

