from dataclasses import dataclass
from typing import Protocol, runtime_checkable, List

## Model for Zipcode 

@dataclass
class Zipcode:
    zipcode:int
    city:str
    county:str
    
@dataclass
class ZipcodeData:
    year:int
    zipcode:int
    city:str
    county:str
    fire_risk:float
    ppc_class:float
    fhsz_ranking:float
    non_cat_fire_claims:int
    non_cat_fire_losses:int
    non_cat_smoke_claims:int
    non_cat_smoke_losses:int
    cat_fire_claims:int
    cat_fire_losses:int
    cat_smoke_claims:int
    cat_smoke_losses:int
    
ZipcodeDataList = List[ZipcodeData]
ZipcodeAllList = List[Zipcode]
    
@runtime_checkable
class PZipCodeRepository(Protocol):
    def findByZip(self, zipcode:int)->Zipcode:
        ...
    def findDataByZip(self, zipcode:int)->ZipcodeDataList:
        ...
    def queryAllZipCodes(self) ->ZipcodeAllList:
        ...