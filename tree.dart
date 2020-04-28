import 'dart:html';

import 'node.dart';

class Tree {
  Node root;
  static Node NIL;

  Tree() {
    NIL = new Node();
    NIL.color = Color.BLACK;
  }

  void insert (int key) {
    Node z = new Node();
    z.key = key;

    Node y = NIL;
    Node x = this.root;

    while(x != NIL) {
      y = x;
      if(z.key < x.key)
        x = x.left;
      else
        x = x.right;
    }

    z.parent = y;
    if(y == NIL)
      this.root = z;
    else if(z.key < y.key)
      y.left = z;
    else
      y.right = z;

    z.left = NIL;
    z.right = NIL;
    z.color = Color.RED;

    insertFixUp(z);
  }

  void insertFixUp(Node z) {
    while (z.parent.color == Color.RED) {
      if (z.parent == z.parent.parent.left) {
        Node y = z.parent.parent.right;
        if(y.color == Color.RED) {
          z.parent.color = Color.BLACK;
          y.color = Color.BLACK;
          z.parent.parent.color = Color.RED;
          z = z.parent.parent;
        } else if(z == z.parent.right) {
          z = z.parent;
          _leftRotate(z);
        } else {
          z.parent.color = Color.BLACK;
          z.parent.parent.color = Color.RED;
          _rightRotate(z);
        }
      }
    }

    this.root.color = Color.BLACK;
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

  void _rightRotate(Node x) {
    
  }
}


void main () {
  Tree tree = new Tree();
}