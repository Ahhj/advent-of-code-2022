# %%
import aocd
import config
from src.utils.read_input import read_input_data

DAY = 7


class CMD:
    """Represents file system objects"""

    def __init__(self, name, root=None, parent=None, size=None, is_dir=False):
        self.name = name
        self.root = root or self
        self.parent = parent
        self.children = {}
        self.size = size
        self.is_dir = is_dir

    def __getitem__(self, key, default=None):
        return self.children.get(key, default)

    def cd(self, dest):
        if dest == "..":
            return self.parent
        elif dest == ".":
            return self
        elif dest == "/":
            return self.root
        else:
            return self.children[dest]

    def ls(self, name, size=None, is_dir=False):
        self.children[name] = CMD(
            name, root=self.root, parent=self, size=size, is_dir=is_dir
        )

    def calculate_size(self):
        total_size = self.size or 0

        for key in self.children:
            if self.children[key].is_dir:
                total_size += self.children[key].calculate_size() or 0
            else:
                total_size += self.children[key].size or 0

        self.size = total_size
        return total_size

    def recurse(self, func):
        func(self)

        for key in self.children:
            self.children[key].recurse(func)


def parse_command_with_output(command_output, cwd):
    command_output = filter(None, map(str.strip, command_output.split("\n")))
    command = next(command_output)

    if command == "ls":
        for output_line in command_output:
            dir_or_size, value = output_line.split()

            if dir_or_size == "dir":
                cwd.ls(value, is_dir=True)
            else:
                size = int(dir_or_size)
                cwd.ls(value, size=size)

        return cwd

    elif "cd" in command:
        _, dest = command.split()
        return cwd.cd(dest)

    else:
        raise ValueError(f"Invalid command {command}")


input_data = read_input_data(DAY)
command_result_sequence = input_data.split("$ ")

cwd = CMD("/")  # Start at root

for command_output in filter(None, command_result_sequence):
    cwd = parse_command_with_output(command_output, cwd)

cwd.root.calculate_size()

# %% Part a

# Flatten
flat_children = []
cwd.root.recurse(flat_children.append)

# Filter directories by threshold
size_threshold = 100000
sizes_below_threshold = [
    x.size for x in flat_children if x.is_dir and x.size < size_threshold
]
aocd.submit(sum(sizes_below_threshold), part="a", year=config.YEAR, day=DAY)

# %% Part b

total_required = 70000000
space_required = 30000000
space_remaining = total_required - cwd.root.size
min_size_to_delete = space_required - space_remaining
sizes_above_threshold = [
    x.size for x in flat_children if x.is_dir and x.size > min_size_to_delete
]
aocd.submit(min(sizes_above_threshold), part="b", year=config.YEAR, day=DAY)

# %%
