import sys

import Creator_tex_file as ctf

nodes = {}


def add_node(node_name):
    """
    создает COUNT вершин и добавляет в глобальный список вершин
    :param count: число вершин
    :return: None
    """
    global nodes
    if node_name not in nodes.keys():
        nodes[node_name] = ctf.Node(node_name)


def read_data():
    """
    читает из файла in.txt данные:
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
    global nodes
    with open("in.txt", "r") as f:
        nodes_count = int(f.readline())
        for i in range(nodes_count):
            temp_file_line = f.readline().strip().split()
            if len(temp_file_line) % 2 == 0:
                print('Incorrect data in file "in.txt"\n'
                      'in line {0}'.format(str(i + 1)))
                sys.exit(1)
            temp_node = temp_file_line[0]
            add_node(temp_node)
            temp_file_line = temp_file_line[1:]
            for j in range(len(temp_file_line) // 2):
                nodes[temp_node].add_adj_node(temp_file_line[2*j], temp_file_line[2*j + 1])
        start_nodes = f.readline().strip().split(" ")
        for node in start_nodes:
            nodes[node].set_start_node()
        end_nodes = f.readline().strip().split()
        for j in range(len(end_nodes)):
            nodes[end_nodes[j]].set_finish_node()


if __name__ == "__main__":
    read_data()
    ctf.create_tex_file(nodes)