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
        self.adj_vertices = {}
        self.is_start_node = False
        self.is_finish_node = False
        self.all_adj_vertices = []

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
        if other_node_name in self.adj_vertices.keys():
            self.adj_vertices[other_node_name].append(char)
        else:
            self.adj_vertices[other_node_name] = [char]


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


def get_max_node(nodes, not_these_nodes):
    """
    ищет вершину с максимальной степенью
    :param nodes: dict [имя вершины: вершина]
    :param not_these_nodes: list [имя вершина]
    :return: Node вершина с максимальной степенью
    """
    max_node = None
    max_adj_count = 0
    for node in nodes.keys():
        temp_node = nodes[node]
        if node not in not_these_nodes and len(temp_node.all_adj_vertices) > max_adj_count:
            max_adj_count = len(temp_node.all_adj_vertices)
            max_node = temp_node
    return max_node


def add_inform_node(node):
    if node.is_finish_node:
        return draw_finish_node(node.numb, node.x, node.y)
    else:
        return "\\node[circle, draw] ({node}) at ({x},{y}) ".format(
            node=node.numb
            , x=node.x
            , y=node.y
        ) + "{" + node.numb + "};\n"


def add_adj_nodes(curr_angle, all_nodes, about_node, not_these_nodes):
    adj_nodes_list = about_node.all_adj_vertices
    delta_angle = 360.0 / (len(adj_nodes_list) + 1)
    radius = len(all_nodes) / 3
    nodes_format = ""

    for node_name in adj_nodes_list:
        if node_name not in not_these_nodes:
            temp_y = radius * round(math.sin(math.radians(curr_angle)), 2) + about_node.y
            temp_x = (-1) * round(radius * math.cos(math.radians(curr_angle)), 2) + about_node.x

            all_nodes[node_name].set_coordinates(temp_x, temp_y)

            nodes_format += add_inform_node(all_nodes[node_name])
            curr_angle += delta_angle
            if math.fabs(curr_angle - 180) < 0.001:
                curr_angle += delta_angle
            not_these_nodes.append(node_name)
    return nodes_format


def draw_nodes(nodes):
    nodes_format = ""
    not_these_nodes = []

    max_node = get_max_node(nodes, not_these_nodes)
    max_node.set_coordinates(-2, 0)
    not_these_nodes.append(max_node.numb)
    adj_nodes_count = len(max_node.all_adj_vertices)

    nodes_format += add_inform_node(max_node)

    next_node = get_max_node(nodes, not_these_nodes)
    next_node.set_coordinates(2, 0)
    name_next_node = next_node.numb
    not_these_nodes.append(next_node.numb)
    if name_next_node in max_node.all_adj_vertices:
        adj_nodes_count -= 1

    nodes_format += add_inform_node(next_node)

    curr_angle = 720.0 / (adj_nodes_count + 1)
    nodes_format += add_adj_nodes(curr_angle, nodes, max_node, not_these_nodes)

    curr_angle = 360.0 / (adj_nodes_count + 1)
    nodes_format += add_adj_nodes(curr_angle, nodes, next_node, not_these_nodes)

    return nodes_format


def draw_loop(name_node, temp_char, nodes):
    x = nodes[name_node].x
    y = nodes[name_node].y
    if math.fabs(x) == 2:
        if y >= 0:
            direction = "above"
        else:
            direction = "below"
    elif x > 0:
        direction = "right"
    else:
        direction = "left"

    return "\\draw[->, -latex][loop " + direction + "] (" + name_node + ") to node[inner sep=1pt]{" + chose_name(
        temp_char) + "} (" + name_node + ");\n"


def add_edge_inf(node_from, node_to, letter):
    node_name_from = node_from.numb
    node_name_to = node_to.numb
    if node_name_from in node_to.all_adj_vertices and node_name_to in node_from.all_adj_vertices and node_name_from > node_name_to:
        return "\draw [->,-latex] (" + node_name_from + \
               ") to[bend left] node[inner sep=1pt] {" + letter + "} (" + node_name_to + ");"
    else:
        return "\\draw[->, -latex] (" + node_name_from + ") --node[inner sep=1pt,swap]{" + letter + "} (" +\
               node_name_to + ");\n"


def draw_edges(nodes):
    nodes_format = ""
    for name_node in nodes.keys():
        temp_adj_nodes = nodes[name_node].adj_vertices
        for adj_node in temp_adj_nodes.keys():
            temp_char = ", ".join(temp_adj_nodes[adj_node])
            if name_node != adj_node:
                nodes_format += add_edge_inf(nodes[name_node], nodes[adj_node], chose_name(temp_char))
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
