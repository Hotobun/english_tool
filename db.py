from sqlalchemy import Column,Integer,String, DateTime, func, Boolean
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import english 

engine = create_engine(DB_URI,echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class English(Base):
    # 定义表名
    __tablename__ = 'english'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。
    
    id = Column(Integer,primary_key = True, unique=True)
    word = Column(String(20))
    count = Column(Integer)
    symbol = Column(String(100))
    translate = Column(String(200))
    en = Column(String(200))
    zh = Column(String(200))
    used = Column(Boolean, default = False)
    
    def __repr__(self):
        return '<English(id="{}", message="{}...")>'.format(self.rpid, self.message[:20].replace("\n", ' '))

def insert(item):
    # item type : dict
    # 插入数据
    Base.metadata.create_all()
    if type(item) == dict:
        new = English()
        new.id = item["id"]
        new.word = item["word"]
        new.count = item["count"]
        new.symbol = item["symbol"]
        new.translate = item["translate"]
        new.en = item["en"]
        new.zh = item["zh"]

        # 查找id是否在数据表里已存在
        temp = session.query(English).filter_by(id=item['id']).all()
        if temp:
            if temp == new:
                return 
            temp = new 
        else:
            session.add(new)
        # print("item --> ", new)
        session.commit()

def get_rand_data():
    # id type : int
    # rtype : tuple
    target = session.query(English).filter( English.used != True).order_by(func.rand()).first()
    result = (target.id, target.word ,target.symbol, target.translate, target.en, target.zh)
    target.used = True
    session.commit()
    return result

def Create_table():
    # 创建数据表
    Base.metadata.create_all()
    print("table {} 创建成功".format(English.__tablename__))

if __name__ == "__main__":
    Create_table()
    english.write_sql()