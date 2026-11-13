# Solutions — Chapter 6: Functions

> Back to the lesson: [Chapter 6 lesson](../lessons/06-functions.md)

---

## Part A — Quick check

**Ex 6.1** A **function** is a named group of statements that performs one coherent task; you run it by calling its name. Reasons: avoid repeating code; break a big problem into small pieces; make code easier to read, test and fix; let several people share the work.

**Ex 6.2**
1. **Function definition** — where the task is actually carried out (the code with its body).
2. **Function declaration / prototype** — tells the compiler that the function exists (name, parameter types, return type) before it's used.
3. **Function call** — the place where the function is used, giving it the arguments it needs.

**Ex 6.3** (1) the return **data type**; (2) the function **name**; (3) the **parameter** list; (4) the **statements** (body); (5) the **return value**.

**Ex 6.4** A function is `void` when it **does not return a value**. `(void)` in the parameter list means it **takes no arguments**.

**Ex 6.5** A **declaration** (prototype) only says *that* a function exists and what it looks like — no body, ends with `;`. A **definition** contains the **body**: the actual instructions.

**Ex 6.6** **Parameters** are the variables listed in the function's definition (the "slots"). **Arguments** are the actual values supplied in the call.

**Ex 6.7** C **copies** the values of the arguments into the parameters. The function works on the copies, so it **cannot change** the caller's variables.

**Ex 6.8** A **local** variable is declared inside a function and is known only there (it is destroyed when the function ends). A **global** variable is declared outside all functions and is known everywhere. Globals are risky because any function can change them, which makes bugs hard to trace and functions hard to reuse/test.

**Ex 6.9** `static` makes a local variable **keep its value between calls**: it is initialised **once** and lives for the whole program (though it is still only visible inside its function).

**Ex 6.10** **Recursion** is when a function calls itself to solve a smaller version of the problem. Essential parts: a **base case** (stops the recursion) and a **recursive case** (calls itself with a simpler input, moving towards the base case).

**Ex 6.11** It keeps calling itself until the computer runs out of stack memory — a **stack overflow** — and the program crashes.

**Ex 6.12** **No.** Functions must be defined separately (no nested functions in standard C).

**Ex 6.13** They are **never executed** — `return` ends the function immediately.

**Ex 6.14**
1. **False** — a function returns one value; the first `return` that executes ends the function.
2. **True.**
3. **False** — arguments match parameters by **position**, not by name.
4. **True.**
5. **False** — a static local is visible only inside its own function.
6. **True.**

---

## Part B — Predict the output

**Ex 6.15** `12` — `twice(3)` = 6, then `twice(6)` = 12.

**Ex 6.16** `A Hello B Hello C`

**Ex 6.17**
```output
inside: 15
outside: 5
```
`addTen` changed only its own copy of `a`.

**Ex 6.18** `7 7` — `|3 − 10|` and `|10 − 3|`; the function returns the absolute difference.

**Ex 6.19** `10 20 10` — in `main` the new local `x` (20) hides the global one, but `show()` was written outside and still sees the global `x` (10).

**Ex 6.20** `3` — `count` is global, so all three calls update the same variable.

**Ex 6.21** `1 2 3` — `n` is static: initialised once, remembered between calls.

**Ex 6.22**
```output
1 1 1
1 2 3
```

**Ex 6.23** `1 3 6 10 15` — a running total: 1, 1+2, 3+3, 6+4, 10+5.

**Ex 6.24** `10` — `f(4) = 4 + 3 + 2 + 1 + 0`.

**Ex 6.25** `3 2 1 1 2 3` — the first `printf` runs on the way *down* the recursion (3, 2, 1); the second runs on the way back *up* (1, 2, 3).

**Ex 6.26** `4 0 9 6` — the recursive call (the digits to the left) comes **before** the `printf`.

**Ex 6.27** `6` — this is **Euclid's algorithm**; `mystery(a, b)` computes the **greatest common divisor** of `a` and `b`. (48, 18) → (18, 12) → (12, 6) → (6, 0) → 6.

**Ex 6.28** `32 27` — 2⁵ and 3³.

**Ex 6.29** `8 25` — `fib(6)` is 8, and computing it takes 25 calls (it recomputes the same values again and again).

**Ex 6.30**
```output
check(3) no
check(9) yes
```
`&&`: `check(3)` is false, so `check(9)` is never called (short-circuit). `||`: `check(9)` is true, so `check(1)` is never called.

**Ex 6.31** `3.0 3.5` — in `half1`, `n / 2` is integer division (3) and is only then converted to `double`.

**Ex 6.32** `7 -7` — converting a `double` to `int` **truncates toward zero** (it doesn't round and doesn't go "down" for negatives).

**Ex 6.33** `25` — 3² + 4².

**Ex 6.34** `19` — the digit sum of 1729 (1 + 7 + 2 + 9).

**Ex 6.35** `2 1` — the inner `x` exists only inside its braces and hides the outer `x` there.

**Ex 6.36** `1 2 1 3 1 2 1` — each call prints its `n` between two copies of the pattern for `n − 1` (the "ruler" pattern).

---

## Part C — Find and fix the bugs

**Ex 6.37** `square` is called before the compiler has seen it. Add a **prototype** before `main` (or move the definition above `main`):
```c
#include <stdio.h>

int square(int n);                    /* prototype */

int main(void)
{
    printf("%d\n", square(4));
    return 0;
}

int square(int n)
{
    return n * n;
}
```
```output
16
```
(Some old compilers silently assume an undeclared function returns `int`, which only works by luck. Modern C does not allow it — never rely on it.)

**Ex 6.38** The function never `return`s anything, so the caller gets whatever happens to be in a register (garbage). The expression `n * n * n;` is computed and thrown away. Fix:
```c
int cube(int n)
{
    return n * n * n;
}
```

**Ex 6.39** `area` needs **two** arguments but was called with one (`too few arguments`). Call `area(5, 3)`.

**Ex 6.40** A `void` function cannot return a value (`return 5;` is an error), and its "result" can't be stored in `x`. Fix: declare it as `int getFive(void)`.

**Ex 6.41** The function swaps its own **copies** of `a` and `b`. The originals in `main` are never touched (pass by value), so the output is still `a = 10, b = 20`. The fix is to pass the **addresses** (pointers) — see Chapter 8:
```c
void swap(int *a, int *b) { int temp = *a; *a = *b; *b = temp; }
/* ... swap(&a, &b); */
```

**Ex 6.42** `level` is a **local** variable of `setup`; `main` cannot see it (`'level' undeclared`). Return it instead:
```c
int setup(void)
{
    int level = 5;
    return level;
}
/* in main:  int level = setup(); */
```

**Ex 6.43** There is no **base case**, so the function never stops calling itself. Add one:
```c
int factorial(int n)
{
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}
```

**Ex 6.44** The `;` after the prototype-looking line `int add(int a, int b);` ends the declaration, so the `{ ... }` that follows has no function header. In a **definition**, there is no semicolon after the header.

**Ex 6.45** A function cannot be defined inside another function. Move `double_it` outside (above) `main`.

**Ex 6.46** The prototype says `avg` returns `float`, the definition says `int`: the declarations **conflict**. Make them agree (and divide by `2.0` to get a decimal result):
```c
#include <stdio.h>

float avg(int a, int b);

int main(void)
{
    printf("%.1f\n", avg(7, 8));
    return 0;
}

float avg(int a, int b)
{
    return (a + b) / 2.0f;
}
```
```output
7.5
```

**Ex 6.47** `(a + b) / 2` is integer division (15 / 2 = 7). Use `2.0`:
```c
#include <stdio.h>

float average(int a, int b)
{
    return (a + b) / 2.0f;
}

int main(void)
{
    printf("%.1f\n", average(7, 8));
    return 0;
}
```
```output
7.5
```

**Ex 6.48** `count` is re-created and set to 0 on every call. Make it `static`:
```c
#include <stdio.h>

void visit(void)
{
    static int count = 0;
    count++;
    printf("Visitor %d\n", count);
}

int main(void)
{
    visit();
    visit();
    visit();
    return 0;
}
```
```output
Visitor 1
Visitor 2
Visitor 3
```

**Ex 6.49** The `for` loop returns after the **first** iteration: either `1` (if `n` is not divisible by 2) or `0`. A number is prime only if **no** divisor divides it, so you can't answer until the loop has finished. Return `0` when you *find* a divisor, and `1` only **after** the loop:
```c
#include <stdio.h>

int isPrime(int n)
{
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
    {
        if (n % d == 0)
            return 0;         /* found a divisor: not prime */
    }
    return 1;                 /* no divisor found: prime */
}

int main(void)
{
    printf("%d %d %d\n", isPrime(7), isPrime(9), isPrime(15));
    return 0;
}
```
```output
1 0 0
```
(The buggy version printed `1 1 1`.)

**Ex 6.50** `printStars` uses the **same global `i`** as the loop in `main`. After `printStars(2)` the shared `i` is 2; back in `main`, `i++` makes it 3 and the loop ends — after only one line. Give each loop its **own local** counter (which hides the global):
```c
#include <stdio.h>

int i;                                  /* still exists, but is no longer used by the loops */

void printStars(int n)
{
    for (int i = 0; i < n; i++)
        printf("*");
}

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printStars(2);
        printf("\n");
    }
    return 0;
}
```
```output
**
**
**
```
**Lesson:** this is exactly why globals are dangerous.

---

## Part D1 — Write the functions

**Ex 6.51**
```c
#include <stdio.h>

void greet(void)
{
    printf("==============\n");
    printf("  Akwaaba!\n");
    printf("==============\n");
}

int main(void)
{
    greet();
    greet();
    greet();
    return 0;
}
```
```output
==============
  Akwaaba!
==============
==============
  Akwaaba!
==============
==============
  Akwaaba!
==============
```

**Ex 6.52**
```c
#include <stdio.h>

void printLine(char c, int n)
{
    for (int i = 0; i < n; i++)
        putchar(c);
    putchar('\n');
}

int main(void)
{
    printLine('+', 9);
    printf("| KNUST |\n");
    printLine('+', 9);
    return 0;
}
```
```output
+++++++++
| KNUST |
+++++++++
```

**Ex 6.53**
<!--exact-->
```c
#include <stdio.h>

int square(int n) { return n * n; }
int cube(int n)   { return n * n * n; }

int main(void)
{
    printf("%3s %7s %6s\n", "n", "square", "cube");
    for (int n = 1; n <= 10; n++)
        printf("%3d %7d %6d\n", n, square(n), cube(n));
    return 0;
}
```
```output
  n  square   cube
  1       1      1
  2       4      8
  3       9     27
  4      16     64
  5      25    125
  6      36    216
  7      49    343
  8      64    512
  9      81    729
 10     100   1000
```

**Ex 6.54**
```c
#include <stdio.h>

int max2(int a, int b)
{
    return (a > b) ? a : b;
}

int max3(int a, int b, int c)
{
    return max2(max2(a, b), c);
}

int min3(int a, int b, int c)
{
    int m = a;
    if (b < m) m = b;
    if (c < m) m = c;
    return m;
}

int main(void)
{
    printf("max3(14, 9, 22) = %d\n", max3(14, 9, 22));
    printf("min3(14, 9, 22) = %d\n", min3(14, 9, 22));
    return 0;
}
```
```output
max3(14, 9, 22) = 22
min3(14, 9, 22) = 9
```

**Ex 6.55**
<!--in: 70 85 92-->
```c
#include <stdio.h>

double average3(double a, double b, double c)
{
    return (a + b + c) / 3;
}

int main(void)
{
    double m1, m2, m3;

    printf("Enter three marks: ");
    scanf("%lf %lf %lf", &m1, &m2, &m3);

    printf("Average = %.2f\n", average3(m1, m2, m3));
    return 0;
}
```
```output
Enter three marks: 70 85 92
Average = 82.33
```

**Ex 6.56**
```c
#include <stdio.h>

int isEven(int n)
{
    return n % 2 == 0;
}

int main(void)
{
    int count = 0;

    for (int i = 1; i <= 50; i++)
    {
        if (isEven(i))
        {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nCount: %d\n", count);
    return 0;
}
```
```output
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50
Count: 25
```

**Ex 6.57**
<!--in: 50-->
```c
#include <stdio.h>

int isPrime(int n)
{
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return 0;
    return 1;
}

int main(void)
{
    int limit, count = 0;

    printf("Primes up to: ");
    scanf("%d", &limit);

    for (int n = 2; n <= limit; n++)
    {
        if (isPrime(n))
        {
            printf("%d ", n);
            count++;
        }
    }
    printf("\nThere are %d primes up to %d\n", count, limit);
    return 0;
}
```
```output
Primes up to: 50
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
There are 15 primes up to 50
```

**Ex 6.58**
```c
#include <stdio.h>

long long factorial(int n)
{
    long long f = 1;
    for (int i = 2; i <= n; i++)
        f *= i;
    return f;
}

long long nCr(int n, int r)
{
    return factorial(n) / (factorial(r) * factorial(n - r));
}

int main(void)
{
    printf("5C2  = %lld\n", nCr(5, 2));
    printf("10C3 = %lld\n", nCr(10, 3));
    return 0;
}
```
```output
5C2  = 10
10C3 = 120
```

**Ex 6.59** For a negative exponent, compute `base^|exp|` and take the reciprocal.
```c
#include <stdio.h>

double power(double base, int exp)
{
    double result = 1;
    int n = (exp < 0) ? -exp : exp;

    for (int i = 0; i < n; i++)
        result *= base;

    return (exp < 0) ? 1 / result : result;
}

int main(void)
{
    printf("2 ^ 10 = %g\n", power(2, 10));
    printf("2 ^ -3 = %g\n", power(2, -3));
    printf("5 ^ 0  = %g\n", power(5, 0));
    return 0;
}
```
```output
2 ^ 10 = 1024
2 ^ -3 = 0.125
5 ^ 0  = 1
```

**Ex 6.60**
```c
#include <stdio.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int lcm(int a, int b)
{
    return a / gcd(a, b) * b;
}

int main(void)
{
    printf("gcd(48, 18) = %d, lcm(48, 18) = %d\n", gcd(48, 18), lcm(48, 18));
    printf("gcd(17, 5)  = %d, lcm(17, 5)  = %d\n", gcd(17, 5), lcm(17, 5));
    return 0;
}
```
```output
gcd(48, 18) = 6, lcm(48, 18) = 144
gcd(17, 5)  = 1, lcm(17, 5)  = 85
```

**Ex 6.61**
<!--exact-->
```c
#include <stdio.h>

double c2f(double c) { return c * 9 / 5 + 32; }
double f2c(double f) { return (f - 32) * 5 / 9; }

int main(void)
{
    printf("%6s %6s\n", "C", "F");
    for (int c = -10; c <= 40; c += 10)
        printf("%6d %6.1f\n", c, c2f(c));

    printf("98.6 F = %.1f C\n", f2c(98.6));
    return 0;
}
```
```output
     C      F
   -10   14.0
     0   32.0
    10   50.0
    20   68.0
    30   86.0
    40  104.0
98.6 F = 37.0 C
```

**Ex 6.62**
```c
#include <stdio.h>
#include <math.h>

double rectArea(double w, double h)
{
    return w * h;
}

double circleArea(double r)
{
    const double PI = 3.14159265358979;
    return PI * r * r;
}

double triangleArea(double a, double b, double c)
{
    double s = (a + b + c) / 2;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

int main(void)
{
    printf("Rectangle 5 x 3     : %.2f\n", rectArea(5, 3));
    printf("Circle r = 2        : %.2f\n", circleArea(2));
    printf("Triangle 3, 4, 5    : %.2f\n", triangleArea(3, 4, 5));
    return 0;
}
```
```output
Rectangle 5 x 3     : 15.00
Circle r = 2        : 12.57
Triangle 3, 4, 5    : 6.00
```

**Ex 6.63**
```c
#include <stdio.h>

int absVal(int n)
{
    return (n < 0) ? -n : n;
}

int sign(int n)
{
    if (n > 0) return 1;
    if (n < 0) return -1;
    return 0;
}

int main(void)
{
    printf("absVal(-7) = %d, absVal(5) = %d\n", absVal(-7), absVal(5));
    printf("sign(-9) = %d, sign(0) = %d, sign(4) = %d\n", sign(-9), sign(0), sign(4));
    return 0;
}
```
```output
absVal(-7) = 7, absVal(5) = 5
sign(-9) = -1, sign(0) = 0, sign(4) = 1
```

**Ex 6.64**
```c
#include <stdio.h>

int isLeap(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int daysInMonth(int month, int year)
{
    switch (month)
    {
        case 4: case 6: case 9: case 11:
            return 30;
        case 2:
            return isLeap(year) ? 29 : 28;
        default:
            return 31;
    }
}

int main(void)
{
    printf("Feb 2024 : %d days\n", daysInMonth(2, 2024));
    printf("Feb 2023 : %d days\n", daysInMonth(2, 2023));
    printf("Apr 2024 : %d days\n", daysInMonth(4, 2024));
    printf("Dec 2024 : %d days\n", daysInMonth(12, 2024));
    return 0;
}
```
```output
Feb 2024 : 29 days
Feb 2023 : 28 days
Apr 2024 : 30 days
Dec 2024 : 31 days
```

**Ex 6.65**
```c
#include <stdio.h>

int countDigits(int n)
{
    int count = 0;
    do
    {
        count++;
        n /= 10;
    }
    while (n > 0);
    return count;
}

int sumDigits(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int reverseNumber(int n)
{
    int rev = 0;
    while (n > 0)
    {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}

int isPalindrome(int n)
{
    return n == reverseNumber(n);
}

int main(void)
{
    int tests[2] = {12321, 1234};

    for (int i = 0; i < 2; i++)
    {
        int n = tests[i];
        printf("%d: digits=%d sum=%d reverse=%d palindrome=%d\n",
               n, countDigits(n), sumDigits(n), reverseNumber(n), isPalindrome(n));
    }
    return 0;
}
```
```output
12321: digits=5 sum=9 reverse=12321 palindrome=1
1234: digits=4 sum=10 reverse=4321 palindrome=0
```
(The little array `tests` is Chapter 7 — it just holds two numbers.)

**Ex 6.66**
```c
#include <stdio.h>

int isVowel(char c)
{
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
           c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
}

char toUpper(char c)
{
    if (c >= 'a' && c <= 'z')
        return c - 32;
    return c;
}

int isDigit(char c)
{
    return c >= '0' && c <= '9';
}

int main(void)
{
    printf("isVowel('e')=%d  isVowel('x')=%d\n", isVowel('e'), isVowel('x'));
    printf("toUpper('g')=%c  toUpper('G')=%c  toUpper('5')=%c\n", toUpper('g'), toUpper('G'), toUpper('5'));
    printf("isDigit('7')=%d  isDigit('a')=%d\n", isDigit('7'), isDigit('a'));
    return 0;
}
```
```output
isVowel('e')=1  isVowel('x')=0
toUpper('g')=G  toUpper('G')=G  toUpper('5')=5
isDigit('7')=1  isDigit('a')=0
```

**Ex 6.67**
```c
#include <stdio.h>

char gradeOf(int score)
{
    if (score < 0 || score > 100) return '?';
    if (score >= 80) return 'A';
    if (score >= 70) return 'B';
    if (score >= 60) return 'C';
    if (score >= 50) return 'D';
    return 'F';
}

int main(void)
{
    int scores[6] = {85, 72, 61, 55, 20, 105};

    for (int i = 0; i < 6; i++)
        printf("%d -> %c\n", scores[i], gradeOf(scores[i]));
    return 0;
}
```
```output
85 -> A
72 -> B
61 -> C
55 -> D
20 -> F
105 -> ?
```

**Ex 6.68** Both functions return the **interest earned**.
```c
#include <stdio.h>

double simpleInterest(double p, double r, int t)
{
    return p * r * t / 100;
}

double compoundInterest(double p, double r, int t)
{
    double amount = p;
    for (int year = 1; year <= t; year++)
        amount *= 1 + r / 100;
    return amount - p;
}

int main(void)
{
    printf("Simple interest   : %.2f\n", simpleInterest(5000, 10, 5));
    printf("Compound interest : %.2f\n", compoundInterest(5000, 10, 5));
    return 0;
}
```
```output
Simple interest   : 2500.00
Compound interest : 3052.55
```

**Ex 6.69**
```c
#include <stdio.h>

void printTriangle(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            printf("*");
        printf("\n");
    }
}

void printPyramid(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int s = 1; s <= n - i; s++)
            printf(" ");
        for (int j = 1; j <= 2 * i - 1; j++)
            printf("*");
        printf("\n");
    }
}

int main(void)
{
    printTriangle(4);
    printf("\n");
    printPyramid(4);
    return 0;
}
```
```output
*
**
***
****

   *
  ***
 *****
*******
```

**Ex 6.70**
```c
#include <stdio.h>

int isPerfect(int n)
{
    int sum = 0;
    for (int d = 1; d <= n / 2; d++)
        if (n % d == 0)
            sum += d;
    return n > 1 && sum == n;
}

int isArmstrong(int n)
{
    int digits = 0, temp = n, sum = 0;

    while (temp > 0) { digits++; temp /= 10; }      /* count the digits */

    temp = n;
    while (temp > 0)
    {
        int d = temp % 10, power = 1;
        for (int i = 0; i < digits; i++)
            power *= d;
        sum += power;
        temp /= 10;
    }
    return sum == n;
}

int main(void)
{
    printf("Perfect numbers up to 1000 : ");
    for (int n = 1; n <= 1000; n++)
        if (isPerfect(n))
            printf("%d ", n);

    printf("\nArmstrong numbers up to 999: ");
    for (int n = 1; n <= 999; n++)
        if (isArmstrong(n))
            printf("%d ", n);
    printf("\n");
    return 0;
}
```
```output
Perfect numbers up to 1000 : 6 28 496
Armstrong numbers up to 999: 1 2 3 4 5 6 7 8 9 153 370 371 407
```

**Ex 6.71**
<!--in: 1 12 5\n2 12 5\n3 12 5\n4 12 0\n4 12 5\n5-->
```c
#include <stdio.h>

double add(double a, double b)      { return a + b; }
double subtract(double a, double b) { return a - b; }
double multiply(double a, double b) { return a * b; }
double divide(double a, double b)   { return a / b; }

int main(void)
{
    int choice;
    double x, y;

    do
    {
        printf("\n1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        if (choice >= 1 && choice <= 4)
        {
            printf("Two numbers: ");
            scanf("%lf %lf", &x, &y);

            switch (choice)
            {
                case 1: printf("= %.2f\n", add(x, y)); break;
                case 2: printf("= %.2f\n", subtract(x, y)); break;
                case 3: printf("= %.2f\n", multiply(x, y)); break;
                case 4:
                    if (y == 0)
                        printf("Cannot divide by zero\n");
                    else
                        printf("= %.2f\n", divide(x, y));
                    break;
            }
        }
        else if (choice != 5)
            printf("Invalid choice\n");
    }
    while (choice != 5);

    printf("Goodbye!\n");
    return 0;
}
```
```output
1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 1
Two numbers: 12 5
= 17.00

1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 2
Two numbers: 12 5
= 7.00

1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 3
Two numbers: 12 5
= 60.00

1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 4
Two numbers: 12 0
Cannot divide by zero

1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 4
Two numbers: 12 5
= 2.40

1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit
Choose: 5
Goodbye!
```

**Ex 6.72**
```c
#include <stdio.h>

void tick(void)
{
    static int count = 0;
    count++;
    printf("tick #%d\n", count);
}

int main(void)
{
    for (int i = 0; i < 5; i++)
        tick();
    return 0;
}
```
```output
tick #1
tick #2
tick #3
tick #4
tick #5
```

**Ex 6.73**
```c
#include <stdio.h>

double transaction(double amount)
{
    static double balance = 0;

    if (balance + amount < 0)
    {
        printf("Refused: insufficient funds\n");
        return balance;
    }
    balance += amount;
    return balance;
}

int main(void)
{
    printf("Balance: %.2f\n", transaction(500));
    printf("Balance: %.2f\n", transaction(-200));
    printf("Balance: %.2f\n", transaction(-1000));
    printf("Balance: %.2f\n", transaction(50.5));
    return 0;
}
```
```output
Balance: 500.00
Balance: 300.00
Refused: insufficient funds
Balance: 300.00
Balance: 350.50
```

**Ex 6.74** The generator's *seed/state* is a static variable that survives between calls.
```c
#include <stdio.h>

unsigned int nextRandom(void)
{
    static unsigned int state = 42;
    state = (state * 1103515245u + 12345u) & 0x7fffffffu;
    return state;
}

int main(void)
{
    for (int i = 0; i < 5; i++)
        printf("%u ", nextRandom() % 100);
    printf("\n");
    return 0;
}
```
```output
27 64 53 6 35
```
Run it twice: it prints the **same five numbers every time** — "random" generators are really long, deterministic sequences. (`rand()` works the same way, which is why people seed it with the time.)

**Ex 6.75**
```c
#include <stdio.h>

int isTriangle(double a, double b, double c)
{
    return a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a;
}

void classify(double a, double b, double c)
{
    if (!isTriangle(a, b, c))
        printf("(%g, %g, %g): not a triangle\n", a, b, c);
    else if (a == b && b == c)
        printf("(%g, %g, %g): equilateral\n", a, b, c);
    else if (a == b || b == c || a == c)
        printf("(%g, %g, %g): isosceles\n", a, b, c);
    else
        printf("(%g, %g, %g): scalene\n", a, b, c);
}

int main(void)
{
    classify(3, 4, 5);
    classify(5, 5, 8);
    classify(4, 4, 4);
    classify(1, 2, 5);
    return 0;
}
```
```output
(3, 4, 5): scalene
(5, 5, 8): isosceles
(4, 4, 4): equilateral
(1, 2, 5): not a triangle
```

**Ex 6.76**
```c
#include <stdio.h>

int hours(int t)   { return t / 3600; }
int minutes(int t) { return (t % 3600) / 60; }
int seconds(int t) { return t % 60; }

int main(void)
{
    int total = 3725;

    printf("%d s = %d:%02d:%02d\n", total, hours(total), minutes(total), seconds(total));
    return 0;
}
```
```output
3725 s = 1:02:05
```

**Ex 6.77**
```c
#include <stdio.h>
#include <math.h>

double roundTo(double x, int places)
{
    double m = pow(10, places);
    return floor(x * m + 0.5) / m;
}

int main(void)
{
    printf("%g\n", roundTo(3.14159, 2));
    printf("%g\n", roundTo(2.5, 0));
    printf("%g\n", roundTo(1234.5678, 1));
    return 0;
}
```
```output
3.14
3
1234.6
```

**Ex 6.78**
```c
#include <stdio.h>

double f2c(double f) { return (f - 32) * 5 / 9; }
double c2k(double c) { return c + 273.15; }
double f2k(double f) { return c2k(f2c(f)); }       /* build on the other two */

int main(void)
{
    printf("98.6 F = %.2f K\n", f2k(98.6));
    return 0;
}
```
```output
98.6 F = 310.15 K
```

**Ex 6.79**
```c
#include <stdio.h>

int divisibleBy(int n, int d)
{
    return n % d == 0;
}

int main(void)
{
    int count = 0;

    for (int n = 1; n <= 1000; n++)
        if (divisibleBy(n, 3) && divisibleBy(n, 5))
            count++;

    printf("%d numbers\n", count);
    return 0;
}
```
```output
66 numbers
```
(They are the multiples of 15: 1000 ÷ 15 = 66.67 → 66.)

**Ex 6.80**
```c
#include <stdio.h>

int luhnValid(long long n)
{
    int sum = 0, position = 0;

    while (n > 0)
    {
        int digit = (int)(n % 10);
        if (position % 2 == 1)
        {
            digit *= 2;
            if (digit > 9)
                digit -= 9;
        }
        sum += digit;
        n /= 10;
        position++;
    }
    return sum % 10 == 0;
}

int main(void)
{
    printf("79927398713 -> %d\n", luhnValid(79927398713LL));
    printf("79927398710 -> %d\n", luhnValid(79927398710LL));
    return 0;
}
```
```output
79927398713 -> 1
79927398710 -> 0
```

---

## Part D2 — Recursion

For every recursive function, first write down the **base case**, then the **recursive case**, then check that every call moves *closer* to the base case.

**Ex 6.81**
<!--exact-->
```c
#include <stdio.h>

long long fact(int n)                 /* recursive */
{
    if (n <= 1)
        return 1;
    return n * fact(n - 1);
}

long long factIter(int n)             /* iterative */
{
    long long f = 1;
    for (int i = 2; i <= n; i++)
        f *= i;
    return f;
}

int main(void)
{
    printf("%3s %10s %10s\n", "n", "recursive", "iterative");
    for (int n = 0; n <= 10; n++)
        printf("%3d %10lld %10lld\n", n, fact(n), factIter(n));
    return 0;
}
```
```output
  n  recursive  iterative
  0          1          1
  1          1          1
  2          2          2
  3          6          6
  4         24         24
  5        120        120
  6        720        720
  7       5040       5040
  8      40320      40320
  9     362880     362880
 10    3628800    3628800
```

**Ex 6.82**
```c
#include <stdio.h>

int sumTo(int n)
{
    if (n == 0)
        return 0;                 /* base case */
    return n + sumTo(n - 1);
}

int main(void)
{
    printf("sumTo(10)  = %d   formula: %d\n", sumTo(10), 10 * 11 / 2);
    printf("sumTo(100) = %d   formula: %d\n", sumTo(100), 100 * 101 / 2);
    return 0;
}
```
```output
sumTo(10)  = 55   formula: 55
sumTo(100) = 5050   formula: 5050
```

**Ex 6.83**
```c
#include <stdio.h>

int calls = 0;

int fib(int n)
{
    calls++;
    if (n < 2)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main(void)
{
    for (int i = 0; i < 15; i++)
        printf("%d ", fib(i));
    printf("\n");

    calls = 0;
    fib(20);
    printf("fib(20) made %d calls\n", calls);
    return 0;
}
```
```output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
fib(20) made 21891 calls
```
21 891 calls to compute one number! (A loop needs just 20 additions.) That's why plain recursive Fibonacci is a *teaching* example, not a good algorithm.

**Ex 6.84** The idea of the fast version: `x¹⁰ = (x⁵)²`, `x⁵ = x · (x²)²`… — the number of multiplications drops from `n` to about `log₂ n`.
```c
#include <stdio.h>

long long power(long long x, int n)
{
    if (n == 0)
        return 1;
    return x * power(x, n - 1);
}

long long fastPower(long long x, int n)
{
    if (n == 0)
        return 1;
    long long half = fastPower(x, n / 2);
    if (n % 2 == 0)
        return half * half;
    return half * half * x;
}

int main(void)
{
    printf("power(2, 10)      = %lld\n", power(2, 10));
    printf("fastPower(3, 13)  = %lld\n", fastPower(3, 13));
    return 0;
}
```
```output
power(2, 10)      = 1024
fastPower(3, 13)  = 1594323
```

**Ex 6.85**
```c
#include <stdio.h>

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main(void)
{
    printf("gcd(48, 18)  = %d\n", gcd(48, 18));
    printf("gcd(17, 5)   = %d\n", gcd(17, 5));
    printf("gcd(100, 75) = %d\n", gcd(100, 75));
    return 0;
}
```
```output
gcd(48, 18)  = 6
gcd(17, 5)   = 1
gcd(100, 75) = 25
```

**Ex 6.86**
```c
#include <stdio.h>

int sumDigits(int n)
{
    if (n == 0)
        return 0;
    return n % 10 + sumDigits(n / 10);
}

int countDigits(int n)
{
    if (n < 10)
        return 1;
    return 1 + countDigits(n / 10);
}

int main(void)
{
    printf("sumDigits(4096)   = %d\n", sumDigits(4096));
    printf("countDigits(4096) = %d\n", countDigits(4096));
    return 0;
}
```
```output
sumDigits(4096)   = 19
countDigits(4096) = 4
```

**Ex 6.87** Print the **last** digit *first*, then recurse on the rest.
```c
#include <stdio.h>

void printReverse(int n)
{
    printf("%d", n % 10);
    if (n >= 10)
        printReverse(n / 10);
}

int main(void)
{
    printReverse(4096);
    printf("\n");
    return 0;
}
```
```output
6904
```

**Ex 6.88** `countdown` prints **before** recursing; `countUp` prints **after** recursing — the order is reversed.
```c
#include <stdio.h>

void countdown(int n)
{
    if (n == 0)
    {
        printf("Liftoff!\n");
        return;
    }
    printf("%d ", n);
    countdown(n - 1);
}

void countUp(int n)
{
    if (n == 0)
        return;
    countUp(n - 1);
    printf("%d ", n);
}

int main(void)
{
    countdown(5);
    countUp(5);
    printf("\n");
    return 0;
}
```
```output
5 4 3 2 1 Liftoff!
1 2 3 4 5
```

**Ex 6.89**
```c
#include <stdio.h>

void toBinary(int n)
{
    if (n > 1)
        toBinary(n / 2);          /* higher bits first */
    printf("%d", n % 2);
}

int main(void)
{
    toBinary(37);
    printf("\n");
    toBinary(0);
    printf("\n");
    return 0;
}
```
```output
100101
0
```

**Ex 6.90** The *accumulator* `acc` collects the reversed number as we go; when no digits are left it is the answer.
```c
#include <stdio.h>

int reverseHelper(int n, int acc)
{
    if (n == 0)
        return acc;
    return reverseHelper(n / 10, acc * 10 + n % 10);
}

int reverseNumber(int n)
{
    return reverseHelper(n, 0);
}

int main(void)
{
    printf("%d\n", reverseNumber(12345));
    return 0;
}
```
```output
54321
```

**Ex 6.91**
```c
#include <stdio.h>

int moves = 0;

void hanoi(int n, char from, char to, char via, int show)
{
    if (n == 0)
        return;
    hanoi(n - 1, from, via, to, show);
    moves++;
    if (show)
        printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n - 1, via, to, from, show);
}

int main(void)
{
    hanoi(3, 'A', 'C', 'B', 1);

    moves = 0;
    hanoi(10, 'A', 'C', 'B', 0);
    printf("Moves for 10 disks: %d\n", moves);
    return 0;
}
```
```output
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Moves for 10 disks: 1023
```
`2¹⁰ − 1 = 1023`. (With 64 disks it would take more than 500 billion years at one move a second!)

**Ex 6.92** `isEven` calls `isOdd` and vice-versa. The prototype of `isOdd` is needed because `isEven` uses it before it is defined.
```c
#include <stdio.h>

int isOdd(int n);                       /* prototype */

int isEven(int n)
{
    if (n == 0)
        return 1;
    return isOdd(n - 1);
}

int isOdd(int n)
{
    if (n == 0)
        return 0;
    return isEven(n - 1);
}

int main(void)
{
    printf("isEven(10) = %d\n", isEven(10));
    printf("isOdd(7)   = %d\n", isOdd(7));
    printf("isEven(7)  = %d\n", isEven(7));
    return 0;
}
```
```output
isEven(10) = 1
isOdd(7)   = 1
isEven(7)  = 0
```

**Ex 6.93**
```c
#include <stdio.h>

int multiply(int a, int b)             /* b >= 0 */
{
    if (b == 0)
        return 0;
    return a + multiply(a, b - 1);
}

int main(void)
{
    printf("6 x 7 = %d\n", multiply(6, 7));
    return 0;
}
```
```output
6 x 7 = 42
```

**Ex 6.94**
```c
#include <stdio.h>

double harmonic(int n)
{
    if (n == 1)
        return 1.0;
    return 1.0 / n + harmonic(n - 1);
}

int main(void)
{
    printf("harmonic(10) = %.6f\n", harmonic(10));
    return 0;
}
```
```output
harmonic(10) = 2.928968
```

**Ex 6.95**
```c
#include <stdio.h>

int sumDigits(int n)
{
    if (n == 0)
        return 0;
    return n % 10 + sumDigits(n / 10);
}

int digitalRoot(int n)
{
    if (n < 10)
        return n;
    return digitalRoot(sumDigits(n));
}

int main(void)
{
    printf("digitalRoot(9875) = %d\n", digitalRoot(9875));
    return 0;
}
```
```output
digitalRoot(9875) = 2
```

**Ex 6.96**
```c
#include <stdio.h>

int binomial(int n, int k)
{
    if (k == 0 || k == n)
        return 1;
    return binomial(n - 1, k - 1) + binomial(n - 1, k);
}

int main(void)
{
    for (int n = 0; n < 6; n++)
    {
        for (int k = 0; k <= n; k++)
            printf("%d ", binomial(n, k));
        printf("\n");
    }
    return 0;
}
```
```output
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```

---

## Part E — Challenges and mini-projects

**Ex 6.97**
```c
#include <stdio.h>
#include <math.h>

double discriminant(double a, double b, double c)
{
    return b * b - 4 * a * c;
}

void solveQuadratic(double a, double b, double c)
{
    if (a == 0)
    {
        printf("(%g, %g, %g): not a quadratic equation\n", a, b, c);
        return;
    }

    double d = discriminant(a, b, c);

    if (d > 0)
        printf("(%g, %g, %g): roots %.2f and %.2f\n", a, b, c,
               (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a));
    else if (d == 0)
        printf("(%g, %g, %g): one repeated root %.2f\n", a, b, c, -b / (2 * a));
    else
        printf("(%g, %g, %g): no real roots\n", a, b, c);
}

int main(void)
{
    solveQuadratic(1, -3, 2);
    solveQuadratic(1, 2, 1);
    solveQuadratic(1, 0, 1);
    solveQuadratic(0, 4, 5);
    return 0;
}
```
```output
(1, -3, 2): roots 2.00 and 1.00
(1, 2, 1): one repeated root -1.00
(1, 0, 1): no real roots
(0, 4, 5): not a quadratic equation
```

**Ex 6.98**
```c
#include <stdio.h>

int isPrime(int n)
{
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return 0;
    return 1;
}

int nextPrime(int n)
{
    n++;
    while (!isPrime(n))
        n++;
    return n;
}

int nthPrime(int k)
{
    int p = 2;
    for (int i = 1; i < k; i++)
        p = nextPrime(p);
    return p;
}

int main(void)
{
    printf("nextPrime(10) = %d\n", nextPrime(10));
    printf("10th prime    = %d\n", nthPrime(10));
    printf("100th prime   = %d\n", nthPrime(100));

    printf("Twin primes below 100: ");
    for (int p = 2; p + 2 < 100; p++)
        if (isPrime(p) && isPrime(p + 2))
            printf("(%d,%d) ", p, p + 2);
    printf("\n");
    return 0;
}
```
```output
nextPrime(10) = 11
10th prime    = 29
100th prime   = 541
Twin primes below 100: (3,5) (5,7) (11,13) (17,19) (29,31) (41,43) (59,61) (71,73)
```

**Ex 6.99**
```c
#include <stdio.h>

void printInBase(int n, int base)
{
    if (n >= base)
        printInBase(n / base, base);

    int digit = n % base;
    if (digit < 10)
        putchar('0' + digit);
    else
        putchar('A' + digit - 10);
}

int main(void)
{
    int bases[4] = {2, 8, 10, 16};

    for (int i = 0; i < 4; i++)
    {
        printf("255 in base %2d = ", bases[i]);
        printInBase(255, bases[i]);
        printf("\n");
    }
    return 0;
}
```
```output
255 in base  2 = 11111111
255 in base  8 = 377
255 in base 10 = 255
255 in base 16 = FF
```

**Ex 6.100** Zeller's congruence returns `h`: 0 = Saturday, 1 = Sunday, 2 = Monday … 6 = Friday. January and February count as months 13 and 14 of the *previous* year.
```c
#include <stdio.h>

int dayOfWeek(int day, int month, int year)
{
    if (month < 3)
    {
        month += 12;
        year -= 1;
    }
    int k = year % 100;
    int j = year / 100;
    return (day + 13 * (month + 1) / 5 + k + k / 4 + j / 4 + 5 * j) % 7;
}

void printDayName(int h)
{
    switch (h)
    {
        case 0: printf("Saturday");  break;
        case 1: printf("Sunday");    break;
        case 2: printf("Monday");    break;
        case 3: printf("Tuesday");   break;
        case 4: printf("Wednesday"); break;
        case 5: printf("Thursday");  break;
        case 6: printf("Friday");    break;
    }
}

int main(void)
{
    printf("12 Nov 2026 was a ");
    printDayName(dayOfWeek(12, 11, 2026));
    printf("\n");

    printf("6 Mar 1957 (Ghana's independence) was a ");
    printDayName(dayOfWeek(6, 3, 1957));
    printf("\n");
    return 0;
}
```
```output
12 Nov 2026 was a Thursday
6 Mar 1957 (Ghana's independence) was a Wednesday
```

**Ex 6.101**
<!--in: 1 5\n2 29\n3 48 18\n4 2 10\n5 10\n6 1234\n7-->
```c
#include <stdio.h>

long long factorial(int n)
{
    long long f = 1;
    for (int i = 2; i <= n; i++)
        f *= i;
    return f;
}

int isPrime(int n)
{
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return 0;
    return 1;
}

int gcd(int a, int b)
{
    return (b == 0) ? a : gcd(b, a % b);
}

double power(double base, int exp)
{
    double r = 1;
    for (int i = 0; i < exp; i++)
        r *= base;
    return r;
}

long long fibonacci(int n)
{
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++)
    {
        long long next = a + b;
        a = b;
        b = next;
    }
    return a;
}

int reverseNumber(int n)
{
    int rev = 0;
    while (n > 0)
    {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}

int main(void)
{
    int choice, a, b;

    do
    {
        printf("\n1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                scanf("%d", &a);
                printf("%d! = %lld\n", a, factorial(a));
                break;
            case 2:
                scanf("%d", &a);
                printf("%d is %s\n", a, isPrime(a) ? "prime" : "not prime");
                break;
            case 3:
                scanf("%d %d", &a, &b);
                printf("gcd = %d\n", gcd(a, b));
                break;
            case 4:
                scanf("%d %d", &a, &b);
                printf("%d ^ %d = %g\n", a, b, power(a, b));
                break;
            case 5:
                scanf("%d", &a);
                printf("fib(%d) = %lld\n", a, fibonacci(a));
                break;
            case 6:
                scanf("%d", &a);
                printf("reversed = %d\n", reverseNumber(a));
                break;
            case 7:
                printf("Goodbye!\n");
                break;
            default:
                printf("Invalid choice\n");
        }
    }
    while (choice != 7);

    return 0;
}
```
```output
1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 1 5
5! = 120

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 2 29
29 is prime

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 3 48 18
gcd = 6

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 4 2 10
2 ^ 10 = 1024

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 5 10
fib(10) = 55

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 6 1234
reversed = 4321

1) Factorial 2) Prime? 3) GCD 4) Power 5) Fibonacci 6) Reverse 7) Exit
Choose: 7
Goodbye!
```
Notice how short and readable `main` is: it only *chooses* and *calls*; each function does one job.

**Ex 6.102**
```c
#include <stdio.h>

int ack(int m, int n)
{
    if (m == 0)
        return n + 1;
    if (n == 0)
        return ack(m - 1, 1);
    return ack(m - 1, ack(m, n - 1));
}

int main(void)
{
    printf("A(2, 3) = %d\n", ack(2, 3));
    printf("A(3, 3) = %d\n", ack(3, 3));
    return 0;
}
```
```output
A(2, 3) = 9
A(3, 3) = 61
```
It grows astonishingly fast because it recurses *inside its own argument*: `A(1, n) = n + 2`, `A(2, n) = 2n + 3`, `A(3, n) = 2ⁿ⁺³ − 3`, and `A(4, 2)` already has 19 729 digits. Even `A(4, 1)` = 65533 needs a huge number of calls and may crash with a stack overflow.

**Ex 6.103** The stack when the base case is reached (the **top** is the most recent call):
```
 ┌──────────────────────────────┐
 │ recfactorial(1)  → returns 1 │  ← top (base case)
 ├──────────────────────────────┤
 │ recfactorial(2)  waiting: 2 * ?  │
 ├──────────────────────────────┤
 │ recfactorial(3)  waiting: 3 * ?  │
 ├──────────────────────────────┤
 │ recfactorial(4)  waiting: 4 * ?  │
 ├──────────────────────────────┤
 │ recfactorial(5)  waiting: 5 * ?  │
 ├──────────────────────────────┤
 │ main()                       │  ← bottom
 └──────────────────────────────┘
```
Unwinding (top to bottom): `fact(1)` returns **1** → `fact(2)` computes 2 × 1 = **2** and returns → `fact(3)` computes 3 × 2 = **6** → `fact(4)` computes 4 × 6 = **24** → `fact(5)` computes 5 × 24 = **120** and returns to `main`. Each pending call is removed from the stack as it returns.

---

## Part F — Research tasks (sample answers)

**Ex 6.104** `exit(code)` (from `<stdlib.h>`) **ends the whole program immediately** no matter which function calls it (after flushing open files). `return` in `main` also ends the program, but `return` in any *other* function only ends *that function* and gives control back to the caller. `exit(0)` means success; any other code signals an error.

**Ex 6.105**
```c
#include <stdio.h>

int addOne(int x)  { return x + 1; }
int doubleIt(int x) { return 2 * x; }

int applyTwice(int (*f)(int), int x)     /* f is a pointer to a function taking and returning an int */
{
    return f(f(x));
}

int main(void)
{
    printf("%d\n", applyTwice(addOne, 5));
    printf("%d\n", applyTwice(doubleIt, 5));
    return 0;
}
```
```output
7
20
```
`int (*f)(int)` reads: "`f` is a pointer to a function that takes an `int` and returns an `int`". The function's name (without parentheses) is its address.

**Ex 6.106**
```c
#include <stdio.h>
#include <stdarg.h>

int sumAll(int count, ...)
{
    va_list args;
    int total = 0;

    va_start(args, count);
    for (int i = 0; i < count; i++)
        total += va_arg(args, int);
    va_end(args);
    return total;
}

int main(void)
{
    printf("%d\n", sumAll(3, 10, 20, 30));
    printf("%d\n", sumAll(5, 1, 2, 3, 4, 5));
    return 0;
}
```
```output
60
15
```
The `...` means "any number of further arguments". The first parameter tells the function how many to expect (this is also how `printf` knows from the format string).

**Ex 6.107** `argc` is the **number of command-line arguments** (including the program's own name) and `argv` is the list of them, as text. If you run `prog hello world`, then `argc` is 3, `argv[0]` is `prog`, `argv[1]` is `hello`, `argv[2]` is `world`.
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Program: %s\n", argv[0]);
    for (int i = 1; i < argc; i++)
        printf("Argument %d: %s\n", i, argv[i]);
    return 0;
}
```
(You'll fully understand `char *argv[]` after Chapter 8.)

---

*Next: [Chapter 7 solutions](07-arrays.md)*
