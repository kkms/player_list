"""Player Model class """

from dataclasses import field
from typing import ClassVar, Type

from marshmallow_dataclass import dataclass
from marshmallow import Schema



first_name_dict = {"data_key":"firstName","attribute":"first_name"}
last_name_dict = {"data_key":"lastName","attribute":"last_name"}
dob_dict = {"data_key":"dateOfBirth","attribute":"dob"}

@dataclass
class Player:
    """ Player Model Implmeentation Class """

    first_name: str = field(metadata=first_name_dict)
    last_name: str = field(metadata=last_name_dict)
    weight: int
    height: int
    age: int
    dob: str = field(metadata=dob_dict)
    Schema: ClassVar[Type[Schema]] = Schema # type: ignore
