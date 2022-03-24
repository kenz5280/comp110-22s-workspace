"""Union type gives flexibility to single vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str or int!"""
    # a single parameter can be more than one type; arg given can be either 
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")
    

log("hello")
log(110)