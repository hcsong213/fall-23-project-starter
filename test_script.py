from interpreterv2 import Interpreter


def notmain():
    i = Interpreter(trace_output=True)

    prog = """
    func main() {
        b = 5;
        f = lambda(a) { print(a*b); }; /* captures b = 5 by making a copy */
        b = 7;                         /* has no impact on captured b */

        f(3);     /* prints 15 */
        print(b); /* prints 7 */
    }
    """

    i.run(prog)


def main():
    i = Interpreter(trace_output=False)

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
    #     print("input: ", i);
    #     print("The input + 5 is: ", x);
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

    ##################################################
    ## function call test
    ##################################################

    prog = """
    func foo() {
        /* a, b and c are in scope here! */
        print("foo: ", a, " ", b, " ", c);   /* prints foo: 10 20 30 */
        b = b + 1;                           /* b is set to 21 */
    }

    func bar() {
        /* a, and b are in scope here! */
        print("bar: ", a, " ", b);   /* prints bar: 10 20 */
        c = 30;
        foo();
    } 

    func main() {
        a = 10;
        b = 20;
        bar();
        print("main: ", a, " ", b);  /* prints bar: 10 21 */
    }
    """

    i.run(prog)

    prog = """
    func main() {
        a = 5;
        foo();
        foo(10);
        foo(20,30);
    }

    func foo() {
        print(a);
    }

    func foo(a) {
        print(a);
    }

    func foo(a,b) {
        print(a," ",b);
    }
    """

    i.run(prog)

    prog = """
    func main() {
        print(fact(5));
    }

    func fact(n) {
        if (n <= 1) { return 1; }
        return n * fact(n-1);
    }
    """

    i.run(prog)

    prog = """
    func main() {
        print(fib(5));
    }

    func fib(n) {
        if (n < 3) {
            return 1;
        } else {
            return fib(n-2) + fib(n-1);
        }
    }
    """

    i.run(prog)

    prog = """
    func main() {
        print("foo");
    }

    func foo() {
        print("foo");
    }

    func bar() {
        print("bar");
    }

    func overload() {
        print("overload");
    }

    func overload(n) {
        print(n);
    }
    """

    i.run(prog)

    prog = """
    func main() {
        a = foo;
        a();
    }

    func foo() {
        print("foo");
    }

    func bar() {
        print("bar");
    }

    func overload() {
        print("overload");
    }

    func overload(n) {
        print(n);
    }
    """

    i.run(prog)

    prog = """
    func main() {
        a = -5;
        if (true == a) { print("This will print!"); }

        if (false || 6) { print("This prints!"); }

        x = true + 6; /* x is 7 */
        y = false * 10; /* y is zero */ 
        z = true + true; /* z is 2 */
        print(x, y, z);
    }
    """

    i.run(prog)

    prog = """
    func main() {
        a = @;
        a.name = "Greg"
        a.say_name = lambda() { print(this.name); }
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

    # badprog = """
    # func foo() {
    #     /* a, b and c are in scope here! */
    #     print("foo: ", a, " ", b, " ", c);   /* prints foo: 10 20 30 */
    #     b = b + 1;                           /* b is set to 21 */
    # }

    # func bar() {
    #     /* a, and b are in scope here! */
    #     print("bar: ", a, " ", b);   /* prints bar: 10 20 */
    #     c = 30;
    #     foo();
    # }

    # func main() {
    #     a = 10;
    #     b = 20;
    #     bar(a, b);
    #     print("main: ", a, " ", b);  /* prints bar: 10 21 */
    # }
    # """

    # i.run(badprog)

    # badprog = """
    # func main() {
    #     print(!false);
    #     print(!2);
    # }
    # """

    # i.run(badprog)


if __name__ == "__main__":
    main()
    # notmain()
