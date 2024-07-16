# wap to print no from 1 to 100
# but print fizz in multiple of three and
# print buzz in multiple of five
# print fizzbuzz in multiple of both three and five


for i in range(1,100):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
