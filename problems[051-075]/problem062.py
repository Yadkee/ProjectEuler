import time


def main(permutations=5):
    cubes = dict()
    n = 0
    while True:
        n += 1
        cube = n ** 3
        sorted_string = "".join(sorted(str(cube)))
        this_cubes = cubes.get(sorted_string, [])
        this_cubes.append(cube)
        if len(this_cubes) == permutations:
            break
        cubes[sorted_string] = this_cubes
    print(this_cubes, min(this_cubes))


if __name__ == '__main__':
    initial_time = time.time()
    main()
    final_time = time.time()
    difference = round(final_time - initial_time, 3)
    print(f"It took {difference} seconds")
