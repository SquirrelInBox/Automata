# как закрыть окно после сохранения
import sys
import GraphicForm

import Creator_tex_file as ctf


OUTPUT_FILE = ""


def add_node(node_name, nodes):
    """
    создает COUNT вершин и добавляет в глобальный список вершин
    :param count: число вершин
    :return: None
    """
    if node_name not in nodes.keys():
        nodes[node_name] = ctf.Node(node_name)


def read_data():
    """
    читает из файла in.txt данные:
        куда писать
        число вершин
        текущая_вершина вершина буква вершина буква ... вершина буква
        ...
        текущая_вершина вершина буква вершина буква ... вершина буква
        стартовая вершина
        конечные вершины
    в первой строке введено число вершин в автомате
    в следующих N строках указаны текущая вершина, пары вершина - буква, по которой можно перейти в эту вершину
    :return: None
    """
    # global nodes_count
    nodes = {}
    with open("in.txt", "r") as f:
        global OUTPUT_FILE
        OUTPUT_FILE = f.readline().strip()
        if OUTPUT_FILE == "":
            OUTPUT_FILE = "out.tex"
        nodes_count = int(f.readline())
        for i in range(nodes_count):
            temp_file_line = f.readline().strip().split()
            if len(temp_file_line) % 2 == 0:
                print('Incorrect data in file "in.txt"\n'
                      'in line {0}'.format(str(i + 1)))
                sys.exit(1)
            temp_node = temp_file_line[0]
            add_node(temp_node, nodes)
            temp_file_line = temp_file_line[1:]
            for j in range(len(temp_file_line) // 2):
                nodes[temp_node].add_adj_node(temp_file_line[2*j], temp_file_line[2*j + 1])
        start_nodes = f.readline().strip().split(" ")

        for node in start_nodes:
            if len(node) > 0:
                nodes[node].set_start_node()
        end_nodes = f.readline().strip().split()
        for j in range(len(end_nodes)):
            if len(end_nodes[j]) > 0:
                nodes[end_nodes[j]].set_finish_node()
    if len(nodes) != 0:
        for node_name in nodes.keys():
            node = nodes[node_name]
            for temp_node in node.adj_vertices.keys():
                if temp_node not in node.all_adj_vertices and temp_node != node.numb:
                    node.all_adj_vertices.extend(temp_node)
            for temp_node_name in node.adj_vertices.keys():
                temp_node = nodes[temp_node_name]
                if node_name not in temp_node.all_adj_vertices and temp_node_name != node.numb:
                    temp_node.all_adj_vertices.append(node_name)
    return nodes


def main_f():
    GraphicForm.write_from_forms()
    print("end")
    nodes = read_data()
    ctf.create_tex_file(nodes, OUTPUT_FILE)


if __name__ == "__main__":
    main_f()