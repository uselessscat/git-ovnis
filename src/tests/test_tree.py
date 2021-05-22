from itertools import zip_longest

from go.tree import Node, Tree


class TestNode:
    def test_node_properties(self):
        n = Node()

        assert hasattr(n, 'name')
        assert hasattr(n, 'vertex_name')
        assert hasattr(n, 'children')
        assert hasattr(n, 'data')

        assert n.name is None
        assert n.vertex_name is None
        assert n.children == []
        assert n.data is None

    def test_node_repr(self):
        n = Node(
            'MyNode',
        )

        assert str(n) == '<Node name:MyNode>'
        assert repr(n) == '<Node name:MyNode>'

    def test_node_methods(self):
        n = Node()

        assert hasattr(n, 'add')

        assert callable(n.add)


class TestTree:
    def test_tree_bft(self):
        t = Tree('root')

        node_list = [t] + [Node(f'{i}') for i in range(21)]

        assert len(node_list) == 22

        node_list[0].add(node_list[1])
        node_list[0].add(node_list[2])
        node_list[0].add(node_list[3])
        node_list[1].add(node_list[4])
        node_list[1].add(node_list[5])
        node_list[2].add(node_list[6])
        node_list[2].add(node_list[7])
        node_list[3].add(node_list[8])
        node_list[4].add(node_list[9])
        node_list[4].add(node_list[10])
        node_list[6].add(node_list[11])
        node_list[6].add(node_list[12])
        node_list[8].add(node_list[13])
        node_list[8].add(node_list[14])
        node_list[9].add(node_list[15])
        node_list[9].add(node_list[16])
        node_list[12].add(node_list[17])
        node_list[12].add(node_list[18])
        node_list[14].add(node_list[19])
        node_list[19].add(node_list[20])
        node_list[19].add(node_list[21])

        for node_in_tree, node in zip_longest(
            Tree.breadth_first_traversal(t),
            node_list
        ):
            assert node_in_tree is node
