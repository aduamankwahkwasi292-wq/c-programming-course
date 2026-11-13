# Solutions — Chapter 3: Operators

> Back to the lesson: [Chapter 3 lesson](../lessons/03-operators.md)

---

## Part A — Quick check

**Ex 3.1** An **operand** is a value that an operator works on (in `5 + 3`, the operands are `5` and `3`). Unary: `-x` (or `!x`, `i++`). Binary: `+` (or `*`, `>`, `&&` …). Ternary: `? :`.

**Ex 3.2** `%` gives the **remainder** after integer division (`17 % 5` is `2`). It works on **integers only**.

**Ex 3.3**
- `b = a++;` with `a = 5`: `b` gets **5**, then `a` becomes **6**.
- `b = ++a;` with `a = 5`: `a` becomes **6** first, then `b` gets **6**.

**Ex 3.4** They give **`1`** (true) or **`0`** (false). In C, **any non-zero value** counts as true, and only `0` is false.

**Ex 3.5** `=` is **assignment** (store the right value into the left variable). `==` is **comparison** (ask whether two values are equal; result 1 or 0).

**Ex 3.6** C evaluates `&&` and `||` from left to right and **stops as soon as the result is certain**. Example: `(x != 0) && (10 / x > 1)` — if `x` is `0`, the left side is false, so the right side (the division by zero) is never executed.

**Ex 3.7** **Precedence** decides which of *different* operators goes first: in `2 + 3 * 4`, `*` goes before `+`, so the answer is 14. **Associativity** decides the order among operators of the *same* level: in `100 / 10 * 10`, `/` and `*` tie, and the direction is left → right, giving `(100 / 10) * 10 = 100`.

**Ex 3.8** `x += 4;` is `x = x + 4;` and `x %= 3;` is `x = x % 3;`.

**Ex 3.9** `(x > 10) ? 1 : 0` (the bare expression `x > 10` already evaluates to 1 or 0, but the conditional form shows the idea).

**Ex 3.10**

| A | B | `A && B` | `A \|\| B` | `!A` |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

**Ex 3.11**
1. **False** — `7 / 2` is `3` (integer division).
2. **True.**
3. **False** — `5 > 3 > 1` is `(5 > 3) > 1` = `1 > 1` = `0`.
4. **True** — `!0` is `1`.
5. **True** — a left shift by one doubles the value (as long as it doesn't overflow).
6. **False** — typically 4, but the size depends on the machine/compiler.

---

## Part B — Predict the output

**Ex 3.12** `3 2` (17 = 5 × 3 + 2)

**Ex 3.13** `-3 -2` (division truncates toward zero; the remainder takes the sign of the left operand)

**Ex 3.14**
```output
3
3.40
3.40
3.00
```
The last line: `(double)(17 / 5)` does the integer division first (3), then converts → `3.00`. Casting *after* is too late.

**Ex 3.15** `5 6` — postfix: `a++ + 2` uses 4, so `b = 6`, and then `a` becomes 5.

**Ex 3.16** `5 7` — prefix: `a` becomes 5 first; `b = 5 + 2 = 7`.

**Ex 3.17** `5`. Trace: 10 → `+= 5` → 15 → `*= 2` → 30 → `-= 10` → 20 → `/= 4` → **5**.

**Ex 3.18** `12 7`. Right to left: `b -= 3` makes `b = 7` (value 7), then `a += 7` makes `a = 12`.

**Ex 3.19** `1 0 1`

**Ex 3.20**
```output
1
1
0
0
```
(1) `(3 < 7)` is 1 and `(7 < 10)` is 1 → 1. (2) `(3 > 7)` is 0 but `(7 == 7)` is 1 → 1. (3) `!(1)` → 0. (4) `a` is 3 (non-zero = true), so `!a` is 0.

**Ex 3.21** `0 5` — `a != 0` is false, so `&&` short-circuits and `b++` **never runs**; `b` stays 5.

**Ex 3.22**
```output
1
1
```
`15 % 3 == 0` and `15 % 5 == 0` are both true → 1. `15 % 2 == 0` is false, but `15 > 10` is true → 1.

**Ex 3.23** `8 -100`

**Ex 3.24**
```output
9
10
2
2
9
```
(1) `3*4=12`, `2+12-5=9`. (2) left to right: `20/4=5`, `5*2=10`. (3) `(7-3)-2 = 2`. (4) `*` and `%` tie, left to right: `(2*3)%4 = 6%4 = 2`. (5) brackets first: `3*3=9`.

**Ex 3.25**
```output
1
7
6
16
25
```
`5 = 101`, `3 = 011`: AND → `001` = 1; OR → `111` = 7; XOR → `110` = 6. `1 << 4` = 16. `100 >> 2` = 100 ÷ 4 = 25.

**Ex 3.26**
```output
0
1
```
(1) `(10 > 5) > 2` → `1 > 2` → 0. (2) `&&` before `||`: `((1+1 == 2) && (3 > 5)) || (4 < 9)` → `(1 && 0) || 1` → 1.

---

## Part C — Find and fix the bugs

**Ex 3.27** `(a + b) / 2` is `15 / 2` — **integer** division → `7`, which is *then* stored as `7.0`. Fix by making one operand a decimal:
```c
#include <stdio.h>

int main(void)
{
    int a = 7, b = 8;
    double avg = (a + b) / 2.0;
    printf("%.1f\n", avg);
    return 0;
}
```
```output
7.5
```

**Ex 3.28** `1 < x < 10` is read as `(1 < x) < 10`; `(1 < x)` is 0 or 1, and both are less than 10, so the result is **always 1**. Fix: `int ok = (x > 1) && (x < 10);`

**Ex 3.29** `==` has higher precedence than `&`, so `n & 1 == 0` is `n & (1 == 0)` = `n & 0` = `0`. Fix: `(n & 1) == 0`.

**Ex 3.30** `count =+ 1;` is parsed as `count = +1;` (assign *positive one*). The two characters are in the wrong order. Write `count += 1;` (or `count++;`).

**Ex 3.31** `%` is only for integers; `d` is a `double`. Fix 1 — convert to int first: `int r = (int) d % 3;`. Fix 2 — use the library function `fmod` from `<math.h>`, which does the remainder for decimals.
```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double d = 10.5;
    int r1 = (int) d % 3;           /* 10 % 3 = 1          */
    double r2 = fmod(d, 3);         /* 10.5 - 3*3 = 1.5    */
    printf("%d %.1f\n", r1, r2);
    return 0;
}
```
```output
1 1.5
```

**Ex 3.32** `i` is changed twice inside one expression, with no rule about which change is seen first — **undefined behaviour**. Make each step its own statement:
```c
#include <stdio.h>

int main(void)
{
    int i = 5;
    int first = i++;      /* first = 5, i = 6  */
    int second = ++i;     /* i = 7, second = 7 */
    int r = first + second;
    printf("%d\n", r);
    return 0;
}
```
```output
12
```

**Ex 3.33** "Not 5 **and** not 6" needs `&&`. With `||` the expression is always true (a number cannot equal both 5 and 6 at the same time, so at least one `!=` is always true).
```c
int ok = (x != 5) && (x != 6);
```

---

## Part D — Write the program

**Ex 3.34**
```c
#include <stdio.h>

int main(void)
{
    int a = 17, b = 5;

    printf("sum        = %d\n", a + b);
    printf("difference = %d\n", a - b);
    printf("product    = %d\n", a * b);
    printf("quotient   = %d\n", a / b);
    printf("remainder  = %d\n", a % b);
    printf("real quot. = %.2f\n", (double) a / b);
    return 0;
}
```
```output
sum        = 22
difference = 12
product    = 85
quotient   = 3
remainder  = 2
real quot. = 3.40
```

**Ex 3.35**
```c
#include <stdio.h>

int main(void)
{
    int n = 28;

    printf("even?            %d\n", n % 2 == 0);
    printf("divisible by 7?  %d\n", n % 7 == 0);
    printf("last digit       %d\n", n % 10);
    return 0;
}
```
```output
even?            1
divisible by 7?  1
last digit       8
```

**Ex 3.36**
```c
#include <stdio.h>

int main(void)
{
    int total = 3725;

    int hours = total / 3600;
    int minutes = (total % 3600) / 60;
    int seconds = total % 60;

    printf("%d s = %d h %d min %d s\n", total, hours, minutes, seconds);
    return 0;
}
```
```output
3725 s = 1 h 2 min 5 s
```
Check: 3600 + 120 + 5 = 3725 ✔.

**Ex 3.37**
```c
#include <stdio.h>

int main(void)
{
    int pesewas = 235;

    printf("GHS %d and %d p\n", pesewas / 100, pesewas % 100);
    return 0;
}
```
```output
GHS 2 and 35 p
```

**Ex 3.38**
```c
#include <stdio.h>

int main(void)
{
    int n = 437;

    int hundreds = n / 100;
    int tens = (n / 10) % 10;
    int units = n % 10;

    printf("Hundreds: %d\n", hundreds);
    printf("Tens    : %d\n", tens);
    printf("Units   : %d\n", units);
    printf("Sum     : %d\n", hundreds + tens + units);
    return 0;
}
```
```output
Hundreds: 4
Tens    : 3
Units   : 7
Sum     : 14
```

**Ex 3.39**
```c
#include <stdio.h>

int main(void)
{
    int n = 1234;

    int d1 = n % 10;            /* 4 */
    int d2 = (n / 10) % 10;     /* 3 */
    int d3 = (n / 100) % 10;    /* 2 */
    int d4 = n / 1000;          /* 1 */

    int reversed = d1 * 1000 + d2 * 100 + d3 * 10 + d4;

    printf("%d reversed is %d\n", n, reversed);
    return 0;
}
```
```output
1234 reversed is 4321
```
(In Chapter 5, a loop will let you do this for a number with *any* number of digits.)

**Ex 3.40**
```c
#include <stdio.h>

int main(void)
{
    int a = 5, b = 9;

    /* swap with + and - */
    a = a + b;      /* 14 */
    b = a - b;      /* 5  */
    a = a - b;      /* 9  */
    printf("after +/- swap: a = %d, b = %d\n", a, b);

    /* swap with XOR */
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    printf("after XOR swap: a = %d, b = %d\n", a, b);
    return 0;
}
```
```output
after +/- swap: a = 9, b = 5
after XOR swap: a = 5, b = 9
```
Why XOR works: `x ^ y ^ y` is `x` (XOR-ing the same value twice cancels out). In practice, use a third variable — it is clearer, and as fast.

**Ex 3.41**
```c
#include <stdio.h>

int main(void)
{
    int a = 17, b = 42, c = 30;

    int larger = (a > b) ? a : b;
    int largest = (larger > c) ? larger : c;

    printf("larger of %d and %d : %d\n", a, b, larger);
    printf("largest of the three : %d\n", largest);
    return 0;
}
```
```output
larger of 17 and 42 : 42
largest of the three : 42
```

**Ex 3.42**
```c
#include <stdio.h>

int main(void)
{
    int x = -17, y = 23;

    printf("|%d| = %d\n", x, (x < 0) ? -x : x);
    printf("|%d| = %d\n", y, (y < 0) ? -y : y);
    return 0;
}
```
```output
|-17| = 17
|23| = 23
```

**Ex 3.43** A year is a leap year if it is divisible by 4 **but not** by 100 — **or** it is divisible by 400.
```c
#include <stdio.h>

int main(void)
{
    int year;

    year = 1900;
    printf("%d -> %d\n", year, (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
    year = 2000;
    printf("%d -> %d\n", year, (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
    year = 2023;
    printf("%d -> %d\n", year, (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
    year = 2024;
    printf("%d -> %d\n", year, (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
    return 0;
}
```
```output
1900 -> 0
2000 -> 1
2023 -> 0
2024 -> 1
```
(Notice the same long expression pasted four times. That repetition is what *functions* fix in Chapter 6.)

**Ex 3.44**
```c
#include <stdio.h>

int main(void)
{
    char ch = 'g';

    printf("lowercase? %d\n", ch >= 'a' && ch <= 'z');
    printf("uppercase? %d\n", ch >= 'A' && ch <= 'Z');
    printf("digit?     %d\n", ch >= '0' && ch <= '9');
    return 0;
}
```
```output
lowercase? 1
uppercase? 0
digit?     0
```
Change `ch` to `'G'` (→ `0 1 0`) and `'5'` (→ `0 0 1`) and re-run.

**Ex 3.45**
```c
#include <stdio.h>

int main(void)
{
    int a = 3, b = 4, c = 5;
    printf("(3,4,5) -> %d\n", (a + b > c) && (a + c > b) && (b + c > a));

    a = 1; b = 2; c = 5;
    printf("(1,2,5) -> %d\n", (a + b > c) && (a + c > b) && (b + c > a));
    return 0;
}
```
```output
(3,4,5) -> 1
(1,2,5) -> 0
```

**Ex 3.46**
```c
#include <stdio.h>

int main(void)
{
    int age = 8;
    printf("age %d pays GHS %d\n", age, (age < 12) ? 5 : 10);

    age = 30;
    printf("age %d pays GHS %d\n", age, (age < 12) ? 5 : 10);
    return 0;
}
```
```output
age 8 pays GHS 5
age 30 pays GHS 10
```

**Ex 3.47**
```c
#include <stdio.h>

int main(void)
{
    int a = 1, b = -3, c = 2;
    int disc = b * b - 4 * a * c;

    printf("discriminant = %d\n", disc);
    printf("real roots?    %d\n", disc >= 0);
    return 0;
}
```
```output
discriminant = 1
real roots?    1
```

**Ex 3.48**
```c
#include <stdio.h>

int main(void)
{
    int hour = 14, minute = 50;
    int add = 135;

    int totalMinutes = hour * 60 + minute + add;   /* 890 + 135 = 1025 */
    int newHour = (totalMinutes / 60) % 24;        /* % 24 keeps it on the clock */
    int newMinute = totalMinutes % 60;

    printf("%02d:%02d\n", newHour, newMinute);
    return 0;
}
```
```output
17:05
```
(`%02d` prints at least 2 digits, padding with `0` — more in Chapter 4.)

**Ex 3.49**
```c
#include <stdio.h>

int main(void)
{
    int n = 47;
    printf("%d -> %d\n", n, ((n + 5) / 10) * 10);

    n = 42;
    printf("%d -> %d\n", n, ((n + 5) / 10) * 10);
    return 0;
}
```
```output
47 -> 50
42 -> 40
```

**Ex 3.50**
```c
#include <stdio.h>

int main(void)
{
    printf("13 * 8   = %d\n", 13 << 3);     /* 8 = 2^3 */
    printf("200 / 4  = %d\n", 200 >> 2);    /* 4 = 2^2 */
    printf("2^10     = %d\n", 1 << 10);
    return 0;
}
```
```output
13 * 8   = 104
200 / 4  = 50
2^10     = 1024
```

**Ex 3.51**
```c
#include <stdio.h>

int main(void)
{
    int n = 40;                               /* 101000 */

    printf("bit 3 set?   %d\n", (n >> 3) & 1);
    printf("set bit 0:   %d\n", n | (1 << 0));
    printf("clear bit 3: %d\n", n & ~(1 << 3));
    printf("toggle bit 5:%d\n", n ^ (1 << 5));
    return 0;
}
```
```output
bit 3 set?   1
set bit 0:   41
clear bit 3: 32
toggle bit 5:8
```
Check: 40 = 32 + 8 → bits 5 and 3 are on. Set bit 0 → +1 = 41. Clear bit 3 → 32. Toggle bit 5 (turn it off) → 8.

**Ex 3.52**
```c
#include <stdio.h>

int main(void)
{
    double pay = 1200;
    double sales = 8000;

    pay += sales * 5 / 100;

    printf("Pay = GHS %.2f\n", pay);
    return 0;
}
```
```output
Pay = GHS 1600.00
```

---

## Part E — Challenges

**Ex 3.53**
```c
#include <stdio.h>

int main(void)
{
    int n;

    n = 64;
    printf("%d -> %d\n", n, (n & (n - 1)) == 0);
    n = 100;
    printf("%d -> %d\n", n, (n & (n - 1)) == 0);
    return 0;
}
```
```output
64 -> 1
100 -> 0
```
*Why it works:* a power of two has **exactly one** `1` bit. Subtracting 1 turns that bit into `0` and all the bits below it into `1`s, so the two patterns share no `1`s:
```
 64 = 1000000        100 = 1100100
 63 = 0111111         99 = 1100011
 &    0000000         &    1100000   (= 96, not 0)
```

**Ex 3.54** Thursday is `3`, so `(3 + 100) % 7`:
```c
#include <stdio.h>

int main(void)
{
    int today = 3;                    /* Mon=0 ... Sun=6 */
    int later = (today + 100) % 7;    /* 103 % 7 = 5 */
    printf("day number = %d\n", later);
    return 0;
}
```
```output
day number = 5
```
Day 5 is **Saturday** (Mon 0, Tue 1, Wed 2, Thu 3, Fri 4, Sat 5). (100 days = 14 weeks + 2 days, and Thursday + 2 days = Saturday.)

**Ex 3.55**
```c
#include <stdio.h>

int main(void)
{
    char lower = 'g';
    char upper = 'M';

    printf("%c\n", lower & ~32);     /* clear bit 5 -> uppercase */
    printf("%c\n", upper | 32);      /* set bit 5   -> lowercase */
    return 0;
}
```
```output
G
m
```

**Ex 3.56**
```c
#include <stdio.h>

int main(void)
{
    double x = 0.1 + 0.2;
    double y = 0.3;

    int exactlyEqual = (x == y);
    int closeEnough = ((x > y ? x - y : y - x) < 0.000001);

    printf("x == y        : %d\n", exactlyEqual);
    printf("close enough  : %d\n", closeEnough);
    return 0;
}
```
```output
x == y        : 0
close enough  : 1
```

**Ex 3.57**
```c
#include <stdio.h>

int main(void)
{
    printf("1) %d\n", 5 + 3 * 2 - 8 / 4 % 3);
    printf("2) %d\n", 10 - 4 - 3 * 2);
    printf("3) %d\n", !5 + 3 > 2 && 1);
    printf("4) %d\n", (5 > 3) + (2 > 1) * 4);
    printf("5) %d\n", 7 & 3 + 1);
    return 0;
}
```
```output
1) 9
2) 0
3) 1
4) 5
5) 4
```
1. `3*2=6`; `8/4=2`, then `2%3=2`; `5+6-2 = 9`.
2. `(10-4)-6 = 0`.
3. `!5` is `0`; `0+3 = 3`; `3 > 2` is `1`; `1 && 1` is `1`.
4. `(1) + (1)*4 = 5`.
5. `+` is higher than `&`: `7 & (3+1)` = `7 & 4` = `4`.

**Ex 3.58**
```c
#include <stdio.h>

int main(void)
{
    int s;

    s = 85; printf("%d -> %c\n", s, s >= 80 ? 'A' : s >= 70 ? 'B' : s >= 60 ? 'C' : s >= 50 ? 'D' : 'F');
    s = 72; printf("%d -> %c\n", s, s >= 80 ? 'A' : s >= 70 ? 'B' : s >= 60 ? 'C' : s >= 50 ? 'D' : 'F');
    s = 61; printf("%d -> %c\n", s, s >= 80 ? 'A' : s >= 70 ? 'B' : s >= 60 ? 'C' : s >= 50 ? 'D' : 'F');
    s = 55; printf("%d -> %c\n", s, s >= 80 ? 'A' : s >= 70 ? 'B' : s >= 60 ? 'C' : s >= 50 ? 'D' : 'F');
    s = 20; printf("%d -> %c\n", s, s >= 80 ? 'A' : s >= 70 ? 'B' : s >= 60 ? 'C' : s >= 50 ? 'D' : 'F');
    return 0;
}
```
```output
85 -> A
72 -> B
61 -> C
55 -> D
20 -> F
```
This works but is hard to read and highly repetitive — a good case for `if/else` (Chapter 5) and functions (Chapter 6).

---

## Part F — Research tasks (sample answers)

**Ex 3.59** **De Morgan's laws:** `!(A && B)` equals `!A || !B`, and `!(A || B)` equals `!A && !B`. So `!(a > 5 && b < 3)` equals `(a <= 5) || (b >= 3)`.
```c
#include <stdio.h>

int main(void)
{
    int a, b;

    a = 7; b = 1;
    printf("%d %d\n", !(a > 5 && b < 3), (a <= 5) || (b >= 3));
    a = 7; b = 5;
    printf("%d %d\n", !(a > 5 && b < 3), (a <= 5) || (b >= 3));
    a = 2; b = 1;
    printf("%d %d\n", !(a > 5 && b < 3), (a <= 5) || (b >= 3));
    a = 2; b = 5;
    printf("%d %d\n", !(a > 5 && b < 3), (a <= 5) || (b >= 3));
    return 0;
}
```
```output
0 0
1 1
1 1
1 1
```
In every row the two columns match.

**Ex 3.60** `sizeof` returns a value of type **`size_t`** — an unsigned integer type that is guaranteed to be big enough to hold the size of any object. On 64-bit systems `size_t` is 8 bytes wide, so printing it with `%d` (which expects a 4-byte `int`) is technically wrong. `%zu` is the placeholder made for `size_t`.

**Ex 3.61** In **two's complement**, to store `-x` the computer flips all the bits of `x` and adds 1. So *flipping the bits* alone (`~x`) gives `-x - 1`. For `x = 12`: `~12 = -12 - 1 = -13` ✔.

---

*Next: [Chapter 4 solutions](04-data-input-and-output.md)*
