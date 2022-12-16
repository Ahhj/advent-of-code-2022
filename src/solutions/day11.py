# %%
import aocd
from itertools import product
from operator import mul
import config

DAY = 11

# %%


class Item:
    def __init__(self, starting_value):
        self.starting_value = starting_value

    def __mul__(self, x):
        pass

    def __add__(self, x):
        pass

    def __mod__(self, x):
        pass


class Monkey:
    def __init__(self, index, starting_items, operation, test_params):
        self.index = index
        self.starting_items = list(map(Item, starting_items[:]))
        self.current_items = self.starting_items[:]
        self._operation = operation
        self.divisible_by = test_params["divisible_by"]
        self.if_true = test_params["if_true"]
        self.if_false = test_params["if_false"]
        self.n_inspections = 0

    def turn(self, divide_by=3):
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
        self.current_items = self.starting_items[:]
        self.n_inspections = 0


test_monkeys = [
    Monkey(
        0,
        starting_items=[79, 98],
        operation=lambda old: old * 19,
        test_params=dict(divisible_by=23, if_true=2, if_false=3),
    ),
    Monkey(
        1,
        starting_items=[54, 65, 75, 74],
        operation=lambda old: old + 6,
        test_params=dict(divisible_by=19, if_true=2, if_false=0),
    ),
    Monkey(
        2,
        starting_items=[79, 60, 97],
        operation=lambda old: old * old,
        test_params=dict(divisible_by=13, if_true=1, if_false=3),
    ),
    Monkey(
        3,
        starting_items=[74],
        operation=lambda old: old + 3,
        test_params=dict(divisible_by=17, if_true=0, if_false=1),
    ),
]

monkeys = [
    Monkey(
        0,
        starting_items=[66, 71, 94],
        operation=lambda old: old * 5,
        test_params=dict(divisible_by=3, if_true=7, if_false=4),
    ),
    Monkey(
        1,
        starting_items=[70],
        operation=lambda old: old + 6,
        test_params=dict(divisible_by=17, if_true=3, if_false=0),
    ),
    Monkey(
        2,
        starting_items=[62, 68, 56, 65, 94, 78],
        operation=lambda old: old + 5,
        test_params=dict(divisible_by=2, if_true=3, if_false=1),
    ),
    Monkey(
        3,
        starting_items=[89, 94, 94, 67],
        operation=lambda old: old + 2,
        test_params=dict(divisible_by=19, if_true=7, if_false=0),
    ),
    Monkey(
        4,
        starting_items=[71, 61, 73, 65, 98, 98, 63],
        operation=lambda old: old * 7,
        test_params=dict(divisible_by=11, if_true=5, if_false=6),
    ),
    Monkey(
        5,
        starting_items=[55, 62, 68, 61, 60],
        operation=lambda old: old + 7,
        test_params=dict(divisible_by=5, if_true=2, if_false=1),
    ),
    Monkey(
        6,
        starting_items=[93, 91, 69, 64, 72, 89, 50, 71],
        operation=lambda old: old + 1,
        test_params=dict(divisible_by=13, if_true=5, if_false=2),
    ),
    Monkey(
        7,
        starting_items=[76, 50],
        operation=lambda old: old * old,
        test_params=dict(divisible_by=7, if_true=4, if_false=6),
    ),
]


def one_round(monkeys, divide_by=3):
    for m in monkeys:
        for item, recipient in m.turn(divide_by=divide_by):
            monkeys[recipient].receive(item)


def evaluate_monkey_business(monkeys, n_rounds=20, divide_by=3):
    [m.reset() for m in monkeys]

    for _ in range(n_rounds):
        one_round(monkeys, divide_by=divide_by)

    inspection_counts = [m.n_inspections for m in monkeys]
    monkey_business = mul(*sorted(inspection_counts, reverse=True)[:2])
    return monkey_business


monkey_business = evaluate_monkey_business(monkeys, 20)
# aocd.submit(monkey_business, part="a", day=DAY, year=config.YEAR)

# %% Part b

divide_bys = [1]
subtracts = [0]
round_results = [
    [1, [2, 4, 3, 6]],
    [20, [99, 97, 8, 103]],
    [1000, [5204, 4792, 199, 5192]],
    # [10000, [52166, 47830, 1938, 52013]
]
monkey_business = None

for divide_by, subtract in product(divide_bys, subtracts):
    [m.reset() for m in test_monkeys]
    elapsed_rounds = 0

    for n_rounds, expected_result in round_results:
        for _ in range(n_rounds - elapsed_rounds):
            one_round(test_monkeys, divide_by=divide_by)

        elapsed_rounds += n_rounds
        actual_result = [m.n_inspections for m in test_monkeys]
        print(n_rounds, actual_result)

        if actual_result != expected_result:
            break
        else:
            continue

    else:
        # print(f"Fitted parameters:\ndivide_by={divide_by}\nsubtract={subtract}")
        # # Use the parameters to evaluate on the real monkeys
        # monkey_business = evaluate_monkey_business(
        #     monkeys,
        #     n_rounds=10000,
        #     divide_by=divide_by,
        #     subtract=subtract,
        # )
        break

# assert monkey_business != None, "Could not find suitable parameters"

# aocd.submit(monkey_business, part="b", day=DAY, year=config.YEAR)
# %%
