"""League Reference Model Class """

from dataclasses import field
from marshmallow_dataclass import dataclass

ref_field_dict = {"data_key":"$ref", "attribute":"ref"}

@dataclass
class LeagueRef:
    """Reference Model Class """

    ref: str = field(metadata=ref_field_dict)
