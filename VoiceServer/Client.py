class client():
    def __init__(self, id, address, name):

        self.cid = id
        self.caddress = address
        self.cname = name

        print("User created: ", self.cname, " Address: ", self.caddress)

    def name(self):
        return self.cname
    def address(self):
        return self.caddress
    def id(self):
        return self.cid

    def setname(self, newname):
        self.cname = newname
