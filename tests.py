import unittest
import Main


def move_data(input, output_filename):
    with open("in.txt", "w") as f:
        f.write(input)
    Main.main_f()
    with open("out.tex", 'r') as f:
        output = f.read()
    with open(output_filename, "w") as f:
        f.write(output)


class Tests(unittest.TestCase):
    def test1(self):
        input = "4\n" \
                "0 1 a 2 b 0 a\n" \
                "1 0 b 3 a 1 b\n" \
                "2 2 n\n" \
                "3 3 f\n" \
                "0 1 2 3\n" \
                "0 1 2 3"
        move_data(input, "tests\out1.tex")

    def test2(self):
        input = "4\n" \
                "0 1 a 2 b 0 a\n" \
                "1 0 b 3 a 1 b\n" \
                "2 2 n 3 b\n" \
                "3 3 f\n" \
                "0\n" \
                "1 3"
        move_data(input, "tests\out2.tex")

    def test3(self):
        input = "10\n" \
                "0\n" \
                "1\n" \
                "2\n" \
                "3\n" \
                "4\n" \
                "5\n" \
                "6\n" \
                "7\n" \
                "8\n" \
                "9\n" \
                "0 4 6 7 8 9\n" \
                "0 1 2 3 4 5 6 7"
        move_data(input, "tests\out3.tex")

    def test4(self):
        input = "2\n" \
                "0 1 a 0 x\n" \
                "1 0 b 1 v\n" \
                "0\n" \
                "1"
        move_data(input, "tests\out4.tex")

    def test5(self):
        input = "5\n" \
                "0 0 p 1 a 2 b 3 b 4 g\n" \
                "1 0 p 1 a 2 b 3 b 4 g\n" \
                "2 0 p 1 a 2 b 3 b 4 g\n" \
                "3 0 p 1 a 2 b 3 b 4 g\n" \
                "4 0 p 1 a 2 b 3 b 4 g\n" \
                "0\n" \
                "3"
        move_data(input, "tests\out5.tex")

    def test6(self):
        input = "4\n" \
                "0 0 p 1 a 2 b 3 b\n" \
                "1 0 p 1 a 2 b 3 b\n" \
                "2 0 p 1 a 2 b 3 b\n" \
                "3 0 p 1 a 2 b 3 b\n" \
                "0\n" \
                "3"
        move_data(input, "tests\out6.tex")

    def test7(self):
        input = "6\n" \
                "0 0 a 1 b 2 b 3 m 4 m 5 j\n" \
                "1\n" \
                "2\n" \
                "3\n" \
                "4\n" \
                "5\n" \
                "0\n" \
                "0"
        move_data(input, "tests\out7.tex")

    def test8(self):
        input = "6\n" \
                "0 0 a 1 b 2 b 3 m 4 m 5 j\n" \
                "1\n" \
                "2\n" \
                "3\n" \
                "4\n" \
                "5 0 a 1 b 2 b 3 m 4 m 5 j\n" \
                "0\n" \
                "0"
        move_data(input, "tests\out8.tex")

    def test9(self):
        input = "8\n" \
                "0 0 a 1 b 2 c 3 d\n" \
                "1 1 v\n" \
                "2 2 n 3 c\n" \
                "3 3 m 7 b\n" \
                "4 4 a 5 b 6 c 7 d\n" \
                "5 5 h\n" \
                "6 6 k\n" \
                "7 7 l\n" \
                "0 1 2 3 4 5 6 7\n" \
                "0 1 2 3 4 5 6 7"
        move_data(input, "tests\out9.tex")


if __name__ == "__main__":
    unittest.main()