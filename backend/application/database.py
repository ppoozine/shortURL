import databases, sqlalchemy, os
from dotenv import load_dotenv
import redis

load_dotenv()
# PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData(schema="public")
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# Redis
REDIS_URL = os.getenv("REDIS_URL")
pool = redis.ConnectionPool(host=REDIS_URL, port=6379)
redis_db = redis.Redis(connection_pool=pool)