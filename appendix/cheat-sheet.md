# C Cheat Sheet

> A one-stop summary of everything in the course. Print it. Keep it next to your keyboard.
> *Details and explanations are in the chapters; reference tables are in [reference-tables.md](reference-tables.md).*

---

## 1. The skeleton of every program

```c
#include <stdio.h>            // header files first

#define SIZE 10               // constants (no = and no ;)

int add(int a, int b);        // function prototypes

int main(void)                // execution starts here
{
    int result = add(2, 3);   // statements end with ;
    printf("%d\n", result);
    return 0;                 // 0 = success
}

int add(int a, int b)         // function definitions
{
    return a + b;
}
```

**Compile & run** (GCC): `gcc prog.c -o prog` then `./prog` (Windows: `prog`). With warnings: `gcc -Wall -Wextra prog.c -o prog`. Math library: add `-lm`.

**Comments:** `// one line` and `/* many lines */`.

---

## 2. Data types

| Type | Holds | Typical size | `printf` | `scanf` |
|---|---|---|---|---|
| `char` | one character | 1 | `%c` | `%c` |
| `int` | whole number | 4 | `%d` | `%d` |
| `unsigned int` | non-negative whole | 4 | `%u` | `%u` |
| `long` / `long long` | big whole | 4 or 8 / 8 | `%ld` / `%lld` | `%ld` / `%lld` |
| `float` | decimal (~7 digits) | 4 | `%f` | `%f` |
| `double` | decimal (~15 digits) | 8 | `%f` | **`%lf`** |
| string | `char` array + `'\0'` | length + 1 | `%s` | `%s` |

Qualifiers: `short`, `long`, `signed`, `unsigned` (sign only for `int`/`char`). Constants: `const double PI = 3.14;` or `#define PI 3.14`.
Casting: `(double) a / b`. `sizeof(x)` gives bytes (`%zu`).

---

## 3. Operators (high → low precedence)

```
 () [] postfix++ --        highest
 prefix++ -- ! ~ (type) * & sizeof  unary + -      (right to left)
 * / %
 + -
 << >>
 < <= > >=
 == !=
 &
 ^
 |
 &&
 ||
 ?:                                                  (right to left)
 = += -= *= /= %= <<= >>= &= ^= |=                   (right to left)
 ,                         lowest
```

- Integer `/` truncates: `9 / 2 == 4`. `%` is the remainder (integers only).
- `a++` use then add 1; `++a` add 1 then use.
- True = any non-zero; false = `0`. Comparisons give `1` or `0`.
- `&&`, `||` short-circuit. `=` assigns, `==` compares.
- `cond ? a : b` picks `a` if true, else `b`.
- Bits: `& | ^ ~ << >>`; `x << n` = `x * 2^n`; `(x >> k) & 1` tests bit `k`.

---

## 4. Input and output

```c
printf("Age: %d, Price: %.2f, Grade: %c, Name: %s\n", age, price, grade, name);
printf("[%5d] [%-5d] [%05d] [%8.3f] [%10s] [%-10s]\n", ...);   // width / left / zeros / precision
scanf("%d", &age);              // & for ordinary variables
scanf("%lf", &price);           // double
scanf(" %c", &ch);              // space skips leftover newline
scanf("%49s", name);            // one word, NO & for arrays
fgets(line, sizeof(line), stdin);               // a whole line (keeps '\n')
line[strcspn(line, "\n")] = '\0';               // remove the '\n'  (needs <string.h>)
putchar(c);  c = getchar();  puts("text");
```
`scanf` returns the number of items read. **Never use `gets`.**

---

## 5. Decisions

```c
if (cond) { ... }
else if (cond2) { ... }
else { ... }

switch (expr)                     // int or char only
{
    case 1:  ...; break;          // break to stop; without it you "fall through"
    case 2:
    case 3:  ...; break;          // several cases, same code
    default: ...;
}
```

## 6. Loops

```c
while (cond) { ... }                         // test first
do { ... } while (cond);                     // test last (note ;), runs at least once
for (int i = 0; i < n; i++) { ... }          // init; test; update  -> runs n times
break;      // leave the loop      continue;   // skip to the next iteration
```

Rule of braces: a single statement needs no `{ }` — but always using them is safer.

**Nested loops** (tables, patterns): outer loop = rows/lines, inner loop = columns; `printf("\n")` after the inner loop.

---

## 7. Functions

```c
double average(double a, double b);       // prototype (declaration)

double average(double a, double b)        // definition: type name(parameters)
{
    return (a + b) / 2;
}

void greet(void) { printf("Hi\n"); }      // void: no result; (void): no parameters

x = average(3, 4);                        // call
```
- Arguments are **copied** (pass by value).
- `static int n = 0;` inside a function remembers its value between calls.
- Local variables live inside a function; globals outside (avoid them).
- **Recursion:** needs a **base case** and a smaller recursive call.

```c
long long fact(int n) { if (n <= 1) return 1; return n * fact(n - 1); }
```

---

## 8. Arrays

```c
int a[5];                         // indices 0..4 (NO bounds checking!)
int b[5] = {1, 2};                // rest become 0
int c[] = {4, 8, 15};             // size counted by compiler
int n = sizeof(c) / sizeof(c[0]); // number of elements
for (int i = 0; i < n; i++) ...
int m[3][4];                      // 2D: m[row][col]
int cube[2][3][4];                // 3D
int t[2][3] = { {1, 2, 3}, {4, 5, 6} };
void f(int arr[], int n);         // array parameter: pass the size too
void g(int m[][4], int rows);     // 2D parameter: columns must be given
```
- Can't copy (`b = a`) or compare (`a == b`) arrays — use loops.
- A function **can** change the caller's array elements.

**Typical algorithms:** sum/average, max/min (start with the first element!), linear search, reverse (swap `i` and `n-1-i`), bubble sort, binary search (sorted data), counting array (`count[value]++`).

---

## 9. Pointers

```c
int x = 5;
int *p = &x;          // p holds the address of x
*p = 10;              // changes x
int *q = NULL;        // points to nothing — check before use
p + 1                 // next element;   a[i]  ==  *(a + i)
```
- `&x` address of x · `*p` the value p points to · pointer type must match (`void *` is the exception).
- **Pass by reference:** `void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }` … `swap(&x, &y);`
- Never return the address of a local variable.
- `malloc` / `free`: `int *a = malloc(n * sizeof(int)); if (a == NULL) ...; ...; free(a);`
- Function pointer: `int (*f)(int, int) = add;  f(2, 3);`

---

## 10. Strings

```c
char s1[] = "Kumasi";        // 7 bytes: 6 letters + '\0'  (modifiable)
char *s2 = "Kumasi";         // points to a read-only literal (don't modify)
char name[30];               // room for 29 characters + '\0'
```

| Task | Code |
|---|---|
| length | `strlen(s)` |
| copy | `strcpy(dest, src)` (dest must be big enough) |
| append | `strcat(dest, src)` |
| compare | `strcmp(a, b) == 0` equal · `< 0` a first · `> 0` b first |
| find char / substring | `strchr(s, 'c')` · `strrchr` · `strstr(s, "sub")` (NULL if not found) |
| duplicate | `p = strdup(s);` … `free(p);` |
| build text safely | `snprintf(buf, sizeof(buf), "Item %d", n);` |
| parse text | `sscanf(text, "%d/%d/%d", &d, &m, &y);` |

**Walk a string:** `for (i = 0; s[i] != '\0'; i++)` or `while (*p) { ... p++; }`.
**Digit char → number:** `c - '0'`. **Letter → index:** `c - 'a'`. **Lower → upper:** `c - 32` (or `toupper`).

---

## 11. Headers you will use

| Header | For |
|---|---|
| `<stdio.h>` | `printf scanf getchar putchar puts fgets` |
| `<string.h>` | `strlen strcpy strcat strcmp strchr strstr strdup` |
| `<math.h>` | `sqrt pow fabs ceil floor round` |
| `<ctype.h>` | `toupper tolower isdigit isalpha isspace` |
| `<stdlib.h>` | `malloc free abs rand srand exit qsort` |
| `<limits.h>` | `INT_MAX INT_MIN UCHAR_MAX …` |

---

## 12. Ten golden rules

1. **Think first** — write the algorithm (pseudocode) before the code.
2. Initialise every variable (and every pointer).
3. `=` assigns, `==` compares.
4. `scanf` needs `&` (except for strings/arrays); use `%lf` for `double`.
5. Array indices run from `0` to `size − 1`.
6. A string needs room for the `'\0'`.
7. Compare strings with `strcmp`, never `==`.
8. Integer ÷ integer is an integer — cast when you want decimals.
9. Always use braces `{ }`; indent consistently.
10. Read the **first** compiler error first, and test with small, tricky inputs.
