from dataclasses import dataclass
from typing import List

@dataclass
class CitySuggestions:
    cities:List[str]
    
@dataclass
class ZipcodeSuggestions:
    zipcodes:List[int]

@dataclass 
class ZipCitySuggestion:
    zip:str
    city:str
    
@dataclass
class SuggestionList:
    suggestionList:List[str]