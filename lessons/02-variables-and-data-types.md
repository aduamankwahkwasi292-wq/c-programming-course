# Chapter 2 — Variables and Data Types

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `02 Variables  Datatypes.pdf`  
> **Solutions:** [Solutions to Chapter 2](../solutions/02-variables-and-data-types.md)

---

## What you will learn

1. What a **variable** is and how to create ("declare") one.
2. The four basic **data types**: `int`, `char`, `float`, `double`.
3. How **qualifiers** (`short`, `long`, `signed`, `unsigned`) change a type.
4. How to use **constants**.
5. How to convert between types — **implicit** and **explicit type-casting** — and why `9 / 2` gives `4`.

> **A quick note before we start.** To *see* the values of our variables we will use `printf` with placeholders such as `%d` (integer), `%f` (decimal) and `%c` (character). Chapter 4 explains them fully. For now, just copy the pattern.

---

## 2.1 What is a variable?

Your program must remember things: a student's age, a bank balance, the price of an item. It remembers them in **variables**.

> A **variable** is a **named storage space in the computer's memory** that holds data.

**Analogy:** imagine a shelf of jars. Every jar has a **label** (the *name*), a **size/shape** suited to what it holds (the *type*) and **something inside** (the *value*).

```
   Memory (a long row of numbered cells)

    address:    1000       1004        1008
              ┌────────┬────────┬────────┐
              │   24   │  3.5   │  'A'   │
              └────────┴────────┴────────┘
    name:        age      price     grade
```

- The **name** (an identifier, see Chapter 1) is just a friendly *symbol* for a memory location. You do not need to remember addresses like `1000`.
- The picture is simplified: in reality each type takes a different number of bytes (a `char` takes 1, an `int` usually 4, a `double` 8). Section 2.4 shows how to check.
- The **value** can **change** while the program runs — that is why it is called a *variable*.

```c
playerScore = 95;     // the box now holds 95
playerScore = 60;     // the box now holds 60 (95 is gone)
```

---

## 2.2 Declaring and initialising variables

In C, a variable must be **declared before it is used**. To **declare** a variable means to state its **data type** (and its name). The type tells the compiler how much memory to reserve and what kind of data the box will hold.

```c
int age;          // declaration: "age is a box for an integer"
age = 24;         // assignment:  put 24 into the box
```

You can combine the two steps — declaring and giving a first value is called **initialising**:

```c
int age = 24;
```

### Reading `=` correctly

In C, `=` is **not** "equals". It means **assign**: *"evaluate the right side, and store the result in the variable on the left."*

```c
int a = 5;
a = a + 1;    // read as: take a (5), add 1 (6), store it back in a. Now a is 6.
```

(In mathematics `a = a + 1` is impossible. In C it is perfectly normal and extremely common.)

### Declaring several variables at once

Variables of the **same type** can be declared in one statement, separated by commas, and some may be initialised:

```c
int age, sum, result;
float weight = 49.36f, cwa = 73.98f;
double balance, interest = 14.3856312;
```

Here `balance` is declared but **not** initialised (see the warning below).

### Putting it into a program

```c
#include <stdio.h>

int main(void)
{
    int age = 21;
    char grade = 'A';
    double balance = 1250.75;

    printf("Age     : %d\n", age);
    printf("Grade   : %c\n", grade);
    printf("Balance : %.2f\n", balance);

    age = 22;                       /* the value changes */
    printf("Next year: %d\n", age);
    return 0;
}
```
```output
Age     : 21
Grade   : A
Balance : 1250.75
Next year: 22
```

> ⚠️ **Common mistakes**
> 1. **Using a variable before declaring it** → compiler error (`'x' undeclared`).
> 2. **Using an uninitialised variable.** A variable declared *inside a function* that was never given a value contains **garbage**: whatever was left in that piece of memory. Sometimes the garbage happens to be 0, so the bug hides on your computer and appears on someone else's. Always initialise: `int total = 0;`.
> 3. **Declaring the same variable twice** in the same block.
> 4. **Wrong case**: `Age` and `age` are different variables.

---

## 2.3 Data types

A **data type** tells the compiler **what kind** of data a variable holds and **how much memory** it needs.

C has **four basic (fundamental) data types**, written with four keywords:

| Keyword | Holds | Example values | `printf` placeholder |
|---|---|---|---|
| `int` | whole numbers (integers) | `0`, `-5`, `10`, `2024` | `%d` |
| `char` | a single character | `'A'`, `'y'`, `'7'`, `'$'` | `%c` |
| `float` | decimal (real) numbers — single precision | `2.34`, `-6.8` | `%f` |
| `double` | decimal numbers — double precision | `23.99`, `3.14159265` | `%f` (for `printf`) |

### 2.3.1 `int` — whole numbers

Integers are whole numbers, positive or negative, **with no decimal point**: `0`, `-5`, `10`.

```c
int age;
age = 24;
```

Declaring `age` as `int` means it will store **only integers**, and the compiler reserves "just the right amount" of memory for one integer (usually **4 bytes**).

### 2.3.2 `char` — single characters

A `char` holds **one** character: a letter, a digit, a punctuation mark. Characters are always written in **single quotes**:

```c
char choice = 'y';
```

> ⚠️ **`'A'` is not `"A"`!** Single quotes → one character (`char`). Double quotes → a **string** (text), which is a different thing (Chapter 8). So `char c = "A";` is a mistake.

**A secret about `char`:** the computer can only store numbers. So each character is stored as a small number — its **ASCII code**.

| Character | Code | | Character | Code |
|---|---|---|---|---|
| `' '` (space) | 32 | | `'A'` … `'Z'` | 65 … 90 |
| `'0'` … `'9'` | 48 … 57 | | `'a'` … `'z'` | 97 … 122 |

So `char` is really a **tiny integer** (1 byte) that we *display* as a character. You can do maths with it:

```c
#include <stdio.h>

int main(void)
{
    char letter = 'A';

    printf("%c has code %d\n", letter, letter);   /* same value, shown two ways */

    letter = letter + 1;                          /* 65 + 1 = 66 */
    printf("The next letter is %c\n", letter);

    char digit = '7';
    int value = digit - '0';                      /* '7' is 55, '0' is 48 -> 7 */
    printf("The digit %c as a number plus 1 is %d\n", digit, value + 1);
    return 0;
}
```
```output
A has code 65
The next letter is B
The digit 7 as a number plus 1 is 8
```

Notice `digit - '0'`: the standard trick to turn a digit **character** into its **numeric value**.

### 2.3.3 `float` and `double` — decimal numbers

Floating-point types hold **real numbers** — numbers with a fractional part, like `2.34` or `-6.8`.

```c
float accountBalance = 3234.23f;
double bookPrice = 23.99;
```

They can also be written in **exponential (scientific) notation**. `22.442e2` means 22.442 × 10², which is `2244.2`:

```c
float normalizationFactor = 22.442e2;
```

(`e2` means "times ten to the power 2". `1.5e-3` is `0.0015`.)

### 2.3.4 `float` versus `double`

Both store decimals. The difference is **size and precision**:

| | `float` | `double` |
|---|---|---|
| Name | single precision | double precision |
| Typical size | 4 bytes | 8 bytes |
| Reliable digits | about **6–7** | about **15–16** |

> 📝 *Slide note:* your slide quotes 6 digits for `float` and 14 for `double`. The exact count depends on the number, so many books quote 6–7 and 15–16 — the message is the same: **`double` is far more precise than `float`**.

Why does precision matter? Computers store decimals in binary, and many decimals (even simple ones like 0.1) cannot be stored exactly. See it for yourself:

```c
#include <stdio.h>

int main(void)
{
    float  f = 1.0f / 3;
    double d = 1.0 / 3;

    printf("float : %.10f\n", f);
    printf("double: %.10f\n", d);
    return 0;
}
```
```output
float : 0.3333333433
double: 0.3333333333
```

The `float` goes wrong after about the 7th digit. **Rule of thumb:** use `double` for real numbers unless you have a reason not to.

> 💡 In C, a number written like `3.14` is a `double`. To make it a `float` write `3.14f`. You will see both styles in the slides; it is fine.

---

## 2.4 How big is each type? — `sizeof`

The `sizeof` operator tells you how many **bytes** a type or variable uses. (1 byte = 8 bits.)

```c
#include <stdio.h>

int main(void)
{
    printf("char      : %zu byte\n",  sizeof(char));
    printf("short     : %zu bytes\n", sizeof(short));
    printf("int       : %zu bytes\n", sizeof(int));
    printf("long      : %zu bytes\n", sizeof(long));
    printf("long long : %zu bytes\n", sizeof(long long));
    printf("float     : %zu bytes\n", sizeof(float));
    printf("double    : %zu bytes\n", sizeof(double));
    return 0;
}
```
```output
char      : 1 byte
short     : 2 bytes
int       : 4 bytes
long      : 4 bytes
long long : 8 bytes
float     : 4 bytes
double    : 8 bytes
```

(`%zu` is the placeholder for the unsigned number `sizeof` returns.)

> ⚠️ **Sizes depend on your computer!** C only *guarantees* that `sizeof(char)` is 1, that `short ≤ int ≤ long ≤ long long`, and some minimums: `short` and `int` have at least 16 bits, `long` at least 32 and `long long` at least 64. The output above is typical for **Windows**. On 64-bit Linux and macOS, `long` is usually **8** bytes. **Never assume a size — ask `sizeof`.**

---

## 2.5 Type qualifiers (modifiers)

A **qualifier** changes the meaning of a basic type and gives a *new* type. There are two groups.

### Size qualifiers: `short` and `long`

They change **how much memory** (and so how big a number) the type can use.

```c
short int small = 100;        // usually 2 bytes
long int count = 1500000;     // at least 4 bytes
long long int huge = 9000000000LL;   // at least 8 bytes
```

- `short` usually *shrinks* an `int` to 2 bytes.
- `long` may *increase* the storage (e.g. `long int count;` can store bigger numbers).
- You may drop the word `int`: `long count;` means `long int count;`.

### Sign qualifiers: `signed` and `unsigned`

They change **whether negative numbers are allowed**.

- `signed` — can store **positive and negative** values (this is the default for `int`).
- `unsigned` — can store **only zero and positive** values, but the *positive range is about twice as large*, because no bit is spent on the sign. (A 2-byte `short` reaches 32 767; an `unsigned short` reaches 65 535.)

```c
unsigned int students = 120;
signed int temperature = -4;
```

> Sign qualifiers apply to **`int` and `char` only** (not to `float` or `double`). `unsigned float` is an error.

### Combining qualifiers — the rules

- Do **not** use `short` and `long` together (they are opposites). Same for `signed` and `unsigned`.
- You **can** combine **one from each group**, for example `long unsigned int age = 25;` (same as `unsigned long age = 25;`).
- Qualifiers are **optional**. Use them only when you need them.

### Typical ranges (a 4-byte `int`, 2-byte `short`)

| Type | Typical size | Range |
|---|---|---|
| `signed char` | 1 byte | −128 to 127 |
| `unsigned char` | 1 byte | 0 to 255 |
| `short` | 2 bytes | −32 768 to 32 767 |
| `unsigned short` | 2 bytes | 0 to 65 535 |
| `int` | 4 bytes | −2 147 483 648 to 2 147 483 647 |
| `unsigned int` | 4 bytes | 0 to 4 294 967 295 |

You do not have to memorise these. The header file **`<limits.h>`** gives the exact limits for *your* compiler:

```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    printf("int       : %d to %d\n", INT_MIN, INT_MAX);
    printf("short     : %d to %d\n", SHRT_MIN, SHRT_MAX);
    printf("unsigned int  max: %u\n", UINT_MAX);
    printf("unsigned char max: %d\n", UCHAR_MAX);
    return 0;
}
```
```output
int       : -2147483648 to 2147483647
short     : -32768 to 32767
unsigned int  max: 4294967295
unsigned char max: 255
```

### What happens when a number is too big? — overflow

Every box has a limit. Push past the limit and the value **wraps around**, like a car's odometer going from 999999 back to 000000:

```c
#include <stdio.h>

int main(void)
{
    unsigned char box = 250;

    printf("%d\n", box);
    box = box + 5;
    printf("%d\n", box);          /* 255 is the largest */
    box = box + 1;
    printf("%d\n", box);          /* wraps around to 0 */
    return 0;
}
```
```output
250
255
0
```

> ⚠️ For *signed* types, going past the limit is called **undefined behaviour** in C — anything can happen. The lesson: **choose a type big enough for your data** (e.g. don't store a population in a `short`).

---

## 2.6 Constants

Sometimes a value must **never change**: π, a tax rate, the number of days in a week. Two ways to make constants in C:

**1. The `const` qualifier** — a variable that cannot be modified after initialisation:

```c
const double PI = 3.14159;
// PI = 3.0;      <-- compile error: you cannot change a const
```

**2. The `#define` preprocessor command** — gives a name to a value; the preprocessor replaces the name with the value *before* compilation. No `=` and no `;`:

```c
#define VAT_RATE 0.15
```

By convention constants are written in **UPPER_CASE** so they stand out.

```c
#include <stdio.h>
#define VAT_RATE 0.15

int main(void)
{
    const double PI = 3.14159;
    double radius = 5.0;
    double price = 200.0;

    double area = PI * radius * radius;
    double vat = price * VAT_RATE;

    printf("Area of the circle: %.2f\n", area);
    printf("VAT on GHS %.2f is GHS %.2f\n", price, vat);
    return 0;
}
```
```output
Area of the circle: 78.54
VAT on GHS 200.00 is GHS 30.00
```

> 💡 **Why bother?** If the VAT rate changes, you change **one line** instead of hunting for `0.15` all over your program. A named constant also tells the reader *what* the number means. (Numbers like `0.15` buried in code are called "magic numbers" — avoid them.)

Also remember **literals** — values written directly in the code: `25` (int), `3.14` (double), `'A'` (char), `"Kumasi"` (string).

---

## 2.7 Type-casting (type conversion)

**Type-casting** means converting a value from one data type to another. Why do we need it?

- **Compatibility** — values of different types sometimes have to work together.
- **Correctness of operations** — the *type* decides *how* an operation behaves.
- **Saving memory** — sometimes you can store a value in a smaller type.

### The surprise: `9 / 2` is `4`

```c
#include <stdio.h>

int main(void)
{
    int x = 9;
    int y = 2;
    int sum = x / y;

    printf("%d\n", sum);
    return 0;
}
```
```output
4
```

When **both** operands are integers, C performs **integer division**: it throws away the fractional part (it does *not* round). So `9 / 2` is `4`, and `1 / 2` is `0`. This catches *every* beginner at least once.

There are two kinds of conversion.

### 2.7.1 Implicit (automatic) conversion

The compiler converts for you, silently.

- **int → float / double** (the value is kept): `float f = 6;` stores `6.000000`. One catch: a `float` holds only about 7 significant digits, so a *very large* `int` such as 16 777 217 cannot be stored exactly in a `float` (Ex 2.45). A `double` holds every `int` value exactly.
- **float → int** (information lost — the decimal part is **cut off**, not rounded): `int x = 9.99;` stores `9`.

```c
#include <stdio.h>

int main(void)
{
    float f = 6;            /* int  -> float */
    int   x = 9.99;         /* float -> int: the .99 is chopped off */
    float y = 3 / 2;        /* 3/2 is computed as integers FIRST (= 1), then converted */

    printf("%f\n", f);
    printf("%d\n", x);
    printf("%f\n", y);
    return 0;
}
```
```output
6.000000
9
1.000000
```

Look at the last one carefully. We wanted `1.5` but got `1.000000`: the division `3 / 2` happens **before** the result is stored in a `float`. Storing it in a `float` does not rescue the lost `.5`. (The compiler may print a *warning* about `int x = 9.99;` — listen to it!)

**Mixed expressions.** When an operation involves different types, C **promotes** the "smaller" one to the "bigger" one: `int` + `double` → `double`. So `3 / 2.0` is `1.5`, because `2.0` is a double and so `3` is converted to `3.0` first.

### 2.7.2 Explicit conversion (the cast operator)

You take control by writing the **new type in parentheses** in front of the value:

```
(type) value
```

```c
#include <stdio.h>

int main(void)
{
    int a = 3, b = 2;

    float c = (float) a / b;          /* a becomes 3.0, then 3.0 / 2 = 1.5 */
    float d = (float)(a / b);         /* 3 / 2 = 1 first, THEN converted to 1.0 */

    printf("%f\n", c);
    printf("%f\n", d);
    return 0;
}
```
```output
1.500000
1.000000
```

Study the difference between `c` and `d`. **Where you put the cast matters.**

- `(float) a / b` — the cast applies to **`a` only** (a cast is "tighter" than `/`). Then `float / int` → `float` division → `1.5` ✔.
- `(float)(a / b)` — the division happens first (integer division → `1`), then the **result** is cast. Too late! ✘

The same idea works on a variable: `(float) a`, `(int) price`, `(char) 66`.

### Rounding a double to the nearest integer

Casting to `int` *truncates*. To round to the nearest whole number (for positive values), add `0.5` first:

```c
double mark = 67.6;
int truncated = (int) mark;          /* 67 */
int rounded   = (int)(mark + 0.5);   /* 68 */
```

### Summary of the traps

| You write | You get | Why |
|---|---|---|
| `9 / 2` | `4` | integer ÷ integer = integer |
| `9 / 2.0` | `4.5` | one operand is double |
| `(float) 9 / 2` | `4.5` | cast `9` first |
| `(float)(9 / 2)` | `4.0` | cast **after** integer division |
| `int n = 7.9;` | `7` | truncation, not rounding |

---

## 2.8 Naming and style tips

- Choose **meaningful names**: `totalMarks`, not `tm`; `radius`, not `r2`.
- Declare variables **close to where you first use them** (modern C allows this) and **always initialise** them.
- Use `double` for real numbers; use `int` for counting.
- Use `const` or `#define` for fixed values.
- One idea per variable: don't reuse a variable for two unrelated purposes.

---

## Key takeaways

- A **variable** is a named place in memory that holds a value. **Declare** it before use: `type name;` or `type name = value;`.
- The four basic types: **`int`** (whole numbers), **`char`** (one character, stored as a small number), **`float`** and **`double`** (decimals; `double` more precise).
- **Qualifiers:** `short`, `long` (size); `signed`, `unsigned` (sign — only for `int`/`char`). One from each group may be combined.
- Use **`sizeof`** and **`<limits.h>`** to find real sizes and limits on your machine.
- **Constants:** `const double PI = 3.14;` or `#define RATE 0.15`.
- **Integer ÷ integer = integer** (`9 / 2 = 4`).
- **Implicit conversion:** int → double keeps the value; float/double → int **truncates** (cuts off the decimals).
- **Explicit cast:** `(float) a / b`. *Where* you put the cast matters.

---

# Exercises — Chapter 2

## Part A — Quick check

**Ex 2.1** In your own words, what is a variable? What three things does every variable have?

**Ex 2.2** What is the difference between *declaring* a variable and *initialising* it?

**Ex 2.3** Name the four basic data types and give one example value for each.

**Ex 2.4** Which of these declarations are **invalid**? Explain each mistake.

```c
(a) int 2x;
(b) float price = 3,50;
(c) char c = "A";
(d) double d = 1.5e3;
(e) long unsigned int n = 5;
(f) unsigned float f = 2.5;
(g) short long x;
(h) int a, b = 3, c;
(i) char name = 'Kofi';
(j) float f = 22.442e2;
```

**Ex 2.5** Choose the **best data type** for each:

1. A student's age
2. A student's CWA (e.g. 73.98)
3. A grade letter (A, B, C…)
4. The price of a loaf of bread
5. The number of people in Ghana (about 33 million)
6. Whether the answer is `'y'` or `'n'`
7. The number of books in a school library (never negative)

**Ex 2.6** What is the difference between `float` and `double`?

**Ex 2.7** Why are `short` and `long` not used together? Which qualifiers can be combined?

**Ex 2.8** True or false?
1. `signed` and `unsigned` can be applied to `float`.
2. A `char` is stored internally as a number.
3. `int x = 9.99;` stores `10` in `x`.
4. `'A'` and `"A"` mean the same thing.
5. `const` variables can be changed later in the program.
6. `sizeof(char)` is always 1.

**Ex 2.9** What is the ASCII code of `'A'`? What do you think it is for `'B'`? For `'a'`? For `'0'`?

**Ex 2.10** Why does `float y = 3 / 2;` store `1.0` and not `1.5`?

## Part B — Predict the output

*(Assume each fragment sits inside `main` and `<stdio.h>` is included.)*

**Ex 2.11**
```c
int a = 7, b = 2;
printf("%d\n", a / b);
```

**Ex 2.12**
```c
float f = 7 / 2;
printf("%f\n", f);
```

**Ex 2.13**
```c
float f = 7 / 2.0;
printf("%.2f\n", f);
```

**Ex 2.14**
```c
int a = 7, b = 2;
float r = (float) a / b;
printf("%.1f\n", r);
```

**Ex 2.15**
```c
int a = 7, b = 2;
float r = (float)(a / b);
printf("%.1f\n", r);
```

**Ex 2.16**
```c
char c = 'C';
printf("%c %d\n", c, c);
printf("%c\n", c + 2);
```
*(Hint: `'A'` is 65.)*

**Ex 2.17**
```c
int x = 5;
x = x + 1.9;
printf("%d\n", x);
```

**Ex 2.18**
```c
unsigned char c = 253;
c = c + 4;
printf("%d\n", c);
```

**Ex 2.19**
```c
double d = 5 / 2;
printf("%.2f\n", d);
```

**Ex 2.20**
```c
int a = 10;
int b = a;
a = 20;
printf("%d %d\n", a, b);
```

**Ex 2.21**
```c
char digit = '5';
int n = digit - '0';
printf("%d\n", n * 2);
```

**Ex 2.22**
```c
double mark = 67.6;
printf("%d %d\n", (int) mark, (int)(mark + 0.5));
```

## Part C — Find and fix the bugs

**Ex 2.23** The program should print the area of a rectangle, but won't compile.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    length = 8;
    width = 5;
    int area = length * width;
    printf("%d\n", area);
    return 0;
}
```

**Ex 2.24** The average of 7 and 8 should be `7.5`, but the program prints `7.000000`. Fix it in **two** different ways.
```c
#include <stdio.h>
int main(void)
{
    int a = 7, b = 8;
    float avg = (a + b) / 2;
    printf("%f\n", avg);
    return 0;
}
```

**Ex 2.25** This program has a hidden bug. On some computers it prints `4`; on others it prints a strange number. Find the mistake.
```c
#include <stdio.h>
int main(void)
{
    int total;
    int apples = 4;
    total = total + apples;
    printf("%d\n", total);
    return 0;
}
```

**Ex 2.26** Why does the compiler complain?
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    const int DAYS = 7;
    DAYS = 8;
    printf("%d\n", DAYS);
    return 0;
}
```

**Ex 2.27** Find **three** mistakes.
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    int age = 20
    char grade = "B";
    float cgpa == 3.5;
    printf("%d %c %f\n", age, grade, cgpa);
    return 0;
}
```

**Ex 2.28** The program should print the price **including 12.5% tax**, which is `112.50`. It prints `112.00`. Why? Fix it.
```c
#include <stdio.h>
int main(void)
{
    int price = 100;
    int taxRate = 12.5;
    double total = price + price * taxRate / 100;
    printf("Total: %.2f\n", total);
    return 0;
}
```
*(Hint: this one is subtle. The arithmetic is fine. Look at what happens to the `12.5` on the line where `taxRate` is created.)*

## Part D — Write the program

**Ex 2.29** Declare variables for a student: age (`int`), CWA (`double`), grade (`char`) and level (`int`). Initialise them with your own data and print them, one per line.

**Ex 2.30** Declare `length` and `width` (integers). Compute and print the **area** and the **perimeter** of the rectangle.

**Ex 2.31** Declare `radius` as a `double` and use a `const` for π (3.14159). Print the **circumference** and the **area** of the circle with 2 decimals.

**Ex 2.32** Convert a temperature in **°C to °F** (`F = C × 9 / 5 + 32`). Start with `double celsius = 37.5;`. *(Watch out for integer division!)*

**Ex 2.33** Read-free practice: store three test marks as **integers** (e.g. 78, 85, 91). Compute and print their **average** as a decimal number with 2 decimals, using a cast.

**Ex 2.34** Swap the values of two variables `a = 5` and `b = 9` using a **third** variable. Print the values before and after.

**Ex 2.35** Compute **simple interest**: `I = P × R × T / 100` with `P = 2500.00` (GHS), `R = 8.5` (percent) and `T = 3` (years). Print the interest and the total amount.

**Ex 2.36** Print the **ASCII codes** of the characters `'A'`, `'a'`, `'0'` and the space `' '`. Then print the character that comes **after** `'K'`.

**Ex 2.37** Convert **GHS to USD**: store the exchange rate in a constant (use 0.065 USD per GHS) and convert GHS 1500. Print the answer with 2 decimals.

**Ex 2.38** A shop sells 3 items at GHS 12.50, GHS 8.25 and GHS 4.75, and the buyer takes **quantities** 2, 4 and 6 respectively. Compute the **total cost** and the **average price per item bought** (total cost ÷ total number of items). Choose sensible types.

**Ex 2.39** Compute the **BMI** (body-mass index) = `weight(kg) / (height(m) × height(m))` for weight `68` kg (int) and height `1.75` m (double). Print the result with 1 decimal.

**Ex 2.40** Print the **limits** of `short`, `int` and `unsigned char` using `<limits.h>`.

**Ex 2.41** Print a small **table** of the sizes of `char`, `short`, `int`, `long`, `long long`, `float` and `double` on **your** machine using `sizeof`.

**Ex 2.42** Convert **kilometres to miles** (1 km = 0.621371 mi) for `42.195` km (a marathon), and convert **70 miles per hour** to **km/h**. Use constants.

**Ex 2.43** A trotro ticket costs GHS 3.50. A passenger pays with a GHS 10 note. Using variables, compute and print the **change** and the **percentage** of the note that the fare represents (fare ÷ note × 100).

## Part E — Challenges

**Ex 2.44 (the 0.1 puzzle)** Store `0.1 + 0.2` in a `double` and print it with `%.17g`. Is it exactly `0.3`? Explain what you see.

**Ex 2.45 (float runs out of digits)** Put the integer `16777217` into a `float` and print it with `%.0f`. What do you get? Compare with a `double`. Explain.

**Ex 2.46 (digit to number and back)** Given `char c = '7';`, (a) convert it to the integer `7`, (b) add 2 to it, and (c) convert the result back to a **character** and print it with `%c`.

**Ex 2.47 (case shift)** The ASCII codes of lowercase letters are **32 more** than their uppercase partners. Using only arithmetic on a `char` (no library functions), convert `'g'` to `'G'` and `'M'` to `'m'`.

**Ex 2.48 (overflow detective)** Declare `unsigned short s = 65535;` then add 1 and print it. Then declare `unsigned int u = 0;`, subtract 1 and print it with `%u`. Explain both results.

**Ex 2.49 (two-digit surprise)** Let `int n = 47;`. Without using `%` (which you meet next chapter), compute the **tens digit** (`4`) by using integer division and then the **units digit** (`7`) by using subtraction.

## Part F — Research tasks

**Ex 2.50** Find out what the header **`<stdint.h>`** offers (types like `int8_t`, `uint32_t`). Why might an engineer prefer them over plain `int`?

**Ex 2.51** Look up the difference between the `%f`, `%e` and `%g` placeholders in `printf`. Print `1234.5678` with all three.

**Ex 2.52** The slides mention the **preprocessor** (`#include`, `#define`). Read about it and list **three** other preprocessor commands.

---

*End of Chapter 2. Next: [Chapter 3 — Operators](03-operators.md)*
