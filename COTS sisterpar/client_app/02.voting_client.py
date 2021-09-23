import xmlrpc.client

s = xmlrpc.client.ServerProxy('localhost:8080')
print(s.vote("candidate_1"))

print(s.querry())

# Print list of available methods
print(s.system.listMethods())
