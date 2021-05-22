class Node:
    def __init__(
        self,
        name: str = '',
        vertex_name: str = ''
    ):
        self.name = name
        self.vertex_name = vertex_name


class Tree(Node):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
