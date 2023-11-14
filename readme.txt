Known Errors:

There are some issues with scoping, particularly regarding parameters needing to shadow variables. For instance, in the code

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

We expect the n-1 in the second fib call to be unaffected by the n-2 in the first fib call. However, upon the second fib call, n is two lower than what it's supposed to be. This leads me to suspect that the first fib call somehow doesn't destroy its n before the second one runs. I know that shadowing isn't completely dysfunctional from other tests and investigations I did through the debugger.
