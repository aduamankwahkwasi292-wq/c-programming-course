# Solutions — Chapter 8: Pointers and Strings

> Back to the lesson: [Chapter 8 lesson](../lessons/08-pointers-and-strings.md)
>
> **Study tip for pointer problems:** before reading a solution, *draw* the boxes (variables) and arrows (pointers). Almost every pointer mistake is visible in the drawing.

---

## Part A — Quick check

**Ex 8.1** A **pointer** is a variable that stores the **address** of another variable. An ordinary variable stores a *value* directly; a pointer stores *where* a value lives.

**Ex 8.2** `&x` gives the **address of** the variable `x`. `*p` (applied to a pointer) **dereferences** it: it means "the variable that `p` points to", which you can read or assign to. (In a declaration, `*` means "pointer to", as in `int *p;`.)

**Ex 8.3**
```c
int    *pa;
double *pd;
char   *pc;
```

**Ex 8.4** `a` is a **pointer to int** (`int *`); `b` is a plain **`int`**. (The `*` belongs to `a` only; write `int *a, *b;` for two pointers.)

**Ex 8.5** `NULL` is a special pointer value meaning "points to nothing". Checking against it prevents dereferencing a pointer that has no valid target (which would crash the program). Functions such as `malloc`, `strchr` and `strstr` return `NULL` to say "failed / not found".

**Ex 8.6** The pointer's type must be the **same as the type of the variable** it points to (`int *` ↔ `int`, `float *` ↔ `float`). The exception is **`void *`**, which can hold the address of any type — but it **cannot be dereferenced** directly (the compiler doesn't know how many bytes to read); you must cast it first.

**Ex 8.7**
- `p` — the pointer's value: the **address** it holds (the address of `x`).
- `*p` — the **value of `x`** (5), reached through the pointer.
- `&p` — the **address of the pointer variable itself**.
- `&x` — the **address of `x`** (equal to `p`).

**Ex 8.8** **By value:** the function receives a *copy* of the argument; changes don't affect the caller. **By reference:** the function receives the *address* of the caller's variable (a pointer) and can read/change the original. Passing by reference lets a function change the caller's variable.

**Ex 8.9** A local variable ceases to exist when its function returns. The returned address then points to memory that is no longer yours (a **dangling pointer**): using it gives garbage or crashes.

**Ex 8.10** `p + 3` is the **address** of `a[3]`; `*(p + 3)` is the **value** `a[3]`; `a[3]` is the same value written with array notation — `a[3]` is defined as `*(a + 3)`.

**Ex 8.11** A **string** is a one-dimensional array of characters terminated by the **null character `'\0'`**, whose code is **0**.

**Ex 8.12** `'A'` is a single character (code 65). `"A"` is a **string**: two bytes — `'A'` followed by `'\0'`.

**Ex 8.13** `char s[] = "Ghana";` occupies **6 bytes** (5 letters + `'\0'`). `strlen(s)` returns **5**.

**Ex 8.14** `s1 == s2` compares the **addresses** of the two arrays, not their text. Use `strcmp(s1, s2)`, which returns **0** when the strings are equal.

**Ex 8.15** `gets` doesn't know the size of the destination array, so long input overflows it (buffer overflow: crashes and security holes). It has been removed from the C standard. Use `fgets(buffer, sizeof(buffer), stdin)`.

**Ex 8.16**
1. **True.**
2. **False** — `*p` is the pointed-to value; `&p` is the address of the pointer variable.
3. **True** (on one machine, all object pointers have the same size).
4. **False** — modifying a string literal is undefined behaviour (usually a crash).
5. **False** — it does no checking at all.
6. **True** (otherwise it is just a character array, not a string).

---

## Part B — Predict the output

**Ex 8.17** `25` — `*p = 25` writes into `x`.

**Ex 8.18** `8 8` — `*p = *q` copies the **value** 8 into `a`.

**Ex 8.19** `5 100` — `p = q` makes `p` point to `b`; then `*p = 100` changes `b`. `a` is untouched.

**Ex 8.20** `7 7 1`

**Ex 8.21** `10 20 21`
- `*p++`: the value `10` is used, then `p` moves to `a[1]`.
- `*p`: now `a[1]` = 20.
- `++*p`: increments the **value** `a[1]` to 21 and prints it.

**Ex 8.22** `2 4 3` — `p` points to `a[1]`: `*p` = 2, `*(p + 2)` = `a[3]` = 4, `p[1]` = `a[2]` = 3.

**Ex 8.23** `4` — the pointers are 4 elements apart.

**Ex 8.24** `30`

**Ex 8.25** `7` — `inc` adds 1 to the original `x`, twice.

**Ex 8.26**
```output
Before calling funct1: u=1 v=3
Within funct1: u=0 v=0
After calling funct1: u=1 v=3

Before calling funct2: u=1 v=3
Within funct2: *pu=0 *pv=0
After calling funct2: u=0 v=0
```
`funct1` passes **by value** (the originals survive); `funct2` passes **by reference** (the originals are changed).

**Ex 8.27** `4 9`

**Ex 8.28** `15 0` — `larger` returns the address of `b` (92); `*p = 0` sets `b` to 0.

**Ex 8.29** `1 4 8 1` — the pointed-to types have sizes 1, 4 and 8, but all pointers have the same size (so the comparison is 1/true).

**Ex 8.30** `6 7` — six characters, seven bytes (the `'\0'`).

**Ex 8.31** `2 10 0` — length 2; the array has 10 bytes; `s[2]` is the `'\0'` (code 0).

**Ex 8.32** `ABC 3` — printing and `strlen` both stop at the first `'\0'`.

**Ex 8.33** `Jell` — `s[4] = '\0'` shortens the string.

**Ex 8.34** `good morning 12`

**Ex 8.35** `Ac 2` — placing `'\0'` at index 2 ends the string after `Ac`.

**Ex 8.36** `1 1 1`

**Ex 8.37** `2` — "Progra**mm**ing" has two `m`s.

**Ex 8.38** `a-b-c-`

**Ex 8.39** `4 6 world` — `'o'` is at index 4; `"wor"` starts at index 6; printing `q` prints the rest of the string from there.

**Ex 8.40** `Ama Y 4` — `names[1]` is `"Ama"`; `names[2][0]` is `'Y'`; `strlen(names[0])` is 4.

---

## Part C — Find and fix the bugs

**Ex 8.41** `p` was never given an address; it contains garbage, so `*p = 5` writes to a random place. Point it at a real variable:
```c
#include <stdio.h>

int main(void)
{
    int x;
    int *p = &x;
    *p = 5;
    printf("%d\n", *p);
    return 0;
}
```
```output
5
```

**Ex 8.42** An `int *` cannot point to a `float`: the pointer would read the float's bytes as an integer. Use a `float *`:
```c
#include <stdio.h>

int main(void)
{
    float f = 2.5f;
    float *p = &f;
    printf("%f\n", *p);
    return 0;
}
```
```output
2.500000
```

**Ex 8.43** `p = 10;` tries to put the number 10 *into the pointer* (making it point to address 10). To change `x` you must **dereference**: `*p = 10;`.

**Ex 8.44** In `int *a, b;` only `a` is a pointer; `b` is an `int`, so `b = &y;` assigns an address to an int. Write `int *a, *b;`.

**Ex 8.45** Pass the **addresses** and dereference inside:
```c
#include <stdio.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    int x = 4, y = 9;
    swap(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```
```output
9 4
```

**Ex 8.46** `x` is local to `makeFive` and is destroyed when the function returns; `p` then points to dead memory (a dangling pointer). Safe alternatives: make `x` **`static`** (it lives as long as the program), or use `malloc`, or let the caller own the variable:
```c
#include <stdio.h>

int *makeFive(void)
{
    static int x = 5;          /* lives for the whole program */
    return &x;
}

int main(void)
{
    int *p = makeFive();
    printf("%d\n", *p);
    return 0;
}
```
```output
5
```

**Ex 8.47** `"Hello"` needs **6** bytes (5 letters + `'\0'`). In `char s[5]` there is no room for the terminator, so `printf("%s")` runs past the end of the array. Use `char s[6]` or, better, `char s[] = "Hello";`.

**Ex 8.48** `answer == "yes"` compares two addresses. Use `strcmp`:
<!--in: yes-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char answer[10];

    scanf("%9s", answer);
    if (strcmp(answer, "yes") == 0)
        printf("match\n");
    else
        printf("no match\n");
    return 0;
}
```
```output
yes
match
```

**Ex 8.49** Arrays cannot be assigned. Copy the text with `strcpy`, or initialise at the declaration:
```c
char name[20] = "Kofi";                /* initialisation is allowed */
/* or:  char name[20]; strcpy(name, "Kofi"); */
```

**Ex 8.50** `char *s = "hello";` makes `s` point to a string **literal** stored in read-only memory; writing to it is undefined behaviour (typically a crash). Make your own modifiable copy in an array:
```c
#include <stdio.h>

int main(void)
{
    char s[] = "hello";
    s[0] = 'J';
    printf("%s\n", s);
    return 0;
}
```
```output
Jello
```

**Ex 8.51** For an array, the name already *is* the address, so `&fullname` is unnecessary (it has a different type — "pointer to the whole array" — and compilers warn). Write `scanf("%s", fullname);` — and limit the input with `scanf("%249s", fullname);`.

**Ex 8.52**
<!--in: Kofi Mensah-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char fullname[250];

    printf("enter your full name\n");
    fgets(fullname, sizeof(fullname), stdin);
    fullname[strcspn(fullname, "\n")] = '\0';     /* optional: remove the newline */
    puts(fullname);
    return 0;
}
```
```output
enter your full name
Kofi Mensah
Kofi Mensah
```

**Ex 8.53** `"Kumasi"` needs 7 bytes but `small` has only 5: `strcpy` writes past the end of the array (**buffer overflow**). Fixes: (1) make the array big enough — `char small[7];`; (2) copy safely and accept truncation:
```c
#include <stdio.h>

int main(void)
{
    char small[5];

    snprintf(small, sizeof(small), "%s", "Kumasi");     /* stores at most 4 characters + '\0' */
    printf("%s\n", small);
    return 0;
}
```
```output
Kuma
```

**Ex 8.54** The string has no `'\0'`: `s[3]` was never set, so it contains garbage, and `printf("%s")` keeps reading until it happens to find a zero byte. Add `s[3] = '\0';` (or initialise the whole array with `= {0}` / `= ""`).

**Ex 8.55** The second `printf` **uses `copy` after it has been freed** (a *use-after-free*): the memory no longer belongs to you, so the program may print garbage or crash. Don't touch memory after `free` (set the pointer to `NULL` to make misuse obvious). If `free(copy)` were left out completely, the memory would never be returned: a **memory leak** (harmless for a tiny program that ends right away, but a serious problem in a long-running program).

**Ex 8.56** `dest` is uninitialised, so `strcat` appends after whatever garbage is in the array (it looks for the first `'\0'`). Start with an empty string:
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char dest[20] = "";                  /* an empty string: dest[0] is '\0' */

    strcat(dest, "Hi ");
    strcat(dest, "there");
    printf("%s\n", dest);
    return 0;
}
```
```output
Hi there
```

---

## Part D1 — Pointers

**Ex 8.57**
```c
#include <stdio.h>

int main(void)
{
    int i = 10;
    double d = 2.5;
    char c = 'A';

    int *pi = &i;
    double *pd = &d;
    char *pc = &c;

    printf("%d %.1f %c\n", *pi, *pd, *pc);       /* read through the pointers */

    *pi = 20;                                    /* write through the pointers */
    *pd = 7.25;
    *pc = 'Z';

    printf("%d %.2f %c\n", i, d, c);             /* the variables have changed */
    return 0;
}
```
```output
10 2.5 A
20 7.25 Z
```

**Ex 8.58** *(The addresses differ on every machine and run, so only the comparison line is predictable.)*
```c
#include <stdio.h>

int main(void)
{
    int x = 42;
    int *p = &x;

    printf("address of x : %p\n", (void *)&x);
    printf("value of p   : %p\n", (void *)p);
    printf("p == &x ?      %d\n", p == &x);
    return 0;
}
```
Sample run:
```text
address of x : 000000000061FE1C
value of p   : 000000000061FE1C
p == &x ?      1
```

**Ex 8.59**
<!--in: 5 9-->
```c
#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void)
{
    int a, b;

    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    printf("Before: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After : a = %d, b = %d\n", a, b);
    return 0;
}
```
```output
Enter two integers: 5 9
Before: a = 5, b = 9
After : a = 9, b = 5
```

**Ex 8.60**
<!--in: 17 4-->
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

int main(void)
{
    int x, y, lo, hi;

    printf("Enter two integers: ");
    scanf("%d %d", &x, &y);

    minmax(x, y, &lo, &hi);
    printf("Smaller: %d, larger: %d\n", lo, hi);
    return 0;
}
```
```output
Enter two integers: 17 4
Smaller: 4, larger: 17
```

**Ex 8.61**
<!--in: 47 5-->
```c
#include <stdio.h>

void divide(int a, int b, int *quotient, int *remainder)
{
    *quotient = a / b;
    *remainder = a % b;
}

int main(void)
{
    int a, b, q, r;

    printf("Enter a and b: ");
    scanf("%d %d", &a, &b);

    divide(a, b, &q, &r);
    printf("%d / %d = %d remainder %d\n", a, b, q, r);
    return 0;
}
```
```output
Enter a and b: 47 5
47 / 5 = 9 remainder 2
```

**Ex 8.62**
```c
#include <stdio.h>

void increment(int *n)
{
    (*n)++;                  /* the brackets matter: *n++ would move the pointer! */
}

void doubleIt(double *x)
{
    *x = *x * 2;
}

int main(void)
{
    int count = 5;
    double amount = 1.5;

    increment(&count);
    increment(&count);
    increment(&count);

    doubleIt(&amount);
    doubleIt(&amount);
    doubleIt(&amount);

    printf("count = %d, amount = %.1f\n", count, amount);
    return 0;
}
```
```output
count = 8, amount = 12.0
```

**Ex 8.63**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = sizeof(a) / sizeof(a[0]);
    int sum = 0;

    for (int *p = a; p < a + n; p++)
        sum += *p;

    printf("sum = %d\n", sum);
    return 0;
}
```
```output
sum = 31
```

**Ex 8.64**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(a) / sizeof(a[0]);
    int *start = a;
    int *end = a + n - 1;

    while (start < end)
    {
        int temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
6 5 4 3 2 1
```

**Ex 8.65**
```c
#include <stdio.h>

int *findMax(int *a, int n)
{
    int *max = a;
    for (int *p = a + 1; p < a + n; p++)
        if (*p > *max)
            max = p;
    return max;                            /* points INTO the caller's array: safe */
}

int main(void)
{
    int a[] = {12, 45, 7, 33, 29};
    int n = sizeof(a) / sizeof(a[0]);

    int *m = findMax(a, n);
    printf("max = %d at index %d\n", *m, (int)(m - a));
    return 0;
}
```
```output
max = 45 at index 1
```

**Ex 8.66**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {5, 2, 9, 1, 7};
    int n = sizeof(a) / sizeof(a[0]);
    int *big = a, *small = a;

    for (int *p = a; p < a + n; p++)
    {
        if (*p > *big)
            big = p;
        if (*p < *small)
            small = p;
    }

    int temp = *big;
    *big = *small;
    *small = temp;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
5 2 1 9 7
```

**Ex 8.67**
```c
#include <stdio.h>

int main(void)
{
    int src[] = {1, 2, 3, 4, 5};
    int dst[5];
    int *s = src, *d = dst;

    for (int i = 0; i < 5; i++)
        *d++ = *s++;                       /* copy, then move both pointers */

    for (int i = 0; i < 5; i++)
        printf("%d ", dst[i]);
    printf("\n");
    return 0;
}
```
```output
1 2 3 4 5
```

**Ex 8.68**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {10, 20, 30, 40};
    int *p = a;

    for (int i = 0; i < 4; i++)
        printf("%d ", a[i]);
    printf("\n");

    for (int i = 0; i < 4; i++)
        printf("%d ", *(a + i));
    printf("\n");

    for (int i = 0; i < 4; i++)
        printf("%d ", p[i]);
    printf("\n");
    return 0;
}
```
```output
10 20 30 40
10 20 30 40
10 20 30 40
```

**Ex 8.69**
```c
#include <stdio.h>

void stats(const int *a, int n, double *mean, int *max, int *min)
{
    int sum = 0;
    *max = *min = a[0];

    for (int i = 0; i < n; i++)
    {
        sum += a[i];
        if (a[i] > *max) *max = a[i];
        if (a[i] < *min) *min = a[i];
    }
    *mean = (double) sum / n;
}

int main(void)
{
    int data[] = {4, 8, 15, 16, 23, 42};
    double mean;
    int max, min;

    stats(data, 6, &mean, &max, &min);
    printf("mean = %.2f, max = %d, min = %d\n", mean, max, min);
    return 0;
}
```
```output
mean = 18.00, max = 42, min = 4
```

**Ex 8.70**
```c
#include <stdio.h>

int *findValue(int *a, int n, int key)
{
    for (int i = 0; i < n; i++)
        if (a[i] == key)
            return &a[i];
    return NULL;                           /* not found */
}

int main(void)
{
    int a[] = {4, 9, 7, 1, 8};
    int keys[2] = {7, 5};

    for (int k = 0; k < 2; k++)
    {
        int *p = findValue(a, 5, keys[k]);
        if (p != NULL)
            printf("%d found at index %d\n", keys[k], (int)(p - a));
        else
            printf("%d not found\n", keys[k]);
    }
    return 0;
}
```
```output
7 found at index 2
5 not found
```

**Ex 8.71**
```c
#include <stdio.h>

int countAbove(const int *a, int n, int threshold)
{
    int count = 0;
    for (int i = 0; i < n; i++)
        if (a[i] > threshold)
            count++;
    return count;
}

int main(void)
{
    int marks[] = {45, 78, 62, 90, 55, 81};

    printf("%d marks are above 60\n", countAbove(marks, 6, 60));
    return 0;
}
```
```output
4 marks are above 60
```

**Ex 8.72**
```c
#include <stdio.h>

void swapDouble(double *a, double *b)
{
    double t = *a;
    *a = *b;
    *b = t;
}

void swapChar(char *a, char *b)
{
    char t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    double x = 1.5, y = 2.5;
    char c = 'x', d = 'y';

    swapDouble(&x, &y);
    swapChar(&c, &d);

    printf("%.1f %.1f %c %c\n", x, y, c, d);
    return 0;
}
```
```output
2.5 1.5 y x
```

**Ex 8.73**
```c
#include <stdio.h>

void rotate3(int *a, int *b, int *c)
{
    int oldA = *a;
    *a = *c;                 /* a gets c's old value */
    *c = *b;                 /* c gets b's old value */
    *b = oldA;               /* b gets a's old value */
}

int main(void)
{
    int a = 1, b = 2, c = 3;

    rotate3(&a, &b, &c);
    printf("a = %d, b = %d, c = %d\n", a, b, c);
    return 0;
}
```
```output
a = 3, b = 1, c = 2
```

**Ex 8.74** `larger` returns a pointer, so `*larger(&a, &b)` *is* the larger variable and can be assigned to or modified directly:
```c
#include <stdio.h>

int *larger(int *x, int *y)
{
    return (*x > *y) ? x : y;
}

int main(void)
{
    int a = 15, b = 92;

    *larger(&a, &b) *= 2;                  /* doubles whichever is bigger */
    printf("a = %d, b = %d\n", a, b);
    return 0;
}
```
```output
a = 15, b = 184
```

**Ex 8.75**
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 6;
    int *a = malloc(n * sizeof(int));

    if (a == NULL)
    {
        printf("Out of memory\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
        a[i] = (i + 1) * (i + 1);

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");

    free(a);
    return 0;
}
```
```output
1 4 9 16 25 36
```

**Ex 8.76**
<!--in: 5 70 80 90 60 75-->
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    double sum = 0;

    printf("How many numbers? ");
    scanf("%d", &n);

    double *a = malloc(n * sizeof(double));
    if (a == NULL)
    {
        printf("Out of memory\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
    {
        printf("Number %d: ", i + 1);
        scanf("%lf", &a[i]);
        sum += a[i];
    }

    printf("Average = %.2f\n", sum / n);
    free(a);
    return 0;
}
```
```output
How many numbers? 5
Number 1: 70
Number 2: 80
Number 3: 90
Number 4: 60
Number 5: 75
Average = 75.00
```
The size `n` is only known at run time — exactly the case that fixed-size arrays cannot handle.

**Ex 8.77**
<!--in: 3 12 4-->
```c
#include <stdio.h>

int add(int a, int b)      { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }

int apply(int (*f)(int, int), int a, int b)
{
    return f(a, b);
}

int main(void)
{
    printf("%d %d %d\n", apply(add, 12, 4), apply(subtract, 12, 4), apply(multiply, 12, 4));

    /* a tiny calculator: choose the operation from a table */
    int (*ops[3])(int, int) = {add, subtract, multiply};
    int choice, x, y;

    printf("1 = add, 2 = subtract, 3 = multiply. Choice and two numbers: ");
    scanf("%d %d %d", &choice, &x, &y);

    if (choice >= 1 && choice <= 3)
        printf("Result: %d\n", ops[choice - 1](x, y));
    else
        printf("Invalid choice\n");
    return 0;
}
```
```output
16 8 48
1 = add, 2 = subtract, 3 = multiply. Choice and two numbers: 3 12 4
Result: 48
```

**Ex 8.78** The sort calls the comparison function to decide **whether a pair is out of order**.
```c
#include <stdio.h>

int ascending(int a, int b)  { return a > b; }     /* out of order if the left one is bigger  */
int descending(int a, int b) { return a < b; }     /* out of order if the left one is smaller */

void sort(int a[], int n, int (*outOfOrder)(int, int))
{
    for (int pass = 0; pass < n - 1; pass++)
        for (int j = 0; j < n - 1 - pass; j++)
            if (outOfOrder(a[j], a[j + 1]))
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
}

void print(const int a[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(a) / sizeof(a[0]);

    sort(a, n, ascending);
    print(a, n);
    sort(a, n, descending);
    print(a, n);
    return 0;
}
```
```output
11 12 22 25 34 64 90
90 64 34 25 22 12 11
```

**Ex 8.79** `m` is an array of rows. `m + i` is the address of row `i`; `*(m + i)` is that row (an array of ints); `*(m + i) + j` is the address of element `j` of the row; `*(*(m + i) + j)` is the element itself — exactly what `m[i][j]` means.
```c
#include <stdio.h>

int main(void)
{
    int m[2][3] = { {1, 2, 3}, {4, 5, 6} };

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
            printf("%d ", *(*(m + i) + j));
        printf("\n");
    }
    return 0;
}
```
```output
1 2 3
4 5 6
```

**Ex 8.80**
```c
#include <stdio.h>

void normalizeTime(int *hours, int *minutes)
{
    int total = *hours * 60 + *minutes;
    *hours = total / 60;
    *minutes = total % 60;
}

int main(void)
{
    int h = 2, m = 75;
    normalizeTime(&h, &m);
    printf("%d:%02d\n", h, m);

    h = 1; m = -10;
    normalizeTime(&h, &m);
    printf("%d:%02d\n", h, m);
    return 0;
}
```
```output
3:15
0:50
```

**Ex 8.81**
```c
#include <stdio.h>

void fillRange(int *a, int n, int start)
{
    for (int i = 0; i < n; i++)
        a[i] = start + i;
}

void scale(int *a, int n, int factor)
{
    for (int i = 0; i < n; i++)
        a[i] *= factor;
}

int main(void)
{
    int a[5];

    fillRange(a, 5, 3);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\n");

    scale(a, 5, 2);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
3 4 5 6 7
6 8 10 12 14
```

**Ex 8.82**
```c
#include <stdio.h>

void swapArrays(int *a, int *b, int n)
{
    for (int i = 0; i < n; i++)
    {
        int t = a[i];
        a[i] = b[i];
        b[i] = t;
    }
}

int main(void)
{
    int x[] = {1, 2, 3};
    int y[] = {7, 8, 9};

    swapArrays(x, y, 3);

    printf("x: %d %d %d\n", x[0], x[1], x[2]);
    printf("y: %d %d %d\n", y[0], y[1], y[2]);
    return 0;
}
```
```output
x: 7 8 9
y: 1 2 3
```

---

## Part D2 — Strings

Remember the two loop styles: `for (i = 0; s[i] != '\0'; i++)` and `while (*p)`. Strings need **no length variable** — the `'\0'` is the stopper.

**Ex 8.83**
```c
#include <stdio.h>

int main(void)
{
    char s[] = "Ghana";

    for (int i = 0; s[i] != '\0'; i++)
        printf("%c %d\n", s[i], s[i]);
    return 0;
}
```
```output
G 71
h 104
a 97
n 110
a 97
```

**Ex 8.84**
```c
#include <stdio.h>
#include <string.h>

int myStrlen(const char *s)
{
    int n = 0;
    while (s[n] != '\0')
        n++;
    return n;
}

int main(void)
{
    const char *tests[3] = {"Kumasi", "", "Hello, World!"};

    for (int i = 0; i < 3; i++)
        printf("\"%s\": mine = %d, library = %zu\n", tests[i], myStrlen(tests[i]), strlen(tests[i]));
    return 0;
}
```
```output
"Kumasi": mine = 6, library = 6
"": mine = 0, library = 0
"Hello, World!": mine = 13, library = 13
```

**Ex 8.85**
<!--in: Hello World 2026-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char line[100];
    int vowels = 0, consonants = 0, digits = 0, spaces = 0;

    printf("Enter a line: ");
    fgets(line, sizeof(line), stdin);

    for (int i = 0; line[i] != '\0'; i++)
    {
        char c = line[i];
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
        {
            if (strchr("aeiouAEIOU", c) != NULL)
                vowels++;
            else
                consonants++;
        }
        else if (c >= '0' && c <= '9')
            digits++;
        else if (c == ' ')
            spaces++;
    }

    printf("vowels=%d consonants=%d digits=%d spaces=%d\n", vowels, consonants, digits, spaces);
    return 0;
}
```
```output
Enter a line: Hello World 2026
vowels=3 consonants=7 digits=4 spaces=2
```
(`strchr("aeiouAEIOU", c)` asks "is `c` one of these letters?")

**Ex 8.86**
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char original[] = "Hello Kumasi 123";
    char upper[40], lower[40], toggled[40];

    strcpy(upper, original);
    strcpy(lower, original);
    strcpy(toggled, original);

    for (int i = 0; original[i] != '\0'; i++)
    {
        char c = original[i];
        if (c >= 'a' && c <= 'z')
        {
            upper[i] = c - 32;
            toggled[i] = c - 32;
        }
        else if (c >= 'A' && c <= 'Z')
        {
            lower[i] = c + 32;
            toggled[i] = c + 32;
        }
    }

    printf("upper  : %s\n", upper);
    printf("lower  : %s\n", lower);
    printf("toggled: %s\n", toggled);
    return 0;
}
```
```output
upper  : HELLO KUMASI 123
lower  : hello kumasi 123
toggled: hELLO kUMASI 123
```

**Ex 8.87**
```c
#include <stdio.h>
#include <string.h>

void reverse(char *s)
{
    int i = 0, j = (int) strlen(s) - 1;

    while (i < j)
    {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
        i++;
        j--;
    }
}

int main(void)
{
    char s[] = "Kumasi";

    reverse(s);
    printf("%s\n", s);
    return 0;
}
```
```output
isamuK
```

**Ex 8.88**
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(const char *s)
{
    int i = 0, j = (int) strlen(s) - 1;

    while (i < j)
    {
        if (tolower((unsigned char) s[i]) != tolower((unsigned char) s[j]))
            return 0;
        i++;
        j--;
    }
    return 1;
}

int main(void)
{
    const char *tests[3] = {"Level", "Madam", "Kofi"};

    for (int k = 0; k < 3; k++)
        printf("%-6s -> %s\n", tests[k], isPalindrome(tests[k]) ? "palindrome" : "not a palindrome");
    return 0;
}
```
```output
Level  -> palindrome
Madam  -> palindrome
Kofi   -> not a palindrome
```

**Ex 8.89**
```c
#include <stdio.h>

void myStrcpy(char *dest, const char *src)
{
    while ((*dest = *src) != '\0')      /* copy a character; stop AFTER copying the '\0' */
    {
        dest++;
        src++;
    }
}

int main(void)
{
    char copy[20];

    myStrcpy(copy, "Accra");
    printf("%s\n", copy);
    return 0;
}
```
```output
Accra
```

**Ex 8.90**
```c
#include <stdio.h>

void myStrcat(char *dest, const char *src)
{
    while (*dest != '\0')               /* 1. find the end of dest */
        dest++;
    while ((*dest = *src) != '\0')      /* 2. copy src there, including its '\0' */
    {
        dest++;
        src++;
    }
}

int main(void)
{
    char text[30] = "Hello, ";

    myStrcat(text, "Ghana!");
    printf("%s\n", text);
    return 0;
}
```
```output
Hello, Ghana!
```

**Ex 8.91**
```c
#include <stdio.h>

int myStrcmp(const char *a, const char *b)
{
    while (*a != '\0' && *a == *b)
    {
        a++;
        b++;
    }
    return (unsigned char)*a - (unsigned char)*b;
}

void compare(const char *a, const char *b)
{
    int r = myStrcmp(a, b);
    printf("\"%s\" vs \"%s\": %s\n", a, b, (r == 0) ? "equal" : (r < 0) ? "less" : "greater");
}

int main(void)
{
    compare("apple", "apple");
    compare("apple", "apricot");
    compare("zebra", "apple");
    compare("abc", "abcd");
    return 0;
}
```
```output
"apple" vs "apple": equal
"apple" vs "apricot": less
"zebra" vs "apple": greater
"abc" vs "abcd": less
```
The loop stops at the first difference **or** at the end of either string. The final subtraction then decides: for `"abc"` vs `"abcd"`, `'\0'` (0) minus `'d'` is negative.

**Ex 8.92**
<!--in: Kofi Mensah Boateng-->
```c
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char name[100];
    int newWord = 1;

    printf("Full name: ");
    fgets(name, sizeof(name), stdin);

    printf("Initials: ");
    for (int i = 0; name[i] != '\0'; i++)
    {
        if (isspace((unsigned char) name[i]))
            newWord = 1;                              /* the next letter starts a word */
        else if (newWord)
        {
            printf("%c.", toupper((unsigned char) name[i]));
            newWord = 0;
        }
    }
    printf("\n");
    return 0;
}
```
```output
Full name: Kofi Mensah Boateng
Initials: K.M.B.
```

**Ex 8.93**
<!--in: the quick brown fox-->
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char s[100];
    int newWord = 1;

    printf("Sentence: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == ' ')
            newWord = 1;
        else if (newWord)
        {
            s[i] = (char) toupper((unsigned char) s[i]);
            newWord = 0;
        }
    }
    printf("%s\n", s);
    return 0;
}
```
```output
Sentence: the quick brown fox
The Quick Brown Fox
```

**Ex 8.94** A word starts wherever a non-space character follows a space (or the start of the string) — this handles repeated spaces.
<!--in: This   is a    sentence -->
```c
#include <stdio.h>

int main(void)
{
    char s[100];
    int words = 0, inWord = 0;

    printf("Sentence: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] != ' ' && s[i] != '\n' && s[i] != '\t')
        {
            if (!inWord)
                words++;                 /* a new word begins here */
            inWord = 1;
        }
        else
            inWord = 0;
    }

    printf("Words: %d\n", words);
    return 0;
}
```
```output
Sentence: This   is a    sentence
Words: 4
```

**Ex 8.95**
<!--in: I love programming in C-->
```c
#include <stdio.h>

int main(void)
{
    char s[100];
    int bestStart = 0, bestLen = 0;
    int start = 0, len = 0;

    printf("Sentence: ");
    fgets(s, sizeof(s), stdin);

    for (int i = 0; ; i++)
    {
        if (s[i] != ' ' && s[i] != '\n' && s[i] != '\0')
        {
            if (len == 0)
                start = i;                    /* a new word starts */
            len++;
        }
        else
        {
            if (len > bestLen)
            {
                bestLen = len;
                bestStart = start;
            }
            len = 0;
            if (s[i] == '\0')
                break;
        }
    }

    printf("Longest word: %.*s (%d letters)\n", bestLen, s + bestStart, bestLen);
    return 0;
}
```
```output
Sentence: I love programming in C
Longest word: programming (11 letters)
```
(`%.*s` prints at most `bestLen` characters, starting at the address `s + bestStart`.)

**Ex 8.96**
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[] = "mississippi";
    char target = 's';
    int count = 0;

    printf("'%c' occurs at positions:", target);
    for (char *p = strchr(s, target); p != NULL; p = strchr(p + 1, target))
    {
        printf(" %d", (int)(p - s));
        count++;
    }
    printf("\nTotal: %d\n", count);
    return 0;
}
```
```output
's' occurs at positions: 2 3 5 6
Total: 4
```

**Ex 8.97**
```c
#include <stdio.h>

int main(void)
{
    char s[] = "banana";

    for (int i = 0; s[i] != '\0'; i++)
        if (s[i] == 'a')
            s[i] = 'o';

    printf("%s\n", s);
    return 0;
}
```
```output
bonono
```

**Ex 8.98** Use a "read" index `i` and a "write" index `k`; copy only the characters you keep.
<!--in: Kumasi Central Market-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];
    int k = 0;

    printf("Text: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';

    for (int i = 0; s[i] != '\0'; i++)
        if (s[i] != ' ')
            s[k++] = s[i];
    s[k] = '\0';

    printf("%s\n", s);
    return 0;
}
```
```output
Text: Kumasi Central Market
KumasiCentralMarket
```

**Ex 8.99**
<!--in: Programming Language-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];
    int k = 0;

    printf("Text: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';

    for (int i = 0; s[i] != '\0'; i++)
        if (strchr("aeiouAEIOU", s[i]) == NULL)
            s[k++] = s[i];
    s[k] = '\0';

    printf("%s\n", s);
    return 0;
}
```
```output
Text: Programming Language
Prgrmmng Lngg
```

**Ex 8.100** `c - 'a'` converts a letter into an index 0–25.
```c
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char s[] = "Hello World";
    int count[26] = {0};

    for (int i = 0; s[i] != '\0'; i++)
        if (isalpha((unsigned char) s[i]))
            count[tolower((unsigned char) s[i]) - 'a']++;

    for (int k = 0; k < 26; k++)
        if (count[k] > 0)
            printf("%c: %d\n", 'a' + k, count[k]);
    return 0;
}
```
```output
d: 1
e: 1
h: 1
l: 3
o: 2
r: 1
w: 1
```

**Ex 8.101** Two words are anagrams if they have exactly the same letter counts.
```c
#include <stdio.h>
#include <ctype.h>

int areAnagrams(const char *a, const char *b)
{
    int count[26] = {0};

    for (int i = 0; a[i] != '\0'; i++)
        if (isalpha((unsigned char) a[i]))
            count[tolower((unsigned char) a[i]) - 'a']++;      /* +1 for each letter of a */
    for (int i = 0; b[i] != '\0'; i++)
        if (isalpha((unsigned char) b[i]))
            count[tolower((unsigned char) b[i]) - 'a']--;      /* -1 for each letter of b */

    for (int k = 0; k < 26; k++)
        if (count[k] != 0)
            return 0;
    return 1;
}

int main(void)
{
    printf("listen / silent: %d\n", areAnagrams("listen", "silent"));
    printf("hello / world  : %d\n", areAnagrams("hello", "world"));
    return 0;
}
```
```output
listen / silent: 1
hello / world  : 0
```

**Ex 8.102**
```c
#include <stdio.h>

int myAtoi(const char *s)
{
    int value = 0;
    for (int i = 0; s[i] >= '0' && s[i] <= '9'; i++)
        value = value * 10 + (s[i] - '0');
    return value;
}

void myItoa(int n, char *s)
{
    int i = 0, negative = (n < 0);

    if (n == 0)
        s[i++] = '0';
    while (n != 0)
    {
        int digit = n % 10;
        s[i++] = '0' + (digit < 0 ? -digit : digit);     /* digits come out last-first */
        n /= 10;
    }
    if (negative)
        s[i++] = '-';
    s[i] = '\0';

    for (int a = 0, b = i - 1; a < b; a++, b--)           /* reverse */
    {
        char t = s[a];
        s[a] = s[b];
        s[b] = t;
    }
}

int main(void)
{
    char buffer[20];

    printf("%d\n", myAtoi("4096") + 1);
    myItoa(-250, buffer);
    printf("%s\n", buffer);
    myItoa(0, buffer);
    printf("%s\n", buffer);
    return 0;
}
```
```output
4097
-250
0
```

**Ex 8.103** For a letter, find its position in the alphabet (`c - 'a'`), add the shift, wrap with `% 26`, and convert back. To **decrypt** shift by `26 − k`.
```c
#include <stdio.h>

void caesar(char *s, int k)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = (s[i] - 'a' + k) % 26 + 'a';
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = (s[i] - 'A' + k) % 26 + 'A';
    }
}

int main(void)
{
    char message[] = "Hello, World!";

    caesar(message, 3);
    printf("Encrypted: %s\n", message);

    caesar(message, 26 - 3);
    printf("Decrypted: %s\n", message);
    return 0;
}
```
```output
Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

**Ex 8.104**
<!--in: Kumasi12-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char pw[100];
    int upper = 0, lower = 0, digit = 0, symbol = 0;

    printf("Password: ");
    scanf("%99s", pw);

    for (int i = 0; pw[i] != '\0'; i++)
    {
        char c = pw[i];
        if (c >= 'A' && c <= 'Z')      upper = 1;
        else if (c >= 'a' && c <= 'z') lower = 1;
        else if (c >= '0' && c <= '9') digit = 1;
        else                           symbol = 1;
    }

    int ok = strlen(pw) >= 8 && upper && lower && digit && symbol;
    if (ok)
    {
        printf("Strong password\n");
    }
    else
    {
        printf("Weak password. Missing:");
        if (strlen(pw) < 8) printf(" 8+ characters;");
        if (!upper)  printf(" uppercase letter;");
        if (!lower)  printf(" lowercase letter;");
        if (!digit)  printf(" digit;");
        if (!symbol) printf(" symbol;");
        printf("\n");
    }
    return 0;
}
```
```output
Password: Kumasi12
Weak password. Missing: symbol;
```

**Ex 8.105** After each match, continue searching **after** the match (`p + strlen(sub)`).
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char text[] = "ababab abab";
    char sub[] = "ab";
    int count = 0;

    for (char *p = strstr(text, sub); p != NULL; p = strstr(p + strlen(sub), sub))
        count++;

    printf("\"%s\" appears %d times in \"%s\"\n", sub, count, text);
    return 0;
}
```
```output
"ab" appears 5 times in "ababab abab"
```

**Ex 8.106** `strrchr` finds the **last** `.`; adding 1 skips it. For the e-mail, `at - email` is the number of characters before the `@`.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char file[] = "report.final.pdf";
    char email[] = "kofi.mensah@knust.edu.gh";

    char *dot = strrchr(file, '.');
    if (dot != NULL)
        printf("extension: %s\n", dot + 1);

    char *at = strchr(email, '@');
    if (at != NULL)
        printf("user name: %.*s\n", (int)(at - email), email);
    return 0;
}
```
```output
extension: pdf
user name: kofi.mensah
```

**Ex 8.107**
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

    printf("A-Z: ");
    for (int i = 0; i < COUNT; i++)
        printf("%s ", names[i]);

    printf("\nZ-A: ");
    for (int i = COUNT - 1; i >= 0; i--)
        printf("%s ", names[i]);
    printf("\n");
    return 0;
}
```
```output
A-Z: Abena Ama Kofi Kwame Yaw
Z-A: Yaw Kwame Kofi Ama Abena
```

**Ex 8.108**
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    const char *names[] = {"Kwame", "Ama", "Nana Yaw", "Efua", "Abena"};
    int n = sizeof(names) / sizeof(names[0]);
    int longest = 0, shortest = 0;

    for (int i = 1; i < n; i++)
    {
        if (strlen(names[i]) > strlen(names[longest]))
            longest = i;
        if (strlen(names[i]) < strlen(names[shortest]))
            shortest = i;
    }

    printf("Longest : %s (%zu)\n", names[longest], strlen(names[longest]));
    printf("Shortest: %s (%zu)\n", names[shortest], strlen(names[shortest]));
    return 0;
}
```
```output
Longest : Nana Yaw (8)
Shortest: Ama (3)
```
(`const char *names[]` is an *array of pointers*, each pointing at a string literal — a compact alternative to a 2D `char` array when you don't need to modify the text.)

**Ex 8.109**
```c
#include <stdio.h>

int main(void)
{
    char item[40];
    char title[40];

    snprintf(item, sizeof(item), "Item %d: GHS %.2f", 7, 12.5);
    snprintf(title, sizeof(title), "Dr. %s %s", "Ama", "Mensah");

    puts(item);
    puts(title);
    return 0;
}
```
```output
Item 7: GHS 12.50
Dr. Ama Mensah
```

**Ex 8.110**
```c
#include <stdio.h>

int daysIn(int month, int year)
{
    int leap = (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    switch (month)
    {
        case 4: case 6: case 9: case 11: return 30;
        case 2: return leap ? 29 : 28;
        default: return 31;
    }
}

void check(const char *text)
{
    int day, month, year;

    if (sscanf(text, "%d/%d/%d", &day, &month, &year) != 3)
    {
        printf("%s: not in dd/mm/yyyy format\n", text);
        return;
    }

    if (month < 1 || month > 12 || day < 1 || day > daysIn(month, year))
        printf("%s: INVALID date\n", text);
    else
        printf("%s: valid (day %d, month %d, year %d)\n", text, day, month, year);
}

int main(void)
{
    check("12/11/2026");
    check("31/04/2026");
    check("29/02/2024");
    check("hello");
    return 0;
}
```
```output
12/11/2026: valid (day 12, month 11, year 2026)
31/04/2026: INVALID date
29/02/2024: valid (day 29, month 2, year 2024)
hello: not in dd/mm/yyyy format
```

**Ex 8.111**
```c
#include <stdio.h>
#include <string.h>

int binaryToDecimal(const char *bits)
{
    int value = 0;
    for (int i = 0; bits[i] != '\0'; i++)
        value = value * 2 + (bits[i] - '0');
    return value;
}

void decimalToBinary(int n, char *out)
{
    int i = 0;

    if (n == 0)
        out[i++] = '0';
    while (n > 0)
    {
        out[i++] = '0' + n % 2;
        n /= 2;
    }
    out[i] = '\0';

    for (int a = 0, b = i - 1; a < b; a++, b--)        /* reverse */
    {
        char t = out[a];
        out[a] = out[b];
        out[b] = t;
    }
}

int main(void)
{
    char bits[40];

    printf("\"101101\" = %d\n", binaryToDecimal("101101"));
    decimalToBinary(45, bits);
    printf("45 = \"%s\"\n", bits);
    return 0;
}
```
```output
"101101" = 45
45 = "101101"
```

**Ex 8.112** (`sprintf` writes formatted text into a string and returns how many characters it wrote.)
```c
#include <stdio.h>

int main(void)
{
    char s[] = "aaabccdddd";
    char out[40];
    int i = 0, k = 0;

    while (s[i] != '\0')
    {
        char c = s[i];
        int run = 0;
        while (s[i] == c)               /* count the run of equal characters */
        {
            run++;
            i++;
        }
        k += sprintf(out + k, "%c%d", c, run);
    }

    printf("%s -> %s\n", s, out);
    return 0;
}
```
```output
aaabccdddd -> a3b1c2d4
```

**Ex 8.113**
```c
#include <stdio.h>

int main(void)
{
    char s[] = "programming";
    char out[40];
    int k = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        int seen = 0;
        for (int j = 0; j < k; j++)          /* did we already keep this character? */
            if (out[j] == s[i])
            {
                seen = 1;
                break;
            }
        if (!seen)
            out[k++] = s[i];
    }
    out[k] = '\0';

    printf("%s -> %s\n", s, out);
    return 0;
}
```
```output
programming -> progamin
```

**Ex 8.114** Reverse the **whole** string, then reverse **each word** back.
```c
#include <stdio.h>
#include <string.h>

void reverseRange(char *s, int i, int j)
{
    while (i < j)
    {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
        i++;
        j--;
    }
}

int main(void)
{
    char s[] = "I love C";
    int n = (int) strlen(s);

    reverseRange(s, 0, n - 1);                  /* "C evol I" */

    int start = 0;
    for (int i = 0; i <= n; i++)
        if (s[i] == ' ' || s[i] == '\0')
        {
            reverseRange(s, start, i - 1);      /* un-reverse this word */
            start = i + 1;
        }

    printf("%s\n", s);
    return 0;
}
```
```output
C love I
```

**Ex 8.115**
```c
#include <stdio.h>
#include <string.h>

int validEmail(const char *s)
{
    const char *at = strchr(s, '@');

    if (at == NULL)                      /* no '@' at all */
        return 0;
    if (strchr(at + 1, '@') != NULL)     /* a second '@' */
        return 0;
    if (strchr(at + 1, '.') == NULL)     /* no '.' after the '@' */
        return 0;
    return 1;
}

int main(void)
{
    const char *tests[4] = {"kofi@knust.edu.gh", "kofi.knust.edu.gh", "a@@b.com", "ama@localhost"};

    for (int i = 0; i < 4; i++)
        printf("%-20s -> %d\n", tests[i], validEmail(tests[i]));
    return 0;
}
```
```output
kofi@knust.edu.gh    -> 1
kofi.knust.edu.gh    -> 0
a@@b.com             -> 0
ama@localhost        -> 0
```

**Ex 8.116**
```c
#include <stdio.h>
#include <string.h>

#define N 5
#define LEN 20

int main(void)
{
    char names[N][LEN] = {"Kofi", "Ama", "Yaw", "Abena", "Kwame"};
    int marks[N] = {72, 85, 60, 91, 78};

    for (int pass = 0; pass < N - 1; pass++)
        for (int j = 0; j < N - 1 - pass; j++)
            if (marks[j] < marks[j + 1])                /* highest first */
            {
                int tm = marks[j];                      /* swap the marks ... */
                marks[j] = marks[j + 1];
                marks[j + 1] = tm;

                char tn[LEN];                           /* ... AND the names, so they stay together */
                strcpy(tn, names[j]);
                strcpy(names[j], names[j + 1]);
                strcpy(names[j + 1], tn);
            }

    printf("%-5s %-8s %4s\n", "Rank", "Name", "Mark");
    for (int i = 0; i < N; i++)
        printf("%-5d %-8s %4d\n", i + 1, names[i], marks[i]);
    return 0;
}
```
```output
Rank  Name     Mark
1     Abena      91
2     Ama        85
3     Kwame      78
4     Kofi       72
5     Yaw        60
```
Whenever you sort *parallel arrays*, every swap must be applied to **all** the arrays, or the names and marks would no longer match.

---

## Part E — Challenges and mini-projects

**Ex 8.117**
```c
#include <stdio.h>
#include <string.h>

void pigLatin(const char *word, char *out)
{
    if (strchr("aeiouAEIOU", word[0]) != NULL)
        sprintf(out, "%sway", word);                       /* starts with a vowel */
    else
        sprintf(out, "%s%cay", word + 1, word[0]);         /* move the first letter to the end */
}

int main(void)
{
    const char *words[3] = {"banana", "apple", "string"};
    char out[40];

    for (int i = 0; i < 3; i++)
    {
        pigLatin(words[i], out);
        printf("%s -> %s\n", words[i], out);
    }
    return 0;
}
```
```output
banana -> ananabay
apple -> appleway
string -> tringsay
```

**Ex 8.118** Work down the table of values from largest to smallest, writing each symbol as many times as it fits.
```c
#include <stdio.h>
#include <string.h>

void toRoman(int n, char *out)
{
    int values[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    const char *symbols[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    out[0] = '\0';
    for (int i = 0; i < 13; i++)
        while (n >= values[i])
        {
            strcat(out, symbols[i]);
            n -= values[i];
        }
}

int valueOf(char c)
{
    switch (c)
    {
        case 'I': return 1;    case 'V': return 5;
        case 'X': return 10;   case 'L': return 50;
        case 'C': return 100;  case 'D': return 500;
        case 'M': return 1000;
    }
    return 0;
}

int fromRoman(const char *s)
{
    int total = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (valueOf(s[i]) < valueOf(s[i + 1]))
            total -= valueOf(s[i]);               /* a smaller symbol before a bigger one is subtracted: IV = 4 */
        else
            total += valueOf(s[i]);
    }
    return total;
}

int main(void)
{
    int tests[3] = {1994, 2026, 49};
    char roman[30];

    for (int i = 0; i < 3; i++)
    {
        toRoman(tests[i], roman);
        printf("%d = %s = %d\n", tests[i], roman, fromRoman(roman));
    }
    return 0;
}
```
```output
1994 = MCMXCIV = 1994
2026 = MMXXVI = 2026
49 = XLIX = 49
```

**Ex 8.119** Take the first word as the candidate prefix and shorten it until every other word starts with it.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    const char *words[3] = {"flower", "flow", "flight"};
    int prefixLen = (int) strlen(words[0]);

    for (int w = 1; w < 3; w++)
    {
        int i = 0;
        while (i < prefixLen && words[w][i] == words[0][i])
            i++;
        prefixLen = i;                      /* keep only the part that still matches */
    }

    printf("Longest common prefix: %.*s\n", prefixLen, words[0]);
    return 0;
}
```
```output
Longest common prefix: fl
```

**Ex 8.120** Push every opening bracket; when a closing bracket arrives, the **most recent** opening bracket (top of the stack) must match it. A stack is "last in, first out" — Chapter 0!
```c
#include <stdio.h>

int balanced(const char *s)
{
    char stack[100];
    int top = 0;                                    /* number of items on the stack */

    for (int i = 0; s[i] != '\0'; i++)
    {
        char c = s[i];

        if (c == '(' || c == '[' || c == '{')
        {
            stack[top++] = c;                       /* push */
        }
        else if (c == ')' || c == ']' || c == '}')
        {
            if (top == 0)
                return 0;                           /* closing bracket with nothing open */

            char open = stack[--top];               /* pop */
            if ((c == ')' && open != '(') ||
                (c == ']' && open != '[') ||
                (c == '}' && open != '{'))
                return 0;                           /* wrong kind of bracket */
        }
    }
    return top == 0;                                /* nothing left open */
}

int main(void)
{
    const char *tests[4] = {"{[()]}", "([)]", "((", ""};

    for (int i = 0; i < 4; i++)
        printf("\"%s\" -> %s\n", tests[i], balanced(tests[i]) ? "balanced" : "NOT balanced");
    return 0;
}
```
```output
"{[()]}" -> balanced
"([)]" -> NOT balanced
"((" -> NOT balanced
"" -> balanced
```

**Ex 8.121** `sscanf` can split the line in one go. The pattern `%49[^,]` means "read up to 49 characters that are **not** a comma".
```c
#include <stdio.h>

int main(void)
{
    char line[] = "Kofi,21,3.5";
    char name[50];
    int age;
    double gpa;

    if (sscanf(line, "%49[^,],%d,%lf", name, &age, &gpa) == 3)
        printf("name=%s age=%d gpa=%.1f\n", name, age, gpa);
    else
        printf("bad line\n");
    return 0;
}
```
```output
name=Kofi age=21 gpa=3.5
```
(`strtok(line, ",")` is the other common tool: it returns the pieces one at a time. Look it up — but note that it *modifies* the string.)

**Ex 8.122**
```c
#include <stdio.h>

void printWords(int n)
{
    const char *ones[20] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                            "sixteen", "seventeen", "eighteen", "nineteen"};
    const char *tens[10] = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    if (n >= 100)
    {
        printf("%s hundred", ones[n / 100]);
        n %= 100;
        if (n > 0)
            printf(" and ");
        else
            return;
    }
    if (n < 20)
        printf("%s", ones[n]);
    else
    {
        printf("%s", tens[n / 10]);
        if (n % 10 > 0)
            printf("-%s", ones[n % 10]);
    }
}

int main(void)
{
    int tests[6] = {0, 12, 100, 345, 709, 999};

    for (int i = 0; i < 6; i++)
    {
        printf("%3d = ", tests[i]);
        printWords(tests[i]);
        printf("\n");
    }
    return 0;
}
```
```output
  0 = zero
 12 = twelve
100 = one hundred
345 = three hundred and forty-five
709 = seven hundred and nine
999 = nine hundred and ninety-nine
```

**Ex 8.123** (guesses are read from the keyboard; here the player types `a x k u m s i`)
<!--in: a x k u m s i-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    const char secret[] = "kumasi";
    int len = (int) strlen(secret);
    char shown[20];
    int wrong = 0, guessed = 0;
    char guess;

    for (int i = 0; i < len; i++)
        shown[i] = '_';
    shown[len] = '\0';

    while (wrong < 6 && guessed < len)
    {
        printf("\nWord: ");
        for (int i = 0; i < len; i++)
            printf("%c ", shown[i]);
        printf("  Wrong guesses: %d/6\nYour guess: ", wrong);
        scanf(" %c", &guess);

        int hit = 0;
        for (int i = 0; i < len; i++)
            if (secret[i] == guess && shown[i] == '_')
            {
                shown[i] = guess;
                guessed++;
                hit = 1;
            }
        if (!hit)
            wrong++;
    }

    if (guessed == len)
        printf("\nYou won! The word was %s.\n", secret);
    else
        printf("\nYou lost. The word was %s.\n", secret);
    return 0;
}
```
```output
Word: _ _ _ _ _ _   Wrong guesses: 0/6
Your guess: a

Word: _ _ _ a _ _   Wrong guesses: 0/6
Your guess: x

Word: _ _ _ a _ _   Wrong guesses: 1/6
Your guess: k

Word: k _ _ a _ _   Wrong guesses: 1/6
Your guess: u

Word: k u _ a _ _   Wrong guesses: 1/6
Your guess: m

Word: k u m a _ _   Wrong guesses: 1/6
Your guess: s

Word: k u m a s _   Wrong guesses: 1/6
Your guess: i

You won! The word was kumasi.
```

**Ex 8.124** Input: add Kofi, add Ama, list, search Ama, search Yaw, exit.
<!--in: 1 Kofi 0244123456\n1 Ama 0201234567\n3\n2 Ama\n2 Yaw\n4-->
```c
#include <stdio.h>
#include <string.h>

#define MAX 10

int main(void)
{
    char names[MAX][30];
    char phones[MAX][15];
    int count = 0, choice;

    do
    {
        printf("\n1) Add  2) Search  3) List  4) Exit\nChoose: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            if (count == MAX)
                printf("Contact book is full\n");
            else
            {
                scanf("%29s %14s", names[count], phones[count]);
                count++;
                printf("Saved.\n");
            }
        }
        else if (choice == 2)
        {
            char key[30];
            int found = 0;
            scanf("%29s", key);
            for (int i = 0; i < count; i++)
                if (strcmp(names[i], key) == 0)
                {
                    printf("%s: %s\n", names[i], phones[i]);
                    found = 1;
                }
            if (!found)
                printf("%s not found\n", key);
        }
        else if (choice == 3)
        {
            for (int i = 0; i < count; i++)
                printf("%d. %-10s %s\n", i + 1, names[i], phones[i]);
        }
    }
    while (choice != 4);

    printf("Goodbye!\n");
    return 0;
}
```
```output
1) Add  2) Search  3) List  4) Exit
Choose: 1 Kofi 0244123456
Saved.

1) Add  2) Search  3) List  4) Exit
Choose: 1 Ama 0201234567
Saved.

1) Add  2) Search  3) List  4) Exit
Choose: 3
1. Kofi       0244123456
2. Ama        0201234567

1) Add  2) Search  3) List  4) Exit
Choose: 2 Ama
Ama: 0201234567

1) Add  2) Search  3) List  4) Exit
Choose: 2 Yaw
Yaw not found

1) Add  2) Search  3) List  4) Exit
Choose: 4
Goodbye!
```

**Ex 8.125** If `b` is a rotation of `a`, then `b` must appear inside `a` written twice: `"waterbottlewaterbottle"` contains `"erbottlewat"`.
```c
#include <stdio.h>
#include <string.h>

int isRotation(const char *a, const char *b)
{
    char doubled[200];

    if (strlen(a) != strlen(b))
        return 0;
    strcpy(doubled, a);
    strcat(doubled, a);
    return strstr(doubled, b) != NULL;
}

int main(void)
{
    printf("waterbottle / erbottlewat: %d\n", isRotation("waterbottle", "erbottlewat"));
    printf("hello / llohe            : %d\n", isRotation("hello", "llohe"));
    printf("hello / olleh            : %d\n", isRotation("hello", "olleh"));
    return 0;
}
```
```output
waterbottle / erbottlewat: 1
hello / llohe            : 1
hello / olleh            : 0
```

**Ex 8.126** `fgets` returns the line including `'\n'`; an **empty line** is just `"\n"`.
<!--in: Ghana is a country in West Africa.\nIt is famous for gold and cocoa!\n-->
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char line[200];
    int characters = 0, words = 0, sentences = 0, letters = 0;
    int inWord = 0;

    printf("Type a paragraph, then an empty line:\n");
    while (fgets(line, sizeof(line), stdin) != NULL && line[0] != '\n')
    {
        for (int i = 0; line[i] != '\0' && line[i] != '\n'; i++)
        {
            char c = line[i];
            characters++;
            if (isalpha((unsigned char) c))
                letters++;
            if (c == '.' || c == '!' || c == '?')
                sentences++;

            if (c != ' ')
            {
                if (!inWord)
                    words++;
                inWord = 1;
            }
            else
                inWord = 0;
        }
        inWord = 0;                           /* a line break also ends a word */
    }

    printf("Characters: %d\nWords: %d\nSentences: %d\n", characters, words, sentences);
    printf("Average word length: %.2f letters\n", (double) letters / words);
    return 0;
}
```
```output
Type a paragraph, then an empty line:
Ghana is a country in West Africa.
It is famous for gold and cocoa!

Characters: 66
Words: 14
Sentences: 2
Average word length: 3.71 letters
```
(Check by hand: the two lines have 34 + 32 = 66 characters; 7 + 7 = 14 words; 27 + 25 = 52 letters, and 52 ÷ 14 ≈ 3.71. The punctuation `.` and `!` is counted as a character but not as a letter.)

---

## Part F — Research tasks (sample answers)

**Ex 8.127** Three differences between an array and a pointer:
1. **`sizeof`:** for `int a[10]`, `sizeof(a)` is the whole array (40 bytes); for `int *p`, `sizeof(p)` is the size of the *pointer* (8 bytes).
2. **Assignment:** a pointer can be re-pointed (`p = q;`); an array name cannot be assigned (`a = b;` is an error).
3. **`++`:** `p++` is fine (move to the next element); `a++` is an error — the array name is a fixed address.
(Also: an array *owns* its memory; a pointer only *refers* to memory owned by something else.)

**Ex 8.128**
- `const char *p` — pointer to **constant** characters: you can change `p` (point elsewhere) but **not** `*p` (the text).
- `char *const p` — **constant pointer** to characters: you can change `*p` but **not** `p` itself.
- `const char *const p` — neither can change.

**Ex 8.129** `strncpy(dest, src, n)` copies **at most `n`** characters. If `src` has `n` or more characters it copies exactly `n` and does **not** append `'\0'`, so `dest` is not a valid string. If `src` is shorter it pads `dest` with zeros up to `n`, which wastes time. Safe pattern:
```c
strncpy(dest, src, sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';          /* always terminate */
```
(Or use `snprintf(dest, sizeof(dest), "%s", src)`.)

**Ex 8.130** `memset(ptr, value, bytes)` sets a block of memory to a byte value (commonly 0); `memcpy(dest, src, bytes)` copies a block of bytes. Both are in `<string.h>`.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    int a[5];
    int b[5] = {1, 2, 3, 4, 5};

    memset(a, 0, sizeof(a));              /* all five ints become 0 */
    memcpy(a, b, sizeof(b));              /* copy 20 bytes: now a is a copy of b */

    for (int i = 0; i < 5; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
1 2 3 4 5
```
`memcpy` is the standard way to copy a whole array in one statement.

**Ex 8.131**
- **`NULL`** is the *null pointer constant* — a pointer that points to nothing. Used with **pointers** (`int *p = NULL;`).
- **`'\0'`** is the *null character* — a **character** whose code is 0. It ends every string.
- **`0`** is the integer zero. It also converts to a null pointer or a null character, which is why `NULL` is usually defined as `0` (or `(void *)0`) and `'\0'` has the value 0 — but they are used for different *purposes*, so use the right one to make your intention clear.

---

*End of the solutions for the core chapters. Next: [Chapter 9 solutions](09-projects-and-final-exam.md)*

