def parrot():
    while True:
        message = yield
        print("Parrot says: {}".format(message))


if __name__ == "__main__":
    generator = parrot()
    generator.send(None)
    generator.send("Hello")
    generator.send("World")
