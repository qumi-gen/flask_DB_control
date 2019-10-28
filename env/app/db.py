from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy.ext.declarative



#print(engine.query.all())

Base = sqlalchemy.ext.declarative.declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    kana = sqlalchemy.Column(sqlalchemy.String)

#url = 'postgresql+psycopg2://ユーザー名:パスワード@ホスト:ポート/DB名' 
#'postgresql+psycopg2://ユーザー名:パスワード@ホスト:ポート/DB名' を./app/url.txtに記述し、.gitignoreにurl.txtを指定する

f = open('url.txt','r')
url = f.readline()
engine = create_engine(url,echo=True)

# スキーマ作成
Base.metadata.create_all(engine)
