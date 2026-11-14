# Chapter 8 — Pointers and Strings

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `08 Pointers and Strings.pdf`  
> **Solutions:** [Solutions to Chapter 8](../solutions/08-pointers-and-strings.md)

---

## What you will learn

**Part I — Pointers**

1. What **memory addresses** are, and what a **pointer** is.
2. How to **declare** a pointer, **assign** an address (`&`) and **dereference** it (`*`).
3. How to **pass pointers to functions** (pass by reference) and **return pointers**.
4. The link between **pointers and arrays** (pointer arithmetic).
5. A first look at **function pointers** and **dynamic memory** (`malloc` / `free`).

**Part II — Strings**

6. What a **string** is — a character array ending in `'\0'`.
7. How to **declare, initialise, read and print** strings.
8. The **string library** `<string.h>`: `strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`, `strstr`, `strdup`…
9. How to write your own string functions.

> 💡 Pointers are famous for being "hard". They are not hard — they are just **new**. Take them one picture at a time. Every pointer idea in this chapter can be drawn as boxes and arrows. **Draw them on paper!**

---

# PART I — POINTERS

## 8.1 Memory and addresses

Your computer's memory is like a very long street of numbered **houses** (called **bytes**). Every house has an **address** — its number. The numbers are usually written in **hexadecimal** (base 16), e.g. `0x61FE1C`.

When you declare a variable, the computer reserves one or more houses for it:

```c
int a = 25;
```

```
   memory (each cell = 1 byte)

   address :   ...   135F   1360   1361   1362   ...
                    ┌──────────────────────────┐
   a (4 bytes)      │          25              │    ← the variable "a"
                    └──────────────────────────┘
```

Three things describe a variable:

| | Meaning | For `int a = 25;` |
|---|---|---|
| **name** | what we call it | `a` |
| **value** | what is stored | `25` |
| **address** | where it lives (the address of its first byte) | `135F` (just an example) |

In the slide, `a` is the name, `25` is its value and `135F` is its hexadecimal address (an assumed number — your computer chooses the real one each time you run the program).

You met the **address-of operator `&`** in Chapter 4: `&a` gives the address of `a`. You can print an address with the `%p` placeholder:

<!--skip-->
```c
#include <stdio.h>

int main(void)
{
    int a = 25;

    printf("value   of a = %d\n", a);
    printf("address of a = %p\n", (void *)&a);
    return 0;
}
```

*Sample output (the address will be different on your machine and may change every run):*
```
value   of a = 25
address of a = 000000000061FE1C
```

---

## 8.2 What is a pointer?

> A **pointer** is a **variable that stores the address of another variable.**

That's all. An ordinary variable holds a *value* (like `25`). A pointer variable holds an *address* (like `135F`) — it **points to** another variable.

**Analogies**

- A pointer is an **address book entry**: it doesn't contain the person, it tells you where to find the person.
- A pointer is a **signpost**: it doesn't *contain* the town, it points the way to it.
- A pointer is a **TV remote**: the remote isn't the TV, but with it you can control the TV from a distance.

**Example from the slide**

```c
int q = 55;
int *m;
m = &q;
```

Assume the address of `q` is `139F` and the address of `m` is `142F`:

```
      name:        q                      m
                ┌──────┐               ┌──────┐
      value:    │  55  │ ◀──────────── │ 139F │      m POINTS TO q
                └──────┘               └──────┘
      address:   139F                    142F
```

- The **value of `q`** is `55`.
- The **value of the pointer `m`** is `139F` — the *address of `q`*.
- The pointer `m` is also a variable in memory, so it has **its own address**, `142F`.

---

## 8.3 Declaring pointers

```c
data_type * pointer_name;
```

The `*` in a declaration means *"this variable is a pointer to"*. Examples (from the slide):

```c
int    * ab;      // ab is a pointer to an int
float  * k;       // k  is a pointer to a float
char   * y;       // y  is a pointer to a char
double * z;       // z  is a pointer to a double
```

Just like any variable, a pointer gets its own space in memory (and, until you give it a value, contains **garbage**):

```
   ab:  [ ? ]    k: [ ? ]    y: [ ? ]    z: [ ? ]
```

> ⚠️ **Watch out:** `int * a, b;` declares `a` as a **pointer** but `b` as an ordinary **`int`**! The `*` belongs to the *name*, not to the type. To declare two pointers write `int *a, *b;`.

> ⚠️ **A pointer that has not been given an address is dangerous.** `int *p; *p = 5;` writes 5 "somewhere" in memory — probably crashing your program. **Always initialise pointers.** If you have no address yet, use **`NULL`**, the special "points to nothing" value:
> ```c
> int *p = NULL;
> if (p != NULL)       /* always check before using a pointer that might be NULL */
>     *p = 5;
> ```

---

## 8.4 Giving a pointer an address

Use the **address-of operator `&`**:

```c
pointer_name = &variable;
```

```c
int q = 55;
int *m;
m = &q;                    /* m now holds the address of q */
```

**The matching-type rule.** The **data type of a pointer must be the same as the type of the variable it points to.** Only an `int *` can hold the address of an `int`; only a `float *` can hold the address of a `float`; and so on.

```c
int   k = 90;
float j = 54.28;

int   *y = &k;      /* OK: int pointer to int      */
float *x = &j;      /* OK: float pointer to float  */
/* int *bad = &j;      WRONG: an int pointer to a float */
```

Why does the type matter? Because the pointer must know **how many bytes to read** at that address, and **how to interpret them** (as an `int`, a `float`, a character…).

### The exception: `void *`

A pointer declared as **`void *`** is a "generic" pointer that can hold the address of **any** type:

```c
int   e = 75;
float b = 98.261;

void *z = &e;       /* OK */
void *h = &b;       /* OK */
```

But a `void *` **cannot be dereferenced** directly (the compiler doesn't know how many bytes to read). You must first **cast** it to the right type: `*(int *)z`.

---

## 8.5 Dereferencing a pointer — reaching the value

Since a pointer holds the address of a variable, it can be used to **access** (read) or **modify** (write) that variable. This is called **dereferencing**, and it uses the **`*` operator** in front of the pointer:

```c
*pointer_name
```

> In a **declaration**, `*` means "pointer to". In an **expression**, `*` means "the thing the pointer points to". Same symbol, two jobs.

With `int x = 49; int *z = &x;` — to dereference `z` is to access the value of `x`. So `*z` **means the same as `x`**, which is currently 49. Whenever we dereference a pointer, we get the variable it points to.

```c
#include <stdio.h>

int main(void)
{
    int x = 49;
    int *z = &x;                  /* z points to x */

    printf("x  = %d\n", x);
    printf("*z = %d\n", *z);      /* reading through the pointer */

    *z = 100;                     /* writing through the pointer */
    printf("x  = %d\n", x);       /* x itself has changed! */

    x = x + 1;
    printf("*z = %d\n", *z);      /* and z sees the change too */
    return 0;
}
```
```output
x  = 49
*z = 49
x  = 100
*z = 101
```

`x` and `*z` are **two names for the same box**.

### A cheat-sheet for `p`, `*p`, `&x`, `&p`

Given `int x = 7; int *p = &x;`:

| Expression | Means | Value here |
|---|---|---|
| `x` | the variable | 7 |
| `&x` | the address of `x` | e.g. `1000` |
| `p` | the pointer's value = the address it holds | same as `&x` |
| `*p` | the variable `p` points to | 7 |
| `&p` | the address of the pointer variable itself | e.g. `2000` |

```c
#include <stdio.h>

int main(void)
{
    int x = 7;
    int *p = &x;

    printf("%d\n", p == &x);       /* p holds the address of x     -> 1 */
    printf("%d\n", *p == x);       /* *p is the same value as x    -> 1 */
    printf("%d\n", &*p == &x);     /* "address of what p points to" is the address of x -> 1 */
    return 0;
}
```
```output
1
1
1
```

### How big is a pointer?

An address needs the same number of bytes whatever it points to, so on everyday computers **all pointers have the same size** (8 bytes on a 64-bit computer, 4 on a 32-bit one). What differs is the size of the thing *pointed to*:

```c
#include <stdio.h>

int main(void)
{
    char c;
    int i;
    double d;
    char *pc = &c;
    int *pi = &i;
    double *pd = &d;

    printf("%zu %zu %zu\n", sizeof(*pc), sizeof(*pi), sizeof(*pd));
    printf("%d\n", sizeof(pc) == sizeof(pi) && sizeof(pi) == sizeof(pd));
    return 0;
}
```
```output
1 4 8
1
```

---

## 8.6 Pointers and arrays — pointer arithmetic

At the end of Chapter 7 you were told that **an array's name is the address of its first element**. Now you can see what that means:

```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;          /* same as  int *p = &a[0];  */
```

```
   a:    ┌────┬────┬────┬────┬────┐
         │ 10 │ 20 │ 30 │ 40 │ 50 │
         └────┴────┴────┴────┴────┘
          a[0] a[1] a[2] a[3] a[4]
           ▲
           p
```

**Pointer arithmetic.** Adding 1 to a pointer moves it **to the next element** (not the next byte). `p + 1` is the address of `a[1]`, `p + 2` is the address of `a[2]` — C multiplies by the element's size for you.

| Array notation | Pointer notation | Meaning |
|---|---|---|
| `a[0]` | `*p` or `*(p + 0)` | first element |
| `a[i]` | `*(p + i)` | the `i`-th element |
| `&a[i]` | `p + i` | address of the `i`-th element |

In fact **`a[i]` is just a short way of writing `*(a + i)`**.

```c
#include <stdio.h>

int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;

    printf("%d %d %d\n", a[2], *(a + 2), p[2]);     /* three ways to get the same element */

    int sum = 0;
    for (p = a; p < a + 5; p++)                     /* walk the pointer along the array */
        sum += *p;
    printf("sum = %d\n", sum);

    int *start = &a[1];
    int *end = &a[4];
    printf("distance = %d\n", (int)(end - start));  /* pointer subtraction counts elements */
    return 0;
}
```
```output
30 30 30
sum = 150
distance = 3
```

> 📝 **Array name vs pointer.** `p` is a variable — you can change it (`p++`). The array name `a` is a *fixed* address — you cannot write `a++` or `a = p`.

**`*p++` versus `(*p)++`** — a classic trap (because `++` binds tighter than `*`... see the precedence table, Chapter 3):

- `*p++` — take the value `p` points to, **then** move `p` to the next element.
- `(*p)++` — **increase the value** that `p` points to; `p` doesn't move.

---

## 8.7 Passing pointers to functions (pass by reference)

C allows you to pass a **pointer** to a function as an argument. Since a pointer holds the address (a *reference*) of a variable, this is called **passing by reference**, in contrast with **passing by value** (Chapter 6).

- **By value:** the function receives a **copy** of the value. Changes inside the function **do not** affect the caller's variable.
- **By reference (via a pointer):** the function receives the **address** of the caller's variable. By dereferencing it the function reads and changes the **original** variable, directly in memory.

> 📝 **Strictly speaking**, C always passes arguments by value. When you pass `&m`, the function gets a *copy of the address*. But a copy of an address still leads to the original variable, so the effect is exactly that of passing by reference. That is why books (and your slides) use the name.

Functions that accept pointers say so in their declaration **and** definition: the parameter is declared with a `*`.

### The famous `swap`

*Without pointers* it cannot work (Ex 6.41). *With pointers:*

```c
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int m = 10, n = 20;

    printf("Before Swapping:\n");
    printf("m = %d\n", m);
    printf("n = %d\n\n", n);

    swap(&m, &n);                      /* pass the ADDRESSES of m and n */

    printf("After Swapping:\n");
    printf("m = %d\n", m);
    printf("n = %d", n);
    return 0;
}

/* pointers 'a' and 'b' hold the addresses of 'm' and 'n' */
void swap(int *a, int *b)
{
    int temp;
    temp = *a;                         /* temp = the value that a points to */
    *a = *b;                           /* the value at a becomes the value at b */
    *b = temp;
}
```
```output
Before Swapping:
m = 10
n = 20

After Swapping:
m = 20
n = 10
```

Picture of what happens during `swap(&m, &n)`:

```
   main:   m [ 10 ] ◀────── a          After the three lines:
           n [ 20 ] ◀────── b          m [ 20 ]   n [ 10 ]
                      (a, b are the pointers inside swap)
```

Here is the slide's **tweaked version that passes by value** — compare the results. *(Question from your slide: "Would you say the two codes produced the same output? If yes why, if no why?")*

```c
#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int m = 10, n = 20;

    printf("Before Swapping:\n");
    printf("m = %d\n", m);
    printf("n = %d\n\n", n);

    swap(m, n);                        /* pass the VALUES */

    printf("After Swapping:\n");
    printf("m = %d\n", m);
    printf("n = %d", n);
    return 0;
}

/* variables 'a' and 'b' hold COPIES of the values of 'm' and 'n' */
void swap(int a, int b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}
```
```output
Before Swapping:
m = 10
n = 20

After Swapping:
m = 10
n = 20
```

**No — the outputs differ.** The by-value `swap` swapped only its own copies, which vanished when the function ended. The by-reference version swapped the originals.

### Comparing the two methods side by side (from your slide)

```c
#include <stdio.h>

void funct1(int u, int v);
void funct2(int *pu, int *pv);

int main(void)
{
    int u = 1;
    int v = 3;

    printf("\nBefore calling funct1: u=%d v=%d", u, v);
    funct1(u, v);
    printf("\nAfter calling funct1: u=%d v=%d", u, v);

    printf("\n\nBefore calling funct2: u=%d v=%d", u, v);
    funct2(&u, &v);
    printf("\nAfter calling funct2: u=%d v=%d", u, v);

    return 0;
}

void funct1(int u, int v)               /* by value */
{
    u = 0;
    v = 0;
    printf("\nWithin funct1: u=%d v=%d", u, v);
    return;
}

void funct2(int *pu, int *pv)           /* by reference */
{
    *pu = 0;
    *pv = 0;
    printf("\nWithin funct2: *pu=%d *pv=%d", *pu, *pv);
    return;
}
```
```output
Before calling funct1: u=1 v=3
Within funct1: u=0 v=0
After calling funct1: u=1 v=3

Before calling funct2: u=1 v=3
Within funct2: *pu=0 *pv=0
After calling funct2: u=0 v=0
```

`funct1` passes by **variable (value)**; `funct2` passes by **reference**. After `funct1` the originals are unchanged; after `funct2` they have become 0.

### Why pointers matter: functions with several results

A function can `return` only **one** value. With pointers it can "send back" as many as you like — by writing into variables of the caller:

```c
#include <stdio.h>

void minmax(int a, int b, int *min, int *max)
{
    if (a < b)
    {
        *min = a;
        *max = b;
    }
    else
    {
        *min = b;
        *max = a;
    }
}

void divide(int a, int b, int *quotient, int *remainder)
{
    *quotient = a / b;
    *remainder = a % b;
}

int main(void)
{
    int lo, hi, q, r;

    minmax(9, 4, &lo, &hi);
    printf("min = %d, max = %d\n", lo, hi);

    divide(17, 5, &q, &r);
    printf("17 / 5 = %d remainder %d\n", q, r);
    return 0;
}
```
```output
min = 4, max = 9
17 / 5 = 3 remainder 2
```

> 💡 **You have been doing this all along!** `scanf("%d", &x)` works exactly like this: you hand `scanf` the **address** of `x` so it can write the number into `x`. Now you know why the `&` is needed.

### Arrays are passed as pointers

In Chapter 7 you saw that a function can change the original array. Now you know why: `void addTen(int arr[], int n)` is really `void addTen(int *arr, int n)`. The function receives the **address of the first element**. Both spellings mean the same.

### Protecting data with `const`

If a function should only **read** through a pointer, declare the parameter `const`: `int sum(const int *a, int n)`. Then any attempt to write `*a = ...` is a compile error — a safety net.

---

## 8.8 Functions returning pointers

A function can also **return a pointer** to the caller. The caller must have a pointer ready to receive it.

```c
#include <stdio.h>

int *larger(int *x, int *y);            /* returns a pointer to an int */

int main(void)
{
    int a = 15;
    int b = 92;
    int *p;

    p = larger(&a, &b);
    printf("%d is larger", *p);
    return 0;
}

int *larger(int *x, int *y)
{
    if (*x > *y)
        return x;
    else
        return y;
}
```
```output
92 is larger
```

`larger` returns the **address of the bigger variable** (here, `b`). We can use it to *change* that variable, too: `*larger(&a, &b) = 0;` would set `b` to 0.

> ⚠️ **The big danger: never return the address of a local variable.**
> ```c
> int *makeFive(void)
> {
>     int x = 5;          /* local: destroyed when the function ends */
>     return &x;          /* WRONG: returns the address of a box that no longer exists */
> }
> ```
> The slide warns: the *local pointer* (and local variables) inside the called function are not recognised outside it. The returned address points to memory that has been freed and may be reused — a **dangling pointer**. Safe things to return: a pointer to a variable that **outlives** the function (a parameter pointing into the caller's data, a `static` or global variable, or memory from `malloc`).

---

## 8.9 Function pointers (assignment from your slides)

It is also possible to have pointers **point to functions**. Every function lives at an address in memory, and the function's **name** (without parentheses) *is* that address.

```c
int (*op)(int, int);        /* op is a pointer to a function that takes (int, int) and returns int */
```

Read it from the inside out: `(*op)` — `op` is a pointer; `(int, int)` — to a function taking two ints; `int` — returning an int. The brackets around `*op` are essential.

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int main(void)
{
    int (*op)(int, int);                 /* pointer to a function */

    op = add;                            /* point it at add */
    printf("%d\n", op(6, 3));            /* call through the pointer */

    op = mul;                            /* now point it at mul */
    printf("%d\n", op(6, 3));

    int (*table[3])(int, int) = {add, sub, mul};     /* an array of function pointers */
    for (int i = 0; i < 3; i++)
        printf("%d ", table[i](10, 2));
    printf("\n");
    return 0;
}
```
```output
9
18
12 8 20
```

Why is this useful? You can **choose behaviour at run time** (a menu that picks a function from a table), or hand a function to another function as a parameter — for example `qsort` takes the comparison function as a parameter (Ex 7.111). These are called **callbacks**.

---

## 8.10 Dynamic memory: `malloc` and `free` (a short peek)

Ordinary variables and arrays are created when their function starts and disappear when it ends, and array sizes must be constants. **Dynamic memory** lets you ask for memory **while the program is running**, in any size, and keep it as long as you need. The functions are in `<stdlib.h>`:

| Function | Job |
|---|---|
| `malloc(bytes)` | reserve that many bytes; returns a pointer to them (or `NULL` if it fails) |
| `free(pointer)` | give the memory back |

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 5;
    int *a = malloc(n * sizeof(int));        /* room for n integers */

    if (a == NULL)
    {
        printf("Out of memory\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
        a[i] = (i + 1) * (i + 1);            /* use it exactly like an array */

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");

    free(a);                                 /* ALWAYS give it back */
    a = NULL;                                /* and don't keep a dangling pointer */
    return 0;
}
```
```output
1 4 9 16 25
```

**Rules:** (1) always check for `NULL`; (2) every `malloc` needs exactly one `free`; (3) never use memory after freeing it; (4) never free the same memory twice. Forgetting `free` is a **memory leak**. (You'll meet `malloc` again when we need `strdup` below.)

---

# PART II — STRINGS

## 8.11 What is a string?

> A **string** in C is a **one-dimensional array of characters that is terminated by the null character `'\0'`**.

C has no special "text" type. A string is just a `char` array whose last meaningful element is the **null character** (the character with code **0**), which marks *"the text ends here"*.

String **literals** are written in double quotes: `"hello world"`, `"Kofi Mensah"`.

```
   "Kumasi" is stored as 7 characters:

     index:    0    1    2    3    4    5    6
             ┌────┬────┬────┬────┬────┬────┬────┐
             │ K  │ u  │ m  │ a  │ s  │ i  │ \0 │
             └────┴────┴────┴────┴────┴────┴────┘
                                            ▲
                          the null terminator (invisible, but essential)
```

- The string has **6 characters** (its **length**) but needs **7 bytes** (its **size**), because of the `'\0'`.
- Every string function (`printf("%s")`, `strlen`, …) walks along the array **until it finds `'\0'`**. Forget the terminator and they run off the end into garbage.

> ⚠️ **`'A'` vs `"A"`:** `'A'` is one character (code 65). `"A"` is a string: two bytes, `'A'` and `'\0'`.

---

## 8.12 Declaring strings

There are two ways (from your slide):

```c
char city[7];        // using an array: room for 6 characters + '\0'
char *city;          // using a pointer: points to characters somewhere
```

The array version **owns** its memory. The pointer version only holds an address, so it must be made to point at something (a literal, an array, or `malloc` memory) before use.

---

## 8.13 Initialising strings

All five of these produce the text `Kumasi` (from your slide):

```c
char city[7] = {'K', 'u', 'm', 'a', 's', 'i', '\0'};   // 1. every character, including '\0'
char city[]  = {'K', 'u', 'm', 'a', 's', 'i', '\0'};   // 2. size worked out by the compiler
char city[7] = "Kumasi";                               // 3. string literal, explicit size
char city[]  = "Kumasi";                               // 4. string literal, size = 7 automatically
char *city   = "Kumasi";                               // 5. pointer to a string literal
```

```c
#include <stdio.h>

int main(void)
{
    char a[7] = {'K', 'u', 'm', 'a', 's', 'i', '\0'};
    char b[]  = {'K', 'u', 'm', 'a', 's', 'i', '\0'};
    char c[7] = "Kumasi";
    char d[]  = "Kumasi";
    char *e   = "Kumasi";

    printf("%s %s %s %s %s\n", a, b, c, d, e);
    printf("%zu %d\n", sizeof(d), sizeof(e) == sizeof(char *));
    return 0;
}
```
```output
Kumasi Kumasi Kumasi Kumasi Kumasi
7 1
```

Form 4 is the one you will use most.

> ⚠️ **Leave room for the `'\0'`!** `char s[6] = "Kumasi";` has no space for the terminator, so `s` is **not a valid string**. Writing `char s[] = "Kumasi";` lets the compiler count for you.

### Array versus pointer — an important difference

- `char d[] = "Kumasi";` makes **your own copy** of the text in a normal array. You **may modify** it (`d[0] = 'k';`).
- `char *e = "Kumasi";` points to the **string literal**, which lives in **read-only memory**. **Modifying it is undefined behaviour** (usually a crash): `e[0] = 'k';` ✘.

If you need to change the text, use an **array**. Use `const char *` for pointers to literals so the compiler protects you: `const char *e = "Kumasi";`.

```c
#include <stdio.h>

int main(void)
{
    char word[] = "hello";

    word[0] = 'J';           /* fine: it's our own array */
    word[4] = '\0';          /* shorten the string: "Jell" */
    printf("%s\n", word);
    return 0;
}
```
```output
Jell
```

Putting `'\0'` in the middle simply makes the string *end* earlier — the characters after it are still in memory, but string functions never look there.

---

## 8.14 Using strings: printing

```c
#include <stdio.h>

int main(void)
{
    char city[7] = {'K', 'u', 'm', 'a', 's', 'i', '\0'};

    printf("We live in %s\n", city);
    return 0;
}
```
```output
We live in Kumasi
```

You can also print with `puts(city)` (adds a newline), or one character at a time:

```c
#include <stdio.h>

int main(void)
{
    char s[] = "Kumasi";

    for (int i = 0; s[i] != '\0'; i++)
        printf("%c(%d) ", s[i], s[i]);
    printf("\n");
    return 0;
}
```
```output
K(75) u(117) m(109) a(97) s(115) i(105)
```

---

## 8.15 Reading strings

You met this in Chapter 4. Quick recap with the slide's two versions:

**Using `scanf` / `printf`** — reads **one word** (stops at whitespace). Note: **no `&`** for a char array:

<!--in: Kofi-->
```c
#include <stdio.h>

int main(void)
{
    char fullname[250];

    printf("enter your full name\n");
    scanf("%s", fullname);               /* the slide writes &fullname — unnecessary for an array */
    printf("%s\n", fullname);
    return 0;
}
```
```output
enter your full name
Kofi
Kofi
```

**Using `gets` / `puts`** — the slide reads a whole line with `gets(fullname)`. **Do not use `gets`** (Chapter 4: it cannot limit how much is typed, so it can overflow the array; it was removed from C in 2011).

> **Question from your slide: *Why is using `gets` risky?*** Because it has **no idea how big the array is**. If the user types more characters than the array holds, `gets` keeps writing past the end — overwriting other variables or the return address — a *buffer overflow*, one of the most exploited bugs in history. **Read on `fgets` and `fputs`** (as the slide says):

<!--in: Kofi Mensah-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char fullname[250];

    printf("enter your full name\n");
    fgets(fullname, sizeof(fullname), stdin);          /* at most 249 characters are stored */
    fullname[strcspn(fullname, "\n")] = '\0';          /* remove the newline fgets keeps */
    puts(fullname);
    return 0;
}
```
```output
enter your full name
Kofi Mensah
Kofi Mensah
```

---

## 8.16 Walking through a string

Because a string ends with `'\0'`, we can loop **until we hit it** — we don't need to know the length in advance. Two equivalent styles:

```c
for (int i = 0; s[i] != '\0'; i++)      /* index style  */
    ...

for (char *p = s; *p != '\0'; p++)      /* pointer style (and  *p != '\0'  can be written just  *p) */
    ...
```

**Example — write your own `strlen`:**

```c
#include <stdio.h>

int myStrlen(const char *s)
{
    int count = 0;
    while (s[count] != '\0')
        count++;
    return count;
}

int main(void)
{
    printf("%d\n", myStrlen("Kumasi"));
    printf("%d\n", myStrlen(""));
    return 0;
}
```
```output
6
0
```

**Example — convert to uppercase, count vowels, reverse:**

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[] = "Hello Kumasi";

    /* count vowels */
    int vowels = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            vowels++;
    }
    printf("vowels: %d\n", vowels);

    /* uppercase every letter */
    for (int i = 0; s[i] != '\0'; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = s[i] - 32;
    printf("%s\n", s);

    /* reverse in place */
    int n = (int) strlen(s);
    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
    printf("%s\n", s);
    return 0;
}
```
```output
vowels: 5
HELLO KUMASI
ISAMUK OLLEH
```

---

## 8.17 The string library `<string.h>`

Library functions for manipulating strings are stored in the **`string.h`** header file. Add `#include <string.h>` to use them.

| Function | Job |
|---|---|
| `strlen(s)` | length of `s` (not counting `'\0'`) |
| `strcpy(dest, src)` | copy `src` into `dest` |
| `strncpy(dest, src, n)` | copy at most `n` characters |
| `strcat(dest, src)` | append `src` to the end of `dest` |
| `strncat(dest, src, n)` | append at most `n` characters |
| `strcmp(a, b)` | compare two strings |
| `strncmp(a, b, n)` | compare at most `n` characters |
| `strchr(s, c)` | pointer to the first `c` in `s` |
| `strrchr(s, c)` | pointer to the **last** `c` in `s` |
| `strstr(s, sub)` | pointer to the first occurrence of `sub` in `s` |
| `strdup(s)` | make a **new copy** of `s` in freshly allocated memory |

> ⚠️ **The golden safety rule:** `strcpy`, `strcat` and friends **never check that the destination is big enough**. *You* must make sure the destination array has room for the result **and** the `'\0'`.

### `strcat` — concatenating strings

`strcat(mainString, stringToAdd)` appends `stringToAdd` to the end of `mainString`.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello";
    char stringToAdd[250] = "world!!!";

    printf("\nmainString = %s", mainString);
    printf("\nstringToAdd = %s", stringToAdd);

    strcat(mainString, stringToAdd);
    printf("\nmainString string after strcat( ) = %s", mainString);
    return 0;
}
```
```output
mainString = hello
stringToAdd = world!!!
mainString string after strcat( ) = helloworld!!!
```

### `strncat` — appending a portion

`strncat(mainString, stringToAdd, size)` appends at most `size` characters:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello";
    char stringToAdd[250] = "world!!!";

    printf("\nmainString = %s", mainString);
    printf("\nstringToAdd = %s", stringToAdd);

    strncat(mainString, stringToAdd, 5);
    printf("\nmainString string after strncat( ) = %s", mainString);
    return 0;
}
```
```output
mainString = hello
stringToAdd = world!!!
mainString string after strncat( ) = helloworld
```

### `strcpy` — copying strings

`strcpy(mainString, stringToReplace)` copies the contents of `stringToReplace` into `mainString` (replacing what was there). **You cannot write `mainString = stringToReplace`** — arrays can't be assigned.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello";
    char stringToReplace[250] = "world!!!";

    printf("\nmainString = %s", mainString);
    printf("\nstringToReplace = %s", stringToReplace);

    strcpy(mainString, stringToReplace);
    printf("\nmainString string after strcpy( ) = %s", mainString);
    return 0;
}
```
```output
mainString = hello
stringToReplace = world!!!
mainString string after strcpy( ) = world!!!
```

### `strlen` — the length

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello";

    int len = strlen(mainString);
    printf("\nlength of mainString = %d", len);
    return 0;
}
```
```output
length of mainString = 5
```

> 💡 **`strlen` vs `sizeof`:** `strlen("hello")` is **5** (characters before the `'\0'`); for `char s[250] = "hello"`, `sizeof(s)` is **250** (the whole array). Different questions, different answers.

### `strcmp` — comparing strings

You **cannot** compare strings with `==` (that compares addresses). `strcmp(str1, str2)` compares them **character by character** (alphabetically, using ASCII codes) and returns:

- **0** if they are **equal**;
- a **negative** number if `str1 < str2`;
- a **positive** number if `str1 > str2`.

It is **case sensitive** (`'a' != 'A'`).

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str1[] = "hello";
    char str2[] = "hell";
    int a, b, c, d;

    a = strcmp(str1, "hello");          /* identical                       */
    b = strcmp(str1, str2);             /* "hello" is longer than "hell"   */
    c = strcmp(str1, "hello world");    /* "hello" is shorter              */
    d = strcmp(str1, "Hello");          /* 'h' (104) comes after 'H' (72)  */

    /* only the SIGN of the result is guaranteed, so we print just the sign: -1, 0 or 1 */
    printf("%d %d %d %d\n", (a > 0) - (a < 0), (b > 0) - (b < 0), (c > 0) - (c < 0), (d > 0) - (d < 0));
    return 0;
}
```
```output
0 1 -1 1
```

> 📝 **Note on the slide.** Your slide prints `0 111 -32 32`. That is what *some* compilers return: the **difference** between the first two characters that differ (`'o'` − `'\0'` = 111, `'\0'` − `' '` = −32, `'h'` − `'H'` = 32). Other compilers return just `-1`, `0` or `1`. The C standard promises only the **sign**, so **always compare the result with `0`**: `if (strcmp(a, b) == 0) …equal…`, `if (strcmp(a, b) < 0) …a comes first…`.

### `strchr` — searching for a character

`strchr(mainString, 'o')` returns a **pointer** to the first `'o'` in `mainString` (or `NULL` if there is none). Subtracting the start of the string from that pointer gives the **index**. (Read on `strrchr`, which finds the **last** occurrence.)

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello world, I can program now";
    char *ptr;

    ptr = strchr(mainString, 'o');
    int p = ptr - mainString + 1;                       /* +1 gives a position starting at 1 */

    printf("Character o is found at position %d\n", p);
    printf("First occurrence of character \"o\" in \"%s\" is \"%s\"", mainString, ptr);
    return 0;
}
```
```output
Character o is found at position 5
First occurrence of character "o" in "hello world, I can program now" is "o world, I can program now"
```

Notice that `ptr` points **into** `mainString`, so printing `ptr` with `%s` prints the rest of the text from that point.

### `strstr` — searching for a substring

`strstr(mainString, "ello")` returns a pointer to the first occurrence of `"ello"`, or `NULL`:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char mainString[250] = "hello world, the sun is yellow, my heart is mellow";
    char *ptr;

    ptr = strstr(mainString, "ello");
    if (ptr)
    {
        printf("string found\n");
        printf("First occurrence of string \"ello\" in \"%s\" is \"%s\"", mainString, ptr);
    }
    else
        printf("string not found\n");
    return 0;
}
```
```output
string found
First occurrence of string "ello" in "hello world, the sun is yellow, my heart is mellow" is "ello world, the sun is yellow, my heart is mellow"
```

(Note: in a condition, a pointer counts as *true* if it is not `NULL`, so `if (ptr)` means "if found".) The slide's text shows `strstr(mainString,'ello')` with single quotes — that is a typo; the second argument must be a **string** in double quotes.

### `strdup` — duplicating a string

`str2 = strdup(str1)` allocates new memory, copies `str1` into it and returns a pointer to the copy. Because the memory comes from `malloc`, **you must `free` it** when finished.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *str1 = "copy me";
    char *str2;

    str2 = strdup(str1);
    printf("Duplicated string is : %s", str2);

    free(str2);                                   /* the slide forgets this step */
    return 0;
}
```
```output
Duplicated string is : copy me
```

> 📝 `strdup` is a POSIX function (standard C only from C23). Some compilers spell it `_strdup` and give a *warning* about the plain name; it still works.

### Safe use — `strncpy`, `snprintf`

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char small[8];
    char title[40];

    strncpy(small, "Kumasi Central Market", sizeof(small) - 1);   /* copy at most 7 characters */
    small[sizeof(small) - 1] = '\0';                              /* strncpy may NOT add '\0' */
    printf("%s\n", small);

    snprintf(title, sizeof(title), "Dr. %s %s", "Ama", "Mensah");  /* printf into a string, size-limited */
    printf("%s\n", title);
    return 0;
}
```
```output
Kumasi 
Dr. Ama Mensah
```

(`strncpy` copies *at most* `n` characters and, if the source is longer, does **not** add a `'\0'` — so we add it ourselves.)

---

## 8.18 Writing your own string functions

Writing the library functions yourself is the best way to see how strings really work.

```c
#include <stdio.h>

void myStrcpy(char *dest, const char *src)
{
    while (*src != '\0')
    {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';                      /* don't forget the terminator! */
}

int myStrcmp(const char *a, const char *b)
{
    while (*a != '\0' && *a == *b)
    {
        a++;
        b++;
    }
    return (unsigned char)*a - (unsigned char)*b;
}

int main(void)
{
    char copy[20];

    myStrcpy(copy, "Accra");
    printf("%s\n", copy);

    int r = myStrcmp("apple", "apricot");
    printf("%s\n", (r < 0) ? "apple comes first" : "apricot comes first");
    return 0;
}
```
```output
Accra
apple comes first
```

The famous C one-liner for copying is `while ((*dest++ = *src++)) ;` — it copies each character *and* stops after copying the `'\0'`. Don't worry if it looks cryptic; understand the long version first.

---

## 8.19 Arrays of strings

A **2D array of `char`** holds several strings, one per row:

```c
char names[3][20] = {"Kofi", "Ama", "Kwame"};
```

```
            col: 0   1   2   3   4   5 ...
   names[0]:     K   o   f   i   \0  ...
   names[1]:     A   m   a   \0  ...
   names[2]:     K   w   a   m   e   \0 ...
```

`names[i]` is the `i`-th string (so `printf("%s", names[i])`). Every row has the same size, 20 bytes.

**Sorting names alphabetically** — compare with `strcmp`, swap with `strcpy` (arrays can't be assigned):

```c
#include <stdio.h>
#include <string.h>

#define COUNT 5
#define LEN 20

int main(void)
{
    char names[COUNT][LEN] = {"Kwame", "Ama", "Yaw", "Abena", "Kofi"};

    for (int pass = 0; pass < COUNT - 1; pass++)
        for (int j = 0; j < COUNT - 1 - pass; j++)
            if (strcmp(names[j], names[j + 1]) > 0)
            {
                char temp[LEN];
                strcpy(temp, names[j]);
                strcpy(names[j], names[j + 1]);
                strcpy(names[j + 1], temp);
            }

    for (int i = 0; i < COUNT; i++)
        printf("%s\n", names[i]);
    return 0;
}
```
```output
Abena
Ama
Kofi
Kwame
Yaw
```

It is the **bubble sort** from Chapter 7 — only the comparison and the swap changed.

---

## 8.20 Common mistakes — checklist

| Mistake | What goes wrong | Fix |
|---|---|---|
| Using a pointer before giving it an address | writes to a random place → crash | initialise: `= &x`, `= NULL`, or `malloc` |
| `*p` on a `NULL` pointer | crash | check `p != NULL` |
| `int *a, b;` | `b` is not a pointer | `int *a, *b;` |
| Returning `&local` | dangling pointer | return a parameter pointer / `static` / heap memory |
| Pointer type ≠ variable type | wrong bytes read | match the types |
| `s1 == s2` to compare strings | compares addresses | `strcmp(s1, s2) == 0` |
| `dest = src;` for char arrays | doesn't compile / only copies an address | `strcpy` |
| Array too small (`char s[5] = "Hello"`) | no room for `'\0'` | `char s[] = "Hello"` |
| `strcpy` into a too-small array | buffer overflow | make the destination big enough, or use `snprintf` |
| Modifying a string literal via `char *p = "abc"; p[0]='X';` | crash | use `char p[] = "abc";` |
| `scanf("%s", &name)` | unnecessary `&` | `scanf("%s", name)` |
| Using `gets` | overflow | `fgets` |
| Forgetting `free` / using memory after `free` | leak / crash | one `free` per `malloc`, then set to `NULL` |

---

## Key takeaways

**Pointers**
- A **pointer** stores the **address** of another variable. Declare with `type *name;`.
- `&x` = address of `x`. `*p` = the value `p` points to (dereference). `*p = 5;` changes the original.
- A pointer's type must match what it points to (`void *` is the exception). Use `NULL` for "points to nothing".
- `p + 1` moves to the next **element**; `a[i]` is `*(a + i)`.
- **Pass by reference:** pass `&x`, take `int *p`, use `*p` — the function can change the original and return several results. **Pass by value** passes copies.
- A function may return a pointer, but **never to a local variable**.
- Function pointers: `int (*f)(int, int);`. Dynamic memory: `malloc` / `free`.

**Strings**
- A **string** = `char` array ending with `'\0'`. Size = length + 1.
- Declare: `char s[] = "text";` (modifiable) or `char *s = "text";` (read-only literal).
- Read with `scanf("%s", s)` (one word, no `&`) or `fgets(s, size, stdin)`; print with `%s` / `puts`. **Never `gets`.**
- `<string.h>`: `strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`, `strstr`, `strdup`. Compare with `strcmp`, **never `==`**. Check the **destination size**.

---

# Exercises — Chapter 8

## Part A — Quick check

**Ex 8.1** What is a pointer? How is it different from an ordinary variable?

**Ex 8.2** What do the operators `&` and `*` do when applied to a variable and to a pointer?

**Ex 8.3** Declare: (a) a pointer `pa` to an `int`; (b) a pointer `pd` to a `double`; (c) a pointer `pc` to a `char`.

**Ex 8.4** In `int *a, b;` what is the type of `a` and what is the type of `b`?

**Ex 8.5** What is `NULL`? Why should you check a pointer against it?

**Ex 8.6** What is the rule about the data type of a pointer and the variable it points to? What is the one exception, and what can't you do with that exception?

**Ex 8.7** Given `int x = 5; int *p = &x;` — what are the meanings of `p`, `*p`, `&p` and `&x`?

**Ex 8.8** What is the difference between passing by value and passing by reference? Which one lets a function change the caller's variable?

**Ex 8.9** Why is it a mistake to return the address of a local variable from a function?

**Ex 8.10** If `p` points to `a[0]` in `int a[10]`, what do `p + 3`, `*(p + 3)` and `a[3]` mean?

**Ex 8.11** What is a string in C? What is the null character, and what is its code?

**Ex 8.12** What is the difference between `'A'` and `"A"`? How many bytes does each occupy?

**Ex 8.13** How many bytes does `char s[] = "Ghana";` occupy? What does `strlen(s)` return?

**Ex 8.14** Why can't you compare two strings with `==`? Which function do you use? What does it return when the strings are equal?

**Ex 8.15** Why is `gets` dangerous? What should you use instead?

**Ex 8.16** True or false?
1. A pointer variable has its own address.
2. `*p` and `&p` mean the same thing.
3. All pointers occupy the same number of bytes on one machine.
4. `char *s = "abc"; s[0] = 'X';` is perfectly safe.
5. `strcpy` checks that the destination is big enough.
6. A string must end with `'\0'`.

## Part B — Predict the output

*(Assume `<stdio.h>` and `<string.h>` are included and the code is inside `main`. Draw boxes and arrows!)*

**Ex 8.17**
```c
int x = 10;
int *p = &x;
*p = 25;
printf("%d\n", x);
```

**Ex 8.18**
```c
int a = 5, b = 8;
int *p = &a;
int *q = &b;
*p = *q;
printf("%d %d\n", a, b);
```

**Ex 8.19**
```c
int a = 5, b = 8;
int *p = &a;
int *q = &b;
p = q;
*p = 100;
printf("%d %d\n", a, b);
```

**Ex 8.20**
```c
int x = 7;
int *p = &x;
printf("%d %d %d\n", x, *p, p == &x);
```

**Ex 8.21**
```c
int a[3] = {10, 20, 30};
int *p = a;
printf("%d ", *p++);
printf("%d ", *p);
printf("%d\n", ++*p);
```

**Ex 8.22**
```c
int a[5] = {1, 2, 3, 4, 5};
int *p = a + 1;
printf("%d %d %d\n", *p, *(p + 2), p[1]);
```

**Ex 8.23**
```c
int a[6] = {0};
int *p = &a[1];
int *q = &a[5];
printf("%d\n", (int)(q - p));
```

**Ex 8.24**
```c
int a[5] = {2, 4, 6, 8, 10};
int sum = 0;
for (int *p = a; p < a + 5; p++)
    sum += *p;
printf("%d\n", sum);
```

**Ex 8.25**
```c
#include <stdio.h>
void inc(int *n)
{
    (*n)++;
}
int main(void)
{
    int x = 5;
    inc(&x);
    inc(&x);
    printf("%d\n", x);
    return 0;
}
```

**Ex 8.26** *(from your slides — identify which function passes by value and which by reference)*
```c
#include <stdio.h>
void funct1(int u, int v);
void funct2(int *pu, int *pv);
int main(void)
{
    int u = 1;
    int v = 3;
    printf("\nBefore calling funct1: u=%d v=%d", u, v);
    funct1(u, v);
    printf("\nAfter calling funct1: u=%d v=%d", u, v);
    printf("\n\nBefore calling funct2: u=%d v=%d", u, v);
    funct2(&u, &v);
    printf("\nAfter calling funct2: u=%d v=%d", u, v);
    return 0;
}
void funct1(int u, int v)
{
    u = 0;
    v = 0;
    printf("\nWithin funct1: u=%d v=%d", u, v);
}
void funct2(int *pu, int *pv)
{
    *pu = 0;
    *pv = 0;
    printf("\nWithin funct2: *pu=%d *pv=%d", *pu, *pv);
}
```

**Ex 8.27**
```c
#include <stdio.h>
void minmax(int a, int b, int *min, int *max)
{
    if (a < b) { *min = a; *max = b; }
    else       { *min = b; *max = a; }
}
int main(void)
{
    int lo, hi;
    minmax(9, 4, &lo, &hi);
    printf("%d %d\n", lo, hi);
    return 0;
}
```

**Ex 8.28**
```c
#include <stdio.h>
int *larger(int *x, int *y)
{
    return (*x > *y) ? x : y;
}
int main(void)
{
    int a = 15, b = 92;
    int *p = larger(&a, &b);
    *p = 0;
    printf("%d %d\n", a, b);
    return 0;
}
```

**Ex 8.29**
```c
char c;
int i;
double d;
char *pc = &c;
int *pi = &i;
double *pd = &d;
printf("%zu %zu %zu %d\n", sizeof(*pc), sizeof(*pi), sizeof(*pd), sizeof(pc) == sizeof(pd));
```

**Ex 8.30**
```c
char s[] = "Kumasi";
printf("%zu %zu\n", strlen(s), sizeof(s));
```

**Ex 8.31**
```c
char s[10] = "Hi";
printf("%zu %zu %d\n", strlen(s), sizeof(s), s[2]);
```

**Ex 8.32**
```c
char s[] = {'A', 'B', 'C', '\0', 'D', 'E', '\0'};
printf("%s %zu\n", s, strlen(s));
```

**Ex 8.33**
```c
char s[] = "hello";
s[0] = 'J';
s[4] = '\0';
printf("%s\n", s);
```

**Ex 8.34**
```c
char a[20] = "good";
char b[] = "morning";
strcat(a, " ");
strcat(a, b);
printf("%s %zu\n", a, strlen(a));
```

**Ex 8.35**
```c
char dest[10];
strcpy(dest, "Accra");
dest[2] = '\0';
printf("%s %zu\n", dest, strlen(dest));
```

**Ex 8.36**
```c
printf("%d %d %d\n", strcmp("abc", "abc") == 0, strcmp("abc", "abd") < 0, strcmp("b", "a") > 0);
```

**Ex 8.37**
```c
char s[] = "Programming";
int count = 0;
for (int i = 0; s[i] != '\0'; i++)
    if (s[i] == 'm')
        count++;
printf("%d\n", count);
```

**Ex 8.38**
```c
char s[] = "abc";
char *p = s;
while (*p)
{
    printf("%c-", *p);
    p++;
}
printf("\n");
```

**Ex 8.39**
```c
char s[] = "hello world";
char *p = strchr(s, 'o');
char *q = strstr(s, "wor");
printf("%d %d %s\n", (int)(p - s), (int)(q - s), q);
```

**Ex 8.40**
```c
char names[3][8] = {"Kofi", "Ama", "Yaw"};
printf("%s %c %zu\n", names[1], names[2][0], strlen(names[0]));
```

## Part C — Find and fix the bugs

**Ex 8.41** The program crashes. Why? Fix it.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    int *p;
    *p = 5;
    printf("%d\n", *p);
    return 0;
}
```

**Ex 8.42** What is wrong with the types?
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    float f = 2.5f;
    int *p = &f;
    printf("%f\n", *p);
    return 0;
}
```

**Ex 8.43** The programmer wants to change `x` to 10 through `p`. Fix the mistake.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    int x = 3;
    int *p = &x;
    p = 10;
    printf("%d\n", x);
    return 0;
}
```

**Ex 8.44** Why does this not compile? Fix it.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    int x = 1, y = 2;
    int *a, b;
    a = &x;
    b = &y;
    return 0;
}
```

**Ex 8.45** The values are not swapped. Rewrite `swap` so that it works.
```c
#include <stdio.h>
void swap(int a, int b)
{
    int t = a;
    a = b;
    b = t;
}
int main(void)
{
    int x = 4, y = 9;
    swap(x, y);
    printf("%d %d\n", x, y);
    return 0;
}
```

**Ex 8.46** What is wrong with returning `&x`?
<!--skip-->
```c
#include <stdio.h>
int *makeFive(void)
{
    int x = 5;
    return &x;
}
int main(void)
{
    int *p = makeFive();
    printf("%d\n", *p);
    return 0;
}
```

**Ex 8.47** The output has garbage at the end. Why?
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    char s[5] = "Hello";
    printf("%s\n", s);
    return 0;
}
```

**Ex 8.48** The program never prints "match", even though the user types `yes`. Fix it.
```c
#include <stdio.h>
int main(void)
{
    char answer[10];
    scanf("%9s", answer);
    if (answer == "yes")
        printf("match\n");
    else
        printf("no match\n");
    return 0;
}
```

**Ex 8.49** This does not compile. Fix it.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    char name[20];
    name = "Kofi";
    printf("%s\n", name);
    return 0;
}
```

**Ex 8.50** The program crashes on most systems. Why? Fix it.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    char *s = "hello";
    s[0] = 'J';
    printf("%s\n", s);
    return 0;
}
```

**Ex 8.51** Find the (small) mistake in reading the name, taken from your slides.
```c
#include <stdio.h>
int main(void)
{
    char fullname[250];
    printf("enter your full name\n");
    scanf("%s", &fullname);
    printf("%s\n", fullname);
    return 0;
}
```

**Ex 8.52** Rewrite this program (from your slides) without the dangerous function.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    char fullname[250];
    printf("enter your full name\n");
    gets(fullname);
    puts(fullname);
    return 0;
}
```

**Ex 8.53** This may crash or corrupt memory. Why? Give two fixes.
<!--skip-->
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char small[5];
    strcpy(small, "Kumasi");
    printf("%s\n", small);
    return 0;
}
```

**Ex 8.54** The program prints strange extra characters. Why?
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    char s[4];
    s[0] = 'a';
    s[1] = 'b';
    s[2] = 'c';
    printf("%s\n", s);
    return 0;
}
```

**Ex 8.55** There is a serious mistake involving `copy`. Find it. Then say what would happen if the line `free(copy);` were removed completely.
<!--skip-->
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    char *copy = strdup("Kumasi");
    printf("%s\n", copy);
    free(copy);
    printf("%s\n", copy);
    return 0;
}
```

**Ex 8.56** `strcat` produces junk. Fix it.
<!--skip-->
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char dest[20];
    strcat(dest, "Hi ");
    strcat(dest, "there");
    printf("%s\n", dest);
    return 0;
}
```

## Part D1 — Write the program: pointers

**Ex 8.57** Declare an `int`, a `double` and a `char` variable together with a pointer to each. Print the three values **through the pointers**, then change each value through its pointer and print the variables.

**Ex 8.58** Print the **address** of a variable with `%p`, and show that the value stored in a pointer to it equals `&variable` (print the result of a comparison).

**Ex 8.59** Write `void swap(int *a, int *b)` and use it to swap two integers read from the user.

**Ex 8.60** Write `void minmax(int a, int b, int *min, int *max)`. Use it to print the smaller and the larger of two numbers read from the user.

**Ex 8.61** Write `void divide(int a, int b, int *quotient, int *remainder)` and use it to print `a / b` and `a % b`.

**Ex 8.62** Write `void increment(int *n)` and `void doubleIt(double *x)`. Call each several times and show the effect.

**Ex 8.63** Compute the **sum** of an array using a **pointer** that walks from the first to the last element (no `[ ]`).

**Ex 8.64** **Reverse** an array using two pointers — one at the start and one at the end, moving towards each other.

**Ex 8.65** Write `int *findMax(int *a, int n)` that returns a **pointer to the largest element**. In `main`, print the maximum value and its index (use pointer subtraction).

**Ex 8.66** Swap the **largest** and **smallest** elements of an array using pointers.

**Ex 8.67** **Copy** one array into another using pointers: `*dst++ = *src++`.

**Ex 8.68** Print an array in three ways: `a[i]`, `*(a + i)` and `p[i]` (where `p` points to `a[0]`).

**Ex 8.69** Write `void stats(const int *a, int n, double *mean, int *max, int *min)` that returns **three results** through pointers.

**Ex 8.70** Write `int *findValue(int *a, int n, int key)` that returns a pointer to the first element equal to `key` — or `NULL`. Use it to search an array, and print the index or `not found`.

**Ex 8.71** Write `int countAbove(const int *a, int n, int threshold)` and use it for an array of marks.

**Ex 8.72** Write `void swapDouble(double *a, double *b)` and `void swapChar(char *a, char *b)` and test both.

**Ex 8.73** Write `void rotate3(int *a, int *b, int *c)` that moves the value of `a` to `b`, of `b` to `c` and of `c` to `a`.

**Ex 8.74** Using the pointer-returning `larger` function from the lesson, **double the larger** of two variables without an `if` in `main`.

**Ex 8.75** Allocate an array of `n` integers **dynamically** (`malloc`), fill it with the squares `1, 4, 9, …`, print it and `free` it.

**Ex 8.76** Read `n`, allocate an array of `n` doubles dynamically, read the numbers, print their **average**, and `free` the memory. Check for `NULL`.

**Ex 8.77** Write `int apply(int (*f)(int, int), int a, int b)` and use it with `add`, `subtract` and `multiply`. Then build a tiny calculator that picks the function from an **array of function pointers**.

**Ex 8.78** Sort an array in ascending **or** descending order, where the **comparison function** (`int ascending(int, int)` or `int descending(int, int)`) is passed to the sort function as a function pointer.

**Ex 8.79** Print a 2 × 3 matrix using pointer notation: `*(*(m + i) + j)`.

**Ex 8.80** Write `void normalizeTime(int *hours, int *minutes)` that turns `(2, 75)` into `(3, 15)` and `(1, -10)` into `(0, 50)`.

**Ex 8.81** Write `void fillRange(int *a, int n, int start)` that fills an array with `start, start+1, …` and `void scale(int *a, int n, int factor)` that multiplies every element. Use them together.

**Ex 8.82** Write `void swapArrays(int *a, int *b, int n)` that swaps the contents of two arrays, element by element.

## Part D2 — Write the program: strings

**Ex 8.83** Print the characters of a string **one per line** with their **ASCII codes**.

**Ex 8.84** Write `int myStrlen(const char *s)` and compare its result with `strlen`.

**Ex 8.85** Read a line and count its **vowels, consonants, digits and spaces**.

**Ex 8.86** Convert a string to **uppercase**, to **lowercase**, and **toggle** the case of each letter.

**Ex 8.87** **Reverse** a string in place.

**Ex 8.88** Check whether a string is a **palindrome**, ignoring case (e.g. `Level`, `Madam`).

**Ex 8.89** Write `void myStrcpy(char *dest, const char *src)` without using `strcpy`.

**Ex 8.90** Write `void myStrcat(char *dest, const char *src)` without using `strcat`.

**Ex 8.91** Write `int myStrcmp(const char *a, const char *b)` without using `strcmp` and test it on several pairs.

**Ex 8.92** Read a **full name** (with spaces) using `fgets`. Print its **initials** (`Kofi Mensah Boateng` → `K.M.B.`).

**Ex 8.93** Capitalise the **first letter of every word** in a sentence (`the quick brown fox` → `The Quick Brown Fox`).

**Ex 8.94** Count the **words** in a sentence.

**Ex 8.95** Find and print the **longest word** in a sentence.

**Ex 8.96** Count how many times a given character occurs in a string, and print **every position** (use `strchr` in a loop).

**Ex 8.97** **Replace** every occurrence of one character by another.

**Ex 8.98** Remove all **spaces** from a string.

**Ex 8.99** Remove all **vowels** from a string.

**Ex 8.100** Count the **frequency of every letter** (case-insensitive) in a string using a counting array of 26 integers.

**Ex 8.101** Check whether two strings are **anagrams** (same letters, different order — e.g. `listen` and `silent`).

**Ex 8.102** Write `int myAtoi(const char *s)` that converts a string of digits like `"4096"` to the integer 4096, and `void myItoa(int n, char *s)` that does the reverse.

**Ex 8.103** Implement a **Caesar cipher**: shift every letter by `k` positions (keeping case, leaving other characters alone). Encrypt and then decrypt a message.

**Ex 8.104** A password is **strong** if it has at least 8 characters, an uppercase letter, a lowercase letter, a digit and a symbol. Write a program that checks a password and reports what is missing.

**Ex 8.105** Count how many times a **substring** (e.g. `"ab"`) appears in a text, using `strstr` in a loop.

**Ex 8.106** Using `strrchr`, print the **extension** of a file name (`report.final.pdf` → `pdf`). Using `strchr`, print the part of an e-mail address before the `@`.

**Ex 8.107** **Sort** five names alphabetically (as in the lesson) and print them. Then print the names in **reverse** alphabetical order.

**Ex 8.108** Find the **longest** and the **shortest** string in an array of names.

**Ex 8.109** Use `snprintf` to build the text `"Item 7: GHS 12.50"` and `"Dr. Ama Mensah"` in character arrays, safely.

**Ex 8.110** A date is stored as the string `"12/11/2026"`. Extract the day, month and year as integers (with `sscanf`) and check that the date is valid (month 1–12, day valid for that month).

**Ex 8.111** Convert a **binary string** like `"101101"` to its decimal value, and a decimal number to a binary **string**.

**Ex 8.112** **Run-length encoding:** compress `"aaabccdddd"` into `"a3b1c2d4"`.

**Ex 8.113** Remove the **duplicate characters** from a string, keeping the first occurrence (`programming` → `progamin`).

**Ex 8.114** **Reverse the order of the words** in a sentence (`I love C` → `C love I`).

**Ex 8.115** An e-mail address is *minimally valid* if it has exactly one `@` and at least one `.` after the `@`. Write `int validEmail(const char *s)` and test it.

**Ex 8.116** Store the **names** and **marks** of five students in parallel arrays (a 2D `char` array and an `int` array). Sort them by marks, highest first, and print a **ranking table**.

## Part E — Challenges and mini-projects

**Ex 8.117 (Pig Latin)** Translate a word to Pig Latin: if it starts with a consonant, move the first letter to the end and add `ay` (`banana` → `ananabay`); if it starts with a vowel, add `way` (`apple` → `appleway`).

**Ex 8.118 (Roman numerals)** Write `void toRoman(int n, char *out)` for `1 ≤ n ≤ 3999`, and `int fromRoman(const char *s)`.

**Ex 8.119 (common prefix)** Find the **longest common prefix** of an array of strings (`flower`, `flow`, `flight` → `fl`).

**Ex 8.120 (brackets)** Check that the brackets in a string such as `{[()]}` are **balanced**, using a character array as a **stack** (push on an opening bracket, pop and match on a closing one).

**Ex 8.121 (CSV)** Split the line `"Kofi,21,3.5"` at the commas into a name, an age and a GPA (manually, or with `strtok` — research it).

**Ex 8.122 (number to words)** Convert 0–999 into English words (`345` → `three hundred and forty-five`).

**Ex 8.123 (hangman)** A hangman game with a fixed secret word. Show the word with `_` for unguessed letters, read letter guesses, and allow 6 wrong guesses.

**Ex 8.124 (contact book)** A menu-driven program that stores up to 10 names and phone numbers (arrays of strings) and lets you **add**, **search by name** and **list** them.

**Ex 8.125 (rotation)** Check whether string `b` is a **rotation** of string `a` (`"erbottlewat"` is a rotation of `"waterbottle"`). *(Hint: `b` must appear inside `a` joined to itself.)*

**Ex 8.126 (text statistics)** Read a paragraph (several lines until an empty line) and report the number of **characters, words and sentences** and the **average word length**.

## Part F — Research tasks

**Ex 8.127** List three differences between an **array** and a **pointer** (consider `sizeof`, assignment and `++`).

**Ex 8.128** What is the difference between `const char *p`, `char *const p` and `const char *const p`?

**Ex 8.129** Why does `strncpy` not always put a `'\0'` at the end? How do you use it safely?

**Ex 8.130** What do `memcpy` and `memset` do? Use `memset` to fill an array with zeros and `memcpy` to copy an array.

**Ex 8.131** Explain the difference between `NULL`, `'\0'` and `0`. Where is each one used?

---

*End of Chapter 8 — and of the lessons. Next: [Chapter 9 — Projects and Final Exam](09-projects-and-final-exam.md)*
