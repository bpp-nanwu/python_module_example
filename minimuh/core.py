import numpy

def cow_say(text):
    return f"im cow: {text}"


def car_say(text):
    return f"im car: {text}"


def martin_say(text):
    return f"im martin: {text}"


def robot_say(text):
    robot_id = numpy.random.randint(10000)
    return f"im robot_{robot_id}: {text}"
