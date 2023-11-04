from interpreterv1 import Interpreter


def main():
    i = Interpreter(trace_output=True)

    prog = """
    func main() {   
        x = 5 * 6;
        print("5 * 6 = ", x);
    }
    """

    i.run(prog)

    prog = """
    func main() {   
        x = 12 / 5;
        print("12 / 5 = ", x);
    }
    """

    i.run(prog)

    # prog1 = """
    # func main() {
    #     i = inputi("Please enter a number: ");
    #     x = 5 + i;
    #     y = 6 + x;
    #     print("The sum is: ", x);
    #     print("y = x + 6 is: ", y);
    # }
    # """

    # i.run(prog1)

    # prog1 = """
    # func main() {
    #     i = inputi("Please enter a number: ") + 10;
    #     x = 5 + i;
    #     y = 6 - x;
    #     print("The sum is input + 15: ", x);
    #     print("y is: ", y);
    # }
    # """

    # i.run(prog1)

    ##################################################
    ## Operations test
    ##################################################

    prog1 = """
    func main() {
        print("1 < 2 ", 1 < 2);
        print("1 > 2 ", 1 > 2);
        print("1 <= 2 ", 1 <= 2);
        print("1 >= 2 ", 1 >= 2);
        print("1 >= 1 ", 1 >= 1);
        print("'foo' == 'bar' ", "foo" == "bar");
        print("'foo' != 'bar' ", "foo" != "bar");
        print("'foo' == 'foo' ", "foo" == "foo");
        print("'foo' != 'foo' ", "foo" != "foo");
        print("'foo' + 'bar' ", "foo" + "bar");
        print("true && false ", true && false);
        print("true || false ", true || false);
        print("true == false ", true == false);
        print("true != false ", true != false);
        print("!false ", !false);
        f = false;
        print("!f ", !f);
        print("-6 ", -6);
        s = 6;
        print("-s ", -s);
    }
    """

    i.run(prog1)

    ##################################################
    ## if test
    ##################################################

    prog = """
    func main() {   
        if (true) {
            print("Correctly executed 'if' for true");
        }
        print("foobar");
    }
    """

    i.run(prog)

    prog = """
    func main() {   
        if (true) {
            print("Correctly executed 'if' for true");
        } else {
            print("bad");
        }
        print("foobar");
    }
    """

    i.run(prog)

    prog = """
    func main() {   
        if (false) {
            print("bad");
        } else {
            print("Correctly executed 'else' for false");
        }
        print("foobar");
    }
    """

    i.run(prog)

    prog = """
    func main() {   
        if (1 > 2) {
            print("bad");
        } else {
            print("Correctly executed 'else' for false");
        }
        print("foobar");
    }
    """

    i.run(prog)

    prog = """
    func main() {   
        x = 1 > 2;
        print(x);
        if (x) {
            print("bad");
        } else {
            print("Correctly executed 'else' for false");
        }
        print("foobar");
    }
    """

    i.run(prog)

    ##################################################
    ## while test
    ##################################################

    prog = """
    func main() {   
        x = 0;
        while(x < 10) {
            print("x = ", x);
            x = x + 1;
        }
    }
    """

    i.run(prog)

    # badprog = """
    # func main() {
    #     i = inputi("Please enter a number: ", "foo bar") + 10;
    # }
    # """

    # i.run(badprog)

    # badprog = """
    # func foobar() {
    #     x = 1 + 1;
    # }
    # """

    # i.run(badprog)

    # badprog = """
    # func main() {   
    #     x = "foo" + 1;
    # }
    # """

    # i.run(badprog)


    # badprog = """
    # func main() {   
    #     x = idk + 1;
    # }
    # """

    # i.run(badprog)

    # badprog = """
    # func main() {   
    #     if("not a boolean") {
    #         print("illegal");
    #     }
    # }
    # """

    # i.run(badprog)


if __name__ == "__main__":
    main()
