ch=input("Enter a letter:")
v='a e i o u'.split(' ')
if(ch in v):
    print("Enter lette is vowel")
elif ch=='y':
    print("Sometimes it's vowel and sometime it's consonant")
else:
    print("Enter letter is consonant")
