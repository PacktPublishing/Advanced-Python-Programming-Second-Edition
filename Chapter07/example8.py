def range_generator(n):
    i = 0
    while i < n:
        print("Generating value {}".format(i))
        yield i
        i += 1


if __name__ == "__main__":
    generator = range_generator(3)
    print(generator)

    next(generator)

    next(generator)
