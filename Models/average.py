from typing import List, Literal
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

## This is the model for all the averages. These numbers are all averages grouped by year
@dataclass
class DataAvg:
    year:Literal[2018,2019,2020,2021,2022,2023]
    fire_risk:float
    ppc_class:float
    non_cat_fire_claims:float
    non_cat_fire_losses:float
    non_cat_smoke_claims:float
    non_cat_smoke_losses:float
    cat_fire_claims:float
    cat_fire_losses:float
    cat_smoke_claims:float
    cat_smoke_losses:float
    
    
DataAvgData = List[DataAvg]

@runtime_checkable
class PZipCodeRepository(Protocol):
    def getDataAvg(self)->DataAvgData:
        ...