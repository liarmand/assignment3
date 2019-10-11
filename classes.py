class AST:
    def __init__(self, node_type, vertices=None, value="", ):
        self.node_type = node_type
        if value != "":
            self.value = value

        if vertices is None:
            self.vertices = []
        else:
            self.vertices = vertices

    def __repr__(self):
        if len(self.vertices) == 0:
            return str(str(self.node_type) + ":{}")

        temp = ""
        internal =""
        if len(self.vertices) == 1:
            temp = str(self.node_type + ":[")
            internal = self.vertices[0].__repr__()
        else:
            temp = str(self.node_type+":[")
            for elem in self.vertices:
                internal += elem.__repr__() + ","
            internal = internal[0:-1]
        if len(self.vertices) == 1:
            temp += internal + "]"
        else:
            temp += internal + "]"
        return str(temp)
            #str(self.node_type) + ":[" + "".join([elem.node_type + "," for elem in self.vertices]).rstrip(",") + "]")
