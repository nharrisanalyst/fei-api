from Repositories.suggestion_repository import SuggestionRepository

class SuggestionService:
    def __init__(self, repo:SuggestionRepository):
        self.repo = repo
    def getZipCodeSuggestions(self, zipcdoeSuggestion:int):
        return self.repo.findZipCodeSuggestions(zipcdoeSuggestion)
    def getCitySuggestions(self, citySuggestion:str):
        return self.repo.findCitySuggestions(citySuggestion)