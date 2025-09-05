from typing import List
from dataclasses import dataclass

@dataclass
class PPC:
    zipcode:int
    year:int
    ppc_avg_score:float
    
PPC_Years = List[PPC]

@dataclass
class Fire:
    zipcode:int
    year:int
    avg_fire_score:float

Fire_Years = List[Fire]
