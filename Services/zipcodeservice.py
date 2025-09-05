from Repositories.zipcode_repository import ZipCodeRepository

class ZipcodeService:
    def __init__(self, repo: ZipCodeRepository):
        self.repo = repo
    def getZipCode(self, zipcode:int):
        return self.repo.findByZip(zipcode)
    def getZipCodeData(self, zipcode:int):
        return self.repo.findDataByZip(zipcode)
    def getAllZipCodes(self):
        return self.repo.queryAllZipCodes()
