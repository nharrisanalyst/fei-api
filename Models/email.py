from dataclasses import dataclass
from typing import Literal

@dataclass
class EmailForm:
    type:Literal['FindAnAgent', 'BuyHomeIns', 'BuyCarIns']
    name:str
    email:str
    message:str