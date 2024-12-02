import time
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

from utils.puzzle import Puzzle


class SeedMap:
    def __init__(self, input_str: str):
        self.input_str = input_str
        seeds, *maps = self.get_input_parts()
        self.seeds = [int(s) for s in seeds.split(": ")[-1].split(" ")]
        self.seed_ranges: [range] = self.create_seed_ranges()
        self.maps = self.process_maps(maps)

    def get_input_parts(self):
        parts = self.input_str.split("\n\n")
        return parts

    @staticmethod
    def process_map(map_str):
        out = {}
        lines = map_str.split("\n")
        out["name"] = lines.pop(0).replace(" map:", "")
        for line in lines:
            destination_range_start, source_range_start, range_length = [
                int(i) for i in line.split(" ")
            ]
            out[range(source_range_start, source_range_start + range_length)] = (
                destination_range_start
            )
        return out

    def process_maps(self, maps: [str]):
        out = []
        for map_str in maps:
            out.append(self.process_map(map_str))
        return out

    @lru_cache(maxsize=None)
    def get_location(self, object_id: int, lookup_id: int) -> int:
        lookup = self.maps[lookup_id]
        # example: find soil from seed
        for start_range, destination_start in lookup.items():
            if start_range == "name":
                continue
            if object_id in start_range:
                offset = object_id - start_range.start
                return destination_start + offset
        return object_id

    def get_end_position(self, object_id: int) -> int:
        cur = object_id
        for mapping in range(len(self.maps)):
            cur = self.get_location(cur, mapping)
        return cur

    def get_all_end_positions(self):
        out = []
        for seed in self.seeds:
            out.append(self.get_end_position(seed))
        return out

    def get_lowest_position(self):
        return min(self.get_all_end_positions())

    def create_seed_ranges(self):
        out = []
        for i in range(len(self.seeds) // 2):
            start, count = self.seeds[i * 2], self.seeds[(i * 2) + 1]
            out.append(range(start, start + count))
        return out

    def get_total_range_size(self):
        total = 0
        for r in self.seed_ranges:
            total += r.stop - r.start
        return total

    def get_lowest_for_seed_range(self, r: range):
        lowest = 999999999999999
        start = time.time()
        print(f"Processing {r.stop-r.start} items")
        with ThreadPoolExecutor(max_workers=8) as exe:
            results = list(exe.map(self.get_end_position, r))
        """
        for i in r:
            end_location = self.get_end_position(i)
            if end_location < lowest:
                lowest = end_location
        
        return lowest
        """
        time_taken = time.time() - start
        speed = (r.stop - r.start) / time_taken  # items per s
        print(f"Took {time_taken}s with a speed of {speed} items/s")

        return min(results)

    def get_lowest_part2_position(self):
        lowest = 999999999999999999999999999
        total_seeds = self.get_total_range_size()
        print(f"Total seeds: {total_seeds}")
        print(f"Seed ranges: {len(self.seed_ranges)}")
        for i, seed_range in enumerate(self.seed_ranges):
            print(f"{i}/{len(self.seed_ranges)}")
            l = self.get_lowest_for_seed_range(seed_range)
            print(f"Seed range {i}: Lowest: {l}")
            if l < lowest:
                lowest = l
        return lowest


class AintMuchButHonestWork(Puzzle):
    DAY = 5
    YEAR = 2023

    def part1(self):
        return SeedMap(self.input).get_lowest_position()

    def part2(self):
        return SeedMap(self.input).get_lowest_part2_position()
