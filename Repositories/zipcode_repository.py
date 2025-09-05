from Models.zipcode import Zipcode, ZipcodeDataList, ZipcodeData, ZipcodeAllList

class ZipCodeRepository:
    def __init__(self, pool):
        self.pool = pool
    # %s where zipcode goes 
    def findByZip(self, zipcode: int) -> Zipcode:
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT zipcode, city, county FROM zipcodes z join cities using(city_id) join counties using(county_id) where zipcode = %s',
                    (zipcode,)
                )
                row_sql = cur.fetchone()
            return Zipcode(zipcode=row_sql[0], city=row_sql[1], county=row_sql[2])
    
    def findDataByZip(self, zipcode:int)->ZipcodeDataList:
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT * FROM fire_pp_claims_and_losses WHERE zipcode = %s',
                    (zipcode,)
                )
                rows_sql = cur.fetchall()
            return [ZipcodeData(year=row[0], zipcode=row[1], city=row[2],  county=row[3], fire_risk=row[4], ppc_class=row[5], fhsz_ranking =row[6],
                                non_cat_fire_claims=row[7], non_cat_fire_losses=row[8],
                                non_cat_smoke_claims=row[9], non_cat_smoke_losses=row[10],
                                cat_fire_claims=row[11], cat_fire_losses=row[12],
                                cat_smoke_claims=row[13], cat_smoke_losses=row[14]) for row in rows_sql]
    
    def queryAllZipCodes(self) ->ZipcodeAllList:
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT zipcode, city, county FROM zipcodes z join cities using(city_id) join counties using(county_id) WHERE zipcode IN (SELECT real_zipcodes from real_zipcodes)'
                )
                rows_sql = cur.fetchall()
                return [Zipcode(zipcode=row[0], city=row[1], county=row[2]) for row in  rows_sql]