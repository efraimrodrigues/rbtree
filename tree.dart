import 'node.dart';

class Tree {
  Node root;
  static Node NIL;

  Tree() {
    NIL = new Node();
    NIL.color = Color.BLACK;
  }

  void insert (int value) {

  }

  void delete (int value) {
    
  }

  void _leftRotate(Node x) {
    Node y = x.right;
    x.right = y.left;

    if(y.left != NIL)
      y.left.parent = x;

    y.parent = x.parent; 

    if(x.parent == NIL)
      this.root = y;
    else if(x == x.parent.left)
      x.parent.left = y;
    else
      x.parent.right = y;

    y.left = x;
    x.parent = y;
  }
}


void main () {
  Tree tree = new Tree();
}