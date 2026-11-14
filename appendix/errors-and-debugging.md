# Errors and Debugging Guide

> Every programmer — including your professor — spends a large part of their life fixing mistakes. The skill is not "never making mistakes". The skill is **finding and fixing them quickly and calmly.**

---

## 1. The three kinds of bugs

| Kind | When you meet it | Example | How you find it |
|---|---|---|---|
| **Syntax / compile error** | The compiler refuses to build your program | missing `;`, misspelled `printf` | read the compiler message |
| **Runtime error** | The program starts, then crashes or hangs | divide by zero, bad pointer, infinite loop | find *where* it dies |
| **Logic error** | The program runs but gives the **wrong answer** | `+` instead of `-`, off-by-one | trace by hand, print values |

Logic errors are the hardest because **nothing complains**. Trust your tests, not your feelings.

---

## 2. Reading compiler messages

A message has a **file**, a **line number**, a **kind** (`error` or `warning`) and a **description**:

```
prog.c:7:5: error: 'total' undeclared (first use in this function)
```

**Golden rules**

1. Fix the **first** error first — later ones are often "echoes" of it.
2. Look at the reported line **and the line above it**. A missing `;` or `}` is usually noticed one line late.
3. **Recompile after every fix.**
4. **Never ignore warnings.** A warning is the compiler saying "this looks like a bug". Compile with `-Wall -Wextra` (GCC) or `/W3` (Microsoft).

### Common compile-time errors

| Message (GCC style) | Microsoft style | Usual cause | Fix |
|---|---|---|---|
| `expected ';' before ...` | `C2143: syntax error: missing ';'` | forgot a semicolon | add the `;` at the end of the unfinished statement (GCC points right at that spot; Microsoft reports the next line) |
| `'x' undeclared` | `C2065: undeclared identifier` | variable not declared, or misspelled / wrong case | declare it; check spelling |
| `implicit declaration of function 'foo'` | `C4013: 'foo' undefined; assuming extern` | function used before its prototype, or missing `#include` | add the `#include` or a prototype |
| `missing terminating " character` | `C2001: newline in constant` | unclosed string | add the closing `"` |
| `expected declaration or statement at end of input` | `C1075: no matching token found` | missing `}` | balance the braces |
| `too few arguments to function 'f'` | `C2198: too few arguments for call` | wrong number of arguments | match the prototype |
| `conflicting types for 'f'` | only a warning, `C4142: benign redefinition of type` (so read warnings!) | prototype and definition disagree | make them identical |
| `assignment of read-only variable 'x'` | `C2166: l-value specifies const object` | assigning to a `const` | remove the assignment |
| `invalid operands to binary % (have 'double' and 'int')` | `C2296: '%': illegal, left operand has type 'double'` | `%` on decimals | use integers or `fmod` |
| `warning: format '%d' expects argument of type 'int', but argument 2 has type 'double'` | `C4477: format string mismatch` | wrong `printf` specifier | match specifier and type |
| `warning: 'x' is used uninitialized` | `C4700: uninitialized local variable` | read before assigning | initialise it |
| `warning: ... makes integer from pointer without a cast` | `C4047: differs in levels of indirection` | `char c = "A";` or similar | `'A'` for a char |
| `undefined reference to 'f'` (linker) | `LNK2019: unresolved external symbol` | function declared but never defined; or misspelled `main` | define it; check spelling and case |
| `undefined reference to 'sqrt'` | `LNK2019` | math library not linked (GCC) | add `-lm` |

---

## 3. Runtime errors

| Symptom | Likely cause | What to check |
|---|---|---|
| **"Segmentation fault"** / program crashes | using a pointer that has no valid address (uninitialised, `NULL`, freed, or pointing to a dead local); array index out of range; writing into a string literal; forgetting `&` in `scanf`; `printf("%s")` on something that is not a string | every pointer is initialised; every index is within `0 … size−1`; arrays are big enough (including the `'\0'`) |
| **Stack overflow** (crash with no message) | recursion without a base case, or too deep | does every call move towards the base case? |
| **Program never ends** | infinite loop (no update, wrong condition, stray `;` after the loop header, a `float` counter) | trace the loop variable by hand; `Ctrl + C` stops the program |
| **"Floating point exception"** | integer division or `%` by zero | check the divisor first |
| **Garbage numbers** | uninitialised variable or array; wrong `printf` specifier; reading past the end of an array | initialise; match types |
| **Output "jumps" / input skipped** | leftover newline in the input buffer | `" %c"`; `getchar()` before `fgets` |

---

## 4. Finding logic errors — a toolkit

### Technique 1 — Predict, then check
Before you run the program, write down what **you** expect it to print for a small input. When the real output differs, you have found the area of the bug.

### Technique 2 — Trace table
Work through the program by hand, one statement at a time, recording every variable in a table (as in Chapters 0 and 5). This is the single most effective technique for beginners.

| step | i | sum | note |
|---|---|---|---|
| start | 1 | 0 | |
| loop | 2 | 1 | added 1 |
| … | | | |

### Technique 3 — Print debugging
Add temporary `printf`s to **look inside** the program:
```c
printf("DEBUG: i=%d sum=%d\n", i, sum);
```
Print values **before** and **after** the suspicious statement. Remove them when done.

### Technique 4 — Divide and conquer
Comment out half of the program (`/* … */` or `//`) and see whether the bug is still there. Keep halving. Test each **function** alone from a tiny `main`.

### Technique 5 — Shrink the problem
Reproduce the bug with the **smallest** program and smallest input. Bugs hide in big programs and show themselves in small ones.

### Technique 6 — Explain it aloud ("rubber-duck debugging")
Explain your code, line by line, to a friend — or a rubber duck. Very often you discover the bug while explaining.

### Technique 7 — Test the edges
Always test: the **smallest** input (0, 1, empty), **negative** numbers, the **largest** value, an array that is **full**, input that is **invalid**, and a case where the answer is **"not found"**.

---

## 5. Using a debugger

A **debugger** runs your program under your control: you can pause it, step through line by line, and look at variables.

**In an IDE** (Code::Blocks, VS Code, Visual Studio):
1. Click in the margin next to a line to set a **breakpoint** (the program will pause there).
2. Start debugging (F5 / the *Debug* button).
3. Use **Step Over** (F10) to run one line, **Step Into** (F11) to enter a function, **Continue** (F5) to run to the next breakpoint.
4. Watch the **Variables / Watch** window to see values change.

**With GCC's GDB** (command line). Compile with `-g`: `gcc -g prog.c -o prog`, then:

| Command | Meaning |
|---|---|
| `gdb ./prog` | start the debugger |
| `break main` / `break 25` | stop at a function / at line 25 |
| `run` | start the program |
| `next` / `step` | execute one line (stepping over / into functions) |
| `print x` / `print a[2]` / `print *p` | show a value |
| `backtrace` (`bt`) | show the chain of function calls (great for crashes!) |
| `continue` | run on until the next breakpoint |
| `quit` | leave GDB |

**Extra safety nets** (GCC/Clang on Linux/macOS): compile with `-fsanitize=address,undefined -g`. The program then reports out-of-bounds accesses, use-after-free and other undefined behaviour **as soon as they happen**, with the line number.

---

## 6. How to avoid bugs in the first place

1. **Plan before you code** (pseudocode / flowchart). Most logic errors are *design* errors.
2. **Write a little, test a little.** Compile after every few lines.
3. **Initialise** every variable and pointer.
4. Use **meaningful names** and **consistent indentation**. Always use braces.
5. Use **constants** (`#define SIZE 10`) instead of "magic numbers".
6. Keep **functions short**, with one job each.
7. **Check inputs** — validate what the user types; check `scanf`'s return value; check `malloc` for `NULL`.
8. **Compile with warnings on** and fix every warning.
9. **Comment the *why*** (not the obvious *what*).
10. Keep a **bug diary** (Ex 1.43): write down each bug and its cause. Patterns will emerge, and you will stop making the same mistakes.

---

## 7. Quick checklist when "it doesn't work"

- [ ] Did I read the **first** error message, slowly?
- [ ] Are all variables **declared** and **initialised**?
- [ ] `=` or `==`? `&&` or `||`? `<` or `<=`?
- [ ] Does every `scanf` have the right specifier and `&`?
- [ ] Are all **array indices** within range? Is there room for the `'\0'`?
- [ ] Does every loop **update** its variable and have the right condition?
- [ ] Is there an accidental **`;`** after `if (…)`, `for (…)` or `while (…)`?
- [ ] Integer **division** where I wanted decimals?
- [ ] Have I **traced** a small example by hand?
- [ ] Have I printed the values in the middle of the program?
