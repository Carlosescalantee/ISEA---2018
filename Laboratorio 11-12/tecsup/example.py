import functools
import xmlrpc.client
HOST = 'localhost'
PORT = 8069
DB = 'bd_isea'
USER = 'carlos.escalante@tecsup.edu.pe'
PASS = '12345'
root = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid:%d)" % (USER,iud))

call = functools.partial(
	xmlrpc.client.ServerProxy(ROOT + 'object').execute,
	DB, uid, PASS)

sessions = call('openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
	print("Session %s (%s seats)" % (session['name'], session['seats']))

session_id = call('openacademy.session', 'create', {
	'name' : 'My session',
	'course_id' : 2,
	})	
