import subprocess, Connection

server = Connection.Connection("127.0.0.1", 666)
server.establish_connection()