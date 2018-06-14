'testing code'

import orm
from models import User,Blog,Comment
import asyncio

async def test():

    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='www-data', password='www-data',db='awesome')

    #没有设置默认值的一个都不能少
    u = User(name='Tim', email='frogswawa@outlook.com', passwd='password', image='about:blank',id='110')

    await u.save()

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()

'sql check code'
import mysql.connector

conn=mysql.connector.connect(user='www-data', password='www-data', database='awesome')
cursor=conn.cursor()
cursor.execute('select * from users')
data=cursor.fetchall()
print(data)
