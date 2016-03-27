import math


class Node:
    def __init__(self, node_numb):
        """
        инициализация вершины
        :param node_numb: номер создаваемой вершины
        :return:
        """
        self.numb = node_numb
        self.x = 0
        self.y = 0
        self.adjVertices = {}
        self.is_start_node = False
        self.is_finish_node = False

    def set_start_node(self):
        self.is_start_node = True

    def set_finish_node(self):
        self.is_finish_node = True

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def add_adj_node(self, other_node_name, char):
        """
        добавляет новую смежную вершину
        :param other_node: номер вершины, в которую можем перейти по CHAR
        :param char: буква, по которой осуществляется переход
        :return:
        """
        if other_node_name in self.adjVertices.keys():
            self.adjVertices[other_node_name].append(char)
        else:
            self.adjVertices[other_node_name] = [char]


def get_start_coord(x_coord, y_coord, radius):
    inc_coef = 1.2
    if x_coord == 0:
        if y_coord <= 0:
            return 0.0, float(y_coord - inc_coef), "below"
        else:
            return 0.0, float(y_coord + inc_coef), "above"
    x = (float)((inc_coef + radius) * x_coord) / math.sqrt(x_coord * x_coord + y_coord * y_coord)
    y = (float)(x) * (y_coord / x_coord)
    if x_coord > 0:
        return x, y, "right"
    return x, y, "left"


def draw_start_node(name_node, x_coord, y_coord, radius):
    start_x, start_y, napr = get_start_coord(x_coord, y_coord, radius)
    node_format = "\\node (start) at (" + str(start_x) + "," + str(start_y) \
                  + "){};\n"
    node_format += "\\draw[->, -latex] (start) --node[inner sep=0pt, swap] {}(" + name_node + ");\n"
    return node_format


def draw_finish_node(name_node, x_coord, y_coord):
    return "\\node [circle, accepting, draw] (" + name_node + ") at (" + str(x_coord) + "," + str(
        y_coord) + ") [] {" + chose_name(name_node) + "};\n"


def chose_name(name):
    if name == "\\varepsilon":
        return "$" + name + "$"
    else:
        return name


def draw_nodes(nodes):
    count_nodes = len(nodes)
    delta_angle = 360.0 / count_nodes
    curr_angle = 0
    nodes_format = ""
    radius = len(nodes) / 3
    for name_node in nodes.keys():
        temp_y = radius * round(math.sin(math.radians(curr_angle)), 2)
        temp_x = (-1) * round(radius * math.cos(math.radians(curr_angle)), 2)
        nodes[name_node].set_coordinates(temp_x, temp_y)
        if nodes[name_node].is_finish_node:
            nodes_format += draw_finish_node(name_node, temp_x, temp_y)
        else:
            nodes_format += "\\node[circle, draw] ({node}) at ({x},{y}) ".format(
                node=chose_name(name_node)
                , x=temp_x
                , y=temp_y
            ) + "{" + name_node + "};\n"
            print(str(temp_x) + " " + str(temp_y))
        if nodes[name_node].is_start_node:
            nodes_format += draw_start_node(name_node, temp_x, temp_y, radius)
        curr_angle += delta_angle
    return nodes_format


def draw_loop(name_node, temp_char, nodes):
    x = nodes[name_node].x
    y = nodes[name_node].y
    if y == 0:
        direction = "below"
    elif x == 0:
        if y >= 0:
            direction = "above"
        else:
            direction = "below"
    elif x > 0:
        direction = "right"
    else:
        direction = "left"

    return "\\draw[->, -latex][loop " + direction + "] (" + name_node + ") to node[inner sep=1pt]{" + chose_name(temp_char) + "} (" + name_node + ");\n"


def draw_edges(nodes):
    nodes_format = ""
    for name_node in nodes.keys():
        temp_adj_nodes = nodes[name_node].adjVertices
        for adj_node in temp_adj_nodes.keys():
            temp_char = ", ".join(temp_adj_nodes[adj_node])
            if name_node != adj_node:
                nodes_format += \
                    "\\draw[->, -latex] (" + name_node + ") --node[inner sep=1pt,swap]{" + chose_name(temp_char) + "} (" + adj_node + ");\n"
            else:
                nodes_format += draw_loop(name_node, temp_char, nodes)
    return nodes_format


def create_tex_file(nodes):
    with open('out.tex', 'w') as f:
        f.write(
            "\\documentclass[tikz]{standalone}\n"
            "\\usepackage{gastex}\n"
            "\\usetikzlibrary{automata}\n"
            "\\begin{document}\n"
            "   \\begin{tikzpicture}[auto]\n"
        )

        nodes_format = draw_nodes(nodes)
        f.write(nodes_format)
        nodes_format = draw_edges(nodes)
        f.write(nodes_format)

        f.write(
            "\\end{tikzpicture}\n"
            "\\end{document}"
        )
