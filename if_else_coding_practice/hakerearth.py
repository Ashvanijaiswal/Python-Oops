import re

txt = "The rain \bin \nSpain\b hello"
x = re.search(r"", txt)
print(x.span())
print(x.string)
print(x.group())
print(re.sub(r'\b','\b',txt))
