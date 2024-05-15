import abc
import dis
import math
from typing import Iterable, Literal, NamedTuple

import pyperf


    
type Request = tuple[Literal["trianlge", "circle", "square"], float, float]

def sum_areas(requests: Iterable[Request]) -> float:
    total = 0
    for shape, a, b in requests:
        if shape == "trianlge":
            total += a * b /2
        elif shape == "circle":
            total += math.pi * a * b
        elif shape == "square":
            total += a*b
    return total


def main():
    shapes = [("triangle", 3, 4), ("circle", 5, 5), ("square", 5, 5)] * 1_000_000
    sum_areas(shapes)
    

if __name__ == "__main__":
    # runner = pyperf.Runner()
    # benchmark = runner.bench_func("main", main)
    # # benchmark.dump("polymorphic_protocol_main.json")
    # dis.dis(main, file=open("branching_if_main.txt", "w"))
    
    objs = [("triangle", 3, 4), ("circle", 5, 5), ("square", 5, 5)] * 1_000_000
    runner = pyperf.Runner()
    benchmark = runner.bench_func("sum_areas", sum_areas, objs)
    # benchmark.dump("polymorphic_protocol_sum_areas.json")
    dis.dis(sum_areas, file=open("branching_if_sum_areas.txt", "w"))

