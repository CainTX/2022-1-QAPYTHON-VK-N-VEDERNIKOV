from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class FirstModel(Base):

    __tablename__ = 'test1'
    __table_args__ = {'mysql_charset': 'utf8'}

    amount = Column(Integer, primary_key=True, nullable=False)


class SecondModel(Base):

    __tablename__ = 'test2'
    __table_args__ = {'mysql_charset': 'utf8'}

    status_code = Column(String(1000), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)


class ThirdModel(Base):

    __tablename__ = 'test3'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(50), nullable=False)
    size = Column(Integer, nullable=False)


class FourthModel(Base):

    __tablename__ = 'test4'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(10000), nullable=False)
    status_code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(50), nullable=False)


class FifthModel(Base):

    __tablename__ = 'test5'
    __table_args__ = {'mysql_charset': 'utf8'}

    position = Column(Integer, primary_key=True, nullable=False)
    ip = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
