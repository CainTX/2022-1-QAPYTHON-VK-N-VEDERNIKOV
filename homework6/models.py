from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class FirstModel(Base):

    __tablename__ = 'total_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)


class SecondModel(Base):

    __tablename__ = 'total_requests_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    status_code = Column(String(1000), nullable=False)
    amount = Column(Integer, nullable=False)


class ThirdModel(Base):

    __tablename__ = 'top_frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    size = Column(Integer, nullable=False)


class FourthModel(Base):

    __tablename__ = 'top_requests_client_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(10000), nullable=False)
    status_code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(50), nullable=False)


class FifthModel(Base):

    __tablename__ = 'top_requests_server_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
