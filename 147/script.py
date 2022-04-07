class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


n = int(input())
fibonacci_of = Fibonacci()
print(fibonacci_of(n))
