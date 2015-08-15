from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	
	id = Column(String(20),primary_key = True)
	name = Column(String(20))
#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test') #数据库类型+数据库驱动名称：//用户名：口令@机器地址：端口号/数据库名
#创建DBSession类型
DBSession = sessionmaker(bind = engine)

#添加记录
session = DBSession()
new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
session.close()

#查询
session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('name:',user.name)
session.close()