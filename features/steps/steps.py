from behave import *
from calculator import *

@given('a {values}')
def step_impl(context, values):
    context.values = values.split(',')

@when('the calculator sums the values')
def step_impl(context):
    context.calculator_total = add(int(context.values[0]),int(context.values[1]))

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.calculator_total == total)
