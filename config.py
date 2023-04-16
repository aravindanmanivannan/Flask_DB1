from app import app
from flaskext.mysql import MySQL
 
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'aravind'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ZQGq6qMmpG6TFbdBk'
app.config['MYSQL_DATABASE_DB'] = 'aravind-testing'
app.config['MYSQL_DATABASE_HOST'] = '210.18.157.101'
app.config['MYSQL_DATABASE_PORT'] = 3307

mysql.init_app(app)