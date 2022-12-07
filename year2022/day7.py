import dataclasses

from utils.puzzle import Puzzle


@dataclasses.dataclass
class File:
    name: str
    filesize: int


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children: list[Directory] = []
        self.dirs = {}
        self.files = {}
        self.parent = parent
        self.size = -1
        self.all_dirs = []  # because im lazy

    def add_dir(self, d):
        d.parent = self
        self.dirs[d.name] = d

    def add_file(self, f: File):
        self.files[f.name] = f

    def get_dir(self, name):
        return self.dirs[name]

    def dir_exists(self, name):
        return name in self.dirs

    def file_exists(self, name):
        return name in self.files

    def get_size(self):
        if self.size != -1:
            return self.size
        self.size = sum([f.filesize for name, f in self.files.items()]) + sum(
            [d.get_size() for name, d in self.dirs.items()]
        )
        return self.size

    def get_full_path(self):
        if self.parent is None:
            return self.name
        else:
            r = self.parent.get_full_path() + "/" + self.name
            return r.replace("//", "/")

    def __repr__(self):
        return f"<Dir {self.get_full_path()}>"

    def __str__(self):
        return f"Dir: {self.name}"


def get_line_type(line: str):
    if line[0] == "$":
        # command
        return "cmd"
    if line[0].isnumeric():
        return "file"
    if line[:3] == "dir":
        return "dir"


def create_filetree(inputs: [str]) -> Directory:
    root = Directory("/")
    current_dir = root
    for line in inputs:
        if line == "$ cd /":
            current_dir = root
            continue

        if line.startswith("$ cd"):
            dirname = line.split(" ", 2)[-1]

            if dirname == "..":
                current_dir = current_dir.parent
                continue

            if current_dir.dir_exists(dirname):
                current_dir = current_dir.get_dir(dirname)
                continue

            else:
                # create dir
                newdir = Directory(dirname)
                current_dir.add_dir(newdir)
                root.all_dirs.append(newdir)
                continue

        if line == "$ ls":
            continue  # we don't need to know that

        if line.startswith("dir"):
            dirname = line.split(" ", 1)[-1]
            if not current_dir.dir_exists(dirname):
                newdir = Directory(dirname)
                current_dir.add_dir(newdir)
                root.all_dirs.append(newdir)
            continue

        if line[0].isnumeric():
            # file
            size, filename = line.split(" ", 1)
            current_dir.add_file(File(filename, int(size)))
            continue

    return root


class Day7(Puzzle):
    YEAR = 2022
    DAY = 7

    def part1(self):
        root = create_filetree(self.input.split("\n"))
        total = 0
        for d in root.all_dirs:
            size = d.get_size()
            if size <= 100000:
                total += size
        return total

    def part2(self):
        root = create_filetree(self.input.split("\n"))
        total_space = 70000000
        space_needed = 30000000
        free = total_space - root.get_size()
        diff = space_needed - free
        possible = [d for d in root.all_dirs if d.get_size() >= diff]
        smallest = min(possible, key=lambda d: d.get_size())
        return smallest.get_size()
