from multiprocessing import Pool, cpu_count

import psycopg2

import random

from tqdm import tqdm

from faker import Faker

fake = Faker()

num_cores = cpu_count() - 1

def insert_data(arg):
    x = int(60000/num_cores)
    print(x)

    with psycopg2.connect (database = "db_1", user = "postgres", password = "",host = "localhost", port = 5432) as conn:
        
        with conn.cursor() as cursor:

                for i in tqdm (range(x), desc = "Inserting Data"):
                     
                     sql = "INSERT INTO orders (user_id,product_name) VALUES (%s,%s)"

                     val = (random.randint(2,59000),fake.company())

                     cursor.execute(sql,val)




if __name__ == "__main__":
     
     with Pool() as pool:
          
          pool.map(insert_data,range(num_cores))



'''from faker import Faker

fake = Faker()

for i in range(0,10):
    print(fake.random_number(digits=2,fix_len=False))

'''