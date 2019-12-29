def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
print(times3(9))

times5 = make_multiplier_of(5)
print(times5(3))

print(times5(times3(2)))
