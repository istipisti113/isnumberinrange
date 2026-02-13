from behave import given, when, then
from src.is_number_in_range import *

@given('the number is "{number}"')
def step_given_number_is(context, number):
    context.number = number

@given('the maximum is "{max}"')
def step_given_the_maximum_is(context, max):
    context.max = max

@given('the minimum is "{min}"')
def step_given_the_minimum_is(context, min):
    context.min = min

@when("I check if the number is in range")
def step_when_I_check_if_the_number_is_in_range(context):
    context.actual_answer = is_num_in_range(context.number, context.min, context.max)

@then('the result shall be "{result}"')
def step_then_the_result_shall_be(context, result):
    print(result)
    assert context.actual_answer == result, \
        f"Expected '{result}', but got '{context.actual_answer}'"