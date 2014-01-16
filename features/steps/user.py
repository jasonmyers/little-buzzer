import secrets

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
    username = br.find_element_by_name("openid")
    username.send_keys("https://www.google.com/accounts/o8/id")
    br.find_element_by_id("submit").click()

    if br.title == "Sign in - Google Accounts":
        email = br.find_element_by_id("Email")
        email.send_keys(secrets.GOOGLE_USERNAME)
        passwd = br.find_element_by_id("Passwd")
        passwd.send_keys(secrets.GOOGLE_PASSWORD)
        br.find_element_by_id("signIn").click()

@then(u'I should see welcome text')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('welcome')

@when(u'I click the logout button')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("Logout").click()

@then(u'I should see a request to log in again')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('openid')
