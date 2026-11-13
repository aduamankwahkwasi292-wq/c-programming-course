# Solutions — Chapter 4: Data Input and Output

> Back to the lesson: [Chapter 4 lesson](../lessons/04-data-input-and-output.md)
>
> In the sample runs, the text the **user types** is shown right after the prompt, exactly as it appears in a terminal.

---

## Part A — Quick check

**Ex 4.1**
- `printf()` — prints formatted output.
- `scanf()` — reads formatted input.
- `putchar()` — prints one character.
- `getchar()` — reads one character.
- `puts()` — prints a string followed by a newline.
- `gets()` — reads a string/line. **Never use it:** it does not check the size of the array, so long input overflows the array (buffer overflow). It was removed from the language in C11. Use `fgets()`.

**Ex 4.2** A **format specifier** is a `%`-code in the control string that marks where a value goes and what type it is. `int` → `%d`; `float` → `%f`; `char` → `%c`; string → `%s`; a literal percent sign → `%%`.

**Ex 4.3** `&` is the **address-of** operator. It gives `scanf` the memory address of `age`, so `scanf` knows *where* to store the number. Without it, `scanf` is handed the (garbage) value of `age` and treats it as an address — the program crashes or misbehaves.

**Ex 4.4** `puts("Hi");` prints `Hi` **and then a newline**. `printf("Hi");` prints just `Hi` (no newline unless you write `\n`). `puts` can't format values; `printf` can.

**Ex 4.5**
- `%5d` — integer in a field at least 5 wide, right-aligned.
- `%-5d` — same, left-aligned.
- `%05d` — width 5, padded with zeros on the left.
- `%.2f` — decimal with 2 digits after the point.
- `%8.3f` — decimal with 3 digits after the point, in a field at least 8 wide.
- `%10s` — string right-aligned in 10 characters.
- `%-10s` — string left-aligned in 10 characters.
- `%.3s` — print at most the first 3 characters of the string.

**Ex 4.6** `printf`: `%f` (`%lf` is also accepted). `scanf`: **`%lf`**.

**Ex 4.7** `%c` does not skip whitespace, so it reads the **newline** (Enter key) that is still in the input buffer after the number. Fix: put a space before the specifier: `scanf(" %c", &ch);`.

**Ex 4.8** `scanf` returns the **number of items successfully read** (or `EOF` if the input ended). Use it to check that the user typed valid input, e.g. `if (scanf("%d", &n) != 1) { /* bad input */ }`.

**Ex 4.9** `gets` has no way to know how big the array is, so it keeps writing whatever the user types, even beyond the end of the array (**buffer overflow**) — causing crashes and security holes. The safe replacement is **`fgets(buffer, size, stdin)`**: it needs the **size** of the buffer and will read at most `size − 1` characters.

**Ex 4.10**
1. **False** — the comma in the format must also be typed: `3, 4` is OK; `3 4` is not (the second number is not read).
2. **False** — `printf("%d")` has a specifier but no value: undefined behaviour (garbage).
3. **False** — `%s` stops at the first whitespace. Use `fgets` for a whole line.
4. **True.**
5. **True** — width 5 and 1 decimal: two spaces then `3.1`.
6. **True.**

---

## Part B — Predict the output

**Ex 4.11** `3 + 4 = 7`

**Ex 4.12**
```output
KNU
75
```

**Ex 4.13**
```output
[   123]
[123   ]
[000123]
```

**Ex 4.14**
```output
[2.7] [2.718] [    2.72]
```

**Ex 4.15** `ff FF 10`   (255 = FF in hex; 8 in octal is `10`)

**Ex 4.16**
```output
Kumasi has 6 letters
[   KNUST] [KNUST   ]
```

**Ex 4.17**
```output
90%
H
104
```

**Ex 4.18** `a = 12`, `b = 7` → prints `5`.

**Ex 4.19** `12 7` (the comma in the input matches the comma in the format).

**Ex 4.20** It prints `3`. The characters `.9` and the newline are **left over** in the input buffer (`%d` stops at the `.`).

**Ex 4.21** `0 99` — `scanf` read 0 items, so `n` keeps its old value 99. (`hello` is left in the buffer.)

**Ex 4.22** `Hi Ama` — `%s` stops at the space. ` Serwaa` is left in the buffer.

**Ex 4.23** `yx` — `c1` = `'x'`, `c2` = `'y'`; they are printed in reverse order (`y` then `x`).

---

## Part C — Find and fix the bugs

**Ex 4.24** Missing `&`: `scanf("%d", &age);`

**Ex 4.25** For a `double`, `scanf` needs `%lf`: `scanf("%lf", &price);`

**Ex 4.26** Two mistakes: (1) three `%d` but only two values (`a`, `b`); (2) `%f` is used for an `int` (`a`). Correct:
```c
printf("%d and %d\n", a, b);
printf("%d\n", a);
```

**Ex 4.27** The `\n` in the control string means "skip any whitespace". `scanf` can't know the whitespace has ended until it sees a **non-whitespace** character, so it waits for more input. Fix: `scanf("%d", &n);` (no `\n`).

**Ex 4.28** The leftover newline after the score is read by `%c`. Fix: `scanf(" %c", &grade);` (space before `%c`).

**Ex 4.29**
```c
char line[100];
fgets(line, sizeof(line), stdin);
fputs(line, stdout);          /* fputs does not add another newline;  fgets kept the one the user typed */
```
(If you use `puts(line)` you get an extra blank line, because `fgets` keeps the user's `\n` and `puts` adds another.)

**Ex 4.30** Two mistakes: (1) `%d` is used to read text — it should be `%s`; (2) `&name` — for an array the name itself is the address, so use `scanf("%19s", name);` (and `%19s` guards against overflow).

**Ex 4.31** Use widths instead of tabs:
```c
#include <stdio.h>

int main(void)
{
    printf("%-10s%5d\n", "Kofi", 95);
    printf("%-10s%5d\n", "Akosua", 8);
    printf("%-10s%5d\n", "Nana Yaw", 100);
    return 0;
}
```
```output
Kofi         95
Akosua        8
Nana Yaw    100
```

---

## Part D — Write the program

**Ex 4.32**
<!--in: Kofi 21-->
```c
#include <stdio.h>

int main(void)
{
    char name[30];
    int age;

    printf("Enter your first name and age: ");
    scanf("%29s %d", name, &age);

    printf("Hello %s, you will be %d next year.\n", name, age + 1);
    return 0;
}
```
```output
Enter your first name and age: Kofi 21
Hello Kofi, you will be 22 next year.
```

**Ex 4.33**
<!--in: 12 5-->
```c
#include <stdio.h>

int main(void)
{
    int a, b;

    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    printf("Sum        = %d\n", a + b);
    printf("Difference = %d\n", a - b);
    printf("Product    = %d\n", a * b);
    return 0;
}
```
```output
Enter two integers: 12 5
Sum        = 17
Difference = 7
Product    = 60
```

**Ex 4.34**
<!--in: 7.5 4-->
```c
#include <stdio.h>

int main(void)
{
    double length, width;

    printf("Enter length and width: ");
    scanf("%lf %lf", &length, &width);

    printf("Area      = %.2f\n", length * width);
    printf("Perimeter = %.2f\n", 2 * (length + width));
    return 0;
}
```
```output
Enter length and width: 7.5 4
Area      = 30.00
Perimeter = 23.00
```

**Ex 4.35**
<!--in: 10-->
```c
#include <stdio.h>

int main(void)
{
    const double PI = 3.14159;
    double radius;

    printf("Enter the radius: ");
    scanf("%lf", &radius);

    printf("Circumference = %.2f\n", 2 * PI * radius);
    printf("Area          = %.2f\n", PI * radius * radius);
    return 0;
}
```
```output
Enter the radius: 10
Circumference = 62.83
Area          = 314.16
```

**Ex 4.36**
<!--in: 64 72.5 81-->
```c
#include <stdio.h>

int main(void)
{
    float s1, s2, s3;

    printf("Enter three scores: ");
    scanf("%f %f %f", &s1, &s2, &s3);

    printf("Average = %.2f\n", (s1 + s2 + s3) / 3);
    return 0;
}
```
```output
Enter three scores: 64 72.5 81
Average = 72.50
```

**Ex 4.37**
<!--in: 98.6-->
```c
#include <stdio.h>

int main(void)
{
    double f;

    printf("Temperature in Fahrenheit: ");
    scanf("%lf", &f);

    printf("%.1f F = %.1f C\n", f, (f - 32) * 5 / 9);
    return 0;
}
```
```output
Temperature in Fahrenheit: 98.6
98.6 F = 37.0 C
```

**Ex 4.38**
<!--in: 3725-->
```c
#include <stdio.h>

int main(void)
{
    int total;

    printf("Seconds: ");
    scanf("%d", &total);

    printf("%d:%02d:%02d\n", total / 3600, (total % 3600) / 60, total % 60);
    return 0;
}
```
```output
Seconds: 3725
1:02:05
```

**Ex 4.39**
<!--in: 437-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter a three-digit number: ");
    scanf("%d", &n);

    int sum = n / 100 + (n / 10) % 10 + n % 10;
    printf("Sum of digits = %d\n", sum);
    return 0;
}
```
```output
Enter a three-digit number: 437
Sum of digits = 14
```

**Ex 4.40**
<!--in: 1500 0.065-->
```c
#include <stdio.h>

int main(void)
{
    double ghs, rate;

    printf("Amount in GHS and rate (USD per GHS): ");
    scanf("%lf %lf", &ghs, &rate);

    printf("GHS %.2f = USD %.2f\n", ghs, ghs * rate);
    return 0;
}
```
```output
Amount in GHS and rate (USD per GHS): 1500 0.065
GHS 1500.00 = USD 97.50
```

**Ex 4.41**
<!--in: 2500 8.5 3-->
```c
#include <stdio.h>

int main(void)
{
    double principal, rate;
    int years;

    printf("Principal, rate (%%) and years: ");
    scanf("%lf %lf %d", &principal, &rate, &years);

    double interest = principal * rate * years / 100;
    printf("Interest = %.2f\n", interest);
    printf("Total    = %.2f\n", principal + interest);
    return 0;
}
```
```output
Principal, rate (%) and years: 2500 8.5 3
Interest = 637.50
Total    = 3137.50
```

**Ex 4.42** Exact output (checked character by character):
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    printf("%-12s %8s\n", "Item", "Price");
    printf("%-12s %8.2f\n", "Bread", 5.5);
    printf("%-12s %8.2f\n", "Milk", 12.0);
    printf("%-12s %8.2f\n", "Eggs", 38.75);
    return 0;
}
```
```output
Item            Price
Bread            5.50
Milk            12.00
Eggs            38.75
```

**Ex 4.43**
<!--in: Sugar 3 9.5-->
```c
#include <stdio.h>

int main(void)
{
    char item[30];
    int quantity;
    double price;

    printf("Item, quantity, unit price: ");
    scanf("%29s %d %lf", item, &quantity, &price);

    printf("%s  x%d  GHS %.2f\n", item, quantity, quantity * price);
    return 0;
}
```
```output
Item, quantity, unit price: Sugar 3 9.5
Sugar  x3  GHS 28.50
```

**Ex 4.44**
<!--in: g-->
```c
#include <stdio.h>

int main(void)
{
    char ch;

    printf("Enter a lowercase letter: ");
    scanf(" %c", &ch);

    printf("ASCII code : %d\n", ch);
    printf("Next letter: %c\n", ch + 1);
    printf("Uppercase  : %c\n", ch - 32);
    return 0;
}
```
```output
Enter a lowercase letter: g
ASCII code : 103
Next letter: h
Uppercase  : G
```

**Ex 4.45**
<!--in: 12/11/2026-->
```c
#include <stdio.h>

int main(void)
{
    int d, m, y;

    printf("Date (dd/mm/yyyy): ");
    scanf("%d/%d/%d", &d, &m, &y);

    printf("%04d-%02d-%02d\n", y, m, d);
    return 0;
}
```
```output
Date (dd/mm/yyyy): 12/11/2026
2026-11-12
```

**Ex 4.46**
<!--in: 23:30 90-->
```c
#include <stdio.h>

int main(void)
{
    int hour, minute, add;

    printf("Time (hh:mm) and minutes to add: ");
    scanf("%d:%d %d", &hour, &minute, &add);

    int total = (hour * 60 + minute + add) % (24 * 60);   /* wrap past midnight */
    printf("New time: %02d:%02d\n", total / 60, total % 60);
    return 0;
}
```
```output
Time (hh:mm) and minutes to add: 23:30 90
New time: 01:00
```

**Ex 4.47**
<!--in: Kwame Nkrumah-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[60];

    printf("Full name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Welcome, %s!\n", name);
    puts(name);
    return 0;
}
```
```output
Full name: Kwame Nkrumah
Welcome, Kwame Nkrumah!
Kwame Nkrumah
```

**Ex 4.48**
<!--in: abc-->
```c
#include <stdio.h>

int main(void)
{
    int c1, c2, c3;

    printf("Type three characters: ");
    c1 = getchar();
    c2 = getchar();
    c3 = getchar();

    putchar(c3);
    putchar(c2);
    putchar(c1);
    putchar('\n');
    return 0;
}
```
```output
Type three characters: abc
cba
```

**Ex 4.49**
<!--in: 65-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    printf("decimal : %d\n", n);
    printf("octal   : %o\n", n);
    printf("hex     : %x (lower)  %X (upper)\n", n, n);
    printf("char    : %c\n", n);
    return 0;
}
```
```output
Enter an integer: 65
decimal : 65
octal   : 101
hex     : 41 (lower)  41 (upper)
char    : A
```
(Try `255` to see `ff` vs `FF`.)

**Ex 4.50**
<!--exact-->
```c
#include <stdio.h>

int main(void)
{
    double pi = 3.14159265;

    printf("%.0f\n", pi);
    printf("%.1f\n", pi);
    printf("%.2f\n", pi);
    printf("%.3f\n", pi);
    printf("%.4f\n", pi);
    printf("%.5f\n", pi);
    return 0;
}
```
```output
3
3.1
3.14
3.142
3.1416
3.14159
```

**Ex 4.51** Each line is `"| "` + an 8-character label + a 12-character field + `" |"` → 24 characters, the same width as the border.
<!--in: Ama 19 200 3.65-->
```c
#include <stdio.h>

int main(void)
{
    char name[12];
    int age, level;
    double gpa;

    printf("Name, age, level, GPA: ");
    scanf("%11s %d %d %lf", name, &age, &level, &gpa);

    printf("+----------------------+\n");
    printf("| Name  : %-12s |\n", name);
    printf("| Age   : %-12d |\n", age);
    printf("| Level : %-12d |\n", level);
    printf("| GPA   : %-12.2f |\n", gpa);
    printf("+----------------------+\n");
    return 0;
}
```
```output
Name, age, level, GPA: Ama 19 200 3.65
+----------------------+
| Name  : Ama          |
| Age   : 19           |
| Level : 200          |
| GPA   : 3.65         |
+----------------------+
```

**Ex 4.52**
<!--in: 120 12 14.5-->
```c
#include <stdio.h>

int main(void)
{
    double distance, efficiency, price;

    printf("Distance (km), km per litre, price per litre: ");
    scanf("%lf %lf %lf", &distance, &efficiency, &price);

    double litres = distance / efficiency;
    printf("Litres needed: %.2f\n", litres);
    printf("Trip cost    : GHS %.2f\n", litres * price);
    return 0;
}
```
```output
Distance (km), km per litre, price per litre: 120 12 14.5
Litres needed: 10.00
Trip cost    : GHS 145.00
```

**Ex 4.53**
<!--in: 70 3 80 2 65 4 90 3-->
```c
#include <stdio.h>

int main(void)
{
    double m1, m2, m3, m4;
    int c1, c2, c3, c4;

    printf("Enter m1 c1 m2 c2 m3 c3 m4 c4: ");
    scanf("%lf %d %lf %d %lf %d %lf %d", &m1, &c1, &m2, &c2, &m3, &c3, &m4, &c4);

    double weighted = (m1 * c1 + m2 * c2 + m3 * c3 + m4 * c4) / (c1 + c2 + c3 + c4);
    printf("Weighted average = %.2f\n", weighted);
    return 0;
}
```
```output
Enter m1 c1 m2 c2 m3 c3 m4 c4: 70 3 80 2 65 4 90 3
Weighted average = 75.00
```
Check: (210 + 160 + 260 + 270) / 12 = 900 / 12 = 75.

**Ex 4.54**
<!--in: 245.50 3-->
```c
#include <stdio.h>

int main(void)
{
    double total;
    int friends;

    printf("Bill total and number of friends: ");
    scanf("%lf %d", &total, &friends);

    printf("Each person pays GHS %.2f\n", total / friends);
    return 0;
}
```
```output
Bill total and number of friends: 245.50 3
Each person pays GHS 81.83
```

**Ex 4.55**
<!--in: 42-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    printf("[%10d]\n", n);
    printf("[%-10d]\n", n);
    printf("[%010d]\n", n);
    return 0;
}
```
```output
Enter an integer: 42
[        42]
[42        ]
[0000000042]
```

**Ex 4.56**
<!--in: 5000-->
```c
#include <stdio.h>

int main(void)
{
    int minutes;

    printf("Minutes: ");
    scanf("%d", &minutes);

    int days = minutes / (24 * 60);
    int hours = (minutes % (24 * 60)) / 60;
    int mins = minutes % 60;

    printf("%d days, %d hours, %d minutes\n", days, hours, mins);
    return 0;
}
```
```output
Minutes: 5000
3 days, 11 hours, 20 minutes
```

---

## Part E — Challenges

**Ex 4.57**
<!--in: Kwabena 1500.75 200-->
```c
#include <stdio.h>

int main(void)
{
    char name[30];
    double balance, withdrawal;

    printf("Account name, balance, withdrawal: ");
    scanf("%29s %lf %lf", name, &balance, &withdrawal);

    printf("\n======= ATM RECEIPT =======\n");
    printf("Account         : %s\n", name);
    printf("Previous balance: %10.2f\n", balance);
    printf("Withdrawn       : %10.2f\n", withdrawal);
    printf("-------------------------\n");
    printf("New balance     : %10.2f\n", balance - withdrawal);
    return 0;
}
```
```output
Account name, balance, withdrawal: Kwabena 1500.75 200

======= ATM RECEIPT =======
Account         : Kwabena
Previous balance:    1500.75
Withdrawn       :     200.00
-------------------------
New balance     :    1300.75
```

**Ex 4.58**
<!--in: 7 x-->
```c
#include <stdio.h>

int main(void)
{
    int a = -1, b = -1;

    printf("Enter two integers: ");
    int count = scanf("%d %d", &a, &b);

    printf("values read: %d (a = %d, b = %d)\n", count, a, b);
    return 0;
}
```
```output
Enter two integers: 7 x
values read: 1 (a = 7, b = -1)
```
- `7 x` → **1**: `7` was read into `a`; `x` is not a number, so reading stopped and `b` was untouched.
- `x 7` → **0**: the very first item is not a number, so nothing was read.
- `7 8` → **2**: both read.

**Ex 4.59** The `scanf("%d")` leaves the Enter key (`\n`) in the buffer; one `getchar()` throws it away before `fgets`.
<!--in: 21\nKofi Mensah-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    int age;
    char name[50];

    printf("Age: ");
    scanf("%d", &age);
    getchar();                                  /* discard the leftover newline */

    printf("Full name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("%s is %d years old.\n", name, age);
    return 0;
}
```
```output
Age: 21
Full name: Kofi Mensah
Kofi Mensah is 21 years old.
```
Without the `getchar()`, `fgets` would immediately read the leftover empty line and the name would be blank.

**Ex 4.60**
<!--in: Kofi 21 3.5-->
```c
#include <stdio.h>

int main(void)
{
    char line[100];
    char name[30];
    int age;
    double gpa;

    printf("Enter name, age, GPA: ");
    fgets(line, sizeof(line), stdin);

    sscanf(line, "%29s %d %lf", name, &age, &gpa);
    printf("name=%s age=%d gpa=%.1f\n", name, age, gpa);
    return 0;
}
```
```output
Enter name, age, GPA: Kofi 21 3.5
name=Kofi age=21 gpa=3.5
```
This is a robust pattern: read a **line** safely with `fgets`, then **parse** it with `sscanf`. If the parsing fails, the leftover input is not stuck in the keyboard buffer.

**Ex 4.61**
<!--in: 8 42-->
```c
#include <stdio.h>

int main(void)
{
    int w, x;

    printf("Width and number: ");
    scanf("%d %d", &w, &x);

    printf("[%*d]\n", w, x);
    return 0;
}
```
```output
Width and number: 8 42
[      42]
```

---

## Part F — Research tasks (sample answers)

**Ex 4.62** `stdin` = standard input (normally the keyboard); `stdout` = standard output (normally the screen); `stderr` = standard error (also normally the screen, but a *separate* stream so error messages can be redirected independently of normal output). Use it with `fprintf(stderr, "Error: ...\n");`.

**Ex 4.63** `%n` does not print anything; it **writes** the number of characters printed so far into the `int` whose address you give (`printf("Hello%n", &count);` stores 5). It is risky because it makes `printf` *write to memory*; if an attacker controls the format string they can use `%n` to overwrite memory (a "format string vulnerability"). Some libraries (such as Microsoft's) disable it by default.

**Ex 4.64** *Model answer.* A program that uses `gets` reserves a fixed-size array (say 50 bytes) on the *stack*, which also holds the function's return address — the place the CPU jumps to when the function ends. `gets` doesn't check the length, so an attacker types more than 50 bytes. The extra bytes overwrite the neighbouring memory including the return address. The attacker chooses those bytes so that the return address now points to **their own code**. When the function returns, the CPU runs the attacker's code instead of the program's. This is why modern code uses `fgets` and bounds-checked functions.

**Ex 4.65**
```c
#include <stdio.h>

int main(void)
{
    char text[40];

    snprintf(text, sizeof(text), "Item %d: %.2f", 7, 12.5);
    puts(text);
    return 0;
}
```
```output
Item 7: 12.50
```
`sprintf` / `snprintf` work like `printf` but write into a **string** instead of the screen. `snprintf` takes the buffer size, so it can't overflow — prefer it.

---

*Next: [Chapter 5 solutions](05-flow-of-control.md)*
