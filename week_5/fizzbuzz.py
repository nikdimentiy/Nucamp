def fizzbuzz(num):
    for i in range(1, num):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        print(i)


fizzbuzz(50)
