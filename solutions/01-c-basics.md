# Solutions — Chapter 1: C Basics

> Back to the lesson: [Chapter 1 lesson](../lessons/01-c-basics.md)

---

## Part A — Quick check

**Ex 1.1** **Dennis Ritchie**, at Bell Labs, in the **early 1970s** (development began in 1972; by 1973 it was good enough to write the Unix kernel). C was first used to build (rewrite) the **Unix operating system**.

**Ex 1.2** Any three of:
- It gives a clear mental model of how a computer works (memory, addresses).
- It is the "lingua franca": most languages (Java, Python, JavaScript…) can interface with C.
- Many languages are written in C, so you need C to contribute to them / open-source projects.
- Its syntax is copied by C++, C#, Java, JavaScript and PHP, so you get a head start in them.
- It is used for embedded systems, robotics and efficient AI/hardware code.

**Ex 1.3**

| Name | Valid? | Reason |
|---|---|---|
| `total` | ✅ | |
| `2ndPlace` | ❌ | starts with a digit |
| `_count` | ✅ (discouraged) | valid, but a leading underscore is discouraged |
| `my-name` | ❌ | `-` is not allowed; it means subtraction |
| `float` | ❌ | keyword |
| `Student_Name` | ✅ | |
| `x1` | ✅ | |
| `price$` | ❌ | `$` is not part of the C identifier character set (a few compilers accept it as an extension) |
| `while` | ❌ | keyword |
| `first name` | ❌ | contains a space |
| `Int` | ✅ | different from the keyword `int` (but confusing — avoid) |
| `GPA_2024` | ✅ | |

**Ex 1.4**
1. **False.** C is case sensitive; the program entry point must be `main`.
2. **False.** The keyword is `int` (lowercase). `Int` is just an ordinary identifier.
3. **False.** Comments are ignored by the compiler.
4. **True.** (`#include` lines are preprocessor commands, and `{ }` blocks are not statements by themselves.)
5. **False.** A program must have exactly one `main()`.
6. **False.** C comments cannot be nested. The first `*/` ends the comment, so ` c */` is left over as stray code and causes an error.

**Ex 1.5** It tells the preprocessor to bring in the **standard input/output header file**, which contains the declarations of `printf`, `scanf`, `getchar`, `putchar`, `puts` … If you leave it out, the compiler does not know what `printf` is: older compilers give a warning ("implicit declaration of function") and may still run the program; modern compilers treat it as an **error**. Always include it.

**Ex 1.6** `main()`. **Execution of every C program starts at `main()`** (wherever it appears in the file), and it is mandatory.

**Ex 1.7** It reports the value `0` to the operating system, which means **"the program finished successfully"**. A non-zero value signals an error.

**Ex 1.8**
```c
// A single-line comment (ends at the end of the line)

/* A multi-line
   comment */
```
Neither is executed: the compiler ignores comments.

**Ex 1.9**
- `\n` — newline (cursor to the start of the next line)
- `\t` — horizontal tab
- `\\` — prints a single backslash
- `\"` — prints a double quote
- `\'` — prints a single quote (apostrophe)

**Ex 1.10** (1) **Write** the code; (2) **save** it with a `.c` extension; (3) **build** (compile + link) it; (4) **run** it.

---

## Part B — Predict the output

**Ex 1.11**
```output
A
B
C
```

**Ex 1.12** No newline between the first two `printf`s:
```output
AB
C
```

**Ex 1.13** (`\t` moves to the next tab stop)
```output
Name:   Ama
Age:    19
```

**Ex 1.14**
```output
She said "Hi"
```

**Ex 1.15** Each `\\` prints one backslash:
```output
C:\temp\new
```
(If we had written `\t` and `\n` with single backslashes the output would have been a tab and a newline instead!)

**Ex 1.16** `Two`, `Three` and `Four` are all inside comments:
```output
One
Five
```

**Ex 1.17** The last `printf` has no `\n`, so the text ends without a newline:
```output
HelloWorld
Hello
World
```

**Ex 1.18** **4 lines**: an empty line, another empty line, the line `Hi`, and one more empty line. (The cursor then rests at the start of a 5th line.)

---

## Part C — Find and fix the bugs

**Ex 1.19** Missing `;` after the `printf(...)`.
```c
printf("Welcome to KNUST!\n");
```

**Ex 1.20** C is case sensitive — `Printf` is not `printf`.
```c
printf("Welcome to KNUST!\n");
```

**Ex 1.21** The closing double quote is missing.
```c
printf("Welcome to KNUST!\n");
```

**Ex 1.22** The line `#include <stdio.h>` is missing (so `printf` is unknown).

**Ex 1.23** The `/*` comment is never closed with `*/`, so the compiler swallows the rest of the file. Fix:
```c
/* This program prints a greeting */
```

**Ex 1.24** The closing brace `}` of `main` is missing. Add it after `return 0;`.

**Ex 1.25** `Main` should be `main`. (Typical symptom: the compiler is happy, but the **linker** says "undefined reference to `main`" — there is no entry point.)

**Ex 1.26** Two mistakes:
1. `'Akwaaba!\n'` uses single quotes. Strings need **double** quotes.
2. `return 0` has no semicolon.

```c
printf("Akwaaba!\n");
return 0;
```

---

## Part D — Write the program

**Ex 1.27**
```c
#include <stdio.h>

int main(void)
{
    printf("Name: Kofi Mensah\n");
    printf("Programme: Computer Engineering\n");
    printf("Level: 200\n");
    return 0;
}
```
```output
Name: Kofi Mensah
Programme: Computer Engineering
Level: 200
```

**Ex 1.28**
```c
#include <stdio.h>

int main(void)
{
    printf("Department of Computer Engineering\n");
    printf("KNUST\n");
    printf("Kumasi, Ghana\n");
    return 0;
}
```
```output
Department of Computer Engineering
KNUST
Kumasi, Ghana
```

**Ex 1.29**
```c
#include <stdio.h>

int main(void)
{
    printf("Item\t\tPrice (GHS)\n");
    printf("Rice\t\t12.50\n");
    printf("Gari\t\t8.00\n");
    printf("Kenkey\t\t5.00\n");
    return 0;
}
```
```output
Item            Price (GHS)
Rice            12.50
Gari            8.00
Kenkey          5.00
```
(We used two tabs so the second column lines up even for the short words. Tab stops are normally 8 characters wide, so how it looks depends on your terminal. In Chapter 4 you will learn a more reliable way: field widths such as `%-10s`.)

**Ex 1.30**
```c
#include <stdio.h>

int main(void)
{
    printf("************\n");
    printf("*          *\n");
    printf("*          *\n");
    printf("************\n");
    return 0;
}
```
```output
************
*          *
*          *
************
```

**Ex 1.31** The inner double quotes need `\"`; the apostrophes can stay as they are inside a double-quoted string (writing `\'` is also fine).
```c
#include <stdio.h>

int main(void)
{
    printf("Kwame said, \"Programming isn't hard - it's practice!\"\n");
    return 0;
}
```
```output
Kwame said, "Programming isn't hard - it's practice!"
```

**Ex 1.32** Each backslash must be doubled:
```c
#include <stdio.h>

int main(void)
{
    printf("C:\\Users\\Ama\\Documents\\COE281\n");
    return 0;
}
```
```output
C:\Users\Ama\Documents\COE281
```

**Ex 1.33**
```c
#include <stdio.h>

int main(void)
{
    printf("#\n");
    printf("##\n");
    printf("###\n");
    printf("####\n");
    printf("#####\n");
    return 0;
}
```
```output
#
##
###
####
#####
```

**Ex 1.34**
```c
#include <stdio.h>

int main(void)
{
    printf("   *\n");
    printf("  ***\n");
    printf(" *****\n");
    printf("*******\n");
    return 0;
}
```
```output
   *
  ***
 *****
*******
```

**Ex 1.35**
```c
#include <stdio.h>

int main(void)
{
    printf("===== PROVISION SHOP =====\n");
    printf("Milk\t\tGHS 15.00\n");
    printf("Sugar\t\tGHS  9.50\n");
    printf("Biscuits\tGHS  6.00\n");
    printf("--------------------------\n");
    printf("TOTAL\t\tGHS 30.50\n");
    return 0;
}
```
```output
===== PROVISION SHOP =====
Milk            GHS 15.00
Sugar           GHS  9.50
Biscuits        GHS  6.00
--------------------------
TOTAL           GHS 30.50
```

**Ex 1.36**
```c
#include <stdio.h>

int main(void)
{
    /* (a) one printf */
    printf("Hello World from C\n");

    /* (b) three printfs on the same line */
    printf("Hello ");
    printf("World ");
    printf("from C\n");

    /* (c) one printf per word, each on its own line */
    printf("Hello\n");
    printf("World\n");
    printf("from\n");
    printf("C\n");
    return 0;
}
```
```output
Hello World from C
Hello World from C
Hello
World
from
C
```

**Ex 1.37**
```c
#include <stdio.h>

int main(void)
{
    printf("#   #  #   #  #   #   ####  #####\n");
    printf("#  #   ##  #  #   #  #        #\n");
    printf("###    # # #  #   #   ###     #\n");
    printf("#  #   #  ##  #   #      #    #\n");
    printf("#   #  #   #   ###   ####     #\n");
    return 0;
}
```
```output
#   #  #   #  #   #   ####  #####
#  #   ##  #  #   #  #        #
###    # # #  #   #   ###     #
#  #   #  ##  #   #      #    #
#   #  #   #   ###   ####     #
```

---

## Part E — Challenges

**Ex 1.38** One possibility (R = red, Y = gold, G = green, `*` = the black star):
```c
#include <stdio.h>

int main(void)
{
    printf("RRRRRRRRRRRRRRR\n");
    printf("RRRRRRRRRRRRRRR\n");
    printf("RRRRRRRRRRRRRRR\n");
    printf("YYYYYYYYYYYYYYY\n");
    printf("YYYYYYY*YYYYYYY\n");
    printf("YYYYYYYYYYYYYYY\n");
    printf("GGGGGGGGGGGGGGG\n");
    printf("GGGGGGGGGGGGGGG\n");
    printf("GGGGGGGGGGGGGGG\n");
    return 0;
}
```
```output
RRRRRRRRRRRRRRR
RRRRRRRRRRRRRRR
RRRRRRRRRRRRRRR
YYYYYYYYYYYYYYY
YYYYYYY*YYYYYYY
YYYYYYYYYYYYYYY
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
```

**Ex 1.39** Five statements are enough here:
```c
#include <stdio.h>

int main(void)
{
    printf("1\t2\t3\t4\t5\n");
    printf("2\t4\t6\t8\t10\n");
    printf("3\t6\t9\t12\t15\n");
    printf("4\t8\t12\t16\t20\n");
    printf("5\t10\t15\t20\t25\n");
    return 0;
}
```
```output
1       2       3       4       5
2       4       6       8       10
3       6       9       12      15
4       8       12      16      20
5       10      15      20      25
```
A 50 × 50 table would need 50 statements, each containing 50 hand-typed numbers (2,500 numbers!) — and a single typo would go unnoticed. A **loop** (Chapter 5) does it in about 4 lines. That is the whole point of loops.

**Ex 1.40**
```c
#include <stdio.h>

int main(void)
{
    int n = printf("Hello\n");
    printf("%d\n", n);
    return 0;
}
```
```output
Hello
6
```
`Hello\n` is 6 characters: H, e, l, l, o and the newline. (`\n` counts as one character!)

**Ex 1.41** The five mistakes:
1. `#include <stdio>` — the header file name needs `.h`: `<stdio.h>`.
2. `Int` — must be lowercase `int`.
3. The comment `/* print the course info` is never closed — add `*/`.
4. The string `"Lecturer:\tDr. Mensah\n)` is missing its closing `"`.
5. The same `printf` line is missing its `;`.

```c
#include <stdio.h>

int main(void)
{
    /* print the course info */
    printf("Course:\tCOE 281\n");
    printf("Lecturer:\tDr. Mensah\n");
    printf("Language:\tC\n");
    return 0;
}
```
```output
Course:         COE 281
Lecturer:       Dr. Mensah
Language:       C
```

---

## Part F — Hands-on tasks (sample answers)

**Ex 1.42** *Sample:* "I used Code::Blocks 20.03 with MinGW GCC 8.1." Or: "VS Code with the C/C++ extension and GCC 13.2 from MSYS2". Check your compiler version with `gcc --version` in a terminal. Typing it by hand (rather than pasting) is deliberate — you train your eyes and fingers to notice details like `;` and `"`.

**Ex 1.43** *Sample error diary* (GCC wording; yours may differ):

| What I changed | Error message | Line | What it really meant |
|---|---|---|---|
| Removed `;` after `printf(...)` | `expected ';' before 'return'` | the line **after** the missing `;` | A statement was not ended before the next one started |
| Removed the closing `"` | `missing terminating " character` | the `printf` line | The string never ended |
| Wrote `printF` | `implicit declaration of function 'printF'` / `undefined reference to 'printF'` | the `printF` line | The compiler/linker does not know a function with that exact (case-sensitive) name |
| Removed `#include <stdio.h>` | `implicit declaration of function 'printf'` | the `printf` line | The declaration of `printf` was never included |
| Removed the last `}` | `expected declaration or statement at end of input` | the last line | A block was opened but never closed |

**Ex 1.44** With GCC: `gcc hello.c -o hello`. The executable appears in the **same folder** as `hello.c` (named `hello.exe` on Windows, `hello` on Linux/macOS). A tiny Hello World is usually tens of kilobytes (the exact size depends on the compiler and platform). Run it with `hello` or `./hello`. With the Microsoft compiler: `cl hello.c` produces `hello.exe` and `hello.obj`.

---

*Next: [Chapter 2 solutions](02-variables-and-data-types.md)*
