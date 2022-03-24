"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Default parameters give more flexibility to a function."""
    # can call argument w/o second parameter, more than one parameters/args are optional
    # Default parameters must follow requiered parameters
    # every parameter after first default also has to be default
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))