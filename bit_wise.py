
testNumber = 0x10345678
print(testNumber>>4)

upper = (testNumber>>4) & 0XF
lower = testNumber& 0XF
print(upper) # 4148
print(lower) # 22136


testNumberUp = 1
testNumberDown = 13 #D

finalNumber = (testNumberUp<<4) + testNumberDown
print(hex(finalNumber))
