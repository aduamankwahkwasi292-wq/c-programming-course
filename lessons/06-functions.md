# Chapter 6 — Functions

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `06 Functions.pdf`  
> **Solutions:** [Solutions to Chapter 6](../solutions/06-functions.md)

---

## What you will learn

1. What a **function** is and why we use them.
2. The three things you must know: **definition**, **declaration (prototype)** and **call**.
3. **Parameters**, **arguments** and **return values**; **pass by value**.
4. **Local** and **global** variables, and **static local** variables.
5. **Recursion** — a function that calls itself.
6. How to use **library functions** (`sqrt`, `pow`, `toupper`…).

This chapter is where you stop writing *scripts* and start writing *programs*.

---

## 6.1 What is a function?

A **function** is a **named group of statements that performs one coherent task**. Once you have written it, you can **call** it by name **whenever** you need that task — instead of typing the same instructions again and again.

**Analogy 1 — a recipe.** The recipe for "make tea" is written once. Any time you want tea you say *"make tea"*; you don't re-explain every step.

**Analogy 2 — a vending machine.** You put something **in** (coins, a button), the machine does its work **inside** (you don't care how), and something comes **out** (a drink). A function takes **inputs**, does a **job**, and gives back a **result**.

```
              ┌─────────────────────┐
  inputs ───▶ │      FUNCTION       │ ───▶ output (return value)
 (arguments)  │  (does one task)    │
              └─────────────────────┘
```

**You already use functions:** `printf`, `scanf`, `getchar` and even `main` are all functions. Now you will write your own.

**Why use functions?**

| Benefit | Meaning |
|---|---|
| **No repetition** | write once, use many times (remember Ex 3.43 where the same long expression was pasted four times) |
| **Divide and conquer** | split a big problem into small tasks — exactly the strategy from Chapter 0 |
| **Readability** | `if (isPrime(n))` reads like English |
| **Easy testing / fixing** | test each small function alone; fix a bug in one place |
| **Teamwork** | different people write different functions |

To study functions we must be able to recognise three things:

1. **Function definition** — where the task is *actually carried out*.
2. **Function declaration (prototype)** — an announcement that the function exists.
3. **Function call** — where we *use* the function.

---

## 6.2 Function definition

The **definition** contains all the steps to perform the task. It has up to **five parts**:

```c
data_type  functName (declared parameter list)
{
    statements;
    return value;
}
```

| # | Part | Meaning |
|---|---|---|
| 1 | **Data type** (return type) | the type of the value the function sends back |
| 2 | **Function name** | any valid identifier (Chapter 1 rules) |
| 3 | **Parameters** | what the function **needs ahead of time** (its inputs) |
| 4 | **Statements** (the body) | the instructions that perform the task |
| 5 | **Return value** | the value sent back with `return` |

```
   return type   name    parameter list
        │         │         │
        ▼         ▼         ▼
       int      add( int a, int b )
       {
           int sum = a + b;     ← body (statements)
           return sum;          ← return value
       }
```

Depending on the function, some parts may be missing:

- **No return value?** The type is **`void`** (no value comes back) and there is no `return value;`.
- **No inputs?** The parameter list is empty — write `(void)`.

```c
void sayHello(void)           /* needs nothing, returns nothing */
{
    printf("Hello from a function!\n");
}

int add(int a, int b)         /* needs two ints, returns an int */
{
    return a + b;
}
```

---

## 6.3 Function declaration (prototype)

A **declaration** (or **prototype**) is a statement that only tells the compiler *"a function with this name, these inputs and this return type exists — its details come later"*. Just as we declare a variable before using it, we declare a function **before calling it**.

```c
data_type functName (declared parameter list);       /* note the semicolon */
```

```c
int add(int a, int b);        /* prototype: ends with ; and has no body */
```

Parameter **names are optional** in a prototype: `int add(int, int);` is also fine.

> 💡 It is like an advertisement: *"Dear compiler, a function called `add` exists. It takes two ints and returns an int."*

## 6.4 Function call

To make the function do its task we **call** it by name and give it the values it needs (the **arguments**). When there are no inputs, the parentheses are empty.

```c
functName (arguments);
```

```c
sayHello();                 /* no arguments */
int total = add(3, 4);      /* the call is replaced by the returned value, 7 */
```

**What happens during a call:**

1. The program **pauses** where it is and **jumps** to the function.
2. The argument values are **copied** into the parameters.
3. The function's body runs.
4. At `return` (or the closing brace) the program **jumps back** to exactly where it left off, and the call is **replaced by the returned value**.

> 📝 **In C you cannot define a function inside another function** (no "nested functions"). All functions are written *separately*, one after another.

### The standard layout of a program

```c
#include <stdio.h>

/* 1. prototypes */
int add(int a, int b);
void sayHello(void);

/* 2. main */
int main(void)
{
    sayHello();
    printf("%d\n", add(3, 4));
    return 0;
}

/* 3. definitions */
void sayHello(void)
{
    printf("Hello from a function!\n");
}

int add(int a, int b)
{
    return a + b;
}
```

(If you write the **definitions before `main`** you don't need prototypes — but then `main` ends up at the bottom, which is awkward. The prototype-on-top style keeps `main` as the "table of contents".)

---

## 6.5 A first complete example (from the slides)

Let us identify the **declaration**, **call** and **definition**:

```c
#include <stdio.h>

float calcArea(float rad);                 /* function declaration */

int main(void)
{
    float x, y;
    x = 10.25;
    y = calcArea(x);                       /* function call */
    printf("the area of a circle of radius %g is %g\n", x, y);
    return 0;
}

float calcArea(float rad)                  /* function definition */
{
    float a;
    a = 3.142 * rad * rad;
    return (a);
}
```
```output
the area of a circle of radius 10.25 is 330.106
```

*(Your slide shows `Int main()` with a capital `I` — a typo. It must be lowercase `int`.)*

### Walk through it step by step

1. `#include <stdio.h>` — bring in `printf`.
2. The **declaration** says: a function `calcArea` exists; it needs one `float` and returns a `float`.
3. `main` starts. `x` and `y` are declared; `x` gets `10.25`.
4. `y = calcArea(x);` is the **call**. We **stop** what we are doing in `main` and **jump** to the definition.
5. In the definition, the value in `x` (10.25) is **copied** into `rad`. So `rad` is `10.25`.
6. `a` is declared; `a = 3.142 * rad * rad` gives `330.106`.
7. `return (a);` sends `330.106` **back** to where the function was called.
8. We jump back to `y = ...`; the call is replaced by the value, so `y = 330.106`.
9. `printf` prints the message. The program ends.

### A function that returns nothing — `void`

```c
#include <stdio.h>

void avg(int a, int b, int c);

int main(void)
{
    int x = 3, y = 4, z = 5;

    avg(x, y, z);
    printf("Done!\n");
    return 0;
}

void avg(int a, int b, int c)
{
    int w = (a + b + c) / 3;
    printf("The average of %d, %d and %d is %d\n", a, b, c, w);
}
```
```output
The average of 3, 4 and 5 is 4
Done!
```

Note the **order** of the output: `avg` runs completely (printing its line) *before* `Done!`. And since the function does not return a value, its type is `void`.

---

## 6.6 Parameters, arguments and "pass by value"

Two words that are often confused:

- **Parameters** — the variables in the function's **definition** (`int a, int b`). They are the function's "slots".
- **Arguments** — the actual **values** in the **call** (`add(3, 4)`). They fill the slots.

**Rules:**
- The arguments must match the parameters in **number, order and type**.
- Arguments are matched **by position**: the first argument goes into the first parameter, etc. The names don't need to match.

### The most important idea: C passes **copies**

When you call a function, C **copies** each argument's value into the parameter. The function works on its *own copy*. Changing the parameter inside the function **does not change** the original variable in the caller. This is called **pass by value**.

```c
#include <stdio.h>

void addTen(int n)
{
    n = n + 10;                       /* changes only the COPY */
    printf("inside : %d\n", n);
}

int main(void)
{
    int a = 5;

    addTen(a);
    printf("outside: %d\n", a);       /* a is untouched */
    return 0;
}
```
```output
inside : 15
outside: 5
```

> 💡 **Analogy.** You give a photocopy of your document to a clerk. He can scribble on it all he likes — your original stays clean. (In Chapter 8, with **pointers**, you will learn how to hand over the *original's address* so the function can change it.)

### Returning a result

A function can return **one value** using `return`. The value's type should match the function's type.

```c
#include <stdio.h>

int larger(int a, int b)
{
    if (a > b)
        return a;
    return b;                 /* reached only when a <= b */
}

int main(void)
{
    int m = larger(3, 9);
    printf("%d\n", m);
    printf("%d\n", larger(larger(4, 8), 6));     /* calls can be nested */
    return 0;
}
```
```output
9
8
```

- `return` **immediately ends** the function — no later statement in it is executed.
- A function call is an **expression**: you can store it (`m = larger(3, 9)`), print it, or pass it to another function.
- In a `void` function you may write `return;` (with no value) to leave early.

> ⚠️ **Common mistakes**
> - Calling a function **before** it is declared or defined (the compiler doesn't know it).
> - Wrong number or type of arguments.
> - Forgetting to `return` a value from a non-`void` function.
> - Writing a `;` after the definition's header: `int add(int a, int b); { ... }` is wrong.
> - Defining a function inside `main`.
> - Expecting a function to change the caller's variable (pass-by-value!).

---

## 6.7 Local and global variables (scope)

Where a variable is declared decides **who can see it**.

- A **local variable** is declared **inside** a function (or a block `{ }`). It is known **only there**. When the function ends, it **disappears**.
- A **global variable** is declared **outside all functions**. It is known **everywhere** in the program and lives until the program ends.

```c
#include <stdio.h>

void funct1(void);
int x = 50;                          /* GLOBAL */

int main(void)
{
    int y = 30;                      /* local to main */

    printf("%d\n", y);
    printf("%d\n", x);
    funct1();
    printf("End\n");
    return 0;
}

void funct1(void)
{
    int z = 20;                      /* local to funct1 */

    printf("%d\n", z);
    printf("%d\n", x);
}
```
```output
30
50
20
50
End
```

- `x` is global: both functions can read (and change) it.
- `y` can only be used in `main`; `z` only in `funct1`.

**Same name, different places.** Two different functions may each have their own local variable called `i` or `n` — they are completely separate boxes. A local variable that has the same name as a global one **hides** ("shadows") it inside its block:

```c
#include <stdio.h>

int x = 10;                          /* global */

void show(void)
{
    printf("%d ", x);
}

int main(void)
{
    show();                          /* uses the global x */
    int x = 20;                      /* a NEW local x that hides the global one */
    printf("%d ", x);
    show();                          /* still the global x: 10 */
    printf("\n");
    return 0;
}
```
```output
10 20 10
```

> ⚠️ **Avoid global variables** except for true constants. Any function can change them, so when something goes wrong you can't tell *who* did it. Pass information through **parameters** and **return values** instead — it keeps functions independent and easy to test.

---

## 6.8 Static local variables

Normally a local variable is **created fresh** every time its function is called and **destroyed** when the function ends. A **static local variable** is different:

- It is declared with the keyword **`static`**.
- It is **initialised only once** (the first time).
- It **keeps its value** between calls — it lives for the whole program (but is still visible only inside its function).

**Non-static** — the variable starts again each call:

```c
#include <stdio.h>

int funct1(int k);

int main(void)
{
    int a, b = 0;

    for (a = 0; a < 5; a++)
    {
        b = funct1(a);
        printf("%d\t", b);
    }
    return 0;
}

int funct1(int k)
{
    int j = 0;           /* created and set to 0 on EVERY call */
    j += k;
    return j;
}
```
```output
0       1       2       3       4
```

**Static** — the variable remembers:

```c
#include <stdio.h>

int funct1(int k);

int main(void)
{
    int a, b = 0;

    for (a = 0; a < 5; a++)
    {
        b = funct1(a);
        printf("%d\t", b);
    }
    return 0;
}

int funct1(int k)
{
    static int j = 0;    /* initialised ONCE; remembered between calls */
    j += k;
    return j;
}
```
```output
0       1       3       6       10
```

The only difference is the word `static`. The first call sets `j` to 0, adds 0 → 0. The second call does **not** reset `j`; it continues from 0 and adds 1 → 1; then adds 2 → 3; then 3 → 6; then 4 → 10 (a running total).

**A practical use — a call counter:**

```c
#include <stdio.h>

void visit(void)
{
    static int count = 0;
    count++;
    printf("You are visitor number %d\n", count);
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
You are visitor number 1
You are visitor number 2
You are visitor number 3
```

---

## 6.9 Recursion

**Recursion** is solving a big problem by breaking it into **smaller versions of the same problem**. In programming, a **recursive function** is a function that **calls itself**.

```c
void recursiveFunct(void)
{
    recursiveFunct();           /* the function calls itself */
}
```

C supports recursion — but the example above would **never stop** (it calls itself forever until the computer runs out of memory: a "stack overflow" crash). Every recursive function needs:

1. A **base case** — an *exit condition*: a situation simple enough to answer **directly**, without calling itself.
2. A **recursive case** — it calls itself with a **smaller / simpler** input, moving towards the base case.

> 💡 **Analogy: Russian dolls.** To find the smallest doll you open a doll, and inside is a smaller doll, and you open that… until you reach a doll that cannot be opened (the **base case**).

### Example 1 — Factorial

`n! = n × (n−1) × … × 1`. Notice that `n! = n × (n−1)!` — the factorial of `n` is built from a *smaller* factorial. And `0! = 1! = 1` (the base case).

Your slide shows a **non-recursive** and a **recursive** version side by side:

```c
#include <stdio.h>

int factorial(int);
int recfactorial(int);

int main(void)
{
    int y, num = 10;

    y = factorial(num);
    printf("non-recursive: %d! = %d\n", num, y);

    y = recfactorial(num);
    printf("recursive: %d! = %d\n", num, y);
    return 0;
}

/* non-recursive (uses a loop) */
int factorial(int x)
{
    for (int i = x; i > 1; --i)
    {
        x = x * (i - 1);
    }
    return x;
}

/* recursive */
int recfactorial(int x)
{
    if (x <= 1)
    {
        return 1;                      /* base case */
    }
    return x * recfactorial(x - 1);    /* recursive case */
}
```
```output
non-recursive: 10! = 3628800
recursive: 10! = 3628800
```

(The slide's loop is a clever shortcut: starting from `x`, it multiplies by `x−1`, `x−2`, … `1`. A more readable loop version is `int f = 1; for (i = 2; i <= n; i++) f *= i;`.)

### How does it work? The call stack

When `recfactorial(4)` runs, it needs `recfactorial(3)`, which needs `recfactorial(2)`, … Each waiting call is stored on the **call stack** (like a pile of plates — Chapter 0!). When the base case returns, the answers flow **back up**:

```
 recfactorial(4)  = 4 * recfactorial(3)
                         = 3 * recfactorial(2)
                                 = 2 * recfactorial(1)
                                         = 1        ← base case: starts the return
                                 = 2 * 1  = 2
                         = 3 * 2  = 6
 = 4 * 6  = 24
```

You can *watch* it by printing when each call starts and ends:

```c
#include <stdio.h>

int fact(int n, int depth)
{
    printf("%*scall fact(%d)\n", depth * 2, "", n);
    int result;

    if (n <= 1)
        result = 1;
    else
        result = n * fact(n - 1, depth + 1);

    printf("%*sfact(%d) returns %d\n", depth * 2, "", n, result);
    return result;
}

int main(void)
{
    fact(4, 0);
    return 0;
}
```
```output
call fact(4)
  call fact(3)
    call fact(2)
      call fact(1)
      fact(1) returns 1
    fact(2) returns 2
  fact(3) returns 6
fact(4) returns 24
```

(The `%*s` trick prints `depth * 2` spaces — it just indents the output.)

### Example 2 — Fibonacci

The Fibonacci sequence `0 1 1 2 3 5 8 13 …`: each term is the sum of the previous two. `fib(0) = 0`, `fib(1) = 1`, and `fib(n) = fib(n−1) + fib(n−2)`.

```c
#include <stdio.h>

int fibonacci(int);

int main(void)
{
    for (int i = 0; i < 8; ++i)
    {
        printf("%d\t", fibonacci(i));
    }
    return 0;
}

int fibonacci(int i)
{
    if (i == 0 || i == 1)
    {
        return i;                              /* two base cases */
    }
    return fibonacci(i - 1) + fibonacci(i - 2);
}
```
```output
0       1       1       2       3       5       8       13
```

> ⚠️ Recursive Fibonacci is **elegant but slow** for large `n`: it recomputes the same values again and again (`fib(40)` makes over 300 million calls!). A simple loop is much faster. Choose recursion when it makes the *solution clearer*, not always.

### Example 3 — thinking recursively

Print the numbers `n` down to 1 — *print `n`, then count down from `n−1`*:

```c
#include <stdio.h>

void countdown(int n)
{
    if (n == 0)                  /* base case: nothing left to print */
    {
        printf("Liftoff!\n");
        return;
    }
    printf("%d ", n);
    countdown(n - 1);            /* the same job, on a smaller number */
}

int main(void)
{
    countdown(5);
    return 0;
}
```
```output
5 4 3 2 1 Liftoff!
```

**Where you put the `printf` matters.** Print the digits of a number **left to right**: first deal with all digits *except the last* (recursively), **then** print the last digit:

```c
#include <stdio.h>

void printDigits(int n)
{
    if (n >= 10)
        printDigits(n / 10);     /* first the digits to the left */
    printf("%d ", n % 10);       /* then this (last) digit */
}

int main(void)
{
    printDigits(4096);
    printf("\n");
    return 0;
}
```
```output
4 0 9 6
```

Move the `printf` **above** the recursive call and you'd print the digits in reverse (`6 9 0 4`).

### Example 4 — Towers of Hanoi

A legendary puzzle: move `n` disks from peg A to peg C using peg B, moving one disk at a time and never putting a bigger disk on a smaller one. The recursive idea: *move `n−1` disks out of the way, move the big disk, move the `n−1` disks back on top.*

```c
#include <stdio.h>

void hanoi(int n, char from, char to, char via)
{
    if (n == 0)
        return;                                        /* base case */
    hanoi(n - 1, from, via, to);                       /* clear the way        */
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n - 1, via, to, from);                       /* put them back on top */
}

int main(void)
{
    hanoi(3, 'A', 'C', 'B');
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
```

Seven moves for 3 disks: in general `2ⁿ − 1`. Writing this with loops is very hard; with recursion it takes five lines — a good example of when recursion shines.

### Recursion vs loops

| | Loop (iteration) | Recursion |
|---|---|---|
| Speed & memory | usually faster, less memory | each call uses stack memory; deep recursion can crash |
| Clarity | great for simple repetition | great when the problem is naturally "smaller copies of itself" (trees, Hanoi, divide and conquer) |

Any recursive function can be rewritten with a loop (and vice-versa). Use whichever makes the solution **clearest**, and always ask: **"What is my base case? Am I moving towards it?"**

---

## 6.10 Library functions

You don't have to write everything yourself. C comes with **libraries** of ready-made functions, each described in a **header file**.

| Header | Examples |
|---|---|
| `<stdio.h>` | `printf`, `scanf`, `getchar`, `fgets` |
| `<math.h>` | `sqrt(x)`, `pow(x, y)`, `fabs(x)`, `ceil(x)`, `floor(x)`, `round(x)`, `sin`, `cos`, `log`, `exp` |
| `<ctype.h>` | `toupper(c)`, `tolower(c)`, `isdigit(c)`, `isalpha(c)`, `isspace(c)` |
| `<stdlib.h>` | `abs(n)`, `rand()`, `srand()`, `exit()` |
| `<string.h>` | `strlen`, `strcpy`, `strcmp` … (Chapter 8) |

```c
#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    printf("sqrt(144)    = %.1f\n", sqrt(144));
    printf("pow(2, 10)   = %.1f\n", pow(2, 10));
    printf("fabs(-7.5)   = %.1f\n", fabs(-7.5));
    printf("ceil(4.2)    = %.1f\n", ceil(4.2));
    printf("floor(4.8)   = %.1f\n", floor(4.8));
    printf("round(4.5)   = %.1f\n", round(4.5));
    printf("toupper('g') = %c\n", toupper('g'));
    printf("isdigit('7') = %s\n", isdigit('7') ? "yes" : "no");
    return 0;
}
```
```output
sqrt(144)    = 12.0
pow(2, 10)   = 1024.0
fabs(-7.5)   = 7.5
ceil(4.2)    = 5.0
floor(4.8)   = 4.0
round(4.5)   = 5.0
toupper('g') = G
isdigit('7') = yes
```

> 📝 With the GCC compiler on Linux/macOS you may need to add `-lm` when compiling to link the math library: `gcc prog.c -o prog -lm`.

---

## 6.11 Designing with functions (top-down)

To write a larger program, use **divide and conquer**: write the main idea first, using functions you haven't written yet, then fill in each one.

**Task:** read three marks, print their average and a grade.

```c
#include <stdio.h>

double average(double a, double b, double c);
char grade(double score);
void printReport(double avg, char g);

int main(void)
{
    double m1, m2, m3;

    printf("Enter three marks: ");
    scanf("%lf %lf %lf", &m1, &m2, &m3);

    double avg = average(m1, m2, m3);
    printReport(avg, grade(avg));
    return 0;
}

double average(double a, double b, double c)
{
    return (a + b + c) / 3;
}

char grade(double score)
{
    if (score >= 80) return 'A';
    if (score >= 70) return 'B';
    if (score >= 60) return 'C';
    if (score >= 50) return 'D';
    return 'F';
}

void printReport(double avg, char g)
{
    printf("Average: %.2f\n", avg);
    printf("Grade  : %c\n", g);
}
```

<!--in: 72 65 80-->
```c
#include <stdio.h>

double average(double a, double b, double c);
char grade(double score);
void printReport(double avg, char g);

int main(void)
{
    double m1, m2, m3;

    printf("Enter three marks: ");
    scanf("%lf %lf %lf", &m1, &m2, &m3);

    double avg = average(m1, m2, m3);
    printReport(avg, grade(avg));
    return 0;
}

double average(double a, double b, double c)
{
    return (a + b + c) / 3;
}

char grade(double score)
{
    if (score >= 80) return 'A';
    if (score >= 70) return 'B';
    if (score >= 60) return 'C';
    if (score >= 50) return 'D';
    return 'F';
}

void printReport(double avg, char g)
{
    printf("Average: %.2f\n", avg);
    printf("Grade  : %c\n", g);
}
```
```output
Enter three marks: 72 65 80
Average: 72.33
Grade  : B
```

**Good-function checklist**

1. **One job** per function, and a name that says what it is (`average`, `isPrime`, `printReport`).
2. Keep functions **short** (if it won't fit on one screen, split it).
3. **Compute and return** values; let `main` (or a dedicated `print…` function) do the printing.
4. Use **parameters**, not globals.
5. Test each function by itself with easy inputs.

---

## Key takeaways

- A **function** is a named block of code that does one task; use it by **calling** it.
- Three things: **definition** (the code), **declaration/prototype** (announcement, ends with `;`), **call** (use).
- A definition has: **return type, name, parameters, body, return value**. No result → `void`. No inputs → `(void)`.
- **Parameters** are in the definition; **arguments** are in the call. They match by position.
- C passes **copies** (**pass by value**): the function can't change the caller's variables.
- **Local** variables live inside a function; **global** variables live everywhere (use sparingly).
- **`static` local**: initialised once, remembers its value between calls.
- **Recursion** = a function calling itself. Needs a **base case** and progress towards it.
- Use **library functions** (`sqrt`, `pow`, `toupper`…) — don't reinvent them.
- Design **top-down**: small functions, one job each.

---

# Exercises — Chapter 6

## Part A — Quick check

**Ex 6.1** What is a function? Give two reasons for using functions.

**Ex 6.2** Name the three things you must be able to identify in a program that uses functions, and say what each one does.

**Ex 6.3** List the five parts of a function definition.

**Ex 6.4** When is a function's type `void`? What does `(void)` in the parameter list mean?

**Ex 6.5** What is the difference between a function **declaration** and a function **definition**?

**Ex 6.6** What is the difference between a **parameter** and an **argument**?

**Ex 6.7** What does "pass by value" mean? Can a function change the original variable of its caller this way?

**Ex 6.8** What is the difference between a local and a global variable? Why should global variables be avoided?

**Ex 6.9** What does the keyword `static` do to a local variable?

**Ex 6.10** What is recursion? What are the two essential parts of every recursive function?

**Ex 6.11** What happens if a recursive function has no base case (or never reaches it)?

**Ex 6.12** Can you define a function inside another function in C?

**Ex 6.13** What happens to the statements after a `return` in the same function?

**Ex 6.14** True or false?
1. A function may return two values with two `return` statements executed one after the other.
2. `int add(int a, int b);` is a declaration.
3. The names of the arguments in the call must match the names of the parameters.
4. A `void` function can use `return;`.
5. A static local variable is visible in all functions.
6. `printf` is a function.

## Part B — Predict the output

*(Trace each program on paper first. Then you can run it to check.)*

**Ex 6.15**
```c
#include <stdio.h>
int twice(int x) { return 2 * x; }
int main(void)
{
    printf("%d\n", twice(twice(3)));
    return 0;
}
```

**Ex 6.16**
```c
#include <stdio.h>
void hello(void) { printf("Hello "); }
int main(void)
{
    printf("A ");
    hello();
    printf("B ");
    hello();
    printf("C\n");
    return 0;
}
```

**Ex 6.17**
```c
#include <stdio.h>
void addTen(int n)
{
    n = n + 10;
    printf("inside: %d\n", n);
}
int main(void)
{
    int a = 5;
    addTen(a);
    printf("outside: %d\n", a);
    return 0;
}
```

**Ex 6.18**
```c
#include <stdio.h>
int f(int a, int b)
{
    if (a > b)
        return a - b;
    return b - a;
}
int main(void)
{
    printf("%d %d\n", f(3, 10), f(10, 3));
    return 0;
}
```

**Ex 6.19**
```c
#include <stdio.h>
int x = 10;
void show(void) { printf("%d ", x); }
int main(void)
{
    show();
    int x = 20;
    printf("%d ", x);
    show();
    printf("\n");
    return 0;
}
```

**Ex 6.20**
```c
#include <stdio.h>
int count = 0;
void inc(void) { count++; }
int main(void)
{
    inc();
    inc();
    inc();
    printf("%d\n", count);
    return 0;
}
```

**Ex 6.21**
```c
#include <stdio.h>
int next(void)
{
    static int n = 0;
    n++;
    return n;
}
int main(void)
{
    int a = next();
    int b = next();
    int c = next();
    printf("%d %d %d\n", a, b, c);
    return 0;
}
```

**Ex 6.22**
```c
#include <stdio.h>
int plain(void)
{
    int n = 0;
    n++;
    return n;
}
int remember(void)
{
    static int n = 0;
    n++;
    return n;
}
int main(void)
{
    for (int i = 0; i < 3; i++)
        printf("%d ", plain());
    printf("\n");
    for (int i = 0; i < 3; i++)
        printf("%d ", remember());
    printf("\n");
    return 0;
}
```

**Ex 6.23**
```c
#include <stdio.h>
int running(int k)
{
    static int j = 0;
    j += k;
    return j;
}
int main(void)
{
    for (int a = 1; a <= 5; a++)
        printf("%d ", running(a));
    return 0;
}
```

**Ex 6.24**
```c
#include <stdio.h>
int f(int n)
{
    if (n == 0)
        return 0;
    return n + f(n - 1);
}
int main(void)
{
    printf("%d\n", f(4));
    return 0;
}
```

**Ex 6.25**
```c
#include <stdio.h>
void show(int n)
{
    if (n == 0)
        return;
    printf("%d ", n);
    show(n - 1);
    printf("%d ", n);
}
int main(void)
{
    show(3);
    return 0;
}
```

**Ex 6.26**
```c
#include <stdio.h>
void digits(int n)
{
    if (n < 10)
    {
        printf("%d ", n);
        return;
    }
    digits(n / 10);
    printf("%d ", n % 10);
}
int main(void)
{
    digits(4096);
    return 0;
}
```

**Ex 6.27** What does this function compute?
```c
#include <stdio.h>
int mystery(int a, int b)
{
    if (b == 0)
        return a;
    return mystery(b, a % b);
}
int main(void)
{
    printf("%d\n", mystery(48, 18));
    return 0;
}
```

**Ex 6.28**
```c
#include <stdio.h>
int p(int x, int n)
{
    if (n == 0)
        return 1;
    return x * p(x, n - 1);
}
int main(void)
{
    printf("%d %d\n", p(2, 5), p(3, 3));
    return 0;
}
```

**Ex 6.29** How many times is `fib` called?
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
    int r = fib(6);
    printf("%d %d\n", r, calls);
    return 0;
}
```

**Ex 6.30**
```c
#include <stdio.h>
int check(int x)
{
    printf("check(%d) ", x);
    return x > 5;
}
int main(void)
{
    if (check(3) && check(9))
        printf("yes\n");
    else
        printf("no\n");
    if (check(9) || check(1))
        printf("yes\n");
    else
        printf("no\n");
    return 0;
}
```

**Ex 6.31**
```c
#include <stdio.h>
double half1(int n) { return n / 2; }
double half2(int n) { return n / 2.0; }
int main(void)
{
    printf("%.1f %.1f\n", half1(7), half2(7));
    return 0;
}
```

**Ex 6.32**
```c
#include <stdio.h>
int roundDown(double x) { return x; }
int main(void)
{
    printf("%d %d\n", roundDown(7.9), roundDown(-7.9));
    return 0;
}
```

**Ex 6.33**
```c
#include <stdio.h>
int sq(int x) { return x * x; }
int sumSq(int a, int b) { return sq(a) + sq(b); }
int main(void)
{
    printf("%d\n", sumSq(3, 4));
    return 0;
}
```

**Ex 6.34**
```c
#include <stdio.h>
int ds(int n)
{
    return n == 0 ? 0 : n % 10 + ds(n / 10);
}
int main(void)
{
    printf("%d\n", ds(1729));
    return 0;
}
```

**Ex 6.35**
```c
#include <stdio.h>
int main(void)
{
    int x = 1;
    {
        int x = 2;
        printf("%d ", x);
    }
    printf("%d\n", x);
    return 0;
}
```

**Ex 6.36**
```c
#include <stdio.h>
void pattern(int n)
{
    if (n > 0)
    {
        pattern(n - 1);
        printf("%d ", n);
        pattern(n - 1);
    }
}
int main(void)
{
    pattern(3);
    return 0;
}
```

## Part C — Find and fix the bugs

**Ex 6.37** `square` is used before it is defined.
<!--skip-->
```c
#include <stdio.h>
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

**Ex 6.38** The function should return the cube, but the program prints garbage.
<!--skip-->
```c
#include <stdio.h>
int cube(int n)
{
    n * n * n;
}
int main(void)
{
    printf("%d\n", cube(3));
    return 0;
}
```

**Ex 6.39** Why does this not compile?
<!--skip-->
```c
#include <stdio.h>
int area(int length, int width)
{
    return length * width;
}
int main(void)
{
    printf("%d\n", area(5));
    return 0;
}
```

**Ex 6.40** What is wrong here?
<!--skip-->
```c
#include <stdio.h>
void getFive(void)
{
    return 5;
}
int main(void)
{
    int x = getFive();
    printf("%d\n", x);
    return 0;
}
```

**Ex 6.41** The programmer expected `a = 20` and `b = 10` after the call. Explain why this does not work (you will learn the fix in Chapter 8).
```c
#include <stdio.h>
void swap(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
}
int main(void)
{
    int a = 10, b = 20;
    swap(a, b);
    printf("a = %d, b = %d\n", a, b);
    return 0;
}
```

**Ex 6.42** Why does this not compile?
<!--skip-->
```c
#include <stdio.h>
void setup(void)
{
    int level = 5;
}
int main(void)
{
    setup();
    printf("%d\n", level);
    return 0;
}
```

**Ex 6.43** This program crashes with a "stack overflow". Fix it.
<!--skip-->
```c
#include <stdio.h>
int factorial(int n)
{
    return n * factorial(n - 1);
}
int main(void)
{
    printf("%d\n", factorial(5));
    return 0;
}
```

**Ex 6.44** Find the mistake.
<!--skip-->
```c
#include <stdio.h>
int add(int a, int b);
{
    return a + b;
}
int main(void)
{
    printf("%d\n", add(2, 3));
    return 0;
}
```

**Ex 6.45** Find the mistake.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    int double_it(int x)
    {
        return 2 * x;
    }
    printf("%d\n", double_it(4));
    return 0;
}
```

**Ex 6.46** Most compilers (e.g. GCC) report "conflicting types" here — and even a compiler that lets it through prints the wrong answer. Why?
<!--skip-->
```c
#include <stdio.h>
float avg(int a, int b);
int main(void)
{
    printf("%.1f\n", avg(7, 8));
    return 0;
}
int avg(int a, int b)
{
    return (a + b) / 2;
}
```

**Ex 6.47** The average of 7 and 8 should be `7.5` but prints `7.0`. Fix it.
```c
#include <stdio.h>
float average(int a, int b)
{
    return (a + b) / 2;
}
int main(void)
{
    printf("%.1f\n", average(7, 8));
    return 0;
}
```

**Ex 6.48** The visitor counter always prints `1`. Fix it.
```c
#include <stdio.h>
void visit(void)
{
    int count = 0;
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

**Ex 6.49** `isPrime(9)` returns the wrong answer. Find the logic error and fix it.
```c
#include <stdio.h>
int isPrime(int n)
{
    for (int d = 2; d < n; d++)
    {
        if (n % d != 0)
            return 1;
        else
            return 0;
    }
    return 1;
}
int main(void)
{
    printf("%d %d %d\n", isPrime(7), isPrime(9), isPrime(15));
    return 0;
}
```

**Ex 6.50** The program should print three lines of `**` but prints only one. Why? (A global variable is shared by two loops.) Fix it without removing the global.
```c
#include <stdio.h>
int i;
void printStars(int n)
{
    for (i = 0; i < n; i++)
        printf("*");
}
int main(void)
{
    for (i = 0; i < 3; i++)
    {
        printStars(2);
        printf("\n");
    }
    return 0;
}
```

## Part D1 — Write the functions

*(Write **each function separately** and test it from `main`. Keep `main` for reading input and printing; let the function compute and return.)*

**Ex 6.51** Write `void greet(void)` that prints a three-line welcome banner. Call it three times.

**Ex 6.52** Write `void printLine(char c, int n)` that prints the character `c`, `n` times, followed by a newline. Use it to draw a box around the text `KNUST`.

**Ex 6.53** Write `int square(int)` and `int cube(int)`. Print a table of the numbers 1–10 with their squares and cubes.

**Ex 6.54** Write `int max2(int, int)` and `int max3(int, int, int)` (use `max2` inside `max3`), and `int min3(int, int, int)`.

**Ex 6.55** Write `double average3(double, double, double)` and use it to print the average of three marks read from the user.

**Ex 6.56** Write `int isEven(int n)` (returns 1 or 0). Use it to count and list the even numbers from 1 to 50.

**Ex 6.57** Write `int isPrime(int n)`. Use it to print all primes up to `N` and say how many there are.

**Ex 6.58** Write `long long factorial(int n)` (with a loop) and `long long nCr(int n, int r)` using it. Print `5C2` and `10C3`.

**Ex 6.59** Write `double power(double base, int exp)` using a loop, supporting **negative** exponents (`2^-3 = 0.125`).

**Ex 6.60** Write `int gcd(int, int)` and `int lcm(int, int)` (using `gcd`).

**Ex 6.61** Write `double c2f(double c)` and `double f2c(double f)`. Print a conversion table from −10 °C to 40 °C in steps of 10.

**Ex 6.62** Write `double rectArea(double, double)`, `double circleArea(double)` and `double triangleArea(double a, double b, double c)` (Heron's formula: `s = (a+b+c)/2`, area = √(s(s−a)(s−b)(s−c))).

**Ex 6.63** Write `int absVal(int)` and `int sign(int)` (returns −1, 0 or 1).

**Ex 6.64** Write `int isLeap(int year)` and `int daysInMonth(int month, int year)` (using `isLeap`).

**Ex 6.65** Write `int countDigits(int)`, `int sumDigits(int)`, `int reverseNumber(int)` and `int isPalindrome(int)` (using `reverseNumber`).

**Ex 6.66** Write `int isVowel(char)`, `char toUpper(char)` and `int isDigit(char)` **without** using `<ctype.h>`.

**Ex 6.67** Write `char gradeOf(int score)` that returns `'A'`–`'F'`, or `'?'` for a score outside 0–100. Test it with several scores.

**Ex 6.68** Write `double simpleInterest(double p, double r, int t)` and `double compoundInterest(double p, double r, int t)` (use a loop). Compare them for GHS 5000 at 10 % for 5 years.

**Ex 6.69** Write `void printTriangle(int n)` and `void printPyramid(int n)`.

**Ex 6.70** Write `int isPerfect(int)` and `int isArmstrong(int)`. Use them to list the perfect numbers up to 1000 and the Armstrong numbers up to 999.

**Ex 6.71** Write a **menu-driven calculator**: functions `add`, `subtract`, `multiply`, `divide` (taking two doubles), and a menu loop in `main`.

**Ex 6.72** Write `void tick(void)` that prints `tick #1`, `tick #2`, … on successive calls, using a `static` variable. Call it five times.

**Ex 6.73** Write `double transaction(double amount)` that keeps a **static balance**: a positive amount is a deposit, a negative amount is a withdrawal (refuse it if it would make the balance negative). It returns the new balance.

**Ex 6.74** Write `unsigned int nextRandom(void)` — a tiny pseudo-random generator that keeps its **state in a static variable**: `state = (state * 1103515245u + 12345u) & 0x7fffffffu;`. Print the first five values (use `% 100` to get numbers below 100).

**Ex 6.75** Write `int isTriangle(double a, double b, double c)` and `void classify(double, double, double)` that prints the type of triangle.

**Ex 6.76** Write `int hours(int totalSeconds)`, `int minutes(int totalSeconds)` and `int seconds(int totalSeconds)` and print `3725 s` as `1:02:05`.

**Ex 6.77** Write `double roundTo(double x, int places)` that rounds to the given number of decimals (hint: multiply by 10ᵖ, add 0.5, `floor`, divide back). Test with `3.14159` and 2 places.

**Ex 6.78** Write `double c2k(double c)` (Celsius to Kelvin: `c + 273.15`) and then `double f2k(double f)` **by calling `f2c` and `c2k`** (from Ex 6.61). Convert 98.6 °F.

**Ex 6.79** Write `int divisibleBy(int n, int d)` and use it to count how many numbers from 1 to 1000 are divisible by both 3 and 5.

**Ex 6.80** Write `int luhnValid(long long n)` (from Ex 5.113) and test it on `79927398713` and `79927398710`.

## Part D2 — Recursion

**Ex 6.81** Write a recursive `long long fact(int n)` and an iterative `long long factIter(int n)`. Print both for `n = 0 … 10` side by side.

**Ex 6.82** Write a recursive `int sumTo(int n)` (1 + 2 + … + n). Check it against the formula `n(n+1)/2`.

**Ex 6.83** Write a recursive `int fib(int n)`. Print the first 15 terms, then count how many calls `fib(20)` makes (use a global counter).

**Ex 6.84** Write a recursive `long long power(long long x, int n)`. Then write a faster version using the fact that `xⁿ = (xⁿ/²)²` for even `n`.

**Ex 6.85** Write a recursive `int gcd(int a, int b)` using Euclid's rule: `gcd(a, 0) = a`, otherwise `gcd(b, a % b)`.

**Ex 6.86** Write recursive `int sumDigits(int n)` and `int countDigits(int n)`.

**Ex 6.87** Write a recursive `void printReverse(int n)` that prints the digits of `n` **in reverse order**.

**Ex 6.88** Write a recursive `void countdown(int n)` printing `n … 1` then `Liftoff!`. Then write `void countUp(int n)` printing `1 … n` (hint: recurse first).

**Ex 6.89** Write a recursive `void toBinary(int n)` that prints the binary form of `n`.

**Ex 6.90** Write a recursive helper `int reverseHelper(int n, int acc)` and use it to reverse a number: `reverseHelper(n / 10, acc * 10 + n % 10)`.

**Ex 6.91** Write the **Towers of Hanoi** function, print the moves for 3 disks and also *count* the moves for 10 disks (expected 1023).

**Ex 6.92** **Mutual recursion:** write `int isEven(int)` and `int isOdd(int)` where each calls the other (`isEven(0)` is true; `isOdd(0)` is false). You need a prototype for the one defined later.

**Ex 6.93** Write a recursive `int multiply(int a, int b)` using only addition (`a × b = a + a × (b−1)`).

**Ex 6.94** Write a recursive `double harmonic(int n)` = `1 + 1/2 + … + 1/n`.

**Ex 6.95** Write a recursive `int digitalRoot(int n)` (sum the digits repeatedly until one digit remains).

**Ex 6.96** Write a recursive `int binomial(int n, int k)` using Pascal's rule `C(n,k) = C(n−1,k−1) + C(n−1,k)` with `C(n,0) = C(n,n) = 1`. Print Pascal's triangle for 6 rows.

## Part E — Challenges and mini-projects

**Ex 6.97 (quadratic solver)** Write `double discriminant(double a, double b, double c)` and `void solveQuadratic(double a, double b, double c)` that prints the roots (or says there are none). Test with several equations.

**Ex 6.98 (prime tools)** Write `int nextPrime(int n)` (the smallest prime greater than `n`) and `int nthPrime(int k)`. Print the 10th and 100th primes and all **twin primes** (primes that differ by 2) below 100.

**Ex 6.99 (base converter)** Write a recursive `void printInBase(int n, int base)` for bases 2–16 (digits above 9 use `A`–`F`). Print 255 in bases 2, 8, 10 and 16.

**Ex 6.100 (day of the week)** Write `int dayOfWeek(int day, int month, int year)` using **Zeller's congruence** and a function `void printDayName(int)`. Find the day of the week of **12 November 2026**, and of your birthday.

**Ex 6.101 (math toolkit)** Combine factorial, prime check, gcd, power, Fibonacci and digit reversal in one **menu-driven** program where `main` only shows the menu and calls the functions.

**Ex 6.102 (Ackermann)** The **Ackermann function** is defined by `A(0, n) = n + 1`; `A(m, 0) = A(m − 1, 1)`; `A(m, n) = A(m − 1, A(m, n − 1))`. Implement it and print `A(2, 3)` and `A(3, 3)`. Why does it grow so fast?

**Ex 6.103 (stack drawing)** On paper, draw the call stack for `recfactorial(5)` at the moment the base case is reached. Then draw how the stack unwinds, writing the value returned at each step.

## Part F — Research tasks

**Ex 6.104** What does the function `exit()` do, and how is it different from `return` in `main`?

**Ex 6.105** Read ahead about **function pointers** (also an assignment in your Pointers slides). Write a program with one function that takes another function as a parameter and applies it to a number.

**Ex 6.106** `printf` can take any number of arguments. Find out about `<stdarg.h>` and write `int sumAll(int count, ...)` that adds `count` integers.

**Ex 6.107** What is the meaning of `int main(int argc, char *argv[])`? Write a program that prints the arguments it was started with.

---

*End of Chapter 6. Next: [Chapter 7 — Arrays](07-arrays.md)*
