"""
--- Day 5: If You Give A Seed A Fertilizer ---

https://adventofcode.com/2023/day/5
"""
from collections import defaultdict

def problem(part=1, test=False):
    if not test:
        data = open("day5.input", "rt").readlines()
    else:
        data = test.split("\n")

    # first line is seed list
    seeds_to_process = []
    seeds = list(map(int, data[0].split(" ")[1:]))
    for start, length in zip(seeds[0::2], seeds[1::2]):
        seeds_to_process.append(range(start, start+length))


    mappings = defaultdict(list)
    order = {}

    get_line = iter(data[1:])

    for line in get_line:
        line = line.strip()
        if line.endswith("map:"):
            mapping = line.split(" ")[0]
            source,_,destination = mapping.split("-")
            order[source] = destination

            # will terminate on empty string
            while line := next(get_line, "").strip():
                # store ranges in a list on the mapping
                dest_start, source_start, range_length = map(int,line.split(" "))
                mappings[mapping].append([range(dest_start,dest_start+range_length),range(source_start,source_start+range_length)])



    process = "seed"
    while process in order.keys():
        mapping = f"{process}-to-{order[process]}"
        new_seeds = []
        while seeds_to_process:
            seed = seeds_to_process.pop()
            for destination, source in mappings[mapping]:
                overlap_start = max(seed.start, source.start)
                overlap_end = min(seed.stop, source.stop)
                if overlap_start < overlap_end:
                    new_seeds.append(range(
                        destination[source.index(overlap_start)],
                        destination[source.index(overlap_end-1)]+1
                    ))
                    if overlap_start > seed.start:
                        seeds_to_process.append(range(seed.start, overlap_start))

                    if seed.stop > overlap_end:
                        seeds_to_process.append(range(overlap_end, seed.stop))
                    break
            else:
                new_seeds.append(seed)

        process = order[process]
        seeds_to_process = new_seeds


    lowest = (min(seed.start for seed in seeds_to_process))
    return lowest

if __name__ == '__main__':

    test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    exp_lowest = 46
    lowest = problem(part=2, test=test)
    assert exp_lowest==lowest, f"Part 2: received={lowest} {exp_lowest=}"

    exp_lowest = 104070862
    lowest = problem(part=2)
    print(f"Part 2: {lowest}")
    assert exp_lowest==lowest, f"Part 2: received={lowest} {exp_lowest=}"
