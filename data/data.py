from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_adress: str = None
    permanent_adress : str = None
