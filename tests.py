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
    def test13(self):
        input = "6\n" \
                "1 2 a 3 c 4 s\n" \
                "2 3 a 5 n\n" \
                "3 6 d\n" \
                "4 5 t 6 y\n" \
                "5 6 a\n" \
                "6\n" \
                "1\n" \
                "1"
        move_data(input, "tests\out13.tex")

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
                "0 0 a 1 b 2 c\n" \
                "1 1 v 3 e\n" \
                "2 2 n 3 c\n" \
                "3 3 m 7 b\n" \
                "4 4 a 6 c 7 d\n" \
                "5 5 h 7 t\n" \
                "6 6 k 5 y\n" \
                "7 7 l\n" \
                "0 1 2 3 4 5 6 7\n" \
                "0 1 2 3 4 5 6 7"
        move_data(input, "tests\out9.tex")

    # def test10(self):
    #     input = "8\n" \
    #             "0 1 a 2 a\n" \
    #             "1 3 b\n" \
    #             "2 3 n\n" \
    #             "3 4 \n" \
    #             "4 5 h 6 j\n" \
    #             "5 7 \n" \
    #             "6 7 j\n" \
    #             "7\n" \
    #             "0\n" \
    #             "7"
    #     move_data(input, 'tests\out10.tex')

    def test11(self):
        input = "7\n" \
                "0 1 a 2 b 3 c\n" \
                "1 2 a\n" \
                "2 3 v\n" \
                "3 4 a\n" \
                "4 5 a 6 b\n" \
                "5 6 s\n" \
                "6\n" \
                "0\n" \
                "1"
        move_data(input, "tests\out11.tex")

    def test12(self):
        input = "9\n" \
                "1 2 a 3 c 5 s\n" \
                "2 3 a 4 n\n" \
                "3 6 d\n" \
                "4 5 t 6 y 9 e\n" \
                "5 6 a 7 n\n" \
                "6 8 a\n" \
                "7 8 u 9 o 1 a\n" \
                "8 9 f 2 a\n" \
                "9 3 d\n" \
                "1\n" \
                "1"
        move_data(input, "tests\out12.tex")



if __name__ == "__main__":
    unittest.main()