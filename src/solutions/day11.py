# %%
from __future__ import annotations
import re
import functools
import aocd
from operator import mul, add
import config
from src.utils.read_input import read_input_data

DAY = 11

# %%
GLOBAL_MODULO = functools.reduce(mul, [2, 3, 5, 7, 11, 13, 17, 19, 23, 27])


def update_remainder(op, value, other, divisor):
    # Use properties of modulo operator to prevent numbers getting too large
    return op(value % divisor, other % divisor) % divisor


class _Item:
    # Empty clast, just for type hints inside functools.singledispatchmethod
    pass


class Item(_Item):
    def __init__(self, initial_value):
        self.value = initial_value

    @functools.singledispatchmethod
    def __mul__(self, other: int):
        self.value = update_remainder(mul, self.value, other, GLOBAL_MODULO)
        return self

    @__mul__.register
    def _(self, other: _Item):
        # Override for multiplication by another item value
        return self * other.value

    def __add__(self, other):
        self.value = update_remainder(add, self.value, other, GLOBAL_MODULO)
        return self

    def __mod__(self, divisor):
        return self.value % divisor

    def __div__(self, other):
        self.value /= other
        return self

    def __floordiv__(self, other):
        self.value //= other
        return self


class Monkey:
    def __init__(self, index, starting_items, operation, test_params):
        self.index = index
        self.starting_items = starting_items[:]
        self.current_items = list(map(Item, starting_items))
        self._operation = operation
        self.divisible_by = test_params["divisible_by"]
        self.if_true = test_params["if_true"]
        self.if_false = test_params["if_false"]
        self.n_inspections = 0

    def turn(self, divide_by=1):
        for item in self.current_items:
            new_worry = self._inspect(item)
            new_worry = self._bored(new_worry, divide_by)

            if self._test(new_worry):
                recipient = self.if_true
            else:
                recipient = self.if_false

            yield new_worry, recipient

        self.current_items = []

    def _inspect(self, item):
        self.n_inspections += 1
        return self._operation(item)

    def _bored(self, item, divide_by):
        item //= divide_by
        return item

    def _test(self, item):
        return (item % self.divisible_by) == 0

    def receive(self, new_item):
        self.current_items.append(new_item)

    def reset(self):
        self.current_items = list(map(Item, self.starting_items))
        self.n_inspections = 0


def get_operation_func(operation_string):
    parts = operation_string.split()
    operator_string = parts.pop(1)
    operator_func = {"*": mul, "+": add}.get(operator_string)
    left_string, right_string = parts

    if left_string == "old" and right_string == "old":
        def _operation(x):
            return operator_func(x, x)

    elif left_string == "old":
        def _operation(x):
            return operator_func(x, int(right_string))

    elif right_string == "old":
        def _operation(x):
            return operator_func(int(left_string), x)

    else:
        raise ValueError(f"Unable to parse operation '{operation_string}'")

    return _operation


def parse_monkey(monkey_data):
    index, starting_items, operation, divisible_by, if_true, if_false = monkey_data
    return Monkey(
        index=int(index),
        starting_items=list(map(int, starting_items.split(", "))),
        operation=get_operation_func(operation),
        test_params=dict(
            divisible_by=int(divisible_by),
            if_true=int(if_true),
            if_false=int(if_false)
        )
    )


def one_round(monkeys, divide_by=1):
    for m in monkeys:
        for item, recipient in m.turn(divide_by=divide_by):
            monkeys[recipient].receive(item)


def evaluate_monkey_business(monkeys, n_rounds=20, divide_by=1):
    [m.reset() for m in monkeys]

    for _ in range(n_rounds):
        one_round(monkeys, divide_by=divide_by)

    inspection_counts = [m.n_inspections for m in monkeys]
    monkey_business = mul(*sorted(inspection_counts, reverse=True)[:2])
    return monkey_business


monkey_pattern = r"Monkey (\d):\n  Starting items: (.*)\n  Operation: new = (.*)\n  Test: divisible by (.*)\n    If true: throw to monkey (\d)\n    If false: throw to monkey (\d)"

input_data = read_input_data(DAY)
monkey_data = re.findall(monkey_pattern, input_data)
monkeys = list(map(parse_monkey, monkey_data))

monkey_business = evaluate_monkey_business(monkeys, 20, divide_by=3)
aocd.submit(monkey_business, part="a", day=DAY, year=config.YEAR)

# %% Part b

monkey_business = evaluate_monkey_business(monkeys, 10000, divide_by=1)
aocd.submit(monkey_business, part="b", day=DAY, year=config.YEAR)

# %%