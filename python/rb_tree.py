from node import node

class rb_tree:
    red, black = range(0, 2)

    def __init__(self):
        self.nil = node(0, self.black, None, None, None)
        self.root = self.nil

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

    def add_fixup(self, node):
        while node.get_parent().get_color() == self.red:
            if node.get_parent() == node.get_parent().get_parent().get_left():
                y = node.get_parent().get_parent().get_right()
                if y.get_color() == self.red:
                    node.get_parent().set_color(self.black)
                    y.set_color(self.black)
                    node.get_parent().get_parent().set_color(self.red)
                    node = node.get_parent().get_parent()
                elif node == node.get_parent().get_right():
                    node = node.get_parent()
                    self.left_rotate(node.get_parent().get_parent())
                else:
                    node.get_parent().set_color(self.black)
                    node.get_parent().get_parent().set_color(self.red)
                    self.right_rotate(node.get_parent().get_parent())
            else:
                y = node.get_parent().get_parent().get_left()
                if y.get_color() == self.red:
                    node.get_parent().set_color(self.black)
                    y.set_color(self.black)
                    node.get_parent().get_parent().set_color(self.red)
                    node = node.get_parent().get_parent()
                elif node == node.get_parent().get_left():
                    node = node.get_parent()
                    self.right_rotate(node.get_parent().get_parent())
                else:
                    node.get_parent().set_color(self.black)
                    node.get_parent().get_parent().set_color(self.red)
                    self.left_rotate(node.get_parent().get_parent())
        self.get_root().set_color(self.black)

    def add(self, node):
        y = self.get_nil()
        x = self.get_root()
        while x != self.get_nil():
            y = x
            if node.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        node.set_parent(y)
        if y == self.get_nil():
            self.set_root(node)
        elif node.get_key() < y.get_key():
            y.set_left(node)
        else:
            y.set_right(node)
        
        node.set_left(self.get_nil())
        node.set_right(self.get_nil())
        node.set_color(self.red)
        
        self.add_fixup(node)