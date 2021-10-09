import sys
from typing import NamedTuple
from typing import Set, Tuple, List
from itertools import permutations


class Point(NamedTuple):
    x: int
    y: int

    def __str__(self):
        return f'({self.x}, {self.y})'


def get_dist(p1: Point, p2: Point) -> float:
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5


def find_shortes_path_to_other(start: Point, points: Set[Point]) -> Tuple[Point, float]:
    min_dist = sys.maxsize * 2 + 1
    destination_point = None
    for point in points:
        dist = get_dist(start, point)
        if dist < min_dist:
            min_dist = dist
            destination_point = point
    return destination_point, min_dist


def find_path(start: Point, points: List[Point]) -> List[Tuple]:
    answer = []
    from_visit = start
    total_path = 0
    while points:
        total_path += get_dist(from_visit, points[0])
        answer.append((points[0], total_path))
        from_visit = points[0]
        points.pop(0)

    total_path += get_dist(from_visit, start)
    answer.append((start, total_path))
    return answer


def find_answer(start: Point, points: List[Point]) -> List[Tuple]:
    min_dist = sys.maxsize * 2 + 1
    min_path = None

    for permutation in permutations(points):
        path = find_path(start, list(permutation))
        if (dist := path[-1][-1]) < min_dist:
            min_path = path
            min_dist = dist

    return min_path


def main():
    start = Point(0, 2)
    p2 = Point(2, 5)
    p3 = Point(5, 2)
    p4 = Point(6, 6)
    p5 = Point(8, 3)

    points = [p2, p3, p4, p5]
    answer = find_answer(start, points)

    to_print = f'{start} -> ' + ' -> '.join([f'{i[0]}[{i[1]}]' for i in answer]) + f' = {answer[-1][-1]}'

    print(to_print)


if __name__ == '__main__':
    main()
