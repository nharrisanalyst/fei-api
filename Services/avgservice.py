from Repositories.avg_repository import AverageRepo

class AverageService:
    def __init__(self, repo:AverageRepo):
        self.repo = repo
    def getDataAvg(self):
        return self.repo.queryAvg()
        
