import itertools
import math
import random

POPULATION = 8
Sample = tuple[int, int, int, int, int, int, int, int]


def calculate_fitness(sample: Sample):
    errors = 0
    for (i, v1), (j, v2) in itertools.combinations(enumerate(sample), 2):
        if (v1 == v2) or v1 - v2 == i - j or j - i == v1 - v2:
            errors += 1
    return 28 - errors


def breed(s1: Sample, s2: Sample) -> Sample:
    return s1[:4] + s2[4:]


def generate_random_sample() -> Sample:
    return tuple(random.randint(0, 7) for _ in range(8))


def mutate(s: Sample) -> Sample:
    l = list(s)
    r = random.randint(0, 7)
    l[r] = random.randint(0, 7)
    return tuple(l)


i = 0
current_generation = [generate_random_sample() for i in range(POPULATION)]
while next((s for s in current_generation if calculate_fitness(s) == 28), None) is None:
    weights = [math.gamma((calculate_fitness(s)))  for s in current_generation]
    mothers = random.choices(
        current_generation,
        weights=weights,
        k=POPULATION,
    )
    fathers = random.choices(
        current_generation,
        weights,
        k=POPULATION,
    )
    current_generation = [mutate(breed(f, m)) for f, m in zip(fathers, mothers)]

    i += 1


print(i,)
