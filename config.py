HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'english'
USERNAME = 'root'
PASSWORD = 'password'
# mysql数据库URI
# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE) 