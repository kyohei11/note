import re


def cipher(text):
    return re.sub('([a-z])', chr(219 - ord(r'\1')), text)


text = 'this is a message'
ans = cipher(text)
print(ans)
ans = cipher(ans)
print(ans)
