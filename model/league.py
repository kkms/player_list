""" League Model Class """

from dataclasses import field
from typing import List, ClassVar, Type
from marshmallow_dataclass import dataclass
from marshmallow import Schema
from .league_ref import LeagueRef

page_size_dict = {"data_key":"pageSize", "attribute":"page_size"}
page_index_field_dict = {"data_key":"pageIndex", "attribute":"page_index"}
page_count_field_dict = {"data_key":"pageCount", "attribute":"page_count"}

@dataclass
class League:
    """ League Model class """


    count: int
    page_index: int = field(metadata=page_index_field_dict)
    page_size: int = field(metadata=page_size_dict)
    page_count: int = field(metadata=page_count_field_dict)
    items: List[LeagueRef] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Schema # type: ignore
