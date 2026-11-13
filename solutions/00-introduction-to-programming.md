# Solutions — Chapter 0: Introduction to Programming

> Back to the lesson: [Chapter 0 lesson](../lessons/00-introduction-to-programming.md)
>
> **Did you try first?** Learning happens in the struggle. Cover the answer, try for at least 10 minutes, *then* compare.

---

## Part A — Quick check

**Ex 0.1** Programming is writing a precise set of instructions (called code) that tells a computer what to do, using a programming language.

**Ex 0.2** An algorithm is a **finite sequence of steps** that solves a particular problem. It must be finite because a procedure that never ends never produces an answer — it is useless as a solution.

**Ex 0.3**

| Term | Answer |
|---|---|
| 1. Machine language | **c** — binary codes the CPU understands directly |
| 2. Assembly language | **e** — short abbreviations for basic instructions |
| 3. High-level language | **b** — closest to human language |
| 4. Compiler | **a** — translates the whole program at once |
| 5. Interpreter | **d** — translates and runs one line at a time |

**Ex 0.4**

1. **False.** Machine language is binary and is *not* designed to be human readable.
2. **False.** The CPU only understands machine language, so high-level code must first be compiled or interpreted.
3. **False.** C is a *compiled* language.
4. **False.** That describes a *compiler*. An interpreter translates one line at a time.
5. **True.** (Because the whole program is already translated into machine code before it runs.)
6. **True.**
7. **False.** In a *declarative* language you focus on **what** is needed. Focusing on *how* is the imperative style.
8. **False.** A stack removes the item added **last** (LIFO). A *queue* removes the one added first (FIFO).

**Ex 0.5** Compiled: C++, Rust, Go, Pascal, Fortran. Interpreted: Python, JavaScript, PHP, Ruby. (Java is a *hybrid*: it is compiled to "bytecode", which a virtual machine then runs.)

**Ex 0.6**

| Language | Paradigm |
|---|---|
| C | Procedural (imperative) |
| Java | Object-oriented (imperative) |
| Lisp | Functional (declarative) |
| Prolog | Logic (declarative) |
| Pascal | Procedural (imperative) |
| Python | Object-oriented (it also allows procedural and functional styles) |

**Ex 0.7**

1. **Stack** — the last action is the first to be undone.
2. **Queue** — first come, first served.
3. **Array** — many values of the same type, accessed by position.
4. **Tree** — folders inside folders form a hierarchy.
5. **Linked list** — every item links to the next.

**Ex 0.8** Any three of:
- Can the data be searched and updated easily?
- How much memory does it use?
- Can intermediate results be arranged for fast access (to reduce later computation)?
- Does the problem match a common data structure?
- Can data from earlier computations be recovered?

**Ex 0.9** If you rush to "how" before you are sure *what* is required, you may solve the wrong problem, or lock yourself into the first idea you had (which may be clumsy). Time spent understanding the problem is saved many times over later.

**Ex 0.10**
1. **Use specific examples** — solve the problem by hand with real numbers to discover the mechanism.
2. **Find similarities** — relate the problem to ones you have already solved.
3. **Work backwards** — start from the answer and undo the steps (or guess and test).
4. **Divide and conquer** — split the problem into smaller sub-problems, solve each, combine.

---

## Part B — Trace the algorithm

**Ex 0.11**

| step | a | b |
|---|---|---|
| after 1–2 | 2 | 5 |
| step 3 (`a = a + b`) | 7 | 5 |
| step 4 (`b = a - b`) | 7 | 2 |
| step 5 (`a = a - b`) | 5 | 2 |

Output: `5 2`. The algorithm **swaps** the two values *without* a third variable. (It is a famous trick; in Chapter 8 you will swap using a temp variable and pointers.)

**Ex 0.12**

| x | x > m ? | m |
|---|---|---|
| (first = 7) | — | 7 |
| 12 | yes | 12 |
| 5 | no | 12 |
| 20 | yes | 20 |
| 9 | no | 20 |

Output: `20`. It finds the **maximum** of the list.

**Ex 0.13**

| n (before) | n after `DIV 10` | count |
|---|---|---|
| 4096 | 409 | 1 |
| 409 | 40 | 2 |
| 40 | 4 | 3 |
| 4 | 0 | 4 |
| 0 | loop stops | |

Output: `4`. It **counts the digits** of the number.

**Ex 0.14**

| x | x >= 5 ? | x after |
|---|---|---|
| 17 | yes | 12 |
| 12 | yes | 7 |
| 7 | yes | 2 |
| 2 | no — stop | |

Output: `2`. It computes the **remainder** when 17 is divided by 5 (`17 mod 5`). In C this is the `%` operator (Chapter 3).

**Ex 0.15**

| iteration | print a | a, b after |
|---|---|---|
| 1 | 0 | a=1, b=1 |
| 2 | 1 | a=1, b=2 |
| 3 | 1 | a=2, b=3 |
| 4 | 2 | a=3, b=5 |
| 5 | 3 | a=5, b=8 |
| 6 | 5 | a=8, b=13 |

Output: `0 1 1 2 3 5` — the **Fibonacci** sequence.

---

## Part C — Find the bug

**Ex 0.16** Division is done **before** addition, so `a + b + c / 3` means `a + b + (c/3)`. With `3, 6, 9`: the wrong version gives `3 + 6 + 3 = 12`, but the true average is `6`.
Fix: use brackets — `SET average = (a + b + c) / 3`.

**Ex 0.17** `max` starts at 0. For an all-negative list no number is greater than 0, so the algorithm prints `0` — a value that is not even in the list.
Fix: start with the **first number of the list** (`SET max = first number`) and compare the rest with it.

**Ex 0.18** `i` is never changed inside the loop, so `i <= N` stays true forever (an *infinite loop*). Fix: add `SET i = i + 1` inside the loop (and put `PRINT` after the loop):

```
INPUT N
SET total = 0
SET i = 1
WHILE i <= N:
    SET total = total + i
    SET i = i + 1
PRINT total
```

**Ex 0.19** `n / 2 = 0` tests whether the *quotient* is 0 — which is only true for tiny numbers (and 7/2 = 3.5 is never 0). To test "even" you must look at the **remainder**: `n MOD 2 = 0`.

```
INPUT n
IF n MOD 2 = 0 THEN
    PRINT "even"
ELSE
    PRINT "odd"
END IF
```

---

## Part D — Write the algorithm

**Ex 0.20**
```
START
  INPUT c
  SET f = c * 9 / 5 + 32
  PRINT f
END
```
Check: `c = 100 → f = 212`, `c = 0 → f = 32`, `c = 37 → f = 98.6`.

**Ex 0.21**
```
START
  INPUT a, b, c
  SET max = a
  IF b > max THEN SET max = b
  IF c > max THEN SET max = c
  PRINT max
END
```
Check: `(4, 9, 6)` → max=4 → b is bigger → 9 → c is not bigger → prints 9.

**Ex 0.22**
```
START
  INPUT year
  IF year MOD 400 = 0 THEN
      PRINT "leap year"
  ELSE IF year MOD 100 = 0 THEN
      PRINT "not a leap year"
  ELSE IF year MOD 4 = 0 THEN
      PRINT "leap year"
  ELSE
      PRINT "not a leap year"
  END IF
END
```
Order matters: test the *most special* rule (400) first. Check: 2000 → leap; 1900 → not; 2024 → leap; 2023 → not.

*Curious how this looks in C? Here it is — you will understand every symbol by Chapter 5.*

<!--in: 1900-->
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
Enter a year: 1900
1900 is not a leap year
```

**Ex 0.23**
```
START
  INPUT N
  SET total = 0
  SET i = 1
  WHILE i <= N
      SET total = total + i
      SET i = i + 1
  END WHILE
  PRINT total
END
```
Check `N = 4` → 10 (see the trace in the lesson). *(Bonus: the answer is also `N × (N + 1) / 2` — Gauss's trick — so no loop is needed!)*

**Ex 0.24**
```
START
  INPUT N
  SET product = 1
  SET i = 1
  WHILE i <= N
      SET product = product * i
      SET i = i + 1
  END WHILE
  PRINT product
END
```
Note we start `product` at **1**, not 0 (anything × 0 is 0). This also gives `0! = 1`, which is correct. Check `N = 5` → 120.

**Ex 0.25**
```
START
  INPUT n                       (n > 1)
  SET isPrime = YES
  SET d = 2
  WHILE d * d <= n AND isPrime = YES
      IF n MOD d = 0 THEN
          SET isPrime = NO
      END IF
      SET d = d + 1
  END WHILE
  IF isPrime = YES THEN PRINT "prime" ELSE PRINT "not prime"
END
```
Why `d * d <= n`? If `n` has a factor bigger than its square root, it must also have a matching factor *smaller* than the square root, so we only need to test up to √n. Check: `17` → tests 2, 3, 4 → no divisor → prime. `21` → 21 MOD 3 = 0 → not prime.

**Ex 0.26**
```
START
  INPUT n
  SET rev = 0
  WHILE n > 0
      SET digit = n MOD 10          (last digit)
      SET rev = rev * 10 + digit    (attach it to the right of rev)
      SET n = n DIV 10              (drop the last digit)
  END WHILE
  PRINT rev
END
```
Trace for `1234`:

| digit | rev | n after |
|---|---|---|
| 4 | 4 | 123 |
| 3 | 43 | 12 |
| 2 | 432 | 1 |
| 1 | 4321 | 0 |

In C:

<!--in: 1234-->
```c
#include <stdio.h>

int main(void)
{
    int n, rev = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    while (n > 0)
    {
        int digit = n % 10;
        rev = rev * 10 + digit;
        n = n / 10;
    }

    printf("Reversed: %d\n", rev);
    return 0;
}
```
```output
Enter a positive integer: 1234
Reversed: 4321
```

**Ex 0.27**
```
START
  INPUT total
  IF total > 200 THEN
      SET pay = total - (total * 10 / 100)
  ELSE
      SET pay = total
  END IF
  PRINT pay
END
```
Check: `250 → 225`. `200 → 200` (the discount is for *more than* 200, so exactly 200 gets none).

**Ex 0.28**
```
START
  INPUT score
  IF score >= 80 THEN PRINT "A"
  ELSE IF score >= 70 THEN PRINT "B"
  ELSE IF score >= 60 THEN PRINT "C"
  ELSE IF score >= 50 THEN PRINT "D"
  ELSE PRINT "F"
  END IF
END
```
Because the tests run top to bottom and stop at the first true one, we only need to check the *lower limit* of each band.

**Ex 0.29** One possible answer:
```
1.  Insert the card.
2.  Enter the PIN.
3.  IF the PIN is wrong THEN
        IF this was the 3rd wrong try THEN keep the card, STOP
        ELSE show "wrong PIN" and go back to step 2
4.  Choose "Withdraw".
5.  Enter the amount.
6.  IF amount > account balance THEN show "insufficient funds", go to step 5 (or cancel)
7.  IF amount > cash in the machine THEN show "cannot dispense", go to step 5 (or cancel)
8.  Dispense the cash.
9.  Print the receipt (optional).
10. Return the card.
```
Notice how many *decisions* hide inside an everyday task. This is exactly why we plan before we code.

**Ex 0.30**

```
          ( START )
              │
      / INPUT a, b, c /
              │
          [ max = a ]
              │
        ◇ b > max ? ◇──Yes──▶ [ max = b ]
              │ No                  │
              ◀─────────────────────┘
              │
        ◇ c > max ? ◇──Yes──▶ [ max = c ]
              │ No                  │
              ◀─────────────────────┘
              │
        / PRINT max /
              │
           ( END )
```

---

## Part E — Challenges

**Ex 0.31** **Two weighings.**

- Weigh 3 coins against 3 coins (2 coins stay aside).
  - *If the scale balances*, the light coin is one of the 2 aside. Weigh those two against each other: the lighter one is the answer. (2 weighings.)
  - *If one side is lighter*, the light coin is among those 3. Weigh 1 against 1: if one is lighter, that's it; if they balance, the third coin is the light one. (2 weighings.)

One weighing is not enough: a single weighing has only 3 outcomes (left lighter / right lighter / equal), so it can tell apart at most 3 coins — not 8.

**Ex 0.32** **Always guess the middle of the remaining range.** Each answer cuts the possibilities in half: 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1. Since 2⁷ = 128 ≥ 100, seven guesses always suffice.
Example, secret = 73: guess 50 (higher) → 75 (lower) → 62 (higher) → 68 (higher) → 71 (higher) → 73 ✔ (6 guesses). This method is called **binary search**.

**Ex 0.33** Work backwards: `58 + 6 = 64` → `64 ÷ 4 = 16` → `16 − 9 = 7`. The number was **7**. Check forwards: `7 + 9 = 16`, `16 × 4 = 64`, `64 − 6 = 58` ✔.

**Ex 0.34**
(a) Change the starting value from `0` to `1`, and change `+` to `×` (i.e. `SET product = 1` and `product = product * i`).
(b) Inside the loop, only add when `i` is even: `IF i MOD 2 = 0 THEN total = total + i`. (Or start `i` at 2 and increase it by 2 each time.)

---

## Part F — Research tasks (sample answers)

**Ex 0.35**

| Language | Usually |
|---|---|
| C | Compiled |
| C++ | Compiled |
| Java | Compiled to bytecode, then run by the JVM |
| Python | Interpreted |
| JavaScript | Interpreted / JIT-compiled in the browser |
| PHP | Interpreted |
| Rust, Go | Compiled |

**Ex 0.36** *Model answer.* A **compiler** reads the entire source program and translates it into machine code (an executable file) in one go. *Advantage:* the finished program runs fast and you can ship it without the compiler. *Disadvantage:* you must recompile after each change, and the compile step may take time. An **interpreter** translates and executes one statement at a time. *Advantage:* quick to test small changes — no separate compile step. *Disadvantage:* programs generally run slower, and an error deep in the code may only show up when execution reaches it.

**Ex 0.37** *Examples.* (i) **Operating systems** such as Linux, Windows and the Android kernel are written mostly in C — C talks to the hardware directly. (ii) **Embedded systems** like the controller in a washing machine, a car's engine management unit or a hospital patient monitor use C because it is small, fast and gives direct control over memory and hardware. (iii) The interpreters of **Python** and many other languages are themselves written in C.

---

*Next: [Chapter 1 solutions](01-c-basics.md)*
