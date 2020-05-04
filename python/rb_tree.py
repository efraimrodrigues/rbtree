from node import node

class rb_tree:
    red, black = range(0, 2)

    def __init__(self):
        self.nil = node(0, self.black, None, None, None)
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node

    def get_nil(self):
        return self.nil

    def left_rotate(self, x):
        y = x.get_right()
        x.set_right(y.get_left())
        
        if y.get_left() != self.get_nil():
            y.get_left().set_parent(x)
        y.set_parent(x.get_parent())
        
        if x.get_parent() == self.get_nil():
            self.set_root(y)
        elif x == x.get_parent().get_left():
            x.get_parent().set_left(y)
        else:
            x.get_parent().set_right(y)
        
        y.set_left(x)
        x.set_parent(y)

    def right_rotate(self, x):
        y = x.get_left()
        x.set_left(y.get_right())
        
        if y.get_right() != self.get_nil():
            y.get_right().set_parent(x)
        y.set_parent(x.get_parent())
        
        if x.get_parent() == self.get_nil():
            self.set_root(y)
        elif x == x.get_parent().get_right():
            x.get_parent().set_right(y)
        else:
            x.get_parent().set_left(y)
        
        y.set_right(x)
        x.set_parent(y)

    def add(self, key):
        if self.root is None:
            self.root = node(key, self.black, self.nil, self.nil, self.nil)

