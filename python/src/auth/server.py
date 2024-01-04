import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

#config
server.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
server.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
server.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')

@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return 'missing credentials', 401
    
    #check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        'SELECT email, password FROM user WHERE email=%s', (auth.username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        password = user_row[1]

        if auth.password != password:
            return 'invalid credentials', 401
        else:
            return createJWT(auth.username, os.environ.get('JWT_SECRET', True))     
    else:
        return 'invalid credentials', 401


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'admin': authz
        },
        secret,
        algorithm='HS256')


@server.route('/validate', methods=['POST'])
def validate():
    token = request.headers.get('Authorization')
    if not token:
        return 'missing credentials', 401
    
    token = token.split(' ')[1]

    try:
        decoded = jwt.decode(token, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
    except:
        return 'not authorized', 403
    
    return decoded, 200


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)