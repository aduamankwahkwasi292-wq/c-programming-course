# Solutions — Chapter 5: Flow of Control

> Back to the lesson: [Chapter 5 lesson](../lessons/05-flow-of-control.md)
>
> There are many ways to solve each problem. If your program gives the same results, it is correct — even if it looks different from mine.

---

## Part A — Quick check

**Ex 5.1** The two categories are **decisions** (`if`, `switch`) and **loops** (`while`, `do while`, `for`). An **iteration** is one single pass through the body of a loop.

**Ex 5.2** `if (7)` → true; `if (0)` → false; `if (-3)` → true. In C, **0 is false and every other value is true**.

**Ex 5.3** In three **separate** `if`s, every condition is tested independently, so several blocks can run. In an `if / else if / else` ladder only the **first** true block runs; the rest are skipped.

**Ex 5.4** The **first** true one, reading from the top. As soon as a true condition is found, its block runs and the rest of the ladder is skipped.

**Ex 5.5** No, it is optional. The final `else` is the "default": it runs when **all** the earlier conditions are false.

**Ex 5.6** `break` jumps out of the `switch` immediately. If you forget it, execution **falls through** into the next case(s) and keeps running until a `break` or the end of the switch.

**Ex 5.7** The `switch` expression must be an **integer or character** type. A `case` label must be a **constant** — not a variable, not a range (`case 1..5` is not C), and not a string. A `double` cannot be used as the switch expression.

**Ex 5.8** `while` tests the condition **before** the body, so the body may never run. `do while` tests **after** the body, so it **always runs at least once**.

**Ex 5.9** `for (initialization; condition; update)`. Order: initialization (once) → condition → body → update → condition → body → update … until the condition is false.

**Ex 5.10** When the body is a **single statement**. It is risky because a second statement added later is *not* part of the `if`/loop even if it is indented (and an `else` can attach to the wrong `if`). Always using braces avoids this.

**Ex 5.11** A **nested statement** is a compound statement (if / switch / loop / function body) placed inside another. Example: an `if` inside a `while`, or a `for` inside a `for`.

**Ex 5.12** `break` **ends the whole loop** immediately. `continue` **skips the rest of the current iteration** and jumps to the next one (re-testing the condition, or running the update in a `for`).

**Ex 5.13**
(a) `for` (known count). (b) `do while` — ask at least once, repeat while the password is wrong (a `while` also works). (c) `while` — repeat until 0 is typed. (d) `do while` — show the menu at least once.

**Ex 5.14** (a) 5 (b) 5 (c) 6 (d) 5 (i = 10, 8, 6, 4, 2) (e) 0 times (f) exactly 1 time

---

## Part B — Predict the output

**Ex 5.15** `C` — `5 > 8` is false and `5 == 8` is false, so the final `else` runs.

**Ex 5.16** `big` — the first true condition wins; `n > 5` is never examined.

**Ex 5.17**
```output
big
medium
positive
```
Three independent `if`s — all three conditions are true.

**Ex 5.18**
```output
Y
Z
```
The `else` belongs to the **inner** `if (b == 1)`. Since `a == 1` is true, the inner `if` is tested; `b == 1` is false, so `Y` is printed. `Z` always prints.

**Ex 5.19** `big` — the `;` after the condition is an **empty statement** that forms the whole `if` body. The `printf` is a separate statement that always runs.

**Ex 5.20**
```output
two
three
```
Case 2 matches, prints `two`, falls through into case 3, prints `three`, and `break` stops it.

**Ex 5.21** `30 days` — case 4 falls through the empty cases 6, 9, 11 and reaches `printf("30")`.

**Ex 5.22** `15 6` — the loop adds 1+2+3+4+5 = 15; `i` ends at 6 (the value that made the test fail).

**Ex 5.23** `3 1 -1` — `n` goes 5 → 3 (print) → 1 (print) → −1 (print); then `-1 > 0` is false.

**Ex 5.24** `10` — the body runs once; then `k = 15`, and `15 < 10` is false.

**Ex 5.25** `2 8 14 20`

**Ex 5.26** `10 5 2 1` — `i /= 2` is integer division: 10 → 5 → 2 → 1 → 0 (stop).

**Ex 5.27**
```output
AAAB
```
Without braces only `printf("A")` is in the loop. `printf("B")` runs once afterwards.

**Ex 5.28** `1 3 5` — evens are skipped by `continue`; at `i = 7` the first `if` is false, the second `if (i > 6)` triggers `break`.

**Ex 5.29** `20 19 41 40 64`

| x | even? | y | printed |
|---|---|---|---|
| 20 | yes | 20 | 20 |
| 21 | no | 19 | 19 |
| 22 | yes | 41 | 41 |
| 23 | no | 40 | 40 |
| 24 | yes | 64 | 64 |

**Ex 5.30**
```output
1
12
123
```

**Ex 5.31** `1 2 3 2 4 6 3 6 9` — all products `i × j`, row by row.

**Ex 5.32** `10` — the inner loop runs 4 + 3 + 2 + 1 times.

**Ex 5.33** `8 6`

| iteration | a | b | test |
|---|---|---|---|
| start | 0 | 10 | |
| 1 | 2 | 9 | `0<10 && 10>5` ✔ |
| 2 | 4 | 8 | ✔ |
| 3 | 6 | 7 | ✔ |
| 4 | 8 | 6 | `6<7 && 7>5` ✔ |
| test | | | `8<6` ✘ → stop |

**Ex 5.34** `8` — the sequence is 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1, which is 8 steps.

**Ex 5.35** `9 8 7 6` — decrease first, then print.

**Ex 5.36** `18` — the multiples of 3 up to 10 are 3, 6, 9.

**Ex 5.37**
```output
abcde
ECA
```
`char` values can be looped like numbers. The second loop goes `E`, `C`, `A`, and then `A − 2` is no longer `>= 'A'`.

---

## Part C — Find and fix the bugs

**Ex 5.38** `x = 10` is an **assignment**, not a comparison. It stores 10 in `x`, and the value of the expression is 10 (non-zero → true), so `ten` is always printed. Fix: `if (x == 10)`.

**Ex 5.39** The `;` after `while (i < 5)` is the (empty) body of the loop. `i` is never changed inside it, so the loop never ends. Fix: remove the `;`:
```c
int i = 0;
while (i < 5)
{
    printf("%d\n", i);
    i++;
}
```

**Ex 5.40** `n` is never changed — there is no **update**. Add `n--;` inside the loop.
```c
while (n > 0)
{
    printf("%d ", n);
    n--;
}
```

**Ex 5.41** Without `break`, the cases fall through. Fix:
```c
switch (day)
{
    case 1: printf("Monday\n");    break;
    case 2: printf("Tuesday\n");   break;
    case 3: printf("Wednesday\n"); break;
    default: printf("Another day\n");
}
```

**Ex 5.42** Two fixes:
```c
for (int i = 1; i <= 10; i++)         /* start at 1, include 10 */
    printf("%d ", i);

for (int i = 0; i < 10; i++)          /* or keep the loop and print i + 1 */
    printf("%d ", i + 1);
```

**Ex 5.43** `1 <= x <= 10` is read as `(1 <= x) <= 10`; `(1 <= x)` is 0 or 1, and both are `<= 10`. Fix: `if (x >= 1 && x <= 10)`.

**Ex 5.44** There are two statements after the first `if`, but no braces. So only the first `printf` belongs to the `if`; the `else` then has no `if` to belong to (a compile error). Fix:
```c
#include <stdio.h>

int main(void)
{
    int x = 8;

    if (x > 5)
    {
        printf("big\n");
        printf("really big\n");
    }
    else
    {
        printf("small\n");
    }
    return 0;
}
```
```output
big
really big
```

**Ex 5.45** A `do { } while (condition);` **must end with a semicolon** — it's missing after `while (i < 3)`.

**Ex 5.46** The `switch` expression must be an integer or character type; a `double` is not allowed. Use `if`: `if (price == 2.5) …` (and remember that comparing decimals with `==` is fragile; for money, a common practice is to store the amount in whole pesewas as an `int`).

**Ex 5.47** `sum / count` is **integer division** (`11 / 3 = 3`) and only then converted to `float`. Fix: `float avg = (float) sum / count;`
```c
#include <stdio.h>

int main(void)
{
    int sum = 3 + 4 + 4;
    int count = 3;
    float avg = (float) sum / count;
    printf("%f\n", avg);
    return 0;
}
```
```output
3.666667
```

**Ex 5.48** The conditions are in the wrong order: every score of at least 50 satisfies the very first test, so the others are never reached. Test from the **highest** band to the lowest:
```c
if (score >= 80)
    printf("A\n");
else if (score >= 70)
    printf("B\n");
else if (score >= 60)
    printf("C\n");
else if (score >= 50)
    printf("D\n");
else
    printf("F\n");
```

**Ex 5.49** The stray `;` after the `for` header is the loop's body — an empty statement — so the loop runs five times doing nothing, and then the block with `printf` runs **once**. Fix: remove the `;`.

**Ex 5.50** A `case` label must be a **constant expression**. A variable (even one that never changes) is not allowed. Use a literal (`case 3:`) or a `#define LIMIT 3` / an `enum` constant.

---

## Part D1 — Decisions

**Ex 5.51**
<!--in: -7-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n % 2 == 0)
        printf("%d is even\n", n);
    else
        printf("%d is odd\n", n);
    return 0;
}
```
```output
Enter an integer: -7
-7 is odd
```
(`-7 % 2` is `-1`, which is not `0`, so negative odd numbers are handled correctly: we test `== 0`, never `== 1`.)

**Ex 5.52**
<!--in: 0-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n > 0)
        printf("%d is positive\n", n);
    else if (n < 0)
        printf("%d is negative\n", n);
    else
        printf("%d is zero\n", n);
    return 0;
}
```
```output
Enter an integer: 0
0 is zero
```

**Ex 5.53**
<!--in: 12 45 30-->
```c
#include <stdio.h>

int main(void)
{
    int a, b, c, largest;

    printf("Enter three integers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a >= b && a >= c)
        largest = a;
    else if (b >= a && b >= c)
        largest = b;
    else
        largest = c;

    printf("The largest is %d\n", largest);
    return 0;
}
```
```output
Enter three integers: 12 45 30
The largest is 45
```

**Ex 5.54**
<!--in: 85-->
```c
#include <stdio.h>

int main(void)
{
    int score;

    printf("Enter the score (0-100): ");
    scanf("%d", &score);

    if (score < 0 || score > 100)
        printf("Invalid score\n");
    else if (score >= 80)
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
Enter the score (0-100): 85
Grade A
```
Test also: `105` → Invalid score; `-3` → Invalid score; `49` → Grade F; `50` → Grade D.

**Ex 5.55**
<!--in: 2000-->
```c
#include <stdio.h>

int main(void)
{
    int year;

    printf("Enter a year: ");
    scanf("%d", &year);

    if (year % 400 == 0)
        printf("%d is a leap year\n", year);
    else if (year % 100 == 0)
        printf("%d is not a leap year\n", year);
    else if (year % 4 == 0)
        printf("%d is a leap year\n", year);
    else
        printf("%d is not a leap year\n", year);
    return 0;
}
```
```output
Enter a year: 2000
2000 is a leap year
```

**Ex 5.56** A valid triangle needs positive sides, and each pair of sides must add up to **more** than the third.
<!--in: 5 5 8-->
```c
#include <stdio.h>

int main(void)
{
    double a, b, c;

    printf("Enter three sides: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a)
        printf("Not a triangle\n");
    else if (a == b && b == c)
        printf("Equilateral\n");
    else if (a == b || b == c || a == c)
        printf("Isosceles\n");
    else
        printf("Scalene\n");
    return 0;
}
```
```output
Enter three sides: 5 5 8
Isosceles
```
Try `3 4 5` (Scalene), `4 4 4` (Equilateral), `1 2 5` (Not a triangle).

**Ex 5.57**
<!--in: E-->
```c
#include <stdio.h>

int main(void)
{
    char ch;

    printf("Enter a character: ");
    scanf(" %c", &ch);

    switch (ch)
    {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
            printf("%c is a vowel\n", ch);
            break;
        default:
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
                printf("%c is a consonant\n", ch);
            else
                printf("%c is not a letter\n", ch);
    }
    return 0;
}
```
```output
Enter a character: E
E is a vowel
```

**Ex 5.58**
<!--in: 2 2024-->
```c
#include <stdio.h>

int main(void)
{
    int month, year, days;

    printf("Enter month (1-12) and year: ");
    scanf("%d %d", &month, &year);

    switch (month)
    {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            days = 31;
            break;
        case 4: case 6: case 9: case 11:
            days = 30;
            break;
        case 2:
            if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
                days = 29;
            else
                days = 28;
            break;
        default:
            days = 0;
    }

    if (days == 0)
        printf("Invalid month\n");
    else
        printf("%d days\n", days);
    return 0;
}
```
```output
Enter month (1-12) and year: 2 2024
29 days
```

**Ex 5.59**
<!--in: 8 / 2-->
```c
#include <stdio.h>

int main(void)
{
    double a, b;
    char op;

    printf("Enter an expression (e.g. 8 / 2): ");
    scanf("%lf %c %lf", &a, &op, &b);

    switch (op)
    {
        case '+': printf("%.2f\n", a + b); break;
        case '-': printf("%.2f\n", a - b); break;
        case '*': printf("%.2f\n", a * b); break;
        case '/':
            if (b == 0)
                printf("Error: division by zero\n");
            else
                printf("%.2f\n", a / b);
            break;
        default:
            printf("Unknown operator '%c'\n", op);
    }
    return 0;
}
```
```output
Enter an expression (e.g. 8 / 2): 8 / 2
4.00
```
With `8 / 0` it prints `Error: division by zero`; with `8 % 2` it prints `Unknown operator '%'`.

**Ex 5.60**
<!--in: 1 -3 2-->
```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double a, b, c;

    printf("Enter a, b and c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    if (a == 0)
    {
        printf("Not a quadratic equation\n");
    }
    else
    {
        double disc = b * b - 4 * a * c;

        if (disc > 0)
        {
            double r1 = (-b + sqrt(disc)) / (2 * a);
            double r2 = (-b - sqrt(disc)) / (2 * a);
            printf("Two real roots: %.2f and %.2f\n", r1, r2);
        }
        else if (disc == 0)
        {
            printf("One repeated root: %.2f\n", -b / (2 * a));
        }
        else
        {
            printf("No real roots\n");
        }
    }
    return 0;
}
```
```output
Enter a, b and c: 1 -3 2
Two real roots: 2.00 and 1.00
```

**Ex 5.61**
<!--in: 180-->
```c
#include <stdio.h>

int main(void)
{
    int units;
    double bill;

    printf("Units used: ");
    scanf("%d", &units);

    if (units <= 50)
        bill = units * 0.50;
    else if (units <= 150)
        bill = 50 * 0.50 + (units - 50) * 0.80;
    else
        bill = 50 * 0.50 + 100 * 0.80 + (units - 150) * 1.20;

    bill += 5.00;                       /* service charge */
    printf("Bill: GHS %.2f\n", bill);
    return 0;
}
```
```output
Units used: 180
Bill: GHS 146.00
```
Check: 25 + 80 + 36 + 5 = 146.

**Ex 5.62**
<!--in: 68 1.75-->
```c
#include <stdio.h>

int main(void)
{
    double weight, height;

    printf("Weight (kg) and height (m): ");
    scanf("%lf %lf", &weight, &height);

    double bmi = weight / (height * height);
    printf("BMI = %.1f ", bmi);

    if (bmi < 18.5)
        printf("(Underweight)\n");
    else if (bmi < 25)
        printf("(Normal)\n");
    else if (bmi < 30)
        printf("(Overweight)\n");
    else
        printf("(Obese)\n");
    return 0;
}
```
```output
Weight (kg) and height (m): 68 1.75
BMI = 22.2 (Normal)
```

**Ex 5.63** Compare-and-swap three times (like a tiny sorting network):
<!--in: 9 4 7-->
```c
#include <stdio.h>

int main(void)
{
    int a, b, c, temp;

    printf("Enter three integers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b) { temp = a; a = b; b = temp; }
    if (b > c) { temp = b; b = c; c = temp; }
    if (a > b) { temp = a; a = b; b = temp; }

    printf("Ascending: %d %d %d\n", a, b, c);
    return 0;
}
```
```output
Enter three integers: 9 4 7
Ascending: 4 7 9
```
After the first two comparisons the largest value is guaranteed to be in `c`; the third comparison fixes `a` and `b`.

**Ex 5.64**
<!--in: r s-->
```c
#include <stdio.h>

int main(void)
{
    char p1, p2;

    printf("Player 1 and player 2 (r/p/s): ");
    scanf(" %c %c", &p1, &p2);

    if (p1 == p2)
        printf("Draw\n");
    else if ((p1 == 'r' && p2 == 's') ||
             (p1 == 's' && p2 == 'p') ||
             (p1 == 'p' && p2 == 'r'))
        printf("Player 1 wins\n");
    else
        printf("Player 2 wins\n");
    return 0;
}
```
```output
Player 1 and player 2 (r/p/s): r s
Player 1 wins
```

**Ex 5.65**
<!--in: 6-->
```c
#include <stdio.h>

int main(void)
{
    int day;

    printf("Enter a day number (1 = Monday): ");
    scanf("%d", &day);

    switch (day)
    {
        case 1: printf("Monday\n");    break;
        case 2: printf("Tuesday\n");   break;
        case 3: printf("Wednesday\n"); break;
        case 4: printf("Thursday\n");  break;
        case 5: printf("Friday\n");    break;
        case 6: printf("Saturday\n");  break;
        case 7: printf("Sunday\n");    break;
        default:
            printf("Invalid day\n");
            return 0;
    }

    if (day >= 6)
        printf("Weekend\n");
    else
        printf("Weekday\n");
    return 0;
}
```
```output
Enter a day number (1 = Monday): 6
Saturday
Weekend
```

**Ex 5.66**
<!--in: 250-->
```c
#include <stdio.h>

int main(void)
{
    int balance = 1000;
    int amount;

    printf("Balance: GHS %d. Amount to withdraw: ", balance);
    scanf("%d", &amount);

    if (amount <= 0)
        printf("Invalid amount\n");
    else if (amount > balance)
        printf("Insufficient funds\n");
    else if (amount % 10 != 0)
        printf("Amount must be a multiple of 10\n");
    else if (amount > 500)
        printf("Daily limit is GHS 500\n");
    else
    {
        balance -= amount;
        printf("Dispensing GHS %d\n", amount);
        printf("New balance: GHS %d\n", balance);
    }
    return 0;
}
```
```output
Balance: GHS 1000. Amount to withdraw: 250
Dispensing GHS 250
New balance: GHS 750
```
Note the order of the checks: each `else if` assumes the earlier ones were false.

---

## Part D2 — Loops

**Ex 5.67**
<!--in: 5-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
        printf("%d ", i);
    printf("\n");

    for (int i = n; i >= 1; i--)
        printf("%d ", i);
    printf("\n");
    return 0;
}
```
```output
Enter N: 5
1 2 3 4 5
5 4 3 2 1
```

**Ex 5.68** The loop steps by 7 — no `if` needed.
```c
#include <stdio.h>

int main(void)
{
    int count = 0;

    for (int m = 7; m <= 100; m += 7)
    {
        printf("%d ", m);
        count++;
    }
    printf("\nCount: %d\n", count);
    return 0;
}
```
```output
7 14 21 28 35 42 49 56 63 70 77 84 91 98
Count: 14
```

**Ex 5.69**
<!--in: 10-->
```c
#include <stdio.h>

int main(void)
{
    int n, sum = 0, evens = 0, odds = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        sum += i;
        if (i % 2 == 0)
            evens += i;
        else
            odds += i;
    }

    printf("Sum of 1 to %d : %d\n", n, sum);
    printf("Sum of evens   : %d\n", evens);
    printf("Sum of odds    : %d\n", odds);
    return 0;
}
```
```output
Enter N: 10
Sum of 1 to 10 : 55
Sum of evens   : 30
Sum of odds    : 25
```

**Ex 5.70** The product must start at **1** (not 0). `unsigned long long` holds numbers up to about 1.8 × 10¹⁹.
<!--in: 20-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    unsigned long long f = 1;

    printf("Enter N: ");
    scanf("%d", &n);

    for (int i = 2; i <= n; i++)
        f *= i;

    printf("%d! = %llu\n", n, f);
    return 0;
}
```
```output
Enter N: 20
20! = 2432902008176640000
```
**The largest correct `N` is 20.** 21! is about 5.1 × 10¹⁹, which does not fit in 64 bits, so the result silently wraps around to a wrong number. (A `double` can hold bigger values, but only approximately.)

**Ex 5.71**
<!--in: 7-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Table of: ");
    scanf("%d", &n);

    for (int i = 1; i <= 12; i++)
        printf("%d x %d = %d\n", n, i, n * i);
    return 0;
}
```
```output
Table of: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
```

**Ex 5.72** Keep the last two numbers; each new one is their sum.
<!--in: 10-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    long long a = 0, b = 1;

    printf("How many terms? ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("%lld ", a);
        long long next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
    return 0;
}
```
```output
How many terms? 10
0 1 1 2 3 5 8 13 21 34
```

**Ex 5.73** A `do while` handles `0` correctly (it has one digit). We use `-n` for negative numbers.
<!--in: 4096-->
```c
#include <stdio.h>

int main(void)
{
    int n, count = 0, sum = 0;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n < 0)
        n = -n;

    do
    {
        sum += n % 10;
        count++;
        n /= 10;
    }
    while (n > 0);

    printf("Digits: %d, sum of digits: %d\n", count, sum);
    return 0;
}
```
```output
Enter an integer: 4096
Digits: 4, sum of digits: 19
```

**Ex 5.74**
<!--in: 12321-->
```c
#include <stdio.h>

int main(void)
{
    int n, original, rev = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &n);
    original = n;

    while (n > 0)
    {
        rev = rev * 10 + n % 10;     /* append the last digit of n to rev */
        n /= 10;                     /* drop the last digit of n          */
    }

    printf("Reversed: %d\n", rev);
    if (rev == original)
        printf("%d is a palindrome\n", original);
    else
        printf("%d is not a palindrome\n", original);
    return 0;
}
```
```output
Enter a positive integer: 12321
Reversed: 12321
12321 is a palindrome
```

**Ex 5.75**
<!--in: 97-->
```c
#include <stdio.h>

int main(void)
{
    int n, isPrime = 1;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n < 2)
        isPrime = 0;
    else
        for (int d = 2; d * d <= n; d++)
            if (n % d == 0)
            {
                isPrime = 0;
                break;
            }

    if (isPrime)
        printf("%d is prime\n", n);
    else
        printf("%d is not prime\n", n);
    return 0;
}
```
```output
Enter an integer: 97
97 is prime
```

**Ex 5.76**
<!--in: 30-->
```c
#include <stdio.h>

int main(void)
{
    int limit;

    printf("Primes up to: ");
    scanf("%d", &limit);

    for (int n = 2; n <= limit; n++)
    {
        int isPrime = 1;
        for (int d = 2; d * d <= n; d++)
        {
            if (n % d == 0)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime)
            printf("%d ", n);
    }
    printf("\n");
    return 0;
}
```
```output
Primes up to: 30
2 3 5 7 11 13 17 19 23 29
```

**Ex 5.77** Euclid: replace `(a, b)` by `(b, a mod b)` until `b` is 0; `a` is the GCD. Then LCM = a × b ÷ GCD.
<!--in: 48 18-->
```c
#include <stdio.h>

int main(void)
{
    int a, b;

    printf("Enter two positive integers: ");
    scanf("%d %d", &a, &b);

    int x = a, y = b;
    while (y != 0)
    {
        int remainder = x % y;
        x = y;
        y = remainder;
    }

    printf("GCD = %d\n", x);
    printf("LCM = %d\n", a / x * b);       /* divide first to avoid overflow */
    return 0;
}
```
```output
Enter two positive integers: 48 18
GCD = 6
LCM = 144
```

**Ex 5.78**
<!--in: 2 10-->
```c
#include <stdio.h>

int main(void)
{
    double x, result = 1;
    int n;

    printf("Enter base and exponent: ");
    scanf("%lf %d", &x, &n);

    for (int i = 0; i < n; i++)
        result *= x;

    printf("%g ^ %d = %g\n", x, n, result);
    return 0;
}
```
```output
Enter base and exponent: 2 10
2 ^ 10 = 1024
```
(`result` starts at 1 — the "do nothing" value for multiplication — so `x⁰ = 1`.)

**Ex 5.79**
<!--in: 5 70 80 90 60 75-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    double x, sum = 0;

    printf("How many numbers? ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        printf("Number %d: ", i);
        scanf("%lf", &x);
        sum += x;
    }

    printf("Average = %.2f\n", sum / n);
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

**Ex 5.80** Start `largest` and `smallest` with the **first** value (not 0 — remember Ex 0.17).
<!--in: 6 12 -5 40 7 0 33-->
```c
#include <stdio.h>

int main(void)
{
    int n, x, largest, smallest;

    printf("How many integers? ");
    scanf("%d", &n);

    printf("Integer 1: ");
    scanf("%d", &x);
    largest = smallest = x;

    for (int i = 2; i <= n; i++)
    {
        printf("Integer %d: ", i);
        scanf("%d", &x);
        if (x > largest)
            largest = x;
        if (x < smallest)
            smallest = x;
    }

    printf("Largest : %d\n", largest);
    printf("Smallest: %d\n", smallest);
    return 0;
}
```
```output
How many integers? 6
Integer 1: 12
Integer 2: -5
Integer 3: 40
Integer 4: 7
Integer 5: 0
Integer 6: 33
Largest : 40
Smallest: -5
```

**Ex 5.81** The value `0` is the **sentinel** that ends the input.
<!--in: 4 -2 9 -7 0-->
```c
#include <stdio.h>

int main(void)
{
    int x, positives = 0, negatives = 0, sum = 0;

    printf("Enter integers (0 to stop): ");
    scanf("%d", &x);

    while (x != 0)
    {
        if (x > 0)
            positives++;
        else
            negatives++;
        sum += x;
        scanf("%d", &x);
    }

    printf("Positives: %d\n", positives);
    printf("Negatives: %d\n", negatives);
    printf("Sum      : %d\n", sum);
    return 0;
}
```
```output
Enter integers (0 to stop): 4 -2 9 -7 0
Positives: 2
Negatives: 2
Sum      : 4
```

**Ex 5.82**
<!--in: 28-->
```c
#include <stdio.h>

int main(void)
{
    int n, sum = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for (int d = 1; d <= n / 2; d++)       /* proper divisors are at most n/2 */
        if (n % d == 0)
            sum += d;

    if (n > 0 && sum == n)
        printf("%d is a perfect number\n", n);
    else
        printf("%d is not a perfect number\n", n);

    printf("Perfect numbers up to 1000: ");
    for (int k = 2; k <= 1000; k++)
    {
        int s = 0;
        for (int d = 1; d <= k / 2; d++)
            if (k % d == 0)
                s += d;
        if (s == k)
            printf("%d ", k);
    }
    printf("\n");
    return 0;
}
```
```output
Enter a positive integer: 28
28 is a perfect number
Perfect numbers up to 1000: 6 28 496
```

**Ex 5.83**
```c
#include <stdio.h>

int main(void)
{
    for (int n = 100; n <= 999; n++)
    {
        int a = n / 100;
        int b = (n / 10) % 10;
        int c = n % 10;

        if (a * a * a + b * b * b + c * c * c == n)
            printf("%d ", n);
    }
    printf("\n");
    return 0;
}
```
```output
153 370 371 407
```

**Ex 5.84** Find the largest power of two not above `n`, then peel off the bits from the top.
<!--in: 37-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    printf("Binary: ");
    if (n == 0)
    {
        printf("0");
    }
    else
    {
        int p = 1;
        while (p * 2 <= n)          /* largest power of 2 that is <= n */
            p *= 2;

        while (p > 0)
        {
            printf("%d", n / p);    /* 1 if this power fits, otherwise 0 */
            n = n % p;
            p = p / 2;
        }
    }
    printf("\n");
    return 0;
}
```
```output
Enter a non-negative integer: 37
Binary: 100101
```
Check: 32 + 4 + 1 = 37 ✔. (In Chapter 7 you'll be able to store the digits in an array and print them in reverse — another common approach.)

**Ex 5.85**
<!--in: 6-->
```c
#include <stdio.h>

int main(void)
{
    int n, steps = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    printf("%d", n);
    while (n != 1)
    {
        if (n % 2 == 0)
            n = n / 2;
        else
            n = 3 * n + 1;
        printf(" -> %d", n);
        steps++;
    }
    printf("\nSteps: %d\n", steps);
    return 0;
}
```
```output
Enter a positive integer: 6
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Steps: 8
```
(Nobody has ever proved that this loop ends for **every** starting value — it is the famous Collatz conjecture!)

**Ex 5.86**
<!--in: 0\n11\n5-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    do
    {
        printf("Enter a number from 1 to 10: ");
        scanf("%d", &n);
        if (n < 1 || n > 10)
            printf("Invalid! Try again.\n");
    }
    while (n < 1 || n > 10);

    printf("Valid: %d\n", n);
    return 0;
}
```
```output
Enter a number from 1 to 10: 0
Invalid! Try again.
Enter a number from 1 to 10: 11
Invalid! Try again.
Enter a number from 1 to 10: 5
Valid: 5
```

**Ex 5.87**
<!--in: 1 500\n1 -20\n2 700\n2 200\n3\n4-->
```c
#include <stdio.h>

int main(void)
{
    double balance = 0, amount;
    int choice;

    do
    {
        printf("\n1) Deposit  2) Withdraw  3) Balance  4) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
            case 2:
                printf("Amount: ");
                scanf("%lf", &amount);
                if (amount <= 0)
                {
                    printf("Amount must be positive\n");
                    break;
                }
                if (choice == 1)
                {
                    balance += amount;
                    printf("Deposited %.2f\n", amount);
                }
                else if (amount > balance)
                {
                    printf("Insufficient funds\n");
                }
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
Choose: 1
Amount: 500
Deposited 500.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 1
Amount: -20
Amount must be positive

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 2
Amount: 700
Insufficient funds

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 2
Amount: 200
Withdrew 200.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 3
Balance: 300.00

1) Deposit  2) Withdraw  3) Balance  4) Exit
Choose: 4
Goodbye!
```
(Cases 1 and 2 share the "ask for an amount and validate it" code — a good use of fall-through.)

**Ex 5.88**
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    printf("%8s %12s\n", "Celsius", "Fahrenheit");
    for (int c = 0; c <= 100; c += 10)
        printf("%8d %12.1f\n", c, c * 9.0 / 5 + 32);
    return 0;
}
```
```output
 Celsius   Fahrenheit
       0         32.0
      10         50.0
      20         68.0
      30         86.0
      40        104.0
      50        122.0
      60        140.0
      70        158.0
      80        176.0
      90        194.0
     100        212.0
```

**Ex 5.89**
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    double balance = 1000;
    int year = 0;

    printf("%6s %12s\n", "Year", "Balance");
    while (balance < 2000)
    {
        balance *= 1.07;
        year++;
        printf("%6d %12.2f\n", year, balance);
    }
    printf("The money doubled after %d years.\n", year);
    return 0;
}
```
```output
  Year      Balance
     1      1070.00
     2      1144.90
     3      1225.04
     4      1310.80
     5      1402.55
     6      1500.73
     7      1605.78
     8      1718.19
     9      1838.46
    10      1967.15
    11      2104.85
The money doubled after 11 years.
```
(The "Rule of 72" says 72 ÷ 7 ≈ 10.3 years — our answer of 11 whole years agrees.)

**Ex 5.90**
<!--in: 50 25 37-->
```c
#include <stdio.h>

int main(void)
{
    int secret = 37, guess, tries = 0;

    do
    {
        printf("Your guess: ");
        scanf("%d", &guess);
        tries++;

        if (guess < secret)
            printf("Too low\n");
        else if (guess > secret)
            printf("Too high\n");
    }
    while (guess != secret);

    printf("Correct! It took you %d tries.\n", tries);
    return 0;
}
```
```output
Your guess: 50
Too high
Your guess: 25
Too low
Your guess: 37
Correct! It took you 3 tries.
```

**Ex 5.91** Use `1.0 / i` — with plain `1 / i` integer division would give 0 for every `i > 1`.
<!--in: 10-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    double sum = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
        sum += 1.0 / i;

    printf("Sum = %.6f\n", sum);
    return 0;
}
```
```output
Enter N: 10
Sum = 2.928968
```

**Ex 5.92** The signs alternate; `sign` flips between `+1` and `−1`.
```c
#include <stdio.h>

int main(void)
{
    int terms[3] = {10, 1000, 100000};

    for (int t = 0; t < 3; t++)
    {
        double sum = 0;
        double sign = 1;

        for (int k = 0; k < terms[t]; k++)
        {
            sum += sign / (2 * k + 1);      /* 1, 1/3, 1/5, 1/7, ... */
            sign = -sign;
        }
        printf("%6d terms: pi = %.6f\n", terms[t], 4 * sum);
    }
    return 0;
}
```
```output
    10 terms: pi = 3.041840
  1000 terms: pi = 3.140593
100000 terms: pi = 3.141583
```
(The series converges slowly: 100 000 terms give only five correct digits. Don't worry about the array `terms` — it's Chapter 7.)

**Ex 5.93**
<!--in: 2-->
```c
#include <stdio.h>

int main(void)
{
    double a, x;

    printf("Enter a positive number: ");
    scanf("%lf", &a);

    x = a;
    while (x * x - a > 0.000000001 || a - x * x > 0.000000001)
        x = (x + a / x) / 2;

    printf("sqrt(%g) = %.6f\n", a, x);
    return 0;
}
```
```output
Enter a positive number: 2
sqrt(2) = 1.414214
```
Each step roughly doubles the number of correct digits, so only a handful of iterations are needed.

**Ex 5.94**
```c
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 30; i++)
    {
        if (i % 15 == 0)
            printf("FizzBuzz ");
        else if (i % 3 == 0)
            printf("Fizz ");
        else if (i % 5 == 0)
            printf("Buzz ");
        else
            printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```
```output
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz
```
Test for "both" (15) **first** — otherwise 15 would be caught by the "multiple of 3" test.

**Ex 5.95**
<!--in: Hello World 2026!-->
```c
#include <stdio.h>

int main(void)
{
    int ch, letters = 0, digits = 0, vowels = 0, spaces = 0;

    printf("Type a line of text: ");
    while ((ch = getchar()) != '\n' && ch != EOF)
    {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
        {
            letters++;
            switch (ch)
            {
                case 'a': case 'e': case 'i': case 'o': case 'u':
                case 'A': case 'E': case 'I': case 'O': case 'U':
                    vowels++;
            }
        }
        else if (ch >= '0' && ch <= '9')
            digits++;
        else if (ch == ' ')
            spaces++;
    }

    printf("Letters: %d, digits: %d, vowels: %d, spaces: %d\n", letters, digits, vowels, spaces);
    return 0;
}
```
```output
Type a line of text: Hello World 2026!
Letters: 10, digits: 4, vowels: 3, spaces: 2
```

---

## Part D3 — Patterns

For every pattern: **outer loop = one iteration per line; inner loop(s) = what goes on that line; `\n` after the inner loops.**

**Ex 5.96**
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
*
**
***
****
```

**Ex 5.97**
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = n; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
****
***
**
*
```

**Ex 5.98** Row `i` has `n − i` leading spaces and `2i − 1` stars.
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int s = 1; s <= n - i; s++)
            printf(" ");
        for (int j = 1; j <= 2 * i - 1; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
   *
  ***
 *****
*******
```

**Ex 5.99**
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            printf("%d", j);
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
1
12
123
1234
```

**Ex 5.100** A counter `num` is shared by all the rows and never reset.
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n, num = 1;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("%d ", num);
            num++;
        }
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
1
2 3
4 5 6
7 8 9 10
```

**Ex 5.101** Print a star only on the **border**: first/last row, first/last column.
<!--in: 4 10-->
```c
#include <stdio.h>

int main(void)
{
    int h, w;

    printf("Height and width: ");
    scanf("%d %d", &h, &w);

    for (int i = 1; i <= h; i++)
    {
        for (int j = 1; j <= w; j++)
        {
            if (i == 1 || i == h || j == 1 || j == w)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
    return 0;
}
```
```output
Height and width: 4 10
**********
*        *
*        *
**********
```

**Ex 5.102** An upper half (growing, like the pyramid) plus a lower half (shrinking).
<!--in: 3-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)                 /* upper half, including the widest row */
    {
        for (int s = 1; s <= n - i; s++)
            printf(" ");
        for (int j = 1; j <= 2 * i - 1; j++)
            printf("*");
        printf("\n");
    }
    for (int i = n - 1; i >= 1; i--)             /* lower half */
    {
        for (int s = 1; s <= n - i; s++)
            printf(" ");
        for (int j = 1; j <= 2 * i - 1; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
N: 3
  *
 ***
*****
 ***
  *
```

**Ex 5.103**
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            printf("%4d", i * j);
        printf("\n");
    }
    return 0;
}
```
```output
N: 4
   1   2   3   4
   2   4   6   8
   3   6   9  12
   4   8  12  16
```

**Ex 5.104** The colour of a square depends on whether `row + column` is even or odd.
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    for (int row = 0; row < 8; row++)
    {
        for (int col = 0; col < 8; col++)
        {
            if ((row + col) % 2 == 0)
                printf("#");
            else
                printf(".");
        }
        printf("\n");
    }
    return 0;
}
```
```output
#.#.#.#.
.#.#.#.#
#.#.#.#.
.#.#.#.#
#.#.#.#.
.#.#.#.#
#.#.#.#.
.#.#.#.#
```

**Ex 5.105** Letters are numbers: `'A' + 0` is `'A'`, `'A' + 1` is `'B'`…
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < i; j++)
            printf("%c", 'A' + j);
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
A
AB
ABC
ABCD
```

**Ex 5.106** Each entry is the previous one × `(i − j) / (j + 1)` — the formula for the binomial coefficient. (Multiply *before* dividing so the integer division is exact.)
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    int n = 5;

    for (int i = 0; i < n; i++)
    {
        printf("%*s", 2 * (n - i - 1), "");        /* indentation to centre the row */

        int value = 1;
        for (int j = 0; j <= i; j++)
        {
            printf("%4d", value);
            value = value * (i - j) / (j + 1);
        }
        printf("\n");
    }
    return 0;
}
```
```output
           1
         1   1
       1   2   1
     1   3   3   1
   1   4   6   4   1
```

**Ex 5.107** For row `i`: leading spaces, then `1 … i` going up, then `i − 1 … 1` coming down.
<!--in: 4-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Rows: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int s = 1; s <= n - i; s++)
            printf(" ");
        for (int j = 1; j <= i; j++)
            printf("%d", j);
        for (int j = i - 1; j >= 1; j--)
            printf("%d", j);
        printf("\n");
    }
    return 0;
}
```
```output
Rows: 4
   1
  121
 12321
1234321
```

---

## Part E — Challenges and mini-projects

**Ex 5.108** Divide by 2 as long as possible, then 3, then 4 (it will never divide — all its factors were already removed), then 5 … Whatever is left at the end is itself prime.
<!--in: 360-->
```c
#include <stdio.h>

int main(void)
{
    int n, original, first = 1;

    printf("Enter an integer greater than 1: ");
    scanf("%d", &n);
    original = n;

    printf("%d = ", original);
    for (int f = 2; n > 1; f++)
    {
        while (n % f == 0)
        {
            if (!first)
                printf(" x ");
            printf("%d", f);
            first = 0;
            n /= f;
        }
    }
    printf("\n");
    return 0;
}
```
```output
Enter an integer greater than 1: 360
360 = 2 x 2 x 2 x 3 x 3 x 5
```

**Ex 5.109**
<!--in: 5 78 45 91 60 85-->
```c
#include <stdio.h>

int main(void)
{
    int n, passes = 0, distinctions = 0;
    double mark, sum = 0, highest, lowest;

    printf("Number of students: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        printf("Mark of student %d: ", i);
        scanf("%lf", &mark);

        sum += mark;
        if (i == 1 || mark > highest)
            highest = mark;
        if (i == 1 || mark < lowest)
            lowest = mark;
        if (mark >= 50)
            passes++;
        if (mark >= 80)
            distinctions++;
    }

    printf("\n=== CLASS REPORT ===\n");
    printf("Average      : %.2f\n", sum / n);
    printf("Highest      : %.0f\n", highest);
    printf("Lowest       : %.0f\n", lowest);
    printf("Passes       : %d of %d\n", passes, n);
    printf("Distinctions : %d\n", distinctions);
    return 0;
}
```
```output
Number of students: 5
Mark of student 1: 78
Mark of student 2: 45
Mark of student 3: 91
Mark of student 4: 60
Mark of student 5: 85

=== CLASS REPORT ===
Average      : 71.80
Highest      : 91
Lowest       : 45
Passes       : 4 of 5
Distinctions : 2
```

**Ex 5.110** The first run below: two wrong PINs, then the right one, and a short session.
<!--in: 1111\n2222\n1234\n1\n2 200\n1\n3-->
```c
#include <stdio.h>

int main(void)
{
    const int PIN = 1234;
    double balance = 1000;
    int attempt, entered = 0, choice;

    for (attempt = 1; attempt <= 3; attempt++)
    {
        printf("Enter PIN: ");
        scanf("%d", &entered);
        if (entered == PIN)
            break;
        printf("Wrong PIN (%d attempt(s) left)\n", 3 - attempt);
    }

    if (entered != PIN)
    {
        printf("Card blocked\n");
        return 0;
    }

    do
    {
        printf("\n1) Balance  2) Withdraw  3) Exit\nChoose: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("Balance: %.2f\n", balance);
        }
        else if (choice == 2)
        {
            double amount;
            printf("Amount: ");
            scanf("%lf", &amount);
            if (amount > 0 && amount <= balance)
            {
                balance -= amount;
                printf("Please take your cash\n");
            }
            else
                printf("Cannot process that amount\n");
        }
    }
    while (choice != 3);

    printf("Thank you!\n");
    return 0;
}
```
```output
Enter PIN: 1111
Wrong PIN (2 attempt(s) left)
Enter PIN: 2222
Wrong PIN (1 attempt(s) left)
Enter PIN: 1234

1) Balance  2) Withdraw  3) Exit
Choose: 1
Balance: 1000.00

1) Balance  2) Withdraw  3) Exit
Choose: 2
Amount: 200
Please take your cash

1) Balance  2) Withdraw  3) Exit
Choose: 1
Balance: 800.00

1) Balance  2) Withdraw  3) Exit
Choose: 3
Thank you!
```
With three wrong PINs the loop ends without a `break`, `entered` is wrong, and the program prints `Card blocked`.

**Ex 5.111** Keep a range `[low, high]`; guess the middle; each answer throws away half the range. Here the user is thinking of **73**.
<!--in: h l h h h c-->
```c
#include <stdio.h>

int main(void)
{
    int low = 1, high = 100, guess, guesses = 0;
    char answer;

    printf("Think of a number from 1 to 100.\n");
    do
    {
        guess = (low + high) / 2;
        guesses++;
        printf("Is it %d? (h = higher, l = lower, c = correct): ", guess);
        scanf(" %c", &answer);

        if (answer == 'h')
            low = guess + 1;
        else if (answer == 'l')
            high = guess - 1;
    }
    while (answer != 'c');

    printf("I got it in %d guesses!\n", guesses);
    return 0;
}
```
```output
Think of a number from 1 to 100.
Is it 50? (h = higher, l = lower, c = correct): h
Is it 75? (h = higher, l = lower, c = correct): l
Is it 62? (h = higher, l = lower, c = correct): h
Is it 68? (h = higher, l = lower, c = correct): h
Is it 71? (h = higher, l = lower, c = correct): h
Is it 73? (h = higher, l = lower, c = correct): c
I got it in 6 guesses!
```
Seven guesses are always enough (2⁷ = 128 ≥ 100).

**Ex 5.112**
<!--in: 9875-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    printf("%d", n);
    while (n >= 10)
    {
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        printf(" -> %d", sum);
        n = sum;
    }
    printf("\nDigital root: %d\n", n);
    return 0;
}
```
```output
Enter a positive integer: 9875
9875 -> 29 -> 11 -> 2
Digital root: 2
```

**Ex 5.113** Going from the right: positions 0, 2, 4… are summed as they are; positions 1, 3, 5… are doubled (and 9 is subtracted if the double exceeds 9).
<!--in: 79927398713-->
```c
#include <stdio.h>

int main(void)
{
    long long n;
    int sum = 0, position = 0;

    printf("Enter the number: ");
    scanf("%lld", &n);

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

    printf("Checksum = %d -> %s\n", sum, (sum % 10 == 0) ? "valid" : "NOT valid");
    return 0;
}
```
```output
Enter the number: 79927398713
Checksum = 70 -> valid
```
(`%s` prints text — you will learn strings in Chapter 8.)

---

## Part F — Research tasks (sample answers)

**Ex 5.114** `goto label;` jumps unconditionally to a labelled statement anywhere in the same function. Overused, it produces "spaghetti code" — a tangle of jumps that is very hard to read and test — and nearly everything it does can be done with `if`, loops, `break`, `continue` and functions. One accepted use is **leaving several nested loops at once** (a plain `break` leaves only the innermost):
```c
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            if (i * j == 42)
            {
                printf("Found: %d x %d = 42\n", i, j);
                goto done;
            }
        }
    }
    printf("Not found\n");
done:
    printf("Search finished\n");
    return 0;
}
```
```output
Found: 6 x 7 = 42
Search finished
```

**Ex 5.115** `while (1)` and `for (;;)` have an always-true condition, so they loop **forever** unless something inside uses `break` or `return`.
<!--in: 5 3 8 0-->
```c
#include <stdio.h>

int main(void)
{
    int x, sum = 0;

    printf("Enter numbers (0 to stop): ");
    while (1)
    {
        scanf("%d", &x);
        if (x == 0)
            break;
        sum += x;
    }

    printf("Sum = %d\n", sum);
    return 0;
}
```
```output
Enter numbers (0 to stop): 5 3 8 0
Sum = 16
```

**Ex 5.116** `rand()` (from `<stdlib.h>`) returns a pseudo-random integer; `srand(seed)` sets the starting point; `time(NULL)` (from `<time.h>`) is the current time in seconds, so seeding with it gives a different sequence on every run. `rand() % 100 + 1` gives a number from 1 to 100.
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int secret, guess, tries = 0;

    srand((unsigned) time(NULL));          /* seed the generator once */
    secret = rand() % 100 + 1;             /* 1 to 100 */

    do
    {
        printf("Your guess (1-100): ");
        scanf("%d", &guess);
        tries++;

        if (guess < secret)
            printf("Too low\n");
        else if (guess > secret)
            printf("Too high\n");
    }
    while (guess != secret);

    printf("Correct! It took you %d tries.\n", tries);
    return 0;
}
```
(The output is different every time, so there is no fixed sample run.)

---

*Next: [Chapter 6 solutions](06-functions.md)*
