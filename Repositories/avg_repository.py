from Models.average import DataAvgData, DataAvg
import psycopg


class AverageRepo:
    def __init__(self, pool):
        self.pool = pool
    
    def queryAvg(self) -> DataAvgData:
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute('select * from all_avg')
                rows_sql = cur.fetchall()
                return [DataAvg(
                                year = row[0], 
                                fire_risk=row[1], 
                                ppc_class=row[2], 
                                non_cat_fire_claims=float(row[3]), 
                                non_cat_fire_losses=float(row[4]), 
                                non_cat_smoke_claims=float(row[5]), 
                                non_cat_smoke_losses=float(row[6]), 
                                cat_fire_claims=float(row[7]),
                                cat_fire_losses=float(row[8]),
                                cat_smoke_claims=float(row[9]),
                                cat_smoke_losses=float(row[10])
                                ) for row in rows_sql]
        