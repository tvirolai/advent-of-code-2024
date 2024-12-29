def read_input(filename):
    with open("data/{0}".format(filename), "r") as f:
        return [x.strip() for x in f.readlines()]


def read_input_as_nums(filename):
    return [int(x) for x in read_input(filename)]


def read_raw_input(filename):
    with open("data/{0}".format(filename), "r") as f:
        return f.read()
