# Solutions — Chapter 2: Variables and Data Types

> Back to the lesson: [Chapter 2 lesson](../lessons/02-variables-and-data-types.md)

---

## Part A — Quick check

**Ex 2.1** A **variable** is a named storage space in the computer's memory that holds a piece of data. Every variable has: a **name** (identifier), a **type** (what kind of data and how much memory) and a **value** (what is currently stored). (It also has an *address* — its location in memory — which you will use in Chapter 8.)

**Ex 2.2** *Declaring* means telling the compiler the variable's type and name so memory is reserved: `int age;`. *Initialising* means giving it its first value, usually at the same time: `int age = 24;`.

**Ex 2.3**

| Type | Example |
|---|---|
| `int` | `25` |
| `char` | `'y'` |
| `float` | `2.34f` |
| `double` | `23.99` |

**Ex 2.4** The invalid ones are:

- **(a)** `int 2x;` — a name cannot start with a digit.
- **(b)** `float price = 3,50;` — the comma is a separator, not a decimal point. Write `3.50`.
- **(c)** `char c = "A";` — double quotes make a **string**, not a char. Use `'A'`.
- **(f)** `unsigned float f = 2.5;` — `signed`/`unsigned` apply to `int` and `char` only.
- **(g)** `short long x;` — `short` and `long` are opposites.
- **(i)** `char name = 'Kofi';` — a `char` holds **one** character. (Four characters in single quotes is a "multi-character constant", a compiler warning and a bug. For names you need a *string* — Chapter 8.)

Valid: **(d)**, **(e)**, **(h)** (it declares `a`, `b` initialised to 3, and `c`), **(j)**.

**Ex 2.5**
1. `int`
2. `double` (or `float`)
3. `char`
4. `double` (or `float`) — prices have decimals
5. `int` fits 33 million (4-byte `int` goes up to about 2.1 billion); `unsigned int` or `long` are also fine
6. `char`
7. `unsigned int` (a count can never be negative) — plain `int` is also acceptable

**Ex 2.6** `float` is single precision: usually 4 bytes, about 6–7 reliable digits. `double` is double precision: usually 8 bytes, about 15–16 reliable digits. `double` is more precise but uses more memory.

**Ex 2.7** They are direct opposites (shorter vs longer), so combining them makes no sense. You **can** combine *one size qualifier and one sign qualifier*, e.g. `unsigned long int`.

**Ex 2.8**
1. **False** — only `int` and `char`.
2. **True** — as its ASCII code.
3. **False** — it stores **9** (the decimal part is cut off, not rounded).
4. **False** — `'A'` is one character (a number, 65); `"A"` is a string (Chapter 8).
5. **False** — a `const` cannot be changed after initialisation.
6. **True** — C guarantees it.

**Ex 2.9** `'A'` = **65**, `'B'` = **66**, `'a'` = **97**, `'0'` = **48**.

**Ex 2.10** Because `3` and `2` are both integers, `3 / 2` is evaluated as **integer division** = `1`. Only after that is `1` converted to `1.0` for storage in the `float`. The `.5` was already lost.

---

## Part B — Predict the output

**Ex 2.11** `3`   (7 ÷ 2 = 3, integer division)

**Ex 2.12** `3.000000`   (`7 / 2` is `3`, then converted)

**Ex 2.13** `3.50`   (`2.0` is a double, so the division is real division)

**Ex 2.14** `3.5`   (`(float) a` → 7.0, then 7.0 / 2 = 3.5)

**Ex 2.15** `3.0`   (`a / b` is `3` first, then cast to 3.0)

**Ex 2.16**
```output
C 67
E
```
`'C'` is 67. `c + 2` is 69, and as a character (`%c`) 69 is `'E'`.

**Ex 2.17** `6`   (`5 + 1.9 = 6.9`, then stored in an `int` → truncated to 6)

**Ex 2.18** `1`   (253 + 4 = 257, but an `unsigned char` holds 0–255, so it wraps: 257 − 256 = 1)

**Ex 2.19** `2.00`   (`5 / 2` is integer division = 2, *then* stored as 2.0)

**Ex 2.20** `20 10`   (`b` got a **copy** of `a`'s value. Changing `a` later does not affect `b`.)

**Ex 2.21** `10`   (`'5' - '0'` = 5, times 2)

**Ex 2.22** `67 68`   (`(int) 67.6` truncates to 67; `(int)(67.6 + 0.5)` = `(int) 68.1` = 68)

---

## Part C — Find and fix the bugs

**Ex 2.23** `length` and `width` were never declared. Declare them with a type:
```c
#include <stdio.h>
int main(void)
{
    int length = 8;
    int width = 5;
    int area = length * width;
    printf("%d\n", area);
    return 0;
}
```
```output
40
```

**Ex 2.24** `(a + b) / 2` is `15 / 2`, which is integer division → `7`. Two fixes:
```c
#include <stdio.h>
int main(void)
{
    int a = 7, b = 8;
    float avg1 = (a + b) / 2.0;          /* Fix 1: divide by a decimal number */
    float avg2 = (float)(a + b) / 2;     /* Fix 2: cast the sum before dividing */
    printf("%f\n", avg1);
    printf("%f\n", avg2);
    return 0;
}
```
```output
7.500000
7.500000
```
(Note: `(float)(a + b) / 2` casts the **sum** because of the extra brackets, so it is `15.0 / 2`.)

**Ex 2.25** `total` is **never initialised**; it contains garbage, and `total + apples` is garbage + 4. Fix: `int total = 0;`.

**Ex 2.26** `DAYS` is a `const`, so it cannot be assigned a new value after it is initialised (`assignment of read-only variable 'DAYS'`). Either remove the line `DAYS = 8;` or, if the value really has to change, don't make it `const`.

**Ex 2.27** Three mistakes:
1. `int age = 20` — missing semicolon.
2. `char grade = "B";` — double quotes; should be `'B'`.
3. `float cgpa == 3.5;` — `==` is *comparison*; use `=` for initialisation.

```c
#include <stdio.h>
int main(void)
{
    int age = 20;
    char grade = 'B';
    float cgpa = 3.5;
    printf("%d %c %f\n", age, grade, cgpa);
    return 0;
}
```
```output
20 B 3.500000
```

**Ex 2.28** The mistake is in `int taxRate = 12.5;` — an `int` cannot hold `12.5`, so it silently keeps **12** (truncation). The later arithmetic is fine, but it used 12% instead of 12.5%. Fix: make `taxRate` a `double`.
```c
#include <stdio.h>
int main(void)
{
    int price = 100;
    double taxRate = 12.5;
    double total = price + price * taxRate / 100;
    printf("Total: %.2f\n", total);
    return 0;
}
```
```output
Total: 112.50
```

---

## Part D — Write the program

**Ex 2.29**
```c
#include <stdio.h>

int main(void)
{
    int age = 20;
    double cwa = 73.98;
    char grade = 'B';
    int level = 100;

    printf("Age   : %d\n", age);
    printf("CWA   : %.2f\n", cwa);
    printf("Grade : %c\n", grade);
    printf("Level : %d\n", level);
    return 0;
}
```
```output
Age   : 20
CWA   : 73.98
Grade : B
Level : 100
```

**Ex 2.30**
```c
#include <stdio.h>

int main(void)
{
    int length = 8;
    int width = 5;

    int area = length * width;
    int perimeter = 2 * (length + width);

    printf("Area      = %d\n", area);
    printf("Perimeter = %d\n", perimeter);
    return 0;
}
```
```output
Area      = 40
Perimeter = 26
```

**Ex 2.31**
```c
#include <stdio.h>

int main(void)
{
    const double PI = 3.14159;
    double radius = 6.0;

    double circumference = 2 * PI * radius;
    double area = PI * radius * radius;

    printf("Circumference = %.2f\n", circumference);
    printf("Area          = %.2f\n", area);
    return 0;
}
```
```output
Circumference = 37.70
Area          = 113.10
```

**Ex 2.32** Using `double` and `9.0 / 5` (or `9 * celsius / 5`) avoids the `9 / 5 = 1` trap:
```c
#include <stdio.h>

int main(void)
{
    double celsius = 37.5;
    double fahrenheit = celsius * 9 / 5 + 32;

    printf("%.1f C = %.1f F\n", celsius, fahrenheit);
    return 0;
}
```
```output
37.5 C = 99.5 F
```
*Warning:* writing `celsius * (9 / 5) + 32` would be **wrong** — `(9 / 5)` is `1` in integer arithmetic, giving `69.5`.

**Ex 2.33**
```c
#include <stdio.h>

int main(void)
{
    int mark1 = 78, mark2 = 85, mark3 = 91;
    int sum = mark1 + mark2 + mark3;

    double average = (double) sum / 3;

    printf("Sum     = %d\n", sum);
    printf("Average = %.2f\n", average);
    return 0;
}
```
```output
Sum     = 254
Average = 84.67
```

**Ex 2.34**
```c
#include <stdio.h>

int main(void)
{
    int a = 5, b = 9, temp;

    printf("Before: a = %d, b = %d\n", a, b);

    temp = a;       /* keep a's value safe */
    a = b;          /* a gets b's value    */
    b = temp;       /* b gets the saved one */

    printf("After : a = %d, b = %d\n", a, b);
    return 0;
}
```
```output
Before: a = 5, b = 9
After : a = 9, b = 5
```
Think of two glasses of juice: to swap their contents you need an **empty third glass**.

**Ex 2.35**
```c
#include <stdio.h>

int main(void)
{
    double principal = 2500.00;
    double rate = 8.5;
    int years = 3;

    double interest = principal * rate * years / 100;
    double total = principal + interest;

    printf("Interest     : GHS %.2f\n", interest);
    printf("Total amount : GHS %.2f\n", total);
    return 0;
}
```
```output
Interest     : GHS 637.50
Total amount : GHS 3137.50
```

**Ex 2.36**
```c
#include <stdio.h>

int main(void)
{
    char a = 'A', b = 'a', c = '0', d = ' ';

    printf("'A' = %d\n", a);
    printf("'a' = %d\n", b);
    printf("'0' = %d\n", c);
    printf("' ' = %d\n", d);

    char k = 'K';
    printf("After 'K' comes '%c'\n", k + 1);
    return 0;
}
```
```output
'A' = 65
'a' = 97
'0' = 48
' ' = 32
After 'K' comes 'L'
```

**Ex 2.37**
```c
#include <stdio.h>

int main(void)
{
    const double USD_PER_GHS = 0.065;
    double ghs = 1500;
    double usd = ghs * USD_PER_GHS;

    printf("GHS %.2f = USD %.2f\n", ghs, usd);
    return 0;
}
```
```output
GHS 1500.00 = USD 97.50
```

**Ex 2.38** Prices are decimals → `double`; quantities are counts → `int`.
```c
#include <stdio.h>

int main(void)
{
    double price1 = 12.50, price2 = 8.25, price3 = 4.75;
    int qty1 = 2, qty2 = 4, qty3 = 6;

    double totalCost = price1 * qty1 + price2 * qty2 + price3 * qty3;
    int totalItems = qty1 + qty2 + qty3;
    double averagePrice = totalCost / totalItems;

    printf("Total cost         : GHS %.2f\n", totalCost);
    printf("Items bought       : %d\n", totalItems);
    printf("Average per item   : GHS %.2f\n", averagePrice);
    return 0;
}
```
```output
Total cost         : GHS 86.50
Items bought       : 12
Average per item   : GHS 7.21
```
(No cast is needed: `totalCost` is already a `double`, so the division is real division.)

**Ex 2.39**
```c
#include <stdio.h>

int main(void)
{
    int weight = 68;          /* kg */
    double height = 1.75;     /* m  */

    double bmi = weight / (height * height);

    printf("BMI = %.1f\n", bmi);
    return 0;
}
```
```output
BMI = 22.2
```

**Ex 2.40**
```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    printf("short : %d to %d\n", SHRT_MIN, SHRT_MAX);
    printf("int   : %d to %d\n", INT_MIN, INT_MAX);
    printf("unsigned char : 0 to %d\n", UCHAR_MAX);
    return 0;
}
```
```output
short : -32768 to 32767
int   : -2147483648 to 2147483647
unsigned char : 0 to 255
```

**Ex 2.41** *(Output shown for a typical Windows machine. On 64-bit Linux, `long` prints 8.)*
```c
#include <stdio.h>

int main(void)
{
    printf("Type\t\tBytes\n");
    printf("char\t\t%zu\n", sizeof(char));
    printf("short\t\t%zu\n", sizeof(short));
    printf("int\t\t%zu\n", sizeof(int));
    printf("long\t\t%zu\n", sizeof(long));
    printf("long long\t%zu\n", sizeof(long long));
    printf("float\t\t%zu\n", sizeof(float));
    printf("double\t\t%zu\n", sizeof(double));
    return 0;
}
```
```output
Type            Bytes
char            1
short           2
int             4
long            4
long long       8
float           4
double          8
```

**Ex 2.42**
```c
#include <stdio.h>

int main(void)
{
    const double MILES_PER_KM = 0.621371;
    const double KM_PER_MILE = 1.609344;

    double marathonKm = 42.195;
    double speedMph = 70;

    printf("%.3f km = %.2f miles\n", marathonKm, marathonKm * MILES_PER_KM);
    printf("%.0f mph = %.2f km/h\n", speedMph, speedMph * KM_PER_MILE);
    return 0;
}
```
```output
42.195 km = 26.22 miles
70 mph = 112.65 km/h
```

**Ex 2.43**
```c
#include <stdio.h>

int main(void)
{
    double fare = 3.50;
    double note = 10.00;

    double change = note - fare;
    double percent = fare / note * 100;

    printf("Change: GHS %.2f\n", change);
    printf("The fare is %.1f%% of the note\n", percent);
    return 0;
}
```
```output
Change: GHS 6.50
The fare is 35.0% of the note
```
(`%%` prints a real percent sign. You will see it again in Chapter 4.)

---

## Part E — Challenges

**Ex 2.44**
```c
#include <stdio.h>

int main(void)
{
    double sum = 0.1 + 0.2;
    printf("%.17g\n", sum);
    return 0;
}
```
```output
0.30000000000000004
```
It is **not** exactly `0.3`. Computers store numbers in binary, and `0.1` and `0.2` have no exact binary representation (like `1/3` has no exact decimal form: 0.3333…). Tiny rounding errors appear. Lesson: **never trust `==` to compare decimals** (you will see a better method in Chapter 3's exercises).

**Ex 2.45**
```c
#include <stdio.h>

int main(void)
{
    float f = 16777217;
    double d = 16777217;

    printf("float : %.0f\n", f);
    printf("double: %.0f\n", d);
    return 0;
}
```
```output
float : 16777216
double: 16777217
```
A `float` has only 24 bits for its significant digits, so it can only store *every* integer exactly up to 2²⁴ = 16 777 216. Beyond that it must round to a nearby representable value. A `double` (53 bits) is fine here.

**Ex 2.46**
```c
#include <stdio.h>

int main(void)
{
    char c = '7';

    int n = c - '0';                  /* (a) 7 */
    n = n + 2;                        /* (b) 9 */
    char back = (char)(n + '0');      /* (c) '9' */

    printf("%c\n", back);
    return 0;
}
```
```output
9
```

**Ex 2.47**
```c
#include <stdio.h>

int main(void)
{
    char lower = 'g';
    char upper = 'M';

    printf("%c\n", lower - 32);   /* 'g' is 103, 103 - 32 = 71 = 'G' */
    printf("%c\n", upper + 32);   /* 'M' is 77,  77 + 32 = 109 = 'm' */
    return 0;
}
```
```output
G
m
```

**Ex 2.48**
```c
#include <stdio.h>

int main(void)
{
    unsigned short s = 65535;
    s = s + 1;
    printf("%d\n", s);

    unsigned int u = 0;
    u = u - 1;
    printf("%u\n", u);
    return 0;
}
```
```output
0
4294967295
```
Both **wrap around** like an odometer: `65535 + 1` → `0` for a 2-byte unsigned type, and `0 − 1` → the largest 4-byte unsigned value.

**Ex 2.49**
```c
#include <stdio.h>

int main(void)
{
    int n = 47;
    int tens = n / 10;              /* integer division: 4 */
    int units = n - tens * 10;      /* 47 - 40 = 7 */

    printf("tens = %d, units = %d\n", tens, units);
    return 0;
}
```
```output
tens = 4, units = 7
```
(Next chapter you will learn that `n % 10` gives the units digit directly.)

---

## Part F — Research tasks (sample answers)

**Ex 2.50** `<stdint.h>` defines **fixed-size** integer types: `int8_t`, `int16_t`, `int32_t`, `int64_t` and their unsigned versions `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t`. A plain `int` or `long` can be a different size on different machines (as you saw with `long`). Engineers working with hardware registers, network protocols or file formats need to know *exactly* how many bits they have, so they use these types.

**Ex 2.51**
```c
#include <stdio.h>

int main(void)
{
    double x = 1234.5678;
    printf("%f\n", x);
    printf("%e\n", x);
    printf("%g\n", x);
    return 0;
}
```
```output
1234.567800
1.234568e+03
1234.57
```
`%f` = fixed decimal notation (6 decimals by default); `%e` = scientific notation; `%g` = whichever of the two is **shorter**, with 6 significant digits.

**Ex 2.52** Other preprocessor commands: `#undef` (remove a macro definition), `#ifdef` / `#ifndef` / `#endif` (include code only if a name is / is not defined), `#if` / `#else` / `#elif`, `#pragma` (compiler-specific instructions) and `#error` (stop compiling with a message).

---

*Next: [Chapter 3 solutions](03-operators.md)*
