class Fizzbuzz():
    def go(num):
        if num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        return num
