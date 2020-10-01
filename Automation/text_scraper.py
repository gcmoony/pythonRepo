import re

phoneNumReg = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
emailReg = re.compile(r"\S+@+\S+\.+\w+\S")

with open("Text Files/example_text_from_news_site.txt", 'r') as text:
    text_str = text.read()
    print(phoneNumReg.search(text_str).group())
    print(emailReg.findall(text_str))