from sqlalchemy import Column, Integer, String
from db import Base
from db import ENGINE


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255))


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main()