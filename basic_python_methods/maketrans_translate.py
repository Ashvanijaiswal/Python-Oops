first_string='abc'
second_string='xyz'
third_string='ab'
txt='ebcdefghiabdc'
maketrans_string=txt.maketrans(first_string,second_string)
print(maketrans_string)
print(txt.translate(maketrans_string))

a,b,c=['5*']*3
print(a,b,c)
