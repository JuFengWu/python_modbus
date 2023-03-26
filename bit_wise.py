

testNumber = 29
upper = (testNumber>>4) & 0XF
lower = testNumber& 0XF
print(upper)
print(lower)


testNumberUp = 1
testNumberDown = 13

finalNumber = (testNumberUp<<4) + testNumberDown
print(finalNumber)
