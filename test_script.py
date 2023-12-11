from interpreterv4 import Interpreter


def notmain():
    i = Interpreter(trace_output=False)

    prog = """
    func main() {
        p = @;
        p.x = 10;

        c = @;
        c.proto = p;

        print(c.x);
        c.proto = nil;
        print(c.x);
    }
    """

    i.run(prog)


def main():
    i = Interpreter(trace_output=False)

    prog = """
    func main() {
        a = @;
        a.name = "Greg";
        a.say_name = lambda() { print(this.name); };
        a.say_hi = lambda() { print("hi"); };

        child = @;
        child.proto = a;
        child.name = "Billy";
        child.say_hi();
        child.say_name();
        a.say_name();
    }
    """

    i.run(prog)

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

    func main() {
        a = foo;
        a();
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
        a.name = "Greg";
        a.say_name = lambda() { print(this.name); };
    }
    """

    i.run(prog)

    prog = """
    func main() {
        a = @;
        a.name = "Greg";
        a.say_name = lambda() { print(this.name); };
        a.say_hi = lambda() { print("hi"); };

        a.say_hi();
    }
    """

    i.run(prog)

    prog = """
        func main() {
            c = @;
            /* d captures object c by object reference */ 
            d = lambda() { c.x = 5; };

            d();  
            print("I should print 5:");
            print(c.x);  /* prints 5, since closure modified original object */
        }
    """

    i.run(prog)

    prog = """
        func main() {
            c = lambda() { print(1); };

            /* d captures closure c by reference */
            d = lambda() { c = lambda() { print(2); }; };

            d();
            print("I should print 2:");
            c();  /* prints 2, since c was captured by reference by d */
        }
    """

    i.run(prog)

    prog = """
    func main() {
        a = @;
        a.name = "Greg";
        a.say_name = lambda() { print(this.name); };
        a.say_hi = lambda() { print("hi"); };

        a.say_name();
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

    # i.run(badprog)

    # badprog = """
    #     func main() {
    #         c = @;
    #         c.x = 5;

    #         /* d captures object c by object reference */
    #         d = lambda() {
    #         c = @;  /* changes original c variable, pointing it at a new obj */
    #         c.y = 10; /* adds field y to updated object */
    #         };

    #         d();
    #         print(c.y); /* prints 10 */
    #         print(c.x); /* NAME_ERROR since our original object is gone! */
    #     }
    # """

    # i.run(badprog)


if __name__ == "__main__":
    # main()
    notmain()
