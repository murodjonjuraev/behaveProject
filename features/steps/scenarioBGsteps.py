# Usind background in feature file

from behave import *


@given(u'I launch browser')
def step_impl(context):
    assert True, "test Passed"


@when(u'I open Application')
def step_impl(context):
    assert True, "test Passed"


@when(u'Enter valid username and password')
def step_impl(context):
    assert True, "test Passed"


@when(u'click login')
def step_impl(context):
    assert True, "test Passed"


@then(u'User must login to the Dashboard page')
def step_impl(context):
    assert True, "test Passed"


@when(u'navigate to search page')
def step_impl(context):
    assert True, "test Passed"


@then(u'search page should display')
def step_impl(context):
    assert True, "test Passed"


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True, "test Passed"


@then(u'advanced search page should display')
def step_impl(context):
    assert True, "test Passed"
