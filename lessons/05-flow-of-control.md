# Chapter 5 — Flow of Control

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `05 Flow of Control.pdf`  
> **Solutions:** [Solutions to Chapter 5](../solutions/05-flow-of-control.md)

---

## What you will learn

1. How to make a program **decide** — `if`, `else if`, `else`, `switch`.
2. How to make a program **repeat** — `while`, `do while`, `for`.
3. The **rule of the braces** `{ }` — when you may leave them out and when you shouldn't.
4. **Nested** statements — decisions inside loops, loops inside loops.
5. Two extra tools every programmer uses: `break` and `continue`.

This is the most important chapter so far. After it, you can solve *real* problems.

---

## 5.1 What is "flow of control"?

So far your programs ran **top to bottom, every line, once**. Real programs (like real people) respond to changing circumstances:

- *Choosing* one option out of several (e.g. which menu item the user picked).
- *Repeating* an action many times (e.g. printing 100 results).

The order in which statements are executed is the **flow of control**. Statements that change it are **control statements**. There are two major kinds:

```
              Control statements
        ┌──────────────┴───────────────┐
     DECISIONS                       LOOPS
  (choose a path)               (repeat a path)
   if / else if / else           while
   switch                        do ... while
                                 for
```

---

## 5.2 Decision statements

A **decision statement** lets the program **select one option out of several**, based on a **condition** that is true (or false) at that moment.

It is just like your own decisions: *if you are hungry, you eat; if not, you don't.* Or: *choose what to eat depending on the time of day.*

### 5.2.1 The `if` statement

```c
if (condition)
{
    statements;       // run only when the condition is true
}
```

```
        ┌──────────────┐
        │  condition?  │──── false ───┐
        └──────┬───────┘              │
             true                     │
        ┌──────▼───────┐              │
        │  statements  │              │
        └──────┬───────┘              │
               └──────────┬───────────┘
                    (program continues)
```

Remember from Chapter 3: a condition is any expression. **`0` means false; anything else means true.** Relational and logical operators give `1` or `0`.

```c
#include <stdio.h>

int main(void)
{
    int temperature = 38;

    if (temperature > 37)
    {
        printf("You have a fever.\n");
    }
    printf("Take care!\n");
    return 0;
}
```
```output
You have a fever.
Take care!
```

If `temperature` were `36`, only `Take care!` would be printed.

### 5.2.2 The `if else` statement

Two options: one for **true**, one for **false**.

```c
if (condition)
{
    statements;       // code to execute if the condition is true
}
else
{
    statements;       // code to execute if the condition is false
}
```

Read it as plain English: *"if the condition is true do this, otherwise do that."*

**Example from the slides** — even or odd:

```c
int x = 20;
if (x % 2 == 0)
{
    printf("The value is even \n");
}
else
{
    printf("The value is odd \n");
}
```

*"If x modulus 2 is equal to zero, print 'The value is even', else print 'The value is odd'."* This is selecting **one of two** options.

Better: let the **user** choose the value (also from the slides):

<!--in: 7-->
```c
#include <stdio.h>

int main(void)
{
    int x;

    printf("Please enter an integer value\n");
    scanf("%d", &x);

    if (x % 2 == 0)
    {
        printf("%d is even\n", x);
    }
    else
    {
        printf("%d is odd\n", x);
    }
    return 0;
}
```
```output
Please enter an integer value
7
7 is odd
```

### 5.2.3 The `else if` ladder — more than two options

For three or more options, add **`else if`** (with its own condition) as many times as you like:

```c
if (conditionA)
{
    statements;       // if conditionA is true
}
else if (conditionB)
{
    statements;       // if conditionA is false but conditionB is true
}
else
{
    statements;       // if all the conditions above are false
}
```

**Example from the slides** — positive, negative or zero:

<!--in: -4-->
```c
#include <stdio.h>

int main(void)
{
    int numb;

    printf("Please enter an integer value\n");
    scanf("%d", &numb);

    if (numb < 0)
    {
        printf("%d is negative\n", numb);
    }
    else if (numb > 0)
    {
        printf("%d is positive\n", numb);
    }
    else
    {
        printf("%d is zero\n", numb);
    }
    return 0;
}
```
```output
Please enter an integer value
-4
-4 is negative
```

**How C reads a ladder:** from the **top, downwards**. The **very first condition that is true** wins, its block runs, and **all the rest are skipped** — *even if later conditions are also true.*

```c
#include <stdio.h>

int main(void)
{
    int n = 15;

    if (n > 10)
        printf("big\n");
    else if (n > 5)           /* also true, but never reached */
        printf("medium\n");
    else
        printf("small\n");
    return 0;
}
```
```output
big
```

> 💡 **Contrast.** If you write **three separate `if`s** (no `else`), *each one* is tested independently and several can run. A ladder runs **at most one**.

**The final `else` is the "default".** If everything above is false, the `else` runs. It is **optional**: if you leave it out and no condition is true, nothing happens.

**Order matters!** Put the most specific / highest tests first. This grading program works because it tests from the highest score down:

<!--in: 72-->
```c
#include <stdio.h>

int main(void)
{
    int score;

    printf("Enter your score: ");
    scanf("%d", &score);

    if (score >= 80)
        printf("Grade A\n");
    else if (score >= 70)
        printf("Grade B\n");
    else if (score >= 60)
        printf("Grade C\n");
    else if (score >= 50)
        printf("Grade D\n");
    else
        printf("Grade F\n");
    return 0;
}
```
```output
Enter your score: 72
Grade B
```

Notice we only test the **lower** limit of each band — if we got past `score >= 80` being false, we already know the score is below 80.

### 5.2.4 Nested `if` statements

An `if` inside another `if`. The inner one is only reached when the outer condition is true.

<!--in: 20 1-->
```c
#include <stdio.h>

int main(void)
{
    int age, hasId;

    printf("Enter age and ID status (1 = has ID, 0 = no ID): ");
    scanf("%d %d", &age, &hasId);

    if (age >= 18)
    {
        if (hasId == 1)
            printf("Welcome in!\n");
        else
            printf("Sorry, bring your ID.\n");
    }
    else
    {
        printf("Sorry, you are too young.\n");
    }
    return 0;
}
```
```output
Enter age and ID status (1 = has ID, 0 = no ID): 20 1
Welcome in!
```

The same rule can often be written in one line with `&&`: `if (age >= 18 && hasId == 1)`. Use nesting when each level needs *its own* message.

### 5.2.5 Common `if` mistakes

| Mistake | Example | What happens |
|---|---|---|
| `=` instead of `==` | `if (x = 5)` | assigns 5, always true |
| Semicolon after the condition | `if (x > 5);` | the `;` *is* the (empty) body! The next line always runs |
| Missing braces for 2+ statements | `if (a) x++; y++;` | `y++` is **not** part of the `if` |
| Chained comparison | `if (0 < x < 10)` | always true (Chapter 3) |
| Comparing decimals with `==` | `if (x == 0.1)` | may fail due to rounding |

### The dangling `else`

Which `if` does an `else` belong to? **The nearest unmatched `if`** — *indentation doesn't matter to the compiler*.

```c
#include <stdio.h>

int main(void)
{
    int a = 1, b = 0;

    if (a == 1)
        if (b == 1)
            printf("X\n");
    else                       /* belongs to  if (b == 1), NOT if (a == 1)! */
        printf("Y\n");
    return 0;
}
```
```output
Y
```

The `else` pairs with `if (b == 1)`. To avoid such traps — **use braces**.

---

## 5.3 The `switch` statement

When you compare **one value** against **many exact possibilities** (menu choices, a letter, a day number), a long `else if` ladder gets ugly. `switch` is cleaner.

```c
switch (expression)
{
    case value1:
        statements;
        break;
    case value2:
        statements;
        break;
    ...
    default:
        statements;
        break;
}
```

How it works:

1. The `expression` is evaluated **once**.
2. Its value is compared with each `case` label. When one matches, execution **starts at that label**…
3. …and **continues downward until a `break`** (or the closing brace of the switch).
4. If **no case matches**, the `default` block runs (it is optional).

> 🔑 **`break` means "stop and exit the switch"** — like a car's brake. **The matched case tells us where to start; `break` tells us where to stop.**

**Example from the slides** — are you Ghanaian?

<!--in: y-->
```c
#include <stdio.h>

int main(void)
{
    char choice;

    printf("Are you a Ghanaian ? \n");
    printf("Enter y for yes or n for no \n");
    scanf(" %c", &choice);

    switch (choice)
    {
        case 'y':
            printf("Ghanaians are hospitable people \n");
            break;
        case 'n':
            printf("I don't know much about your country \n");
            break;
        default:
            printf("You did not follow the instruction \n");
    }
    return 0;
}
```
```output
Are you a Ghanaian ?
Enter y for yes or n for no
y
Ghanaians are hospitable people
```

- Input `y` → prints the first message, then `break` exits.
- Input `n` → prints the second message, then `break` exits.
- Anything else → `default` runs.

### What if you forget `break`? — "fall-through"

Without `break`, execution **falls through** into the next case, and the next, until a `break` appears:

<!--in: 2-->
```c
#include <stdio.h>

int main(void)
{
    int d;

    printf("Enter 1, 2, 3 or 4: ");
    scanf("%d", &d);

    switch (d)
    {
        case 1: printf("one\n");
        case 2: printf("two\n");
        case 3: printf("three\n"); break;
        case 4: printf("four\n");
        default: printf("other\n");
    }
    return 0;
}
```
```output
Enter 1, 2, 3 or 4: 2
two
three
```

Input 2 jumped to `case 2:`, printed `two`, **fell through** into `case 3:`, printed `three`, then hit `break`.

Sometimes fall-through is **useful** — to give several cases the **same** action:

<!--in: e-->
```c
#include <stdio.h>

int main(void)
{
    char ch;

    printf("Enter a lowercase letter: ");
    scanf(" %c", &ch);

    switch (ch)
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            printf("%c is a vowel\n", ch);
            break;
        default:
            printf("%c is a consonant\n", ch);
    }
    return 0;
}
```
```output
Enter a lowercase letter: e
e is a vowel
```

### A calculator with `switch`

<!--in: 12 * 5-->
```c
#include <stdio.h>

int main(void)
{
    double a, b;
    char op;

    printf("Enter an expression like 12 * 5: ");
    scanf("%lf %c %lf", &a, &op, &b);

    switch (op)
    {
        case '+': printf("%.2f\n", a + b); break;
        case '-': printf("%.2f\n", a - b); break;
        case '*': printf("%.2f\n", a * b); break;
        case '/': printf("%.2f\n", a / b); break;
        default:  printf("Unknown operator\n");
    }
    return 0;
}
```
```output
Enter an expression like 12 * 5: 12 * 5
60.00
```

### `switch` rules to remember

- The switch expression must be an **integer or character** (`int`, `char`, …) — **not** a `float`/`double` or a string.
- Each `case` label must be a **constant** (like `3` or `'y'`) — not a variable and **not a range** (`case 1..5` does not exist in standard C).
- Two cases may not have the same value.
- `default` can go anywhere, but it is usually last.
- Use `switch` for **exact matches**. Use `if / else if` for **ranges and complicated conditions** (`score >= 80`).

---

## 5.4 Loop statements

A **loop** repeats a section of code **as long as a condition is true**. Each pass through the loop is called an **iteration**.

C has three loops:

| Loop | Best when… |
|---|---|
| `while` | you don't know in advance how many times (repeat *while* something is true) |
| `do while` | the body must run **at least once** (menus, input validation) |
| `for` | you **know** how many times (counting) |

### 5.4.1 The `while` loop

```c
while (condition)
{
    statements;       // repeated as long as the condition is true
}
```

*Read it as:* **"while the condition is true, execute the statements."** The condition is checked **before** each iteration — so if it is false at the start, the body **never runs**.

```
            ┌─────────────┐
      ┌────▶│ condition?  │─── false ──▶ (leave the loop)
      │     └──────┬──────┘
      │          true
      │     ┌──────▼──────┐
      └─────┤   body      │
            └─────────────┘
```

**Example from the slides:**

```c
#include <stdio.h>

int main(void)
{
    int q = 5;

    while (q < 8)
    {
        printf("%d\t", q);
        q++;                     /* increase q by 1 */
    }
    return 0;
}
```
```output
5       6       7
```

**Step by step:**

| q | `q < 8`? | action | output so far |
|---|---|---|---|
| 5 | yes | print 5, q becomes 6 | 5 |
| 6 | yes | print 6, q becomes 7 | 5 6 |
| 7 | yes | print 7, q becomes 8 | 5 6 7 |
| 8 | **no** | loop ends | |

A **countdown** (`b--` decreases the value):

```c
#include <stdio.h>

int main(void)
{
    int b = 10;

    while (b >= 7)
    {
        printf("%d\t", b);
        b--;
    }
    return 0;
}
```
```output
10      9       8       7
```

**The position of statements matters.** Swap the two statements and the output changes:

```c
#include <stdio.h>

int main(void)
{
    int b = 10;

    while (b >= 7)
    {
        b--;                     /* decrease FIRST ... */
        printf("%d\t", b);       /* ... then print     */
    }
    return 0;
}
```
```output
9       8       7       6
```

(Your slide shows this output as `9 8 76` because the tab spaces were lost — it really prints `9 8 7 6`. When `b` is 7 the condition is still true, `b` becomes 6 and `6` is printed.)

**The three ingredients of every loop:**

1. **Initialise** — give the loop variable its starting value (`int q = 5;`).
2. **Test** — the condition (`q < 8`).
3. **Update** — change the variable so the loop eventually stops (`q++`).

> ⚠️ **Forget the update and you get an infinite loop.** The program never ends — press **Ctrl + C** to stop it.

**A classic use: add up numbers 1 to N.**

<!--in: 10-->
```c
#include <stdio.h>

int main(void)
{
    int n, i = 1, sum = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    while (i <= n)
    {
        sum = sum + i;
        i++;
    }
    printf("Sum of 1 to %d = %d\n", n, sum);
    return 0;
}
```
```output
Enter N: 10
Sum of 1 to 10 = 55
```

**Another classic: count digits** (remember `n / 10` drops the last digit):

<!--in: 4096-->
```c
#include <stdio.h>

int main(void)
{
    int n, count = 0;

    printf("Enter an integer: ");
    scanf("%d", &n);

    while (n > 0)
    {
        n = n / 10;
        count++;
    }
    printf("It has %d digits\n", count);
    return 0;
}
```
```output
Enter an integer: 4096
It has 4 digits
```

### 5.4.2 The `do while` loop

Very similar, but the **condition is checked at the END**. The body therefore runs **at least once**, always.

```c
do
{
    statements;       // executed first
}
while (condition);    // <-- NOTE the semicolon!
```

```
            ┌─────────────┐
      ┌────▶│   body      │
      │     └──────┬──────┘
      │     ┌──────▼──────┐
      │true │ condition?  │─── false ──▶ (leave the loop)
      └─────┤             │
            └─────────────┘
```

**Examples from the slides:**

```c
#include <stdio.h>

int main(void)
{
    int m = 1;

    do
    {
        printf("%d\t", m);
        m++;
    }
    while (m <= 5);
    return 0;
}
```
```output
1       2       3       4       5
```

Now a condition that is **false from the start**:

```c
#include <stdio.h>

int main(void)
{
    int m = 1;

    do
    {
        printf("%d\t", m);
        m++;
    }
    while (m >= 5);          /* after the first pass m is 2, so 2 >= 5 is false */
    return 0;
}
```
```output
1
```

The body ran once even though the condition was false from the start. A `while` loop with the same condition would have printed nothing.

**`do while` is perfect for input validation** — ask at least once, and repeat while the answer is bad:

<!--in: 15\n-3\n7-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    do
    {
        printf("Enter a number from 1 to 10: ");
        scanf("%d", &n);
    }
    while (n < 1 || n > 10);

    printf("Thank you. You entered %d\n", n);
    return 0;
}
```
```output
Enter a number from 1 to 10: 15
Enter a number from 1 to 10: -3
Enter a number from 1 to 10: 7
Thank you. You entered 7
```

### 5.4.3 The `for` loop

The `for` loop is one of the most-used loops in C. It packs the three ingredients — initialise, test, update — **into one line**. It is ideal when you can say *how many times* to repeat, and it is the preferred loop for going through **arrays** (Chapter 7).

```c
for (initialization; condition; increment/decrement)
{
    statements;
}
```

**The order of events:**

```
   1. initialization       (done ONCE, at the very start)
          │
          ▼
   2. condition?  ──── false ────▶ leave the loop
          │ true
          ▼
   3. statements (the body)
          │
          ▼
   4. increment / decrement
          │
          └─────────▶ back to step 2
```

> 🔑 The update (step 4) happens **after** the body, **not before**.

**Examples from the slides:**

```c
#include <stdio.h>

int main(void)
{
    int a;

    for (a = 0; a < 4; a++)
    {
        printf("%d\t", a);
    }
    return 0;
}
```
```output
0       1       2       3
```

And a loop that **doubles** each time (`c *= 2`):

```c
#include <stdio.h>

int main(void)
{
    int c = 0;

    for (c = 1; c < 10; c *= 2)
    {
        printf("%d\t", c);
    }
    return 0;
}
```
```output
1       2       4       8
```

(1 → 2 → 4 → 8 → 16: when `c` becomes 16 the test `16 < 10` is false, so 16 is never printed.)

**Handy variations:**

```c
#include <stdio.h>

int main(void)
{
    int i;

    for (i = 10; i >= 1; i--)            /* count down  */
        printf("%d ", i);
    printf("\n");

    for (i = 0; i <= 20; i += 5)         /* step by 5   */
        printf("%d ", i);
    printf("\n");

    for (int k = 1; k <= 5; k++)         /* declare the counter in the loop (C99) */
        printf("%d ", k * k);
    printf("\n");

    for (int a = 0, b = 10; a < b; a += 3, b -= 3)   /* two variables (comma operator) */
        printf("(%d,%d) ", a, b);
    printf("\n");
    return 0;
}
```
```output
10 9 8 7 6 5 4 3 2 1
0 5 10 15 20
1 4 9 16 25
(0,10) (3,7)
```

**Pick the right loop**

| Situation | Loop |
|---|---|
| "Do this 10 times", "for each item" | `for` |
| "Keep going until the user types 0" | `while` |
| "Show the menu, then repeat if they didn't choose Exit" | `do while` |

### Off-by-one errors

The most common loop bug: running one time too many or too few.

| Header | Runs for `i` = | Times |
|---|---|---|
| `for (i = 0; i < 5; i++)` | 0, 1, 2, 3, 4 | **5** |
| `for (i = 1; i <= 5; i++)` | 1, 2, 3, 4, 5 | **5** |
| `for (i = 0; i <= 5; i++)` | 0 … 5 | **6** |
| `for (i = 10; i > 0; i -= 2)` | 10, 8, 6, 4, 2 | **5** |

> 💡 `for (i = 0; i < n; i++)` is the standard way to run `n` times (it matches how arrays are numbered from 0 in Chapter 7).

### 5.4.4 `break` and `continue`

Two small but powerful statements (not in your slides, but you will use them constantly):

- **`break`** — leave the loop (or `switch`) **immediately**.
- **`continue`** — skip the **rest of this iteration** and go to the next one.

```c
#include <stdio.h>

int main(void)
{
    int i;

    for (i = 1; i <= 10; i++)
    {
        if (i == 4)
            continue;               /* skip 4 */
        if (i == 8)
            break;                  /* stop completely at 8 */
        printf("%d ", i);
    }
    printf("\nstopped at i = %d\n", i);
    return 0;
}
```
```output
1 2 3 5 6 7
stopped at i = 8
```

### 5.4.5 Common loop mistakes

| Mistake | Result |
|---|---|
| no update (`while (i < 5) { ... }` never changes `i`) | infinite loop |
| `;` right after the header: `for (...);` `while (...);` | the loop's body is empty; the next block runs once |
| `<=` instead of `<` (or the reverse) | off by one |
| changing the loop counter inside a `for` body | legal, but values get skipped or repeated and the loop is hard to follow |
| using `float` counters (`for (x = 0; x != 1.0; x += 0.1)`) | rounding → may never hit exactly 1.0 |

---

## 5.5 The rule of the braces `{ }`

If the body of a decision (`if`, `else`) or a loop contains **only one statement**, the braces are **optional**. The statement can be an ordinary statement (ending with `;`) or even a whole compound statement such as another `if` or `for`. (This rule does **not** apply to functions: the body of `main` or of any other function always needs its braces.)

Your slide's example — these two loops are identical:

```c
for (int c = 1; c < 10; c *= 2)
{
    printf("%d\t", c);
}

for (int c = 1; c < 10; c *= 2)
    printf("%d\t", c);
```

When there are no braces, the compiler assumes the loop has **only the one statement that immediately follows**. Therefore, in this slide example, the second `printf` is **not** part of the loop:

```c
#include <stdio.h>

int main(void)
{
    for (int c = 1; c < 10; c *= 2)
        printf("%d\t", c);
        printf("\nDone");          /* NOT inside the loop: runs once, after it */
    return 0;
}
```
```output
1       2       4       8
Done
```

> ⚠️ **The danger.** The indentation of the second `printf` *looks* like it belongs to the loop. It doesn't — the compiler ignores indentation. Many bugs come from adding a second statement to a braceless `if` or loop.

> 💡 **Professional advice:** **always use braces**, even for a single statement. It costs two characters and prevents a whole family of bugs. (We omit them in places in these notes only to save space.)

---

## 5.6 Nested statements

A **nested statement** is a compound statement (an `if`, `switch`, loop…) **placed inside another**. The inner statement can only run when the outer one lets it.

**Example from the slides** — an `if-else` inside a `while`:

```c
#include <stdio.h>

int main(void)
{
    int x = 10, y = 0;

    while (x < 15)
    {
        if (x % 2 == 0)
        {
            y += x;
        }
        else
        {
            y--;
        }
        printf("%d\t", y);
        x++;
    }
    return 0;
}
```
```output
10      9       21      20      34
```

Trace table:

| x | x even? | action | y | printed |
|---|---|---|---|---|
| 10 | yes | y += 10 | 10 | 10 |
| 11 | no | y-- | 9 | 9 |
| 12 | yes | y += 12 | 21 | 21 |
| 13 | no | y-- | 20 | 20 |
| 14 | yes | y += 14 | 34 | 34 |
| 15 | — | `15 < 15` false → stop | | |

Since both the `if` and the `else` hold one statement each, the **rule of braces** lets us drop their braces (compare the two versions in your slides):

```c
while (x < 15)
{
    if (x % 2 == 0)
        y += x;
    else
        y--;
    printf("%d\t", y);
    x++;
}
```

### Loops inside loops

A loop in a loop is the tool for **tables, grids and patterns**. The inner loop runs completely **for every single iteration of the outer loop**.

```c
#include <stdio.h>

int main(void)
{
    for (int row = 1; row <= 4; row++)         /* outer: rows    */
    {
        for (int col = 1; col <= row; col++)   /* inner: columns */
        {
            printf("*");
        }
        printf("\n");                           /* end of the row */
    }
    return 0;
}
```
```output
*
**
***
****
```

How to think about it: when `row` is 3, the inner loop runs `col = 1, 2, 3` — printing three stars — and then `\n` ends that line.

> 💡 **Pattern-printing recipe:** (1) the **outer** loop counts **lines**; (2) the **inner** loop prints what goes **on one line** (spaces, then symbols); (3) print `\n` **after** the inner loop.

**A multiplication table:**

```c
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            printf("%4d", i * j);
        }
        printf("\n");
    }
    return 0;
}
```
```output
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

(Remember Exercise 1.39? Four lines instead of five hand-typed rows — and it scales to 50 × 50 by changing one number.)

**Prime test** — a loop with a `break` inside:

<!--in: 29-->
```c
#include <stdio.h>

int main(void)
{
    int n, isPrime = 1;

    printf("Enter an integer greater than 1: ");
    scanf("%d", &n);

    for (int d = 2; d * d <= n; d++)
    {
        if (n % d == 0)
        {
            isPrime = 0;      /* found a divisor */
            break;            /* no need to look further */
        }
    }

    if (isPrime)
        printf("%d is prime\n", n);
    else
        printf("%d is not prime\n", n);
    return 0;
}
```
```output
Enter an integer greater than 1: 29
29 is prime
```

> ⚠️ `break` leaves **only the innermost** loop (or switch) it is in.

---

## 5.7 Putting it all together

### A menu-driven program (`do while` + `switch`)

This is the shape of countless real programs: show a menu, act on the choice, repeat until "Exit".

<!--in: 1 500\n2 120\n3\n4-->
```c
#include <stdio.h>

int main(void)
{
    double balance = 0;
    int choice;
    double amount;

    do
    {
        printf("\n1) Deposit  2) Withdraw  3) Balance  4) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                scanf("%lf", &amount);
                balance += amount;
                printf("Deposited %.2f\n", amount);
                break;
            case 2:
                scanf("%lf", &amount);
                if (amount > balance)
                    printf("Insufficient funds\n");
                else
                {
                    balance -= amount;
                    printf("Withdrew %.2f\n", amount);
                }
                break;
            case 3:
                printf("Balance: %.2f\n", balance);
                break;
            case 4:
                printf("Goodbye!\n");
                break;
            default:
                printf("Invalid choice\n");
        }
    }
    while (choice != 4);

    return 0;
}
```
```output
1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 1 500
Deposited 500.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 2 120
Withdrew 120.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 3
Balance: 380.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 4
Goodbye!
```

### A number-guessing game

<!--in: 50 25 37-->
```c
#include <stdio.h>

int main(void)
{
    int secret = 37, guess, tries = 0;

    do
    {
        printf("Guess the number (1-100): ");
        scanf("%d", &guess);
        tries++;

        if (guess < secret)
            printf("Too low!\n");
        else if (guess > secret)
            printf("Too high!\n");
    }
    while (guess != secret);

    printf("Correct! You needed %d tries.\n", tries);
    return 0;
}
```
```output
Guess the number (1-100): 50
Too high!
Guess the number (1-100): 25
Too low!
Guess the number (1-100): 37
Correct! You needed 3 tries.
```

---

## 5.8 How to design a program with control flow

1. **Understand** the problem (Chapter 0!). Write a few examples by hand.
2. Decide **what repeats** (loop) and **what branches** (if/switch).
3. Choose the **right loop**.
4. Write the **pseudocode** first.
5. Code it, then **trace** it with a table for a small input.
6. Test the **edges**: the smallest input, zero, negatives, the largest.

---

## Key takeaways

- **Decisions:** `if`, `else if`, `else`, `switch`. In a ladder, the **first** true condition wins.
- `switch` compares **one integer/char** against **constant** cases; use **`break`** to stop (otherwise it *falls through*); `default` handles everything else.
- **Loops:** `while` (test first), `do while` (test last — runs at least once; note the **semicolon**), `for` (init; test; update).
- Every loop needs **initialise → test → update**. Forget the update → **infinite loop**.
- `for (i = 0; i < n; i++)` runs `n` times. Beware **off-by-one**.
- **`break`** leaves the loop; **`continue`** skips to the next iteration.
- **Rule of braces:** one statement → braces optional. **But always using braces is safer.**
- **Nested** statements: an inner statement runs only when the outer allows it. Nested loops → tables and patterns (outer loop = lines, inner loop = one line).

---

# Exercises — Chapter 5

## Part A — Quick check

**Ex 5.1** What are the two major categories of control statements? What is an *iteration*?

**Ex 5.2** What does `if (x)` do when `x` is `7`? When `x` is `0`? When `x` is `-3`?

**Ex 5.3** What is the difference between three separate `if` statements and one `if / else if / else` ladder?

**Ex 5.4** In an `else if` ladder, two of the conditions are true. Which block runs? Why?

**Ex 5.5** Is the final `else` mandatory? What does it do?

**Ex 5.6** What does `break` do inside a `switch`? What happens if you forget it?

**Ex 5.7** What kinds of expressions can a `switch` use? Can a `case` label be a variable? A range like `case 1..5`? A string?

**Ex 5.8** What is the difference between `while` and `do while`? Which one always runs its body at least once?

**Ex 5.9** Name the three parts of a `for` header and the order in which they are executed.

**Ex 5.10** When may you leave out the braces of an `if` or a loop? Why can that be risky?

**Ex 5.11** What is a nested statement? Give an example.

**Ex 5.12** What is the difference between `break` and `continue` in a loop?

**Ex 5.13** Which loop would you choose for each? (a) print 1 to 100; (b) keep asking for a password until it is right; (c) read numbers until the user types 0; (d) show a menu at least once and repeat until "Exit".

**Ex 5.14** How many times does the body run?
(a) `for (i = 0; i < 5; i++)` (b) `for (i = 1; i <= 5; i++)` (c) `for (i = 0; i <= 5; i++)` (d) `for (i = 10; i > 0; i -= 2)` (e) `while (0)` (f) `do { ... } while (0);`

## Part B — Predict the output

*(Assume `<stdio.h>` is included and the fragments are inside `main`. Use a trace table where it helps.)*

**Ex 5.15**
```c
int a = 5, b = 8;
if (a > b)
    printf("A\n");
else if (a == b)
    printf("B\n");
else
    printf("C\n");
```

**Ex 5.16**
```c
int n = 15;
if (n > 10)
    printf("big\n");
else if (n > 5)
    printf("medium\n");
else
    printf("small\n");
```

**Ex 5.17**
```c
int n = 15;
if (n > 10) printf("big\n");
if (n > 5)  printf("medium\n");
if (n > 0)  printf("positive\n");
```

**Ex 5.18**
```c
int a = 1, b = 0;
if (a == 1)
    if (b == 1)
        printf("X\n");
    else
        printf("Y\n");
printf("Z\n");
```

**Ex 5.19**
```c
int x = 3;
if (x > 5);
    printf("big\n");
```

**Ex 5.20**
```c
int d = 2;
switch (d)
{
    case 1: printf("one\n");
    case 2: printf("two\n");
    case 3: printf("three\n"); break;
    case 4: printf("four\n");
    default: printf("other\n");
}
```

**Ex 5.21**
```c
int month = 4;
switch (month)
{
    case 2:
        printf("28 or 29");
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        printf("30");
        break;
    default:
        printf("31");
}
printf(" days\n");
```

**Ex 5.22**
```c
int i = 1, sum = 0;
while (i <= 5)
{
    sum += i;
    i++;
}
printf("%d %d\n", sum, i);
```

**Ex 5.23**
```c
int n = 5;
while (n > 0)
{
    n -= 2;
    printf("%d ", n);
}
```

**Ex 5.24**
```c
int k = 10;
do
{
    printf("%d ", k);
    k += 5;
}
while (k < 10);
```

**Ex 5.25**
```c
for (int i = 2; i <= 20; i += 6)
    printf("%d ", i);
```

**Ex 5.26**
```c
for (int i = 10; i > 0; i /= 2)
    printf("%d ", i);
```

**Ex 5.27**
```c
for (int i = 1; i <= 3; i++)
    printf("A");
    printf("B");
printf("\n");
```

**Ex 5.28**
```c
for (int i = 1; i <= 8; i++)
{
    if (i % 2 == 0)
        continue;
    if (i > 6)
        break;
    printf("%d ", i);
}
```

**Ex 5.29**
```c
int x = 20, y = 0;
while (x < 25)
{
    if (x % 2 == 0)
        y += x;
    else
        y--;
    printf("%d ", y);
    x++;
}
```

**Ex 5.30**
```c
for (int i = 1; i <= 3; i++)
{
    for (int j = 1; j <= i; j++)
        printf("%d", j);
    printf("\n");
}
```

**Ex 5.31**
```c
for (int i = 1; i <= 3; i++)
    for (int j = 1; j <= 3; j++)
        printf("%d ", i * j);
```

**Ex 5.32** What is printed?
```c
int count = 0;
for (int i = 0; i < 4; i++)
    for (int j = i; j < 4; j++)
        count++;
printf("%d\n", count);
```

**Ex 5.33**
```c
int a = 0, b = 10;
while (a < b && b > 5)
{
    a += 2;
    b--;
}
printf("%d %d\n", a, b);
```

**Ex 5.34**
```c
int n = 6, steps = 0;
while (n != 1)
{
    if (n % 2 == 0)
        n = n / 2;
    else
        n = 3 * n + 1;
    steps++;
}
printf("%d\n", steps);
```

**Ex 5.35** (from your slides' idea — study the position of the statements)
```c
int b = 10;
while (b >= 7)
{
    b--;
    printf("%d ", b);
}
```

**Ex 5.36**
```c
int total = 0;
for (int i = 1; i <= 10; i++)
{
    if (i % 3 == 0)
        total += i;
}
printf("%d\n", total);
```

**Ex 5.37**
```c
char c;
for (c = 'a'; c <= 'e'; c++)
    printf("%c", c);
printf("\n");
for (c = 'E'; c >= 'A'; c -= 2)
    printf("%c", c);
printf("\n");
```

## Part C — Find and fix the bugs

**Ex 5.38** It should print `ten` only when `x` is 10. It always prints it. Why?
```c
int x = 3;
if (x = 10)
    printf("ten\n");
```

**Ex 5.39** The program never ends. Why? Fix it.
```c
int i = 0;
while (i < 5);
{
    printf("%d\n", i);
    i++;
}
```

**Ex 5.40** The program never ends. Fix it.
```c
int n = 5;
while (n > 0)
{
    printf("%d ", n);
}
```

**Ex 5.41** It should print the **name of the day** only, but prints too much for `2`. Fix it.
```c
int day = 2;
switch (day)
{
    case 1: printf("Monday\n");
    case 2: printf("Tuesday\n");
    case 3: printf("Wednesday\n");
    default: printf("Another day\n");
}
```

**Ex 5.42** Intended: print the numbers **1 to 10**. The result is `0 1 2 ... 9`. Fix it in two different ways.
```c
for (int i = 0; i < 10; i++)
    printf("%d ", i);
```

**Ex 5.43** The programmer wants to test that `x` is between 1 and 10 but it is always true. Fix it.
```c
if (1 <= x <= 10)
    printf("in range\n");
```

**Ex 5.44** This does not compile. Why? Fix it.
```c
int x = 8;
if (x > 5)
    printf("big\n");
    printf("really big\n");
else
    printf("small\n");
```

**Ex 5.45** This does not compile. Why?
```c
int i = 0;
do
{
    printf("%d ", i);
    i++;
}
while (i < 3)
printf("done\n");
```

**Ex 5.46** Why does the compiler reject this?
```c
double price = 2.5;
switch (price)
{
    case 2.5: printf("cheap\n"); break;
    default:  printf("other\n");
}
```

**Ex 5.47** The average of 3, 4 and 4 comes out as `3.000000`. Why? Fix it.
```c
int sum = 3 + 4 + 4;
int count = 3;
float avg = sum / count;
printf("%f\n", avg);
```

**Ex 5.48** Every score of 50 or more gets grade `D` (even 95!). Fix the logic.
```c
if (score >= 50)
    printf("D\n");
else if (score >= 60)
    printf("C\n");
else if (score >= 70)
    printf("B\n");
else if (score >= 80)
    printf("A\n");
else
    printf("F\n");
```

**Ex 5.49** Intended: print `Hello` five times. It prints it once. Fix it.
```c
for (int i = 0; i < 5; i++);
{
    printf("Hello\n");
}
```

**Ex 5.50** Why does this not compile?
```c
int limit = 3, n = 3;
switch (n)
{
    case limit: printf("at the limit\n"); break;
    default:    printf("no\n");
}
```

## Part D1 — Write the program: decisions

*(Read the input with `scanf`. Give a prompt. Use `if`/`switch` as indicated.)*

**Ex 5.51** Read an integer and print whether it is **even** or **odd**.

**Ex 5.52** Read an integer and print whether it is **positive, negative or zero**.

**Ex 5.53** Read three integers and print the **largest** (use `if / else if`, not `?:`).

**Ex 5.54** Read an exam score from 0 to 100 and print the **grade** (A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, F otherwise). If the score is outside 0–100 print `Invalid score`.

**Ex 5.55** Read a year and print whether it is a **leap year** (divisible by 4, except centuries unless divisible by 400).

**Ex 5.56** Read three side lengths and print `Not a triangle`, `Equilateral`, `Isosceles` or `Scalene`.

**Ex 5.57** Read a character and say whether it is a **vowel**, a **consonant** or **not a letter**. Use `switch` for the vowels and handle both upper and lower case.

**Ex 5.58** Read a month number (1–12) and a year. Print the **number of days** in that month (use `switch` with grouped cases; February depends on the leap-year rule).

**Ex 5.59** A **calculator**: read `a op b` (e.g. `8 / 2`) and print the result using a `switch` on the operator. Refuse to divide by zero and report unknown operators.

**Ex 5.60** Read `a`, `b`, `c` of a quadratic equation `ax² + bx + c = 0` and print its roots: two real roots, one repeated root, or "no real roots". If `a` is 0 print "not a quadratic equation". (`sqrt` is in `<math.h>`.)

**Ex 5.61** An **electricity bill**: the first 50 units cost GHS 0.50 each, the next 100 units GHS 0.80 each, and anything above 150 costs GHS 1.20 each. A fixed service charge of GHS 5.00 is added. Read the units used and print the bill.

**Ex 5.62** Read a weight (kg) and height (m); compute the BMI and print its category: below 18.5 Underweight; below 25 Normal; below 30 Overweight; otherwise Obese.

**Ex 5.63** Read three integers and print them in **ascending order** (no arrays, no sorting functions — use `if`s).

**Ex 5.64** **Rock–paper–scissors:** two players each type `r`, `p` or `s`. Print who wins or `Draw`. (rock beats scissors, scissors beat paper, paper beats rock.)

**Ex 5.65** Read a number from 1 to 7 (1 = Monday) and print the **name of the day**; then say whether it is a **weekday** or **weekend**.

**Ex 5.66** **ATM:** the balance is GHS 1000. Read a withdrawal amount and: reject amounts ≤ 0, amounts above the balance, amounts that are not multiples of 10, and amounts above the daily limit of GHS 500. Otherwise dispense the cash and print the new balance.

## Part D2 — Write the program: loops

**Ex 5.67** Read `N`. Print the numbers **1 to N** on one line, then **N down to 1** on the next.

**Ex 5.68** Print all the **multiples of 7** from 7 to 100 on one line and then print **how many** there are.

**Ex 5.69** Read `N`. Print the **sum** of 1 to N, the sum of the **even** numbers up to N and the sum of the **odd** numbers up to N.

**Ex 5.70** Read `N` and print **N!** (N factorial). Use `unsigned long long`. What is the largest `N` that gives a correct answer?

**Ex 5.71** Read `N` and print its **multiplication table** from 1 to 12, in the form `7 x 3 = 21`.

**Ex 5.72** Read `N` and print the first `N` **Fibonacci** numbers (0 1 1 2 3 5 8 …).

**Ex 5.73** Read an integer and print the **number of its digits** and the **sum of its digits**.

**Ex 5.74** Read an integer, **reverse** it, and say whether it is a **palindrome** (reads the same both ways, e.g. 12321).

**Ex 5.75** Read an integer `n > 1` and say whether it is **prime**.

**Ex 5.76** Read `N` and print **all prime numbers** from 2 to N.

**Ex 5.77** Read two positive integers and print their **GCD** (greatest common divisor, using Euclid's algorithm) and their **LCM**.

**Ex 5.78** Read a base `x` and an exponent `n ≥ 0` and compute **xⁿ** using a loop (don't use `pow`).

**Ex 5.79** Read `N` and then `N` numbers; print their **average**.

**Ex 5.80** Read `N` and then `N` integers; print the **largest** and the **smallest**.

**Ex 5.81** Read integers until the user enters `0`. Print how many were **positive**, how many **negative**, and the **sum** of all of them.

**Ex 5.82** Read `n` and say whether it is a **perfect number** (equal to the sum of its proper divisors; e.g. 6 = 1+2+3). Then list all perfect numbers up to 1000.

**Ex 5.83** Print all **Armstrong numbers** between 100 and 999 (a 3-digit number equal to the sum of the cubes of its digits, e.g. 153 = 1³+5³+3³).

**Ex 5.84** Read a non-negative integer and print its **binary** representation.

**Ex 5.85** **Collatz:** read `n`. While `n ≠ 1`: if `n` is even halve it, otherwise replace it by `3n + 1`. Print every value and the number of steps.

**Ex 5.86** Keep asking the user for a number from **1 to 10** until a valid one is entered (use `do while`).

**Ex 5.87** A **menu-driven bank account** program (deposit, withdraw, show balance, exit) with input checks. *(Like the lesson's example, but extend it: reject negative amounts.)*

**Ex 5.88** Print a **table** converting 0 °C to 100 °C in steps of 10 into °F, in neat columns.

**Ex 5.89** You save GHS 1000 at **7%** compound interest per year. Print a **year-by-year table** until the balance has **doubled**, and say how many years it took.

**Ex 5.90** A **guessing game**: the secret number is `37`. Read guesses until correct; print `Too low` / `Too high`, and finally the **number of tries**.

**Ex 5.91** Read `N` and print the sum `1 + 1/2 + 1/3 + … + 1/N`.

**Ex 5.92** Approximate **π** with the Leibniz series `4 × (1 − 1/3 + 1/5 − 1/7 + …)`. Print the approximation for 10, 1000 and 100 000 terms.

**Ex 5.93** Compute the **square root** of a positive number `a` using Newton's method: start with `x = a`, repeat `x = (x + a / x) / 2` until `x*x` is within `0.000000001` of `a`.

**Ex 5.94** **FizzBuzz:** print the numbers 1 to 30, but print `Fizz` for multiples of 3, `Buzz` for multiples of 5 and `FizzBuzz` for multiples of both.

**Ex 5.95** Read a **line of text** one character at a time (`getchar`) until Enter, and count its **letters, digits, vowels and spaces**.

## Part D3 — Write the program: patterns

*(Read `N` (the size) where stated. Think: outer loop = lines, inner loop = one line.)*

**Ex 5.96** A **right triangle** of stars with `N` rows.

**Ex 5.97** An **inverted** right triangle of stars with `N` rows.

**Ex 5.98** A **centred pyramid** with `N` rows (row *i* has `2i − 1` stars).

**Ex 5.99** The **number triangle**: row *i* prints `1 2 … i`.
```
1
12
123
1234
```

**Ex 5.100** **Floyd's triangle** (consecutive numbers fill the rows):
```
1
2 3
4 5 6
7 8 9 10
```

**Ex 5.101** A **hollow rectangle** of stars with `H` rows and `W` columns.

**Ex 5.102** A **diamond** of stars with a maximum width of `2N − 1`.

**Ex 5.103** An `N × N` **multiplication grid** with neat columns.

**Ex 5.104** An 8 × 8 **checkerboard** using `#` and `.`.

**Ex 5.105** The **alphabet triangle**:
```
A
AB
ABC
ABCD
```

**Ex 5.106** **Pascal's triangle** with `N` rows. *(Hint: each number equals the previous number in the row × (row − col) / col — start each row with 1.)*

**Ex 5.107** The **number pyramid**:
```
    1
   121
  12321
 1234321
```

## Part E — Challenges and mini-projects

**Ex 5.108 (prime factors)** Read `n` and print its prime factorisation, e.g. `360 = 2 x 2 x 2 x 3 x 3 x 5`.

**Ex 5.109 (grade book)** Read the number of students `N`, then each student's mark. Print a report: average, highest, lowest, number of **passes** (≥ 50) and number of **distinctions** (≥ 80).

**Ex 5.110 (ATM with PIN)** Allow the user **3 attempts** to enter the PIN `1234`. If they succeed, show a simple menu (balance / withdraw / exit). If they fail three times, print `Card blocked`.

**Ex 5.111 (the computer guesses)** The user thinks of a number from 1 to 100. The computer repeatedly guesses the **middle** of the possible range; the user answers `h` (higher), `l` (lower) or `c` (correct). Print the number of guesses. *(This is binary search from Chapter 0, Ex 0.32.)*

**Ex 5.112 (digital root)** Add the digits of a number repeatedly until a single digit remains (e.g. `9875 → 29 → 11 → 2`).

**Ex 5.113 (check digit)** The **Luhn algorithm** validates card/ID numbers: from the right, double every second digit (subtract 9 if the result is above 9), sum everything; the number is valid if the sum is a multiple of 10. Read a number (as `long long`) and say whether it is valid. (`79927398713` is valid.)

## Part F — Research tasks

**Ex 5.114** What does `goto` do? Why do most programmers avoid it? Is there any situation where it is acceptable?

**Ex 5.115** What do `while (1)` and `for (;;)` mean? Write a program that reads numbers until the user types `0`, using an **infinite loop with `break`**.

**Ex 5.116** Look up `rand()`, `srand()` and `time(NULL)`. Rewrite Ex 5.90 so the secret is a **random** number from 1 to 100.

---

*End of Chapter 5. Next: [Chapter 6 — Functions](06-functions.md)*
