import re


def check_email(s):
    pattern = r'(<\w+\s\w+>\s)?(\w+(.\w+)?@\w+.\w)'
    m = re.match(pattern, s)
    if m:
        print('Email address checked')
        print('Name is', m.group(1))
    else:
        print('Email address is not valid')

address = input('Please input your email address:')
check_email(address)