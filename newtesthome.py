from hometest import get_name_by_email
from place_holder import login_hold_fetch
email,p=login_hold_fetch()
if "sunnykushwaha789@gmail.com"== email:
    print("true")

else:

    print("sunnykushwaha789@gmail.com")
    print(email)

print(email)
print(get_name_by_email(email)[0])




