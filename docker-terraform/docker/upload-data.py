import argparse, os, sys
from time import time
import pandas as pd
from sqlalchemy import create_engine
import gzip

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url

    # Get the name of the file from url
    file_name = url.rsplit('/', 1)[-1].strip()
    print(f'Downloading {file_name} ...')
    # Download file from url
    if file_name not in os.listdir(os.getcwd()):
        os.system(f"wget {url} -O {file_name}")
    cwd_path = os.getcwd()
    print(file_name)
    print('\n')

    # Create SQL Engine
    engine = f"postgresql://{user}:{password}@{host}:{port}/{db}"

    # Read file (csv)
    file_path = os.path.join(cwd_path, file_name)
    if '.csv.gz' in file_name:
        df = pd.read_csv(file_path, nrows=5)
        df_iter = pd.read_csv(file_path, iterator=True, chunksize=100000)
    else:
        print('Error, only csv file allowed.')
        sys.exit()
    
    # Create the table
    df.head(n=0).to_sql(con=engine, name=table, if_exists='replace')

    # Insert Values
    
    try:
        while True:
            start_time = time()
            df = next(df_iter)

            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

            df.to_sql(con=engine, name=table, if_exists='append')

            end_time = time()
            print('Inserted data to database, took %.3f second' % (end_time - start_time))
            
    except:
        print('No more rows to be Insert')

    
    
if __name__ == '__main__':
    # Parsing arguments
    parser = argparse.ArgumentParser(description='Loading data from .paraquet file link to a Postgres datebase.')

    parser.add_argument('--user', help='Username for Postgres.')
    parser.add_argument('--password', help='Password for Postgres.')
    parser.add_argument('--host', help='Host for Postgres.')
    parser.add_argument('--port', help='Port for Postgres.')
    parser.add_argument('--db', help='Database for Postgres.')
    parser.add_argument('--table', help='Target table name.')
    parser.add_argument('--url', help='URL data source.')

    args = parser.parse_args()

    main(args)