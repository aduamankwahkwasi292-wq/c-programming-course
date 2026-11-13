# Chapter 3 — Operators

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `03 Operators.pdf`  
> **Solutions:** [Solutions to Chapter 3](../solutions/03-operators.md)

---

## What you will learn

1. What an **operator** and an **operand** are.
2. The **arithmetic**, **increment/decrement** and **assignment** operators.
3. The **relational** and **logical** operators — the tools for making decisions.
4. The **conditional (`?:`)**, **bitwise**, **comma** and **`sizeof`** operators.
5. How C decides **what to calculate first** — **precedence** and **associativity**.

---

## 3.1 What is an operator?

An **operator** is a symbol that tells the computer to do something with one or more values. The values it works on are called **operands**.

```
        5   +   3
        │   │   │
  operand  operator  operand
```

- A **unary** operator has **one** operand: `-x`, `!flag`, `i++`.
- A **binary** operator has **two** operands: `a + b`, `x > y`.
- The **ternary** operator has **three** operands: `cond ? a : b` (there is only one in C).

C has a rich set of operators. They are grouped like this:

| Group | Operators |
|---|---|
| Arithmetic | `+  -  *  /  %` |
| Increment / decrement | `++  --` |
| Assignment | `=  +=  -=  *=  /=  %=` … |
| Relational | `==  !=  >  <  >=  <=` |
| Logical | `&&  \|\|  !` |
| Conditional | `? :` |
| Bitwise | `&  \|  ^  ~  <<  >>` |
| Special | `,` (comma), `sizeof`, `&` (address-of), `*` (dereference) … |

---

## 3.2 Arithmetic operators

An **arithmetic operator** does mathematics on numbers (constants or variables).

| Operator | Meaning | Example (`A = 10`, `B = 5`) |
|---|---|---|
| `+` | addition (or unary plus) | `A + B` → `15` |
| `-` | subtraction (or unary minus) | `A - B` → `5` |
| `*` | multiplication | `A * B` → `50` |
| `/` | division | `A / B` → `2` |
| `%` | remainder after division (**modulo**) | `A % B` → `0` |

```c
#include <stdio.h>

int main(void)
{
    int A = 10, B = 5;

    printf("A + B = %d\n", A + B);
    printf("A - B = %d\n", A - B);
    printf("A * B = %d\n", A * B);
    printf("A / B = %d\n", A / B);
    printf("A %% B = %d\n", A % B);      /* to print a % sign write %% */
    return 0;
}
```
```output
A + B = 15
A - B = 5
A * B = 50
A / B = 2
A % B = 0
```

### Integer division

As you saw in Chapter 2: when **both** operands are integers, the result is an integer. The fractional part is **thrown away** (not rounded).

```c
#include <stdio.h>

int main(void)
{
    int a = 9, b = 4;

    printf("%d\n", a / b);               /* integer division  */
    printf("%d\n", a % b);               /* the part that was thrown away, as a remainder */
    printf("%.2f\n", (double) a / b);    /* real division     */
    return 0;
}
```
```output
2
1
2.25
```

`9 / 4` is `2` with a **remainder of `1`** (because 4 × 2 + 1 = 9). Division gives the *quotient*; `%` gives the *remainder*. They work as a pair.

### The modulus operator `%` — more useful than it looks

`%` works **only on integers**. Programmers use it all the time:

| Use | Expression | Example |
|---|---|---|
| Is `n` even? | `n % 2 == 0` | `4096 % 2` → `0` ✔ even |
| Last digit of `n` | `n % 10` | `4096 % 10` → `6` |
| Remove last digit | `n / 10` | `4096 / 10` → `409` |
| Wrap-around (clock, days of week) | `(x + k) % 12` | hours on a clock |
| Divisible by `d`? | `n % d == 0` | `15 % 5` → `0` |

```c
#include <stdio.h>

int main(void)
{
    int n = 4096;
    int minutes = 135;

    printf("last digit        : %d\n", n % 10);
    printf("without last digit: %d\n", n / 10);
    printf("%d minutes = %d h %d min\n", minutes, minutes / 60, minutes % 60);
    return 0;
}
```
```output
last digit        : 6
without last digit: 409
135 minutes = 2 h 15 min
```

**Negative numbers.** C truncates division **toward zero**, and the sign of `%` follows the **left** operand:

```c
#include <stdio.h>

int main(void)
{
    printf("%d\n", -7 / 2);
    printf("%d\n", -7 % 3);
    printf("%d\n", 7 % -3);
    return 0;
}
```
```output
-3
-1
1
```

> ⚠️ **Never divide (or `%`) by zero.** The program will crash (or behave unpredictably).
> ⚠️ `5 % 2.0` is a **compile error** — `%` needs integers on both sides.

---

## 3.3 Increment and decrement operators

Adding or subtracting **1** is so common that C has special operators:

| Operator | Name | Meaning |
|---|---|---|
| `++` | increment | add 1 |
| `--` | decrement | subtract 1 |

They are **unary** — they work on one variable.

```c
int a = 10, b = 20;
++a;        // a is now 11
--b;        // b is now 19
```

### Prefix versus postfix

Each can be written **before** (`++a`, **prefix**) or **after** (`a++`, **postfix**) the variable. By itself on a line there is no difference. But **inside a bigger expression** there is:

| Form | What happens |
|---|---|
| `b = ++a;` (prefix) | **first** increase `a`, **then** use the new value |
| `b = a++;` (postfix) | **first** use the current value, **then** increase `a` |

> 💡 **Memory aid:** *prefix* = "change first, use second". *postfix* = "use first, change second".

```c
#include <stdio.h>

int main(void)
{
    int a = 10, b, c;

    b = a++;                        /* b gets 10, THEN a becomes 11 */
    printf("a = %d, b = %d\n", a, b);

    c = ++a;                        /* a becomes 12 FIRST, then c gets 12 */
    printf("a = %d, c = %d\n", a, c);

    int x = 5;
    printf("%d\n", x--);            /* prints 5, then x becomes 4 */
    printf("%d\n", x);
    printf("%d\n", --x);            /* x becomes 3 first, then prints 3 */
    return 0;
}
```
```output
a = 11, b = 10
a = 12, c = 12
5
4
3
```

> ⚠️ **Do not use `++`/`--` on the same variable twice in one expression** (e.g. `i = i++ + ++i;`). C does not define the result — different compilers give different answers. Keep it simple: one `++` per statement.

---

## 3.4 Assignment operators

The basic assignment operator is `=`. C also has **compound** assignment operators — shorthand for "do an operation and store the result back":

| Operator | Example | Same as |
|---|---|---|
| `=` | `a = b` | `a = b` |
| `+=` | `a += b` | `a = a + b` |
| `-=` | `a -= b` | `a = a - b` |
| `*=` | `a *= b` | `a = a * b` |
| `/=` | `a /= b` | `a = a / b` |
| `%=` | `a %= b` | `a = a % b` |

```c
#include <stdio.h>

int main(void)
{
    int x = 10;

    x += 5;   printf("x += 5  -> %d\n", x);
    x -= 3;   printf("x -= 3  -> %d\n", x);
    x *= 2;   printf("x *= 2  -> %d\n", x);
    x /= 5;   printf("x /= 5  -> %d\n", x);
    x %= 3;   printf("x %%= 3  -> %d\n", x);
    return 0;
}
```
```output
x += 5  -> 15
x -= 3  -> 12
x *= 2  -> 24
x /= 5  -> 4
x %= 3  -> 1
```

Two details to remember:

1. The **right side is calculated completely first**: `x *= 2 + 3;` means `x = x * (2 + 3)`, **not** `x = x * 2 + 3`.
2. Assignment works **right to left**, so you can chain: `a = b = c = 0;` sets all three to 0.

Also, assignment is itself an expression with a value — the value that was stored. That is why `a = b = 5` works, and also why the next mistake is so common (see 3.5).

---

## 3.5 Relational operators

A **relational operator** compares two values. The answer is always:

- **`1`** if the relation is **true**
- **`0`** if the relation is **false**

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 3` | `0` |
| `!=` | not equal to | `5 != 3` | `1` |
| `>` | greater than | `5 > 3` | `1` |
| `<` | less than | `5 < 3` | `0` |
| `>=` | greater than or equal to | `5 >= 3` | `1` |
| `<=` | less than or equal to | `5 <= 3` | `0` |

```c
#include <stdio.h>

int main(void)
{
    printf("5 == 3 -> %d\n", 5 == 3);
    printf("5 != 3 -> %d\n", 5 != 3);
    printf("5 >  3 -> %d\n", 5 > 3);
    printf("5 <  3 -> %d\n", 5 < 3);
    printf("5 >= 5 -> %d\n", 5 >= 5);
    printf("5 <= 3 -> %d\n", 5 <= 3);
    return 0;
}
```
```output
5 == 3 -> 0
5 != 3 -> 1
5 >  3 -> 1
5 <  3 -> 0
5 >= 5 -> 1
5 <= 3 -> 0
```

Relational operators are used in **decision-making and loops** (Chapter 5).

> **In C, "true" means any non-zero value, and "false" means exactly `0`.** The comparison operators produce `1` or `0`, but `if (7)` and `if (-3)` are also *true*.

> ⚠️ **The most famous C bug: `=` versus `==`.**
> `a == b` *asks* "are they equal?". `a = b` *stores* `b` into `a`. Writing `a = 5` where you meant `a == 5` is perfectly legal C — it assigns 5 and then the "answer" is 5 (non-zero → true), so the condition is **always true**. Most compilers will warn you; read the warnings!

> ⚠️ **Do not chain comparisons like in mathematics.** `1 < x < 10` is **not** "x is between 1 and 10". C reads it as `(1 < x) < 10`, which is `(0 or 1) < 10` — always true! Use the logical operator: `x > 1 && x < 10`.

> ⚠️ **Comparing decimals with `==` is risky** because of tiny rounding errors (Chapter 2, Ex 2.44). Compare with a tolerance instead.

---

## 3.6 Logical operators

Logical operators combine **true/false** values (such as the results of relational operators). They also return `1` or `0`.

| Operator | Name | Meaning |
|---|---|---|
| `&&` | **AND** | true only if **both** operands are true |
| `\|\|` | **OR** | true if **at least one** operand is true |
| `!` | **NOT** | reverses: true becomes false, false becomes true |

**Truth tables** (`T` = true = 1, `F` = false = 0):

| A | B | `A && B` | `A \|\| B` |
|---|---|---|---|
| F | F | F | F |
| F | T | F | T |
| T | F | F | T |
| T | T | T | T |

| A | `!A` |
|---|---|
| F | T |
| T | F |

**Real-life pictures:** `&&` is like needing **both** a ticket **and** an ID to enter. `||` is like paying by cash **or** mobile money — either works. `!` is "the opposite".

**Example from your slides** (with `c = 5` and `d = 2`):

```c
#include <stdio.h>

int main(void)
{
    int c = 5, d = 2;

    printf("((c == 5) && (d > 5)) -> %d\n", (c == 5) && (d > 5));
    printf("((c == 5) || (d > 5)) -> %d\n", (c == 5) || (d > 5));
    printf("!(c == 5)             -> %d\n", !(c == 5));
    return 0;
}
```
```output
((c == 5) && (d > 5)) -> 0
((c == 5) || (d > 5)) -> 1
!(c == 5)             -> 0
```

Why? `c == 5` is true (1) and `d > 5` is false (0). **AND** needs both → `0`. **OR** needs one → `1`. **NOT** flips `1` to `0`.

**Use `&&` to test a range.** "x is between 10 and 20" is `x >= 10 && x <= 20`.

### Short-circuit evaluation

C is lazy (in a good way). It evaluates left to right and **stops as soon as the answer is known**:

- `A && B`: if `A` is false, the result is false already — `B` is **not evaluated**.
- `A || B`: if `A` is true, the result is true already — `B` is **not evaluated**.

This is useful for safety:

```c
#include <stdio.h>

int main(void)
{
    int x = 0;
    int safe = (x != 0) && (10 / x > 1);     /* 10 / x is skipped, so no crash */
    printf("safe = %d\n", safe);

    int a = 5;
    int r1 = (a > 10) && (++a > 0);          /* left side false: ++a never runs */
    printf("a = %d, r1 = %d\n", a, r1);

    int r2 = (a < 10) || (++a > 0);          /* left side true: ++a never runs */
    printf("a = %d, r2 = %d\n", a, r2);
    return 0;
}
```
```output
safe = 0
a = 5, r1 = 0
a = 5, r2 = 1
```

> ⚠️ **Do not confuse `&&` with `&`, or `||` with `|`.** The single ones are *bitwise* operators (section 3.8).

---

## 3.7 The conditional operator `? :`

The **conditional operator** is C's only **ternary** operator (three operands). It is a compact "if–else" that produces a **value**:

```
condition ? expression1 : expression2
```

**Read it as:** *"If the condition is true, the answer is expression1; otherwise it is expression2."*

```
   result = (alpha < 77) ? beta : gamma;
            └─ test ──┘   └─┬─┘  └─┬─┘
                          if true  if false
```

```
              ┌──────────────┐
              │ Test         │
              │ expression   │
              └──┬────────┬──┘
              True│        │False
        ┌─────────▼──┐  ┌──▼─────────┐
        │ takes the  │  │ takes the  │
        │ value of   │  │ value of   │
        │ expr 1     │  │ expr 2     │
        └────────────┘  └────────────┘
```

```c
#include <stdio.h>

int main(void)
{
    int a = 14, b = 9;
    int max = (a > b) ? a : b;                  /* the bigger of the two */
    printf("max = %d\n", max);

    int age = 15;
    double fare = (age < 12) ? 1.50 : 3.00;     /* child or adult fare */
    printf("fare = %.2f\n", fare);

    int score = 72;
    char grade = (score >= 80) ? 'A' : (score >= 60) ? 'B' : 'C';   /* nested */
    printf("grade = %c\n", grade);
    return 0;
}
```
```output
max = 14
fare = 3.00
grade = B
```

Use it for **short, simple** choices. For anything longer, use `if`/`else` (Chapter 5) — it is much easier to read.

---

## 3.8 Bitwise operators

Inside the computer, every number is stored as **bits** (0s and 1s). **Bitwise operators** work on those bits **one position at a time**. They make processing fast and are heavily used in embedded systems, drivers, graphics and networking.

| Operator | Name | Rule (per bit) |
|---|---|---|
| `&` | AND | 1 only if **both** bits are 1 |
| `\|` | OR | 1 if **at least one** bit is 1 |
| `^` | XOR (exclusive OR) | 1 if the bits are **different** |
| `~` | complement (NOT) | flips every bit (unary) |
| `<<` | shift left | moves bits left, fills with 0s |
| `>>` | shift right | moves bits right |

**Quick binary refresher.** Each position is worth double the one on its right: `... 16 8 4 2 1`. So `12` = `8 + 4` = `1100`, and `10` = `8 + 2` = `1010`.

```
        12 =  1 1 0 0
        10 =  1 0 1 0
   ─────────────────────
   12 & 10 =  1 0 0 0   = 8      (both 1 only in the "8" position)
   12 | 10 =  1 1 1 0   = 14     (at least one 1)
   12 ^ 10 =  0 1 1 0   = 6      (bits differ)
```

```c
#include <stdio.h>

int main(void)
{
    int a = 12;      /* 1100 */
    int b = 10;      /* 1010 */

    printf("a & b  = %d\n", a & b);
    printf("a | b  = %d\n", a | b);
    printf("a ^ b  = %d\n", a ^ b);
    printf("~a     = %d\n", ~a);
    printf("a << 1 = %d\n", a << 1);
    printf("a >> 2 = %d\n", a >> 2);
    return 0;
}
```
```output
a & b  = 8
a | b  = 14
a ^ b  = 6
~a     = -13
a << 1 = 24
a >> 2 = 3
```

**Shifts are fast multiply/divide by powers of 2.**
- `a << 1` doubles `a`: `12 << 1 = 24`. In general `a << n` = `a × 2ⁿ`.
- `a >> 2` divides by 4 (dropping the remainder): `12 >> 2 = 3`. In general `a >> n` = `a ÷ 2ⁿ`.

**`~` (complement)** flips all bits. For ordinary signed integers `~a` equals `-a - 1` (so `~12 = -13`). Do not worry about *why* yet — this is the "two's complement" representation you will study in your digital systems course.

**Common bit tricks**

| Task | Expression |
|---|---|
| Is `n` odd? | `n & 1` (1 if odd, 0 if even) |
| Set bit `k` | `n \| (1 << k)` |
| Clear bit `k` | `n & ~(1 << k)` |
| Toggle bit `k` | `n ^ (1 << k)` |
| Test bit `k` | `(n >> k) & 1` |

---

## 3.9 The comma operator

The comma **operator** evaluates its left expression, throws the result away, then evaluates and **returns the right one**. It is a way to put two expressions where C expects only one:

```c
#include <stdio.h>

int main(void)
{
    int a, b, x;

    x = (a = 3, b = 4, a + b);       /* a=3, then b=4, then the value is 3+4 */
    printf("a = %d, b = %d, x = %d\n", a, b, x);
    return 0;
}
```
```output
a = 3, b = 4, x = 7
```

> 📝 **Note on the slide.** The slide shows `int a, c = 5, d;` as an example of the comma. In that line the commas just **separate declarations** — a related but different use. The true comma *operator* is mostly used inside `for` loops (Chapter 5), e.g. `for (i = 0, j = 10; i < j; i++, j--)`. Don't worry about it for now. And remember the rule all statements follow: they end with a **semicolon `;`**.

---

## 3.10 The `sizeof` operator

`sizeof` is a **unary** operator that returns the **size in bytes** of a type, variable, array, structure and so on.

```c
#include <stdio.h>

int main(void)
{
    int a = 10;
    double d = 2.5;

    printf("sizeof(a)    = %zu\n", sizeof(a));
    printf("sizeof(d)    = %zu\n", sizeof(d));
    printf("sizeof(char) = %zu\n", sizeof(char));
    printf("sizeof(int)  = %zu\n", sizeof(int));
    return 0;
}
```
```output
sizeof(a)    = 4
sizeof(d)    = 8
sizeof(char) = 1
sizeof(int)  = 4
```

For a variable the brackets are optional (`sizeof a` works); for a type they are required. You will use `sizeof` again in Chapter 7 (arrays) to find how many items an array holds.

---

## 3.11 Precedence and associativity

What is `10 + 20 * 30`? Is it `(10 + 20) * 30 = 900` or `10 + (20 * 30) = 610`?

C follows fixed rules, just like the "BODMAS" of mathematics.

- **Precedence** — *which* operator is done **first** when the operators are **different**. (`*` before `+`.)
- **Associativity** — *which direction* to go when the operators have the **same** precedence: **left to right** or **right to left**.

```c
#include <stdio.h>

int main(void)
{
    printf("%d\n", 10 + 20 * 30);                 /* * before +           */
    printf("%d\n", 100 / 10 * 10);                /* same level: left to right */

    int exp = 100 + 200 / 10 - 3 * 10;            /* 100 + 20 - 30 */
    printf("%d\n", exp);

    int a = 6, b = 3, c = 4;
    int res = a + b * c / 2;                      /* 3*4=12, 12/2=6, 6+6 */
    printf("%d\n", res);
    return 0;
}
```
```output
610
100
90
12
```

Look at `100 / 10 * 10`: `/` and `*` have the **same** precedence, so we go **left to right**: `(100 / 10) * 10 = 100`, **not** `100 / (10 * 10) = 1`.

### The precedence table (highest to lowest)

| Level | Operators | Associativity |
|---|---|---|
| 1 (highest) | `()` `[]` `.` `->` and **postfix** `++` `--` | left → right |
| 2 | **prefix** `++` `--`, unary `+` `-`, `!`, `~`, `(type)` cast, `*` (dereference), `&` (address-of), `sizeof` | **right → left** |
| 3 | `*` `/` `%` | left → right |
| 4 | `+` `-` | left → right |
| 5 | `<<` `>>` | left → right |
| 6 | `<` `<=` `>` `>=` | left → right |
| 7 | `==` `!=` | left → right |
| 8 | `&` | left → right |
| 9 | `^` | left → right |
| 10 | `\|` | left → right |
| 11 | `&&` | left → right |
| 12 | `\|\|` | left → right |
| 13 | `?:` | **right → left** |
| 14 | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `\|=` | **right → left** |
| 15 (lowest) | `,` (comma) | left → right |

> 📝 **Note on the slide.** The slide's table is a simplified version. Compare carefully: it leaves out the relational operators `<  <=  >  >=` (level 6 above), and it lists `<<=  >>=` on their own row, when they actually belong with the assignment operators (level 14). Use the table above.

### How to use this table (the practical advice)

1. You do **not** need to memorise it. Remember the big picture: **unary → arithmetic → shifts → relational → equality → bitwise → logical → conditional → assignment → comma.**
2. **When in doubt, use parentheses.** `(a + b) * c` is clear to everyone. Parentheses are free, and they make your intent obvious.

### Worked example

Evaluate `int r = 2 + 3 * 4 > 10 && 8 % 3 == 2;`

1. `3 * 4` → 12 (`*` before `+`)
2. `8 % 3` → 2
3. `2 + 12` → 14
4. `14 > 10` → 1
5. `2 == 2` → 1
6. `1 && 1` → 1
7. `r = 1`

### Right-to-left in action

```c
#include <stdio.h>

int main(void)
{
    int a, b, c;
    a = b = c = 7;                 /* c=7 first, then b=7, then a=7 */
    printf("%d %d %d\n", a, b, c);

    int x = 5, y = 10;
    x += y -= 3;                   /* y -= 3 first (y=7), then x += 7 (x=12) */
    printf("%d %d\n", x, y);
    return 0;
}
```
```output
7 7 7
12 7
```

### A classic precedence trap

`==` binds **tighter** than `&`. So testing a bit like this goes wrong:

```c
#include <stdio.h>

int main(void)
{
    int n = 6;

    printf("%d\n", (n & 1) == 0);    /* correct: is n even? -> 1 */
    printf("%d\n", n & 1 == 0);      /* WRONG: means n & (1 == 0) = n & 0 -> 0 */
    return 0;
}
```
```output
1
0
```

Same lesson: **add parentheses**.

---

## 3.12 Common mistakes — checklist

| Mistake | What goes wrong | Fix |
|---|---|---|
| `if (x = 5)` | assigns instead of comparing | `x == 5` |
| `a / b` with ints | decimal part lost | cast: `(double) a / b` |
| `1 < x < 10` | always true | `x > 1 && x < 10` |
| `a & b` for "and" | bitwise, not logical | `a && b` |
| `i++ + ++i` | undefined behaviour | one `++` per statement |
| `%` with decimals | compile error | cast to `int` first |
| `x =+ 1` | means `x = +1` (!) | `x += 1` or `x++` |
| `n & 1 == 0` | precedence | `(n & 1) == 0` |
| dividing by zero | crash | check the divisor first |

---

## Key takeaways

- **Operators** act on **operands**: unary (1), binary (2), ternary (3).
- `/` on two integers gives an integer; `%` gives the **remainder** (integers only).
- `a++` uses the value **then** adds 1; `++a` adds 1 **then** uses the value.
- Compound assignments (`+=`, `-=`, `*=`, `/=`, `%=`) are shorthand; assignment goes **right to left**.
- Relational and logical operators return **`1` (true)** or **`0` (false)**; any non-zero value counts as true.
- `&&` and `||` **short-circuit**.
- `condition ? a : b` picks `a` if the condition is true, otherwise `b`.
- **Bitwise:** `& | ^ ~ << >>` work on individual bits; `<<` and `>>` multiply/divide by powers of 2.
- `sizeof` gives the size in bytes.
- **Precedence** says who goes first; **associativity** breaks ties. When unsure, **use brackets**.

---

# Exercises — Chapter 3

## Part A — Quick check

**Ex 3.1** What is an operand? Name one unary, one binary and one ternary operator.

**Ex 3.2** What does `%` compute? On what kind of operands can it be used?

**Ex 3.3** Explain the difference between `b = a++;` and `b = ++a;` (`a` starts as 5). What are `a` and `b` after each?

**Ex 3.4** What are the two possible results of a relational or logical expression? What counts as "true" in C?

**Ex 3.5** What is the difference between `=` and `==`?

**Ex 3.6** What is *short-circuit evaluation*? Give an example where it prevents a crash.

**Ex 3.7** What is the difference between **precedence** and **associativity**? Give an example of each.

**Ex 3.8** Fill in the blanks: `x += 4;` is the same as `x = ____ ;` and `x %= 3;` is the same as `x = ____ ;`.

**Ex 3.9** Rewrite `if x is greater than 10 then 1 else 0` as a single expression with the conditional operator.

**Ex 3.10** Complete the truth table for `A && B`, `A || B`, `!A` for all combinations of `A` and `B`.

**Ex 3.11** True or false?
1. `7 / 2` is `3.5`.
2. `7 % 2` is `1`.
3. `5 > 3 > 1` is true because 5 > 3 and 3 > 1.
4. `!0` is `1`.
5. `x << 1` doubles `x` (for small non-negative values).
6. `sizeof(int)` is always 4.

## Part B — Predict the output

*(Assume `<stdio.h>` is included and the code is inside `main`.)*

**Ex 3.12**
```c
printf("%d %d\n", 17 / 5, 17 % 5);
```

**Ex 3.13**
```c
printf("%d %d\n", -17 / 5, -17 % 5);
```

**Ex 3.14**
```c
printf("%d\n", 17 / 5);
printf("%.2f\n", 17 / 5.0);
printf("%.2f\n", (double) 17 / 5);
printf("%.2f\n", (double)(17 / 5));
```

**Ex 3.15**
```c
int a = 4;
int b = a++ + 2;
printf("%d %d\n", a, b);
```

**Ex 3.16**
```c
int a = 4;
int b = ++a + 2;
printf("%d %d\n", a, b);
```

**Ex 3.17**
```c
int x = 10;
x += 5;
x *= 2;
x -= 10;
x /= 4;
printf("%d\n", x);
```

**Ex 3.18**
```c
int a = 5, b = 10;
a += b -= 3;
printf("%d %d\n", a, b);
```

**Ex 3.19**
```c
printf("%d %d %d\n", 4 > 2, 4 == 2, 4 != 2);
```

**Ex 3.20**
```c
int a = 3, b = 7;
printf("%d\n", (a < b) && (b < 10));
printf("%d\n", (a > b) || (b == 7));
printf("%d\n", !(a < b));
printf("%d\n", !a);
```

**Ex 3.21**
```c
int a = 0, b = 5;
int r = (a != 0) && (b++ > 0);
printf("%d %d\n", r, b);
```

**Ex 3.22**
```c
int n = 15;
printf("%d\n", (n % 3 == 0) && (n % 5 == 0));
printf("%d\n", (n % 2 == 0) || (n > 10));
```

**Ex 3.23**
```c
int a = 5, b = 8;
int m = (a > b) ? a : b;
int n = (a == b) ? 100 : -100;
printf("%d %d\n", m, n);
```

**Ex 3.24**
```c
printf("%d\n", 2 + 3 * 4 - 5);
printf("%d\n", 20 / 4 * 2);
printf("%d\n", 7 - 3 - 2);
printf("%d\n", 2 * 3 % 4);
printf("%d\n", (1 + 2) * 3);
```

**Ex 3.25**
```c
printf("%d\n", 5 & 3);
printf("%d\n", 5 | 3);
printf("%d\n", 5 ^ 3);
printf("%d\n", 1 << 4);
printf("%d\n", 100 >> 2);
```
*(Hint: 5 = 101, 3 = 011.)*

**Ex 3.26**
```c
printf("%d\n", 10 > 5 > 2);
printf("%d\n", 1 + 1 == 2 && 3 > 5 || 4 < 9);
```

## Part C — Find and fix the bugs

**Ex 3.27** The program should print the average of 7 and 8 as `7.5` but prints `7`. Why? Fix it.
```c
int a = 7, b = 8;
double avg = (a + b) / 2;
printf("%.1f\n", avg);
```

**Ex 3.28** This line is meant to test whether `x` is between 1 and 10. Why is it wrong? Fix it.
```c
int ok = 1 < x < 10;
```

**Ex 3.29** This tries to test whether `n` is even, but always prints `0`. Why?
```c
int n = 6;
printf("%d\n", n & 1 == 0);
```

**Ex 3.30** The programmer wants to add 1 to `count`, but `count` becomes `1` regardless. What is wrong?
```c
int count = 10;
count =+ 1;
printf("%d\n", count);
```

**Ex 3.31** This doesn't compile. Why? Give two different fixes.
```c
double d = 10.5;
int r = d % 3;
```

**Ex 3.32** The result of this line differs between compilers. Why? Rewrite it so it is well defined.
```c
int i = 5;
int r = i++ + ++i;
```

**Ex 3.33** The programmer wants "`x` is not 5 and not 6". The code is wrong. Fix it.
```c
int ok = (x != 5) || (x != 6);
```

## Part D — Write the program

*(No `if` statements are needed in this chapter. Use the operators you learned, and `printf` to show results — `1` for true, `0` for false.)*

**Ex 3.34** Declare two integers `a = 17`, `b = 5`. Print their sum, difference, product, integer quotient, remainder, and the real quotient (2 decimals).

**Ex 3.35** For `n = 28`, print whether it is **even** (`1`/`0`), whether it is **divisible by 7** (`1`/`0`), and its **last digit**.

**Ex 3.36** Convert `3725` **seconds** into hours, minutes and seconds (answer: `1 h 2 min 5 s`).

**Ex 3.37** You have **235 pesewas**. Print how many cedis and how many pesewas that is (`GHS 2` and `35 p`).

**Ex 3.38** Given a **three-digit** number (e.g. `437`), print its hundreds, tens and units digits, then the **sum** of its digits.

**Ex 3.39** Given `n = 1234`, print its digits **reversed** as a number (`4321`), using only `/` and `%` and arithmetic (no loops yet — four digits, so do it in steps).

**Ex 3.40** Swap `a = 5` and `b = 9` **without** a third variable using `+` and `-`. Then swap again using the XOR trick (`^`).

**Ex 3.41** Given two integers, print the **larger** one using `?:`. Then extend it to find the largest of **three** integers.

**Ex 3.42** Compute the **absolute value** of an integer using `?:` (test with `-17` and `23`).

**Ex 3.43** Given a year, print `1` if it is a **leap year**, else `0`, using **one** logical expression. Test with 1900, 2000, 2023, 2024.

**Ex 3.44** Given a character `ch`, print `1`/`0` for each of: (a) is it a lowercase letter? (b) is it an uppercase letter? (c) is it a digit? Test with `'g'`, `'G'` and `'5'`. *(Hint: characters compare by ASCII code: `ch >= 'a' && ch <= 'z'`.)*

**Ex 3.45** Given three side lengths `a`, `b`, `c` print `1` if they can form a **triangle** (each pair of sides must add up to more than the third), else `0`. Test with `(3,4,5)` and `(1,2,5)`.

**Ex 3.46** A ticket costs GHS 10 for adults and GHS 5 for children under 12. Using `?:`, print the fare for ages `8` and `30`.

**Ex 3.47** Compute the **discriminant** `b² − 4ac` for `a = 1, b = −3, c = 2`, and print `1` if the equation has real roots (discriminant ≥ 0), else `0`.

**Ex 3.48 (clock arithmetic)** It is **14:50**. What time will it be after **135 minutes**? Use `/` and `%` to compute the new hour and minute (answer `17:05`).

**Ex 3.49** Round an integer `n = 47` **to the nearest ten** using only integer arithmetic (answer `50`). Try `n = 42` (answer `40`). *(Hint: add 5, divide by 10, multiply by 10.)*

**Ex 3.50** Using the shift operators only: print `13 × 8`, `200 ÷ 4`, and `2` raised to the power `10`.

**Ex 3.51** Use bit operators on `n = 40` (binary `101000`) to: test whether bit 3 is set, set bit 0, clear bit 3, toggle bit 5. Print the results.

**Ex 3.52** A salesperson earns a base of GHS 1200 plus 5% commission on sales. Starting with `double pay = 1200;`, use a compound assignment (`+=`) to add the commission on sales of GHS 8000 and print the pay.

## Part E — Challenges

**Ex 3.53 (power of two)** A positive integer `n` is a power of two exactly when `(n & (n - 1)) == 0`. Test the expression for `n = 64` and `n = 100` and explain, using the binary patterns of `63` and `99`, why it works.

**Ex 3.54 (day of the week)** Today is **Thursday**. Number the days Monday = 0 … Sunday = 6, so Thursday = 3. What day will it be **100 days** from now? Use `%`.

**Ex 3.55 (upper-case with bits)** In ASCII, a lowercase letter differs from its uppercase partner only in **bit 5** (value 32). Convert `'g'` to `'G'` **using a bitwise operator** (not subtraction), and `'M'` to `'m'` too.

**Ex 3.56 (safe compare of decimals)** `0.1 + 0.2 == 0.3` is false in C. Write an expression that tells whether two doubles `x` and `y` are "equal within `0.000001`" **without** calling any library function. *(Hint: you need an absolute value — use `?:`.)*

**Ex 3.57 (evaluate by hand, then verify)** Work out by hand, then confirm by running:
1. `5 + 3 * 2 - 8 / 4 % 3`
2. `10 - 4 - 3 * 2`
3. `!5 + 3 > 2 && 1`
4. `(5 > 3) + (2 > 1) * 4`
5. `7 & 3 + 1`   *(careful with precedence!)*

**Ex 3.58 (a compact grade)** Without `if`, convert a score `s` into a letter using nested `?:`: A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, else F. Test with 85, 72, 61, 55, 20.

## Part F — Research tasks

**Ex 3.59** Look up **De Morgan's laws** and use them to rewrite `!(a > 5 && b < 3)` without the outer `!`. Verify with a program for several values.

**Ex 3.60** What type does `sizeof` return? Why is `%zu` used to print it?

**Ex 3.61** Find out what **two's complement** is, and use it to explain why `~12` is `-13`.

---

*End of Chapter 3. Next: [Chapter 4 — Data Input and Output](04-data-input-and-output.md)*
