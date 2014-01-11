@when(u'I go to the front page of the site')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see that the title is "Little Buzzer"')
def step_impl(context):
    assert context.browser.title == "Little Buzzer"

@when(u'I submit my username and password')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000/login')
    username = br.find_element_by_name("username")
    password = br.find_element_by_name("password")
    username.send_keys("dummy_user")
    username.send_keys("dummy_password")
    br.find_element_by_id("submit").click()

@then(u'I should see the welcome text')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('welcome')
