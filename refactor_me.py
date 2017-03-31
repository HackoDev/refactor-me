#!/usr/bin/env python3

from collections import namedtuple, defaultdict

MyExpense = namedtuple('MyExpense', ('type_', 'amount'))


def sum_expenses(expenses, min_amount=0):
    aggregated_expenses = defaultdict(int)
    for expense in expenses:
        if expense.amount >= min_amount:
            aggregated_expenses[expense.type_] += expense.amount
    return aggregated_expenses


def print_expenses(expenses):
    for expense, amount in sorted(expenses.items(),
                                  key=lambda x: x[1], reverse=False):
        print(expense, amount)


# test data
# TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
foo = [MyExpense('food', 4), MyExpense('food', 3), MyExpense('car', 3), MyExpense('dog', 1)]
print_expenses(sum_expenses(foo, 2))
