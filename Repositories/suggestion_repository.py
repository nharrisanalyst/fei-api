from Models.suggestions import ZipcodeSuggestions, CitySuggestions, ZipCitySuggestion, SuggestionList

class SuggestionRepository:
    def __init__(self,pool):
        self.pool =pool

    def findZipCodeSuggestions(self, zipSuggestion:int) -> SuggestionList:
        likeQuery = f'{zipSuggestion}%'
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'select real_zipcodes, city from real_zipcodes join zipcodes as zip on zip.zipcode = real_zipcodes.real_zipcodes join cities as cty on zip.city_id = cty.city_id where real_zipcodes::VARCHAR(10) like %s order by real_zipcodes asc  limit 10',
                    (likeQuery,)
                )
                rows = cur.fetchall()
                zip_and_cities =[ZipCitySuggestion(zip=row[0], city=row[1]) for row in rows]
                suggestionList = [f'{zip_city.zip}, {zip_city.city}'  for zip_city in zip_and_cities]
                return SuggestionList(suggestionList=suggestionList)
        
    def findCitySuggestions(self, citySuggestion:str)->CitySuggestions:
        likeQuery = f'{citySuggestion}%'
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'select real_zipcodes, city from real_zipcodes join zipcodes as zip on zip.zipcode = real_zipcodes.real_zipcodes join cities as cty on zip.city_id = cty.city_id where city ilike %s order by real_zipcodes asc  limit 10',
                    (likeQuery,)
                )
                rows = cur.fetchall()
                zip_and_cities =[ZipCitySuggestion(zip=row[0], city=row[1]) for row in rows]
                suggestionList = [f'{zip_city.zip}, {zip_city.city}'  for zip_city in zip_and_cities]
                return SuggestionList(suggestionList=suggestionList)
        

       