import re

phone = '''+91-9000513511
8897411064
'''
reg1= re.compile(r'([+]?[0-9]{2}?[-]?\d{10})')
reg2 = re.compile(r'\d{10}')
mat=re.findall(reg1,phone)
if len(mat)==0:
    mat=re.findall(reg2,phone)
print(mat)

#Hey I'm adding a new branch