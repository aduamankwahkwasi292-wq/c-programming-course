# Chapter 1 — C Basics

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `01 C Basics.pdf`  
> **Solutions:** [Solutions to Chapter 1](../solutions/01-c-basics.md)

---

## What you will learn

1. Where C came from and why it is still worth learning today.
2. The building blocks of C: the character set, **keywords**, **identifiers** and **comments**.
3. How to read, write, build and run your first C program — **Hello, World!**
4. What `#include`, `main()`, `printf()` and `return` actually do.
5. How to use **escape sequences** such as `\n` and `\t`.
6. How to read compiler error messages without panicking.

---

## 1.1 What is C?

C is a programming language that is closely tied to the **Unix** operating system.

**The short history**

- In the late 1960s, the developers of Unix at Bell Labs used a small language called **B**.
- B could not provide some features needed by the Unix version for the **PDP-11** computer. So **Dennis Ritchie** created a new language, which was called **C**.
- **1972** – development of C started on the PDP-11 Unix system. A large part of Unix was then rewritten in C.
- **1973** – C was powerful enough to write the Unix **kernel** (the core of the operating system).
- Dennis Ritchie and **Stephen C. Johnson** kept improving the language so that it became **portable** — meaning the same C program could be moved to different kinds of computers.
- **1978** – the book *The C Programming Language* by Kernighan and Ritchie ("K&R") made C famous.
- **1989/1990** – the language was standardised (**ANSI C / C89 / C90**). Later versions: **C99, C11, C17, C23**.

> 💡 **Why standards matter.** A standard is an official rulebook that says exactly how the language must behave. It is why a C program you write on Windows can (mostly) compile on Linux or macOS.

---

## 1.2 Why learn C?

You may ask, "C is so old. Why not just learn Python?" Here are the reasons your lecturer gives — and they are good ones.

1. **A clear mental model of the computer.** C makes the inner workings of a computer understandable. You see memory, addresses and bytes. After C, nothing about computers feels like magic.
2. **The lingua franca of programming.** Almost all high-level languages — Java, Python, JavaScript — can **interface with C**.
3. **Join open-source projects.** Many popular languages (e.g. Python) are *themselves written in C*. To improve how they work, you must know C.
4. **A head start in other languages.** C++, C#, Java, JavaScript and PHP all borrow C's syntax. Learn C well and the others feel familiar.
5. **Embedded systems, robotics and AI hardware.** Most microprocessor-based systems — from a washing-machine controller to a drone — run efficient C code.

> **Further reading (from the slides):** search for "real-world applications of C". You will find operating systems, databases, game engines, network equipment, microcontrollers, compilers…

---

## 1.3 The building blocks of C

Before sentences you need letters and words. In C the equivalents are the **character set**, **keywords** and **identifiers**.

### 1.3.1 The character set

The **character set** is the collection of letters, digits and symbols that are valid in C. C uses:

- uppercase letters `A`–`Z`
- lowercase letters `a`–`z`
- digits `0`–`9`
- the blank space
- special characters:

```
,  <  >  .  -
(  )  ;  $  :
%  [  ]  #  ?
'  &  {  }  "
^  !  *  /  |
_  \  ~  +  =
```

These are the "bricks" used to build every part of a program.

### 1.3.2 Keywords

**Keywords** are *reserved words* with a fixed meaning to the compiler. You cannot use them as names for your own things. There are **32** keywords in standard (ANSI) C, and **all are written in lowercase** (C is *case sensitive*).

| | | | | |
|---|---|---|---|---|
| `auto` | `break` | `case` | `char` | `const` |
| `continue` | `default` | `do` | `double` | `else` |
| `enum` | `extern` | `float` | `for` | `goto` |
| `if` | `int` | `long` | `register` | `return` |
| `short` | `signed` | `sizeof` | `static` | `struct` |
| `switch` | `typedef` | `union` | `unsigned` | `void` |
| `volatile` | `while` | | | |

**Do not memorise the list today.** You will meet the important ones one at a time. By the end of this course you will use about 20 of them without thinking:
`int char float double short long signed unsigned` (data types), `if else switch case default break continue` (decisions), `for while do` (loops), `return void static sizeof` (functions and more).

> 📝 Newer standards added a few more (e.g. `inline`, `restrict`, `_Bool`). Your course focuses on the classic 32.

### 1.3.3 Identifiers

An **identifier** is a **name** you give to something in your program — a variable, a function, a structure, and so on. Example:

```c
money = 500;
age = 24;
```

Here `money` and `age` are identifiers. Each identifier must be **unique** — it identifies *one* thing.

**The rules**

1. It may contain **letters** (uppercase and lowercase), **digits** and **underscores** `_` — nothing else (no spaces, no `-`, no `@`).
2. It **cannot start with a digit**.
3. It **cannot be a keyword**.
4. It is **case sensitive**: `age`, `Age` and `AGE` are three *different* names.
5. It is *discouraged* to start with an underscore (such names are often used by the compiler itself).
6. Choose **meaningful** names: `age` is better than `a`, and `totalScore` is better than `ts`.

| Name | Valid? | Why |
|---|---|---|
| `age` | ✅ | letters only |
| `student_name` | ✅ | underscore is allowed |
| `studentName` | ✅ | "camelCase" style |
| `score2` | ✅ | digit allowed *after* the first character |
| `2score` | ❌ | starts with a digit |
| `my-name` | ❌ | `-` is not allowed (the compiler reads it as subtraction) |
| `first name` | ❌ | spaces are not allowed |
| `int` | ❌ | it is a keyword |
| `Int` | ✅ | different from `int` because C is case sensitive (but confusing — avoid) |
| `_total` | ✅ but discouraged | starts with underscore |

> 💡 **Naming styles.** Two popular styles are `snake_case` (`total_price`) and `camelCase` (`totalPrice`). **Pick one and stay consistent.** In these notes you will see both, just like in your slides.

---

## 1.4 Comments

A **comment** is a note you leave in the code for yourself or for other people. The compiler **ignores** it completely. Comments exist for **humans**.

Use comments to explain **what** a piece of code is for and **why** you did it that way, so that you can understand it again six months later.

C has two kinds of comments:

**1. Multi-line comment** — starts with `/*` and ends with `*/`. It may cover many lines.

```c
/* This is a comment. */

/*
   This comment
   covers several lines.
*/
```

**2. Single-line comment** — starts with `//` and lasts until the end of that line.

```c
// This is a single-line comment
```

Comments can also sit **after** code on the same line:

```c
age = 24;   // age in years
```

> ⚠️ **Common mistakes with comments**
> - Forgetting to close `/* ... */`. Everything after it becomes a comment — including your real code!
> - You **cannot nest** `/* ... /* ... */ ... */`. The first `*/` ends the comment.
> - Over-commenting: `x = x + 1; // add one to x` tells the reader nothing new. Comment the **reason**, not the obvious.

**Handy trick:** to *temporarily switch off* a line of code, put `//` in front of it. This is called "commenting out".

Comments are not mandatory — but good programmers use them.

---

## 1.5 Your first program — Hello, World!

Tradition says every programmer starts here. Read it once, then we will take it apart line by line.

```c
/*
Finally my very
first C program
*/
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");   // displays Hello, World! on the screen
    return 0;
}
```
```output
Hello, World!
```

> **Question from the slides:** *Can you spot the multi-line and single-line comments?*
> Multi-line: the first four lines (`/* ... */`). Single-line: `// displays Hello, World! on the screen`.

### Anatomy of the program

```
 /* comment */                      ← ignored by the compiler
 #include <stdio.h>                 ← "bring in" the input/output library
 int main()                         ← the function where execution starts
 {                                  ← start of main's body
     printf("Hello, World!\n");     ← a statement: show text on the screen
     return 0;                      ← a statement: finish, report "success"
 }                                  ← end of main's body
```

#### `#include <stdio.h>`

Your program wants to put text on the screen. That means talking to the screen hardware — a long, complicated job. Luckily somebody already did that heavy lifting and packaged it in a **header file** called **`stdio.h`** ("**st**an**d**ard **i**nput/**o**utput").

- `.h` simply means *header file*.
- It contains a **library of functions** for input and output — for example `printf`.
- To use those functions you must first **include** the file with the `#include` **preprocessor command**.

The line starts with `#`: it is not a normal C statement. It is an instruction to the **preprocessor**, a helper that runs *before* the real compilation. It does **not** end with a semicolon.

> 💡 **Analogy:** `#include <stdio.h>` is like borrowing a toolbox before starting work. Without it, the compiler says, "I don't know what `printf` is."

#### `int main()`

- **Execution of every C program begins at `main()`.** It does not matter where in the file it is written.
- `main()` is **mandatory** — no `main`, no program.
- The code between the curly braces `{ }` is the **body** of `main`.
- The word `int` before `main` says "this function gives back an **int**eger when it finishes". That is the `0` in `return 0;`. (There is much more about functions in Chapter 6.)

> 📝 Many modern programmers write `int main(void)` — the word `void` says clearly, "main takes no input". Both forms work in this course; we will mostly use `int main(void)`.

#### `printf("Hello, World!\n");`

- `printf` is a **library function** that sends **formatted output** to the screen.
- Whatever is inside the double quotes `" "` is a **string** — it is printed.
- The `;` (semicolon) ends the statement. **Every statement in C ends with a semicolon.**
- `\n` is an **escape sequence** meaning "go to a new line" (more in a moment).

#### `return 0;`

- It ends `main`, and therefore the program.
- The `0` is reported to the operating system and means "**everything went fine**". A non-zero number would mean "something went wrong".
- It is not strictly mandatory (modern C assumes `return 0` at the end of `main`), but it is **good practice** to write it.

### What happens when this program runs?

1. The OS starts the program and jumps into `main`.
2. `printf` prints `Hello, World!` and moves the cursor to the next line.
3. `return 0;` ends the program with "success".

---

## 1.6 Escape sequences

Look again at `\n` in the `printf`. It is **two characters** in your code (`\` and `n`), but it produces **one special effect**: a new line. Such a pair is called an **escape sequence**: the backslash "escapes" from normal text.

| Escape sequence | What it does |
|---|---|
| `\n` | **Newline** — moves to the start of the next line (like the Enter key) |
| `\t` | **Horizontal tab** — jumps to the next tab stop (like the Tab key) |
| `\\` | prints one **backslash** `\` |
| `\"` | prints a **double quote** `"` |
| `\'` | prints a **single quote** `'` |
| `\?` | prints a question mark `?` |
| `\0` | the **null character** (marks the end of a string — important in Chapter 8) |
| `\a` | **alert** — makes a beep (not in your slides, but part of C) |
| `\b` | **backspace** — moves the cursor back one position |
| `\f` | **form feed** — new page (rarely used) |
| `\r` | **carriage return** — moves the cursor to the start of the *same* line |
| `\v` | **vertical tab** (rarely used) |

Here is a program that uses the most important ones:

```c
#include <stdio.h>

int main(void)
{
    printf("Name:\tKofi\n");
    printf("Age:\t21\n");
    printf("She said, \"Welcome!\"\n");
    printf("Folder: C:\\Users\\Kofi\n");
    printf("It\'s fine\n");
    return 0;
}
```
```output
Name:	Kofi
Age:	21
She said, "Welcome!"
Folder: C:\Users\Kofi
It's fine
```

Why do we need `\"`? Because a plain `"` would end the string! And why `\\`? Because a single `\` means "an escape sequence starts here". To print a real backslash, you write two.

### `\n` decides where lines end

`printf` does **not** add a new line automatically. Compare:

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, ");
    printf("World!");
    printf("\n");
    printf("Line 1\nLine 2\nLine 3\n");
    return 0;
}
```
```output
Hello, World!
Line 1
Line 2
Line 3
```

The first two `printf`s stay on the same line because there is no `\n` between them. The last `printf` produces three lines from **one** statement.

> ⚠️ **Common mistake:** forgetting the final `\n`. Your output works, but the next thing on your screen (such as the command prompt) appears glued to the end of your text.

---

## 1.7 Statements, whitespace and layout

- A **statement** is one complete instruction. It ends with `;`.
- C ignores **extra spaces, tabs and blank lines** between tokens. The following two programs are *identical* to the compiler:

```c
#include <stdio.h>
int main(void){printf("Hi\n");return 0;}
```

```c
#include <stdio.h>

int main(void)
{
    printf("Hi\n");
    return 0;
}
```

Obviously the second is far nicer for **humans**. Good habits:

1. **Indent** the code inside `{ }` by 4 spaces (or one tab).
2. Write **one statement per line**.
3. Put a **blank line** between logical sections.
4. Use meaningful names and helpful comments.

> 🔑 **C is case sensitive.** `printf` works. `Printf`, `PRINTF` and `printF` do not. `main` works; `Main` does not.

---

## 1.8 Running the code: from `.c` file to output

### The four steps

1. **Write** the code in a text editor or an **IDE** (Integrated Development Environment).
2. **Save** the file with the extension **`.c`** — for example `hello.c`.
3. **Build** (compile and link) the file. The compiler checks your code for mistakes and translates it into machine code.
4. **Run** the resulting program. Its output appears on the screen.

### Which tools can I use?

| Option | Notes |
|---|---|
| **Code::Blocks** (with MinGW) | The IDE mentioned in your lecture. Create a *Console application → C* project, paste the code, press **Build and Run** (F9). |
| **VS Code** + a compiler (MinGW-w64 / GCC) | Install the *C/C++* extension and a compiler, then compile in the terminal. |
| **Command line** with GCC | `gcc hello.c -o hello` then run `hello` (Windows) or `./hello` (Linux/Mac). |
| **Microsoft C compiler** | In a *Developer Command Prompt*: `cl hello.c`, then run `hello.exe`. |
| **Online compilers** | Websites such as OnlineGDB or Programiz let you run C in the browser, no installation needed. |

### What the compiler really does (a peek behind the curtain)

```
 hello.c ──▶ Preprocessor ──▶ Compiler ──▶ Assembler ──▶ Linker ──▶ hello.exe
 (source)    (#include is    (checks      (makes        (joins your  (program you
              replaced by     syntax,      machine       code with     can run)
              the header)     makes        code in an    library code
                              assembly)    object file)  such as printf)
```

You press one button, and all of this happens. Remember it, though: if you ever see an error from the **linker** ("undefined reference to …") it means the stages up to there succeeded but a function could not be found.

---

## 1.9 Reading compiler messages: errors and warnings

Every beginner makes mistakes. The difference between a beginner and a professional is that the professional **reads the error message**.

- An **error** means the compiler could not build the program. Fix it.
- A **warning** means "this *might* be a mistake". The program still builds. **Treat warnings seriously** — they often point at real bugs.

### How to read an error

Suppose line 4 of `hello.c` is `printf("Hello, World!\n")` and you forgot its semicolon. GCC says:

```
hello.c: In function 'main':
hello.c:4:30: error: expected ';' before 'return'
```

1. `hello.c` — the file.
2. `4:30` — **line 4**, column 30: the spot right after the `)`, where the `;` should have been.
3. `error: expected ';' before 'return'` — what it expected. It tells you what is missing, and that it only noticed when it reached the next word, `return`.

> ⚠️ Not every compiler points at the same place. GCC points at the end of the line that is missing the `;`. Some other compilers (for example Microsoft's `cl`) report the **next** line, the one that starts with `return`. So always look at the reported line **and the line above it**.

> 💡 **Golden rules for fixing errors**
> 1. Fix the **first** error first. Later errors are often "echoes" of the first one.
> 2. Look at the reported line **and the line above it**.
> 3. Recompile after **each** fix.
> 4. Read the message slowly, word by word.

### The most common beginner mistakes

| Mistake | Example | Typical message (wording differs by compiler) |
|---|---|---|
| Missing semicolon | `printf("Hi\n")` | `expected ';' before ...` |
| Missing closing quote | `printf("Hi\n);` | `missing terminating " character` |
| Wrong case | `Printf("Hi\n");` | `implicit declaration of function 'Printf'; did you mean 'printf'?` (older compilers: a warning, then the linker's `undefined reference to 'Printf'`) |
| Forgot `#include <stdio.h>` | (line missing) | `implicit declaration of function 'printf'` plus the hint `include '<stdio.h>'` |
| Missing closing brace `}` | | `expected declaration or statement at end of input` |
| Single quotes for a string | `printf('Hi');` | `multi-character character constant`, then `passing argument 1 of 'printf' makes pointer from integer without a cast` |
| Unclosed comment `/*` | | everything after it disappears, then `unterminated comment` |
| Using an undeclared name | `x = 5;` without declaring `x` | `'x' undeclared (first use in this function)` |

> 📝 **Newer compilers are stricter.** Since GCC 14, calling a function that was never declared (`Printf`, or `printf` without `#include <stdio.h>`) and passing a number where text is expected are **errors**, not warnings. Older compilers only warned and sometimes built a broken program. Either way, the fix is the same.

---

## Key takeaways

- C was created by **Dennis Ritchie** at Bell Labs in the early 1970s to write **Unix**.
- C gives you a clear picture of how computers work and is the base of many other languages.
- C has **32 keywords** (lowercase); identifiers follow the rules: letters, digits, underscore; not starting with a digit; not a keyword; case sensitive.
- **Comments:** `/* ... */` for many lines, `//` for one line. The compiler ignores them.
- Every program needs **`main()`**. Execution starts there.
- `#include <stdio.h>` gives you `printf`. `printf("...")` prints text. **Every statement ends with `;`.**
- **Escape sequences:** `\n` newline, `\t` tab, `\\` backslash, `\"` quote.
- **Write → Save as `.c` → Build → Run.** Read error messages from the top.

---

# Exercises — Chapter 1

## Part A — Quick check

**Ex 1.1** Who created C, and in which decade? What was C first used to build?

**Ex 1.2** Give **three** reasons why it is useful to learn C.

**Ex 1.3** Which of these are valid C identifiers? Give a reason for each invalid one.

`total` · `2ndPlace` · `_count` · `my-name` · `float` · `Student_Name` · `x1` · `price$` · `while` · `first name` · `Int` · `GPA_2024`

**Ex 1.4** True or false?
1. `Main` and `main` are the same in C.
2. `Int` is a keyword.
3. The compiler runs the code inside comments.
4. Every statement in C must end with a semicolon (except those like `#include` lines and blocks).
5. A C program can have two `main()` functions.
6. `/* a /* b */ c */` is a valid nested comment.

**Ex 1.5** What does `#include <stdio.h>` do? What would happen if you left it out of Hello World?

**Ex 1.6** Which function must every C program contain? What is special about it?

**Ex 1.7** What does `return 0;` at the end of `main` tell the operating system?

**Ex 1.8** Write one single-line comment and one multi-line comment. Are they executed?

**Ex 1.9** State the meaning of: `\n`, `\t`, `\\`, `\"`, `\'`.

**Ex 1.10** Name the **four steps** to turn an idea into running C code.

## Part B — Predict the output

*Write the exact output. Use `⏎` to mark line ends if it helps you.*

**Ex 1.11**
```c
printf("A\nB\nC\n");
```

**Ex 1.12**
```c
printf("A");
printf("B");
printf("\n");
printf("C\n");
```

**Ex 1.13**
```c
printf("Name:\tAma\nAge:\t19\n");
```

**Ex 1.14**
```c
printf("She said \"Hi\"\n");
```

**Ex 1.15**
```c
printf("C:\\temp\\new\n");
```

**Ex 1.16**
```c
printf("One\n");
// printf("Two\n");
/* printf("Three\n");
   printf("Four\n"); */
printf("Five\n");
```

**Ex 1.17**
```c
printf("Hello");
printf("World\n");
printf("Hello\n");
printf("World");
```

**Ex 1.18** How many **lines** (including empty ones) does this print?
```c
printf("\n\nHi\n\n");
```

## Part C — Find and fix the bugs

*For each program, list **every** mistake and write the corrected version.*

**Ex 1.19**
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    printf("Welcome to KNUST!\n")
    return 0;
}
```

**Ex 1.20**
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    Printf("Welcome to KNUST!\n");
    return 0;
}
```

**Ex 1.21**
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    printf("Welcome to KNUST!\n);
    return 0;
}
```

**Ex 1.22**
<!--skip-->
```c
int main(void)
{
    printf("Welcome to KNUST!\n");
    return 0;
}
```

**Ex 1.23**
<!--skip-->
```c
#include <stdio.h>
/* This program prints a greeting
int main(void)
{
    printf("Akwaaba!\n");
    return 0;
}
```

**Ex 1.24**
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    printf("Akwaaba!\n");
    return 0;
```

**Ex 1.25**
```c
#include <stdio.h>
int Main(void)
{
    printf("Akwaaba!\n");
    return 0;
}
```

**Ex 1.26**
<!--skip-->
```c
#include <stdio.h>
int main(void)
{
    printf('Akwaaba!\n');
    return 0
}
```

## Part D — Write the program

**Ex 1.27** Print your **name**, **programme of study** and **level** on three separate lines.

**Ex 1.28** Print this address (use your own details if you like), one `printf` per line:
```
Department of Computer Engineering
KNUST
Kumasi, Ghana
```

**Ex 1.29** Print a price list using `\t` to line up the columns:
```
Item        Price (GHS)
Rice          12.50
Gari           8.00
Kenkey         5.00
```

**Ex 1.30** Print a rectangle of stars, 4 rows by 12 columns:
```
************
*          *
*          *
************
```

**Ex 1.31** Print this quotation, with the quotation marks and the apostrophe exactly as shown:
```
Kwame said, "Programming isn't hard - it's practice!"
```

**Ex 1.32** Print this Windows file path:
```
C:\Users\Ama\Documents\COE281
```

**Ex 1.33** Print a staircase with 5 steps:
```
#
##
###
####
#####
```

**Ex 1.34** Print a centred triangle (pyramid) with 4 rows:
```
   *
  ***
 *****
*******
```

**Ex 1.35** Print a small **receipt**. Use `\t` for alignment:
```
===== PROVISION SHOP =====
Milk          GHS 15.00
Sugar         GHS  9.50
Biscuits      GHS  6.00
--------------------------
TOTAL         GHS 30.50
```

**Ex 1.36** Produce the output `Hello World from C` in **three** different ways: (a) one `printf`; (b) three `printf`s on the same line; (c) one `printf` per word, each on its own line.

**Ex 1.37** Print the word **KNUST** in big block letters (5 rows high) using the `#` character.

## Part E — Challenges

**Ex 1.38** Print the Ghana flag in text: three horizontal bands labelled `RED`, `GOLD` (with a `*` star in the middle) and `GREEN`, each band 3 lines tall and 15 characters wide. Use any layout you like.

**Ex 1.39 (why we need loops)** Print the 5 × 5 multiplication table below using **only** `printf` statements. Count how many statements you used. How would it feel to print a 50 × 50 table this way? (You will fix this pain in Chapter 5.)

```
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20
5	10	15	20	25
```

**Ex 1.40 (preview of a surprise)** `printf` itself *returns* a value: the number of characters it printed. Write a program that prints `Hello` followed by a newline, and then prints how many characters the first `printf` printed. (Hint: `int n = printf("..."); printf("%d\n", n);` — you will learn `%d` in Chapter 4.)

**Ex 1.41 (code archaeology)** The program below has **five** mistakes. Find all five and write the corrected program so it prints the three lines shown. (The gaps are tabs, shown here with the usual tab stops every 8 columns.)

<!--skip-->
```c
#include <stdio>
Int main(void)
{
    /* print the course info
    printf("Course:\tCOE 281\n");
    printf("Lecturer:\tDr. Mensah\n)
    printf("Language:\tC\n");
    return 0;
}
```
Expected output:
```
Course: COE 281
Lecturer:       Dr. Mensah
Language:       C
```
*Bonus question:* why does the first line not line up with the other two?

## Part F — Hands-on tasks

**Ex 1.42** Install a C compiler/IDE (Code::Blocks, or VS Code + GCC, or use an online compiler). Type **Hello, World!** by hand (don't copy-paste!) and run it. Write down the tool you used and its version.

**Ex 1.43 (error diary)** Take your working Hello World and **break it on purpose** in five different ways (remove the `;`, remove a quote, misspell `printf`, remove `#include`, remove a `}`). For each one, write in a notebook: (1) what you changed, (2) the exact error message, (3) which line the compiler reported, (4) what the message *really* meant.

**Ex 1.44** Compile `hello.c` from the command line (not from the IDE). Write down the command you used. Where did the executable appear? How big is it?

---

*End of Chapter 1. Next: [Chapter 2 — Variables and Data Types](02-variables-and-data-types.md)*
