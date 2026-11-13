# Chapter 4 — Data Input and Output

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `04 Data Input and Output.pdf`  
> **Solutions:** [Solutions to Chapter 4](../solutions/04-data-input-and-output.md)

---

## What you will learn

1. How to **display** data neatly with `printf` — including field widths and decimal places.
2. How to **read** data from the user with `scanf`, and what the `&` is for.
3. How to read and write **single characters** (`getchar`, `putchar`) and **text lines** (`puts`, `fgets`).
4. Why `gets` is dangerous and what to use instead.
5. How to avoid the classic input traps (the leftover newline, wrong specifiers…).

Until now your programs have only had *fixed* data written inside the code. After this chapter they can **talk to the user** — and that is when programming becomes fun.

---

## 4.1 Input and output in C

- **Output** = displaying data to the user (you already did this with `printf`).
- **Input** = getting data from the user (keyboard).

C has **no built-in** input/output commands. Both are provided by **functions** in the standard library header **`stdio.h`**, so every program in this chapter starts with:

```c
#include <stdio.h>
```

Your slides introduce six functions:

| Function | Job |
|---|---|
| `printf()` | print **formatted** output of any kind |
| `scanf()` | read **formatted** input of any kind |
| `putchar()` | print **one character** |
| `getchar()` | read **one character** |
| `puts()` | print a **string** (text) and then a newline |
| `gets()` | read a string — **dangerous, avoid!** We will use `fgets()` instead |

```
            ┌───────────┐   scanf / getchar / fgets    ┌───────────────┐
  Keyboard ─▶ INPUT      ├──────────────────────────────▶   YOUR PROGRAM │
            │ (stdin)   │                              │  (variables)  │
            └───────────┘                              └───────┬───────┘
            ┌───────────┐   printf / putchar / puts            │
  Screen  ◀─┤ OUTPUT    ◀──────────────────────────────────────┘
            │ (stdout)  │
            └───────────┘
```

---

## 4.2 `printf` — formatted output

You have been using `printf` since Chapter 1. Its general form is:

```c
printf("control string", arg1, arg2, ..., argn);
```

- The **control string** (also called the *format string*) is the text in quotes. It contains the text to print **plus** *format specifiers* that say where and how to insert values.
- `arg1 … argn` are the **values** to insert, in order.

### Text only

When there is nothing to insert, you need only the text (plus any escape sequences):

```c
printf("Hello, World!\n");
printf("I am 50 years old");
```

### Inserting values: format specifiers

A **format specifier** (a.k.a. **control string**, **string formatter**) starts with `%` and is a *placeholder* for a value. The letter after the `%` says what **type** of value goes there.

```c
int age = 50;
printf("%d \n", age);                 // prints:  50
printf("I am %d years old", age);     // prints:  I am 50 years old
```

Several values at once — **the order matters**: the first specifier gets the first value, the second the second, and so on.

```c
#include <stdio.h>

int main(void)
{
    int count = 4;
    float weight = 90.61f;

    printf("Angela who bought %d oranges weighs %g kilograms\n", count, weight);
    return 0;
}
```
```output
Angela who bought 4 oranges weighs 90.61 kilograms
```

> ⚠️ **Mix the order and you get nonsense.** The compiler will not stop you: `printf("%d %f", 2.5, 7);` prints garbage, because the *type* you promise in the specifier must match the *type* of the value you provide.

### The format specifiers (control strings)

This is the table from your slide. Learn the first rows by heart — you will use them every day.

| Specifier | Prints | Example output |
|---|---|---|
| `%d` or `%i` | signed decimal integer | `392` |
| `%u` | unsigned decimal integer | `7235` |
| `%o` | unsigned **octal** (base 8) | `610` |
| `%x` | unsigned **hexadecimal**, lowercase | `7fa` |
| `%X` | unsigned hexadecimal, UPPERCASE | `7FA` |
| `%f` (or `%F`) | decimal floating point | `392.650000` |
| `%e` (or `%E`) | scientific notation | `3.926500e+02` |
| `%g` (or `%G`) | the shorter of `%e` / `%f` | `392.65` |
| `%a` (or `%A`) | hexadecimal floating point | `-0xc.90fep-2` |
| `%c` | a single **character** | `a` |
| `%s` | a **string** of characters | `sample` |
| `%p` | a **pointer** (memory address) | `00B8000000` (varies) |
| `%n` | prints nothing; stores how many characters have been printed so far | |
| `%%` | a literal percent sign `%` | `%` |

```c
#include <stdio.h>

int main(void)
{
    printf("%d\n", 392);
    printf("%i\n", 392);
    printf("%u\n", 7235u);
    printf("%o\n", 392);          /* 392 in base 8 */
    printf("%x\n", 2042);         /* 2042 in base 16 */
    printf("%X\n", 2042);
    printf("%f\n", 392.65);
    printf("%e\n", 392.65);
    printf("%g\n", 392.65);
    printf("%c\n", 'a');
    printf("%s\n", "sample");
    printf("100%%\n");
    return 0;
}
```
```output
392
392
7235
610
7fa
7FA
392.650000
3.926500e+02
392.65
a
sample
100%
```

**Which one should I use for which type?**

| Type | `printf` | `scanf` |
|---|---|---|
| `int` | `%d` | `%d` |
| `unsigned int` | `%u` | `%u` |
| `long` | `%ld` | `%ld` |
| `long long` | `%lld` | `%lld` |
| `float` | `%f` | `%f` |
| `double` | `%f` (or `%lf`) | **`%lf`** |
| `char` | `%c` | `%c` |
| string (char array) | `%s` | `%s` |

> 💡 Notice the one real difference: for `double`, `printf` uses `%f` but `scanf` needs **`%lf`** ("long float").

### A character is a number, a number can be a character

The *same* value can be shown differently depending on the specifier:

```c
#include <stdio.h>

int main(void)
{
    char c = 'A';
    int n = 66;

    printf("%c %d\n", c, c);     /* A 65 */
    printf("%c %d\n", n, n);     /* B 66 */
    return 0;
}
```
```output
A 65
B 66
```

### Controlling the layout: width, precision and flags

Your slides say: *"The control strings can also be used to specify the length of value to be displayed as well as how many decimal points a floating point has. Find out more."* Here it is.

The full shape of a specifier is:

```
%  [flags]  [width]  [.precision]  [length]  type
```

- **width** — the *minimum* number of characters the value occupies. Shorter values are padded (with spaces on the left by default).
- **precision** — for decimals (`%f`): the number of digits **after** the point. For strings (`%s`): the maximum characters to print.
- **flags:**
  - `-` left-align (pad on the right)
  - `0` pad with zeros instead of spaces
  - `+` always show the sign
  - (space) leave a space for the sign
- **length:** `l` (long / double in `scanf`), `ll` (long long), `h` (short).

I will use `[` and `]` around each value so you can **see** the padding. (The program below was checked character by character, so the spaces you see are exact.)

<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    printf("[%d]\n", 42);            /* plain                       */
    printf("[%5d]\n", 42);           /* width 5, right-aligned      */
    printf("[%-5d]\n", 42);          /* width 5, left-aligned       */
    printf("[%05d]\n", 42);          /* width 5, zero padded        */
    printf("[%+d]\n", 42);           /* always show the sign        */
    printf("[%f]\n", 3.14159);       /* default: 6 decimals         */
    printf("[%.2f]\n", 3.14159);     /* 2 decimals                  */
    printf("[%.0f]\n", 3.7);         /* 0 decimals (rounds)         */
    printf("[%8.3f]\n", 3.14159);    /* width 8, 3 decimals         */
    printf("[%-8.1f]\n", 3.14159);   /* width 8, 1 decimal, left    */
    printf("[%s]\n", "Kumasi");
    printf("[%10s]\n", "Kumasi");    /* width 10, right-aligned     */
    printf("[%-10s]\n", "Kumasi");   /* width 10, left-aligned      */
    printf("[%.3s]\n", "Kumasi");    /* at most 3 characters        */
    return 0;
}
```
```output
[42]
[   42]
[42   ]
[00042]
[+42]
[3.141590]
[3.14]
[4]
[   3.142]
[3.1     ]
[Kumasi]
[    Kumasi]
[Kumasi    ]
[Kum]
```

**Why width matters: neat tables.** Compare these two ways of printing a price list:

<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    printf("%-10s %5s %9s\n", "Item", "Qty", "Price");
    printf("%-10s %5d %9.2f\n", "Rice", 3, 12.5);
    printf("%-10s %5d %9.2f\n", "Gari", 10, 8.0);
    printf("%-10s %5d %9.2f\n", "Kenkey", 25, 5.25);
    return 0;
}
```
```output
Item         Qty     Price
Rice           3     12.50
Gari          10      8.00
Kenkey        25      5.25
```

Text is left-aligned (`%-10s`), numbers are right-aligned (`%5d`, `%9.2f`), and the decimals line up. This is **much** more reliable than using `\t` (tab stops differ between machines).

**Other bases and the `0` flag**

<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    printf("%d in octal is %o\n", 255, 255);
    printf("%d in hex   is %x\n", 255, 255);
    printf("%d in HEX   is %X\n", 255, 255);
    printf("Time: %02d:%02d\n", 7, 5);        /* leading zeros for a clock */
    printf("Percent: %d%%\n", 85);
    return 0;
}
```
```output
255 in octal is 377
255 in hex   is ff
255 in HEX   is FF
Time: 07:05
Percent: 85%
```

> 📝 `printf("%p", ...)` prints a memory **address**. You will use it in Chapter 8 (Pointers). The exact number differs on each run.

---

## 4.3 `scanf` — formatted input

`scanf` is the mirror image of `printf`: it **reads** values the user types and **stores** them in variables. Its form:

```c
scanf("control string", arg1, arg2, ..., argn);
```

The *control string* uses the **same specifiers** (`%d`, `%f`, `%c`…), but this time they say what **type of input to expect**. The `arg`s are **where to store** the values.

### The simplest example: reading an age

```c
#include <stdio.h>

int main(void)
{
    int personAge;

    printf("Enter your age: ");
    scanf("%d", &personAge);
    printf("You are %d years old.\n", personAge);
    return 0;
}
```

What happens when you run it:

1. `printf` shows the prompt `Enter your age: `.
2. When the computer reaches `scanf`, it **waits** (a cursor blinks) until the user types a value and presses **Enter**.
3. Because we wrote `%d`, the text typed is converted to an **integer**.
4. That integer is **stored in `personAge`**.
5. The next `printf` can use it.

<!--in: 21-->
```c
#include <stdio.h>

int main(void)
{
    int personAge;

    printf("Enter your age: ");
    scanf("%d", &personAge);
    printf("You are %d years old.\n", personAge);
    return 0;
}
```
```output
Enter your age: 21
You are 21 years old.
```

*(The `21` after the prompt is what the user typed.)*

> 💡 **Good habit:** always `printf` a **prompt** before a `scanf`, so the user knows what to type.

### The `&` — the "address of" operator

Did you notice the `&` in `&personAge`? It is the **address-of operator**. It gives `scanf` the **memory address** of the variable — *where to put the value*.

**Analogy.** If you ask a courier to deliver a parcel, you must give him the **address** of the house, not a photo of the house's current contents. `scanf` is the courier: it needs to know *where* `personAge` lives so it can drop the number inside.

Without `&`, `scanf` would receive the *value* currently in the variable (garbage!) and try to treat it as an address — the program will usually crash or misbehave. **Forgetting the `&` is the #1 `scanf` mistake.** (There is one exception — reading strings into a char array, Chapter 8.)

The same operator can print an address: `printf("%p", (void *)&personAge);`. More on that when we study pointers.

### Reading several values

Two ways. Suppose we need three exam scores to compute an average.

**Way 1 — one `scanf` per value:**
```c
float score_1, score_2, score_3;
scanf("%f", &score_1);
scanf("%f", &score_2);
scanf("%f", &score_3);
```

**Way 2 — one `scanf`, several values:**
```c
float score_1, score_2, score_3;
scanf("%f %f %f", &score_1, &score_2, &score_3);
```

Notice: the **specifiers are separated by spaces** (or nothing) — **not commas**. The commas separate the *arguments* (the variables) after the quoted string.

<!--in: 70 85.5 92-->
```c
#include <stdio.h>

int main(void)
{
    float score_1, score_2, score_3;

    printf("Enter three scores: ");
    scanf("%f %f %f", &score_1, &score_2, &score_3);

    printf("Average = %.2f\n", (score_1 + score_2 + score_3) / 3);
    return 0;
}
```
```output
Enter three scores: 70 85.5 92
Average = 82.50
```

The user can separate the numbers by spaces, tabs, or by pressing Enter between them — `scanf` treats all of these as "whitespace".

> 📝 Your slide used `%g` for these `float`s. `scanf` accepts `%f`, `%e` and `%g` all as "a decimal number", so both work. `%f` is the most common.

### Reading a `double`

For a `double` you **must** use `%lf` in `scanf` (with `%f` the value is stored wrongly):

<!--in: 5.5 3-->
```c
#include <stdio.h>

int main(void)
{
    double length, width;

    printf("Length (m): ");
    scanf("%lf", &length);
    printf("Width  (m): ");
    scanf("%lf", &width);

    printf("Area = %.2f square metres\n", length * width);
    return 0;
}
```
```output
Length (m): 5.5
Width  (m): 3
Area = 16.50 square metres
```

### Reading with separators in the format

Characters in the control string that are **not** specifiers must be matched exactly by the input. This is handy for dates or times:

<!--in: 12-11-2026-->
```c
#include <stdio.h>

int main(void)
{
    int day, month, year;

    printf("Enter a date (dd-mm-yyyy): ");
    scanf("%d-%d-%d", &day, &month, &year);

    printf("Day %d, month %d, year %d\n", day, month, year);
    return 0;
}
```
```output
Enter a date (dd-mm-yyyy): 12-11-2026
Day 12, month 11, year 2026
```

### `scanf` tells you whether it worked

`scanf` **returns** the number of values it successfully read. Use this to detect bad input:

<!--in: abc-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    int itemsRead = scanf("%d", &n);

    printf("items read: %d\n", itemsRead);
    return 0;
}
```
```output
items read: 0
```

The user typed `abc`, which is not a number, so `scanf` read **0** values. (In Chapter 5 you will combine this with `if` to ask the user to try again.)

### Reading a single character with `scanf` — the leftover newline trap

When the user types `5` and presses Enter, the keyboard sends **two** things: the digit `5` **and** the Enter key (a newline character `\n`). Your program can only use `5` at that moment; the `\n` is **left waiting** in the *input buffer* (the computer's waiting room for typed characters).

```
 You type:    5 ⏎ A ⏎
 The buffer:  [ 5 ][\n][ A ][\n]
 scanf("%d"): takes "5"  ──▶  buffer now: [\n][ A ][\n]
 scanf("%c"): takes "\n" !!!  (not the 'A' you wanted)
```

`%d`, `%f` and `%s` **skip** leading whitespace, but `%c` does **not** — it reads the very next character, even a newline. So the next `%c` happily grabs the leftover `\n`.

**The bug:**

<!--in: 5\nA-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    char ch;

    scanf("%d", &n);
    scanf("%c", &ch);                 /* BUG: reads the leftover newline */
    printf("%d [%c]\n", n, ch);
    return 0;
}
```
```output
5 [
]
```

**The fix:** put a **space before `%c`**. A space in the control string means *"skip any whitespace here"*:

<!--in: 5\nA-->
```c
#include <stdio.h>

int main(void)
{
    int n;
    char ch;

    scanf("%d", &n);
    scanf(" %c", &ch);                /* the space skips the leftover newline */
    printf("%d [%c]\n", n, ch);
    return 0;
}
```
```output
5 [A]
```

> 🔑 **Rule of thumb:** use `" %c"` (space before `%c`) whenever you read a character after other input.

### Common `scanf` mistakes

| Mistake | Problem |
|---|---|
| `scanf("%d", x);` | missing `&` → crash |
| `scanf("%d", &price);` with `double price` | wrong specifier → garbage; use `%lf` |
| `scanf("%d, %d", &a, &b);` | the user **must** type a comma too |
| `scanf("%d\n", &a);` | the `\n` means "skip whitespace" → the program seems to hang until you type something extra |
| `scanf("%c", &ch);` after a number | leftover newline → use `" %c"` |
| `scanf("%s", &name);` | for char arrays no `&` is needed (Chapter 8) |

---

## 4.4 `getchar` and `putchar`

These two work with **single characters**.

- `getchar()` **reads** one character from the keyboard and *returns* it.
- `putchar(c)` **prints** the character `c`.

```c
char choice = getchar();     /* waits for the user to type a character */
putchar(choice);             /* displays it */
```

<!--in: k-->
```c
#include <stdio.h>

int main(void)
{
    char choice;

    printf("Type one character and press Enter: ");
    choice = getchar();

    printf("You typed: ");
    putchar(choice);
    putchar('\n');
    return 0;
}
```
```output
Type one character and press Enter: k
You typed: k
```

`getchar()` reads *one character at a time*, including spaces and the Enter key (`\n`). It also suffers from the leftover-newline trap: if you call it after typing `5` and Enter, the first `getchar()` returns the `\n`.

<!--in: ab-->
```c
#include <stdio.h>

int main(void)
{
    int first = getchar();
    int second = getchar();

    putchar(second);        /* print them in reverse order */
    putchar(first);
    putchar('\n');
    return 0;
}
```
```output
ab
ba
```

> 📝 Real code stores the result of `getchar()` in an `int` (not a `char`), because `getchar` can also return the special value `EOF` ("end of input"), which does not fit in a `char`. You will see that in more advanced courses.

---

## 4.5 `puts`, `gets` — and why we use `fgets`

Both are for **strings** (text, which you study in Chapter 8). A quick preview is useful now because you will often want to read a **name**.

### `puts` — print a string

`puts("text")` prints the text **and automatically adds a newline**.

```c
#include <stdio.h>

int main(void)
{
    puts("Akwaaba!");
    puts("Welcome to KNUST");
    printf("Same job with printf\n");
    return 0;
}
```
```output
Akwaaba!
Welcome to KNUST
Same job with printf
```

### `gets` — read a line (**do not use it!**)

`gets(buffer)` reads a whole line (including spaces) into an array. Your slide shows it:

```c
char fullname[250];
gets(fullname);        /* looks innocent... */
```

**Why is `gets` risky?** It **never checks how much the user types.** The array `fullname` can hold 250 characters. If the user (or an attacker) types 400 characters, `gets` happily writes all 400 — **past the end of the array**, overwriting whatever lives next to it in memory. This is a **buffer overflow**. It can crash the program or let a hacker run their own code. This flaw was behind many real attacks.

Because it can *never* be used safely, `gets` was **removed from the C language in the 2011 standard (C11)**. Many compilers refuse it or print a stern warning.

### `fgets` and `fputs` — the safe replacements

```c
fgets(buffer, size, stdin);     /* read at most size-1 characters from the keyboard */
fputs(text, stdout);            /* print text, WITHOUT adding a newline */
```

- `fgets` is told **the size of the array**, so it can never overflow it.
- `stdin` means "the keyboard" and `stdout` means "the screen".
- `fgets` also stores the **Enter key's `\n`** at the end of what it read. Usually you want to remove it. This one-liner does it (you will understand how in Chapter 8; for now just use it):

```c
buffer[strcspn(buffer, "\n")] = '\0';     /* needs #include <string.h> */
```

<!--in: Kofi Mensah-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char fullname[50];

    printf("Enter your full name: ");
    fgets(fullname, sizeof(fullname), stdin);
    fullname[strcspn(fullname, "\n")] = '\0';     /* remove the newline */

    printf("Hello, %s!\n", fullname);
    puts(fullname);
    fputs("Welcome to KNUST", stdout);
    fputs("\n", stdout);
    return 0;
}
```
```output
Enter your full name: Kofi Mensah
Hello, Kofi Mensah!
Kofi Mensah
Welcome to KNUST
```

### Reading text with `scanf("%s")`

`scanf("%s", name)` is fine for **one word**, but it **stops at the first space**:

<!--in: Kofi Mensah-->
```c
#include <stdio.h>

int main(void)
{
    char name[50];

    printf("Enter your name: ");
    scanf("%s", name);              /* no & needed for an array */
    printf("[%s]\n", name);
    return 0;
}
```
```output
Enter your name: Kofi Mensah
[Kofi]
```

Only `Kofi` was read; ` Mensah` stays in the buffer. (To read a whole line with `scanf` you can write `scanf("%[^\n]", name)` — "read everything up to the newline" — but `fgets` is the better choice.)

> 📝 **Note on the slide.** The slide writes `scanf("%s", &fullname);` — with an `&`. For an array the name already *is* the address, so write `scanf("%s", fullname);`. Also protect against overflow by limiting the width: `scanf("%49s", fullname);` for a 50-element array.

### The "scanf then fgets" trap

If you use `scanf("%d", ...)` and then `fgets(...)`, `fgets` will read the **leftover newline** as an *empty line* and return at once. Discard the leftover first, for example with `getchar();` (or switch fully to `fgets` for everything and convert with `sscanf` — an exercise at the end).

---

## 4.6 Putting it all together — small programs

### Celsius to Fahrenheit

<!--in: 36.6-->
```c
#include <stdio.h>

int main(void)
{
    double celsius;

    printf("Temperature in Celsius: ");
    scanf("%lf", &celsius);

    printf("%.1f C = %.1f F\n", celsius, celsius * 9 / 5 + 32);
    return 0;
}
```
```output
Temperature in Celsius: 36.6
36.6 C = 97.9 F
```

### A tiny receipt

<!--in: Sugar 3 9.5-->
```c
#include <stdio.h>

int main(void)
{
    char item[30];
    int quantity;
    double unitPrice;

    printf("Item, quantity and unit price: ");
    scanf("%29s %d %lf", item, &quantity, &unitPrice);

    printf("\n----- RECEIPT -----\n");
    printf("%-10s x%-3d GHS %7.2f\n", item, quantity, quantity * unitPrice);
    printf("-------------------\n");
    return 0;
}
```
```output
Item, quantity and unit price: Sugar 3 9.5

----- RECEIPT -----
Sugar      x3   GHS   28.50
-------------------
```

---

## 4.7 Common mistakes — summary

| Mistake | Symptom | Fix |
|---|---|---|
| specifier does not match the type | garbage or wrong numbers | `%d` int, `%f` float/double (print), `%lf` double (scan), `%c` char, `%s` string |
| fewer arguments than specifiers | garbage / crash | one value per specifier |
| missing `&` in `scanf` | crash | `scanf("%d", &x);` |
| `%f` for a `double` in `scanf` | wrong value | `%lf` |
| `%c` after another input | reads the newline | `" %c"` |
| using `gets` | overflow risk, removed from C11 | `fgets` |
| forgetting `\n` | prompt/prints run together | add `\n` |
| `%d` to print `sizeof` | wrong on 64-bit | `%zu` |

---

## Key takeaways

- All input/output functions live in **`<stdio.h>`**.
- `printf("…%d…", value)` — the specifiers `%d %f %c %s %u %x %o %e %g %%` mark where values go; **order and type must match**.
- **Width** and **precision**: `%5d`, `%-5d`, `%05d`, `%8.2f`, `%.3s` make tidy output.
- `scanf("%d", &x)` reads into the variable's **address** — **don't forget `&`**. Use `%lf` for `double`.
- `scanf` reads whitespace-separated items; it returns how many it read.
- Use **`" %c"`** (with a space) to read a character after other input.
- `getchar()`/`putchar()` read/print one character; `puts()` prints a line.
- **Never use `gets`.** Use **`fgets(buffer, size, stdin)`**.

---

# Exercises — Chapter 4

## Part A — Quick check

**Ex 4.1** Name the six I/O functions in your slides and say what each one does. Which one should never be used, and why?

**Ex 4.2** What is a format specifier? Which specifier would you use for: an `int`, a `float`, a `char`, a string, a literal `%`?

**Ex 4.3** What does the `&` in `scanf("%d", &age);` do? What happens if you forget it?

**Ex 4.4** What is the difference between `puts("Hi");` and `printf("Hi");`?

**Ex 4.5** Explain the meaning of each: `%5d`, `%-5d`, `%05d`, `%.2f`, `%8.3f`, `%10s`, `%-10s`, `%.3s`.

**Ex 4.6** For `double x;`, which specifier do you use in `printf`, and which in `scanf`?

**Ex 4.7** Why does `scanf("%c", &ch);` often read a "strange" character after a number was entered? How do you fix it?

**Ex 4.8** What value does `scanf` return? Give one use for it.

**Ex 4.9** Why is `gets` dangerous? Name its safe replacement and say what extra information it needs.

**Ex 4.10** True or false?
1. `scanf("%d, %d", &a, &b);` accepts `3 4`.
2. `printf("%d")` with no value is safe.
3. `scanf("%s", name)` reads a whole line with spaces.
4. `putchar('A');` prints `A`.
5. `printf("%5.1f", 3.14159)` prints `  3.1`.
6. `%x` prints a number in hexadecimal.

## Part B — Predict the output

**Ex 4.11**
```c
printf("%d + %d = %d\n", 3, 4, 3 + 4);
```

**Ex 4.12**
```c
printf("%c%c%c\n", 'K', 'N', 'U');
printf("%d\n", 'K');
```

**Ex 4.13**
```c
printf("[%6d]\n", 123);
printf("[%-6d]\n", 123);
printf("[%06d]\n", 123);
```
*(Mark each space carefully.)*

**Ex 4.14**
```c
printf("[%.1f] [%.3f] [%8.2f]\n", 2.718281, 2.718281, 2.718281);
```

**Ex 4.15**
```c
printf("%x %X %o\n", 255, 255, 8);
```

**Ex 4.16**
```c
printf("%s has %d letters\n", "Kumasi", 6);
printf("[%8s] [%-8s]\n", "KNUST", "KNUST");
```

**Ex 4.17**
```c
printf("%d%%\n", 90);
printf("%c\n", 72);
printf("%d\n", 'h');
```

**Ex 4.18** The user types `12 7` and presses Enter. What are `a` and `b`?
```c
int a, b;
scanf("%d %d", &a, &b);
printf("%d\n", a - b);
```

**Ex 4.19** The user types `12,7`. What is printed?
```c
int a, b;
scanf("%d,%d", &a, &b);
printf("%d %d\n", a, b);
```

**Ex 4.20** The user types `3.9`. What is printed, and what is **left over** in the input buffer?
```c
int n;
scanf("%d", &n);
printf("%d\n", n);
```

**Ex 4.21** The user types `hello`. What does this print?
```c
int n = 99;
int r = scanf("%d", &n);
printf("%d %d\n", r, n);
```

**Ex 4.22** The user types `Ama Serwaa` and Enter. What is printed?
```c
char name[30];
scanf("%s", name);
printf("Hi %s\n", name);
```

**Ex 4.23** The user types `xyz` + Enter. What is printed?
```c
int c1 = getchar();
int c2 = getchar();
putchar(c2);
putchar(c1);
putchar('\n');
```

## Part C — Find and fix the bugs

**Ex 4.24**
```c
int age;
scanf("%d", age);
printf("Age: %d\n", age);
```

**Ex 4.25** The program should read a price like `12.75`, but prints rubbish:
```c
double price;
scanf("%f", &price);
printf("%.2f\n", price);
```

**Ex 4.26** Find **two** mistakes:
```c
int a = 5, b = 7;
printf("%d and %d and %d\n", a, b);
printf("%f\n", a);
```

**Ex 4.27** The user must type an extra value for the program to move on. Why?
```c
int n;
scanf("%d\n", &n);
printf("Got %d\n", n);
```

**Ex 4.28** The program should print the grade the user types, but it prints a blank line:
```c
int score;
char grade;
scanf("%d", &score);
scanf("%c", &grade);
printf("%d %c\n", score, grade);
```

**Ex 4.29** Rewrite this using a safe function:
```c
char line[100];
gets(line);
puts(line);
```

**Ex 4.30** Find **two** mistakes:
```c
char name[20];
printf("Name: ");
scanf("%d", &name);
printf("Hello %s\n", name);
```

**Ex 4.31** The table is crooked. Rewrite the `printf` lines so the columns line up (names left-aligned in 10 spaces, scores right-aligned in 5).
```c
printf("Kofi\t%d\n", 95);
printf("Akosua\t%d\n", 8);
printf("Nana Yaw\t%d\n", 100);
```

## Part D — Write the program

*(Unless stated otherwise: prompt the user, read the data with `scanf`, compute, and print.)*

**Ex 4.32** Ask for the user's **first name** (one word) and **age**, then print: `Hello Kofi, you will be 22 next year.`

**Ex 4.33** Read two integers and print their **sum, difference and product**, each on its own line.

**Ex 4.34** Read the **length and width** of a rectangle (decimals) and print the **area** and **perimeter** with 2 decimals.

**Ex 4.35** Read the **radius** of a circle and print its **circumference** and **area** (use `3.14159`).

**Ex 4.36** Read **three exam scores** (decimals) in one `scanf` and print their **average** with 2 decimals.

**Ex 4.37** Read a temperature in **Fahrenheit** and print it in **Celsius**: `C = (F − 32) × 5 / 9`.

**Ex 4.38** Read a number of **seconds** and print it as `h:mm:ss` (use `%02d`). Example: `3725` → `1:02:05`.

**Ex 4.39** Read a **three-digit integer** and print the **sum of its digits**.

**Ex 4.40** Read an amount in **GHS** and an **exchange rate** (USD per GHS) and print the amount in USD with 2 decimals.

**Ex 4.41** Read **principal, rate (%) and years** and print the **simple interest** and the **total**.

**Ex 4.42** Print a three-row price list using **width specifiers** (no tabs). Item names are left-aligned in 12 characters, prices right-aligned with 2 decimals in width 8, e.g.:
```
Item            Price
Bread            5.50
Milk            12.00
Eggs            38.75
```

**Ex 4.43** Read an **item name** (one word), a **quantity** and a **unit price** and print a one-line bill: `Sugar  x3  GHS 28.50`.

**Ex 4.44** Read **one lowercase letter** and print: its ASCII code, the **next** letter, and its **uppercase** version (use `ch - 32`; assume the input is a lowercase letter).

**Ex 4.45** Read a **date** typed as `dd/mm/yyyy` and print it as `yyyy-mm-dd`.

**Ex 4.46** Read a **time** typed as `hh:mm` and a number of minutes to add. Print the new time as `hh:mm` (wrap past midnight).

**Ex 4.47** Read a **full name with spaces** using `fgets`, then print `Welcome, <full name>!` and, on the next line, the same name using `puts`.

**Ex 4.48** Use `getchar` to read **three characters** and `putchar` to print them **in reverse order**.

**Ex 4.49** Read an integer and print it in **decimal, octal, hexadecimal (lower and upper case)** and as a **character**. Try `65`.

**Ex 4.50** Print `3.14159265` with 0, 1, 2, 3, 4 and 5 digits after the point, one per line, using the `.precision` specifier.

**Ex 4.51** A **student ID card**: read name (one word), age, level and GPA, then print a bordered card:
```
+----------------------+
| Name  : Ama          |
| Age   : 19           |
| Level : 200          |
| GPA   : 3.65         |
+----------------------+
```
Use field widths so the right border lines up.

**Ex 4.52** Read the **distance** (km), the car's **fuel efficiency** (km per litre) and the **price per litre** (GHS). Print the **litres needed** and the **cost** of the trip.

**Ex 4.53** Four courses have marks and credit hours. Read `m1 c1 m2 c2 m3 c3 m4 c4` in one `scanf` and print the **weighted average**: `(m1*c1 + … ) / (c1 + … )`.

**Ex 4.54** A restaurant bill of a given total is shared equally among `n` friends. Read both and print how much **each person** pays (2 decimals).

**Ex 4.55** Read an integer and print it **three ways** inside brackets: right-aligned in width 10, left-aligned in width 10 and zero-padded in width 10.

**Ex 4.56** Read a number of **minutes** and print how many **days, hours and minutes** it is. (`5000` → `3 days, 11 hours, 20 minutes`.)

## Part E — Challenges

**Ex 4.57 (ATM receipt)** Read an account name (one word), the previous balance, a withdrawal amount and print a neat receipt with right-aligned money amounts (two decimals), including the new balance.

**Ex 4.58 (input check)** Read two integers with **one** `scanf`. Print how many values were successfully read. Test it with the inputs `7 x`, `x 7` and `7 8`. Explain the three results.

**Ex 4.59 (scanf then fgets)** Read an integer age with `scanf`, then read a **full name with spaces** with `fgets`, and print both. Make the program work correctly (remember the leftover newline).

**Ex 4.60 (sscanf)** Read a **whole line** of the form `Kofi 21 3.5` with `fgets`, then use `sscanf` (it works like `scanf` but reads from a string instead of the keyboard) to split it into a name, an age and a GPA.

**Ex 4.61 (variable width)** `printf("%*d", w, x)` takes the width from an argument. Read a width and a number and print the number right-aligned in that width inside brackets.

## Part F — Research tasks

**Ex 4.62** What do `stdin`, `stdout` and `stderr` mean? Which one would you use for error messages?

**Ex 4.63** What does `%n` do in `printf`? (Hint: see the slide's table.) Why is it considered risky?

**Ex 4.64** Look up the **buffer overflow** attack. Write four sentences explaining how a program using `gets` could be hacked.

**Ex 4.65** Find out what **`sprintf`** and **`snprintf`** do and give an example that builds the text `"Item 7: 12.50"` in a character array.

---

*End of Chapter 4. Next: [Chapter 5 — Flow of Control](05-flow-of-control.md)*
