# Configuración de la conexión

url = <insert server URL>
db = <insert database name>
username = 'admin'
password = <insert password for your admin user (default: admin)>


# Uso XML-RPC

import xmlrpc.client

url_db1 = "http://127.0.0.1:8015"
db_1 = 'odoo15_demo'
username_db_1 = 'admin'
password_db_1 = 'admin'

common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))

version_db1 = common_1.version()

url_db2 = "http://localhost:8065"
db_2 = 'odoo16_demo'
username_db_2 = 'admin'
password_db_2 = 'admin'

common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))

version_db2 = common_2.version()
