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


def get_start_coord(node, radius):
    inc_coef = 1.2
    if node.numb in node.adj_vertices.keys():
        inc_coef = 0.2
    if node.x == 0:
        x = 0.0
        if node.y <= 0:
            y = float(node.y - inc_coef)
            direct = "below"
        else:
            y = float(node.y + inc_coef)
            direct = "above"
    else:
        x = (float)((inc_coef + radius) * node.x) / math.sqrt(node.x * node.x + node.y * node.y)
        y = (float)(x) * (node.y / node.x)
        if node.x > 0:
            direct = "right"
        else:
            direct = "left"

    if node.numb in node.adj_vertices.keys():
        delta = 1
        if x <= 0 and y < 0:
            x -= delta
            y -= delta
        elif x > 0 >= y:
            x += delta
            y -= delta
        elif x < 0 <= y:
            y += delta
            x -= delta
        else:
            y += delta
            x += delta
    return x, y, direct


def draw_start_node(node, radius):
    start_x, start_y, napr = get_start_coord(node, radius)
    node_format = "\\node (start) at (" + str(start_x) + "," + str(start_y) \
                  + "){};\n"
    node_format += "\\draw[->, -latex] (start) --node[inner sep=0pt, swap] {}(" + node.numb + ");\n"
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
    temp_node = None
    for node in nodes.keys():
        temp_node = nodes[node]
        if node not in not_these_nodes and len(temp_node.all_adj_vertices) >= max_adj_count:
            max_adj_count = len(temp_node.all_adj_vertices)
            max_node = temp_node
    if max_node is None:
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


def do_one_iteration(temp_node, radius, curr_angle, center):
    temp_y = radius * round(math.sin(math.radians(curr_angle)), 2) + center.y
    temp_x = (-1) * round(radius * math.cos(math.radians(curr_angle)), 2) + center.x
    temp_node.set_coordinates(temp_x, temp_y)
    return add_inform_node(temp_node)


def get_not_using_nodes(nodes_name, not_these):
    i = 0
    for node in nodes_name:
        if node not in not_these:
            i += 1
    return i


def add_adj_nodes(curr_angle, all_nodes, about_node):
    adj_nodes_list = about_node.all_adj_vertices
    # delta_angle = 360.0 / (len(adj_nodes_list) + 1)
    delta_angle = 360.0 / len(adj_nodes_list)
    radius = 2.5
    # radius = len(all_nodes)
    nodes_format = ""

    adj_nodes_count = len(adj_nodes_list)
    i = 0
    not_these = []
    while i < adj_nodes_count:
        max_node = get_max_node(all_nodes, not_these)
        if max_node is None:
            print('Nodes ended')
            return

        not_these.append(max_node.numb)
        if len(max_node.all_adj_vertices) == 0:
            nodes_format += do_one_iteration(max_node, radius, curr_angle, about_node)
            if max_node.is_start_node:
                nodes_format += draw_start_node(max_node, radius)
            curr_angle += delta_angle
        for j in range(len(max_node.all_adj_vertices)):
            if j == len(max_node.all_adj_vertices) // 2:
                nodes_format += do_one_iteration(max_node, radius, curr_angle, about_node)
                if max_node.is_start_node:
                    nodes_format += draw_start_node(max_node, radius)
                curr_angle += delta_angle
            temp_node = all_nodes[max_node.all_adj_vertices[j]]
            if temp_node.numb not in not_these:
                nodes_format += do_one_iteration(temp_node, radius, curr_angle, about_node)
                if temp_node.is_start_node:
                    nodes_format += draw_start_node(temp_node, radius)
                curr_angle += delta_angle
                not_these.append(temp_node.numb)
                i += 1
        i += 1
    return nodes_format


def draw_nodes(nodes):
    centre = Node("centre")
    centre.set_coordinates(0, 0)
    for node in nodes:
        centre.all_adj_vertices.append(node)

    curr_angle = 0
    nodes_format = add_adj_nodes(curr_angle, nodes, centre)

    return nodes_format


def draw_loop(name_node, temp_char, nodes):
    x = nodes[name_node].x
    y = nodes[name_node].y
    if math.fabs(x) == 0:
        if y >= 0:
            direction = "above"
        else:
            direction = "below"
    elif x > 0:
        direction = "right"
    else:
        direction = "left"

    return "\\draw[->, -latex][loop " + direction + "] (" + name_node + ") to node[inner sep=0.2pt]{" + chose_name(
        temp_char) + "} (" + name_node + ");\n"


def add_edge_inf(node_from, node_to, letter):
    node_name_from = node_from.numb
    node_name_to = node_to.numb
    # if node_name_from in node_to.adj_vertices.keys() and node_name_to in node_from.adj_vertices.keys():
    if math.fabs(node_from.x - node_to.x) < 0.001:
        print(node_from.numb + " " + node_to.numb)
        direction = "right"
        if node_from.y > node_to.y:
            direction = "left"
        return "\draw [->,-latex] (" + node_name_from + \
               ") to[bend left=15, " + direction + "] node[inner sep=1.3pt] {" + letter + "} (" + node_name_to + ");\n"
    if node_from.x < node_to.x and (node_to.y > 0 or node_from.y > 0):
        size = "15"
    else:
        size = "-15"
    direction = 'below'
    if node_name_from in node_to.adj_vertices.keys() and node_name_to in node_from.adj_vertices.keys():
        direction = "above"
        size = "15"
    return "\draw [->,-latex] (" + node_name_from + \
           ") to[bend left=" + size + ", " + direction + "] node[inner sep=2.5pt] {" + letter + "} (" + node_name_to + ");\n"
    # else:
    #     return "\\draw[->, -latex] (" + node_from.numb + ") --node[inner sep=0.2pt,swap]{" + letter + "} (" +\
    #                node_to.numb + ");\n"


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
