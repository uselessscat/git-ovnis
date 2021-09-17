from typing import List, Union

import pyglet

from go.tree import Tree, Node


template = pyglet.gl.Config(sample_buffers=1, samples=16)
window = pyglet.window.Window(
    config=template,
    resizable=True
)


@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')


def draw_tree(tree: Tree, starting_x, starting_y):
    tree.data = pyglet.shapes.Circle(
        x=starting_x, y=starting_y, radius=10, color=(50, 225, 30)
    )

    queue: List[Union[Tree, Node]] = [tree]

    while len(queue) != 0:
        for node in queue:
            if isinstance(node, Tree):
                print(node.data.x)

            if node.data is None:
                node.data = pyglet.shapes.Circle(
                    x=100, y=150, radius=10, color=(50, 225, 30)
                ).draw()

        new = []
        for e in queue:
            new.extend(e.children)

        queue = new


t = Tree('root')
node_list = [t] + [Node(f'{i}') for i in range(21)]
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

circle = pyglet.shapes.Circle(
    x=100, y=150, radius=100, color=(50, 225, 30)
)
square = pyglet.shapes.Rectangle(
    x=200, y=200, width=200,
    height=200, color=(55, 55, 255)
)


@window.event
def on_draw():
    global t
    window.clear()

    draw_tree(t, 500, 500)


pyglet.app.run()
