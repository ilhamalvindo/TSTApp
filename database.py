from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://xpjfchbo:urdE0vW2Q8Q9iVYuX6-DGmundndpKKBc@rosie.db.elephantsql.com/xpjfchbo"

#"postgresql://postgres:vestionarmy73@localhost:5432/local_db_tst_rpl" //local database
#"postgresql://xpjfchbo:urdE0vW2Q8Q9iVYuX6-DGmundndpKKBc@rosie.db.elephantsql.com/xpjfchbo"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()