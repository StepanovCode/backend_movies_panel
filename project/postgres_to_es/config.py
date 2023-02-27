import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

es_schema = 'es_schema.json'
es_state = 'es_state.json'

etl_fetch_delay = 1

fetchmany_size = int(os.environ.get('FETCHMANY_SIZE'))

dsn = {'dbname': os.environ.get('DB_NAME'),
       'user': os.environ.get('DB_USER'),
       'password': os.environ.get('DB_PASSWORD'),
       # 'host': '127.0.0.1',
       'host': os.environ.get('DB_HOST'),
       'port': os.environ.get('DB_PORT')
       }

es_params = {
       # 'host': '127.0.0.1',
       # 'port': 9200,
       'host': os.environ.get('ES_HOST'),
       'port': os.environ.get('ES_PORT'),
       'index_name': 'movies',
       'index_config': "es_schema.json"
}
