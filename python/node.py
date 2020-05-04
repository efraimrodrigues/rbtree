class node:
    def __init__(self, key, color, parent, left, right):
        self.__key = key
        self.__color = color
        self.__parent = parent
        self.__left = left
        self.__right = right
        self.__visited = None
        self.__index = None

    def get_key(self):
        return self.__key
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def get_parent(self):
        return self.__parent

    def set_parent(self, node):
        self.__parent = node
    
    def get_left(self):
        return self.__left

    def set_left(self, node):
        self.__left = node

    def get_right(self):
        return self.__right

    def set_right(self, node):
        self.__right = node

    def get_visited(self):
        if self.__visited is None:
            return False
        else:
            return True

    def set_visited(self):
        self.__visited = True

    def get_index(self):
        return self.__index
    
    def set_index(self, index):
        self.__index = index