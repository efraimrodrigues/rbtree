from node import node
from rb_tree import rb_tree

def draw(tree):
        import networkx as nx
        from networkx.drawing.nx_agraph import write_dot, graphviz_layout
        import warnings
        import matplotlib.pyplot as plt

        graph = nx.DiGraph()
        nx.set_node_attributes(graph, [], 'color')
        nx.set_node_attributes(graph, [], 'key')

        current_node = tree.get_root()
        tree.nil.set_visited()
        i = 1
        while current_node != tree.get_nil() and not current_node.get_visited():
                """
                        1. If both left and right nodes were visited and the current node wasn't, then current node is visited.
                        2. If left node isn't visited, then it becomes the current node and its subtrees will be addressed.
                        3. If left node is visited and current node isn't visited, then right node becomes the current node and its subtrees will be addressed.
                """
                if current_node.get_left().get_visited() and current_node.get_right().get_visited() and not current_node.get_visited():
                        graph.add_node(i)
                        graph.nodes[i]['color'] = current_node.get_color()
                        graph.nodes[i]['key'] = current_node.get_key()
                        
                        current_node.set_visited()
                        current_node.set_index(i)

                        if current_node.get_left().get_visited() and current_node.get_left() != tree.get_nil():
                                graph.add_edge(current_node.get_index(), current_node.get_left().get_index())
                        
                        if current_node.get_right().get_visited() and current_node.get_right() != tree.get_nil():
                                graph.add_edge(current_node.get_index(), current_node.get_right().get_index())

                        current_node = current_node.get_parent()
                        i = i+1
                elif not current_node.get_left().get_visited():
                        current_node = current_node.get_left()
                else:
                        current_node = current_node.get_right()

        val_map = {0: 'red', 1: 'black'}

        colors = [val_map.get(node_color) for node_color in nx.get_node_attributes(graph, 'color').values()]
        keys = nx.get_node_attributes(graph, 'key')

        pos = graphviz_layout(graph, prog='dot')
        plt.figure(2,figsize=(15,5)) 
        nx.draw(graph,pos,node_color=colors,with_labels=True, font_color='white', labels = nx.get_node_attributes(graph, 'key'))