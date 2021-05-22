from go.tree import Node


class TestTree:
    def test_node_properties(self):
        n = Node()

        assert hasattr(n, 'name')
        assert hasattr(n, 'vertex_name')
