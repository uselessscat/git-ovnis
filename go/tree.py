from typing import Any, Generator, Optional, List, Union


class Node:
    def __init__(
        self,
        name: Optional[str] = None,
        vertex_name: Optional[str] = None,
        data: Optional[Any] = None,
        parent: Optional['Node'] = None,
        children: Optional[List['Node']] = None
    ):
        self.name = name
        self.vertex_name = vertex_name

        self.data = data
        self.parent = None
        self.children = children if children is not None else []

    def add(self, node: 'Node'):
        node.parent
        self.children.append(node)

    def __str__(self):
        return f'<Node name:{self.name}>'

    def __repr__(self):
        return self.__str__()


class Tree(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def breadth_first_traversal(
        cls,
        tree: 'Tree'
    ) -> Generator[Union['Tree', Node], None, None]:
        queue: List[Union[Tree, Node]] = [tree]

        while len(queue) != 0:
            yield from queue

            new = []
            for e in queue:
                new.extend(e.children)

            queue = new
