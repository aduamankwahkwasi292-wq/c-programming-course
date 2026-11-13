# The Complete C Programming Course

### COE 281 — Programming and Problem-Solving 1

A full course in C for beginners, built chapter-by-chapter from the COE 281 lecture slides (KNUST). Every idea is explained in simple language with pictures, analogies and small programs, followed by **a large number of diverse exercises with complete solutions.**

> **Written for:** a first-year student with no programming experience.

🌐 **Read it online** (searchable, with dark mode and a jump-to-exercise box): **https://aduamankwahkwasi292-wq.github.io/c-programming-course/**

---

## 1. The course map

| Ch | Topic (from your slides) | Lesson + exercises | Solutions | Exercises |
|---|---|---|---|---|
| 0 | Introduction to Programming | [lesson](lessons/00-introduction-to-programming.md) | [solutions](solutions/00-introduction-to-programming.md) | 37 |
| 1 | C Basics | [lesson](lessons/01-c-basics.md) | [solutions](solutions/01-c-basics.md) | 44 |
| 2 | Variables and Data Types | [lesson](lessons/02-variables-and-data-types.md) | [solutions](solutions/02-variables-and-data-types.md) | 52 |
| 3 | Operators | [lesson](lessons/03-operators.md) | [solutions](solutions/03-operators.md) | 61 |
| 4 | Data Input and Output | [lesson](lessons/04-data-input-and-output.md) | [solutions](solutions/04-data-input-and-output.md) | 65 |
| 5 | Flow of Control | [lesson](lessons/05-flow-of-control.md) | [solutions](solutions/05-flow-of-control.md) | 116 |
| 6 | Functions | [lesson](lessons/06-functions.md) | [solutions](solutions/06-functions.md) | 107 |
| 7 | Arrays | [lesson](lessons/07-arrays.md) | [solutions](solutions/07-arrays.md) | 112 |
| 8 | Pointers and Strings | [lesson](lessons/08-pointers-and-strings.md) | [solutions](solutions/08-pointers-and-strings.md) | 131 |
| 9 | Projects and Final Exam | [lesson](lessons/09-projects-and-final-exam.md) | [solutions](solutions/09-projects-and-final-exam.md) | 4 worked projects, 10 project ideas, 100-mark exam |
| | **Total** | | | **725 exercises + projects + exam** |

**Appendices:** [Cheat sheet](appendix/cheat-sheet.md) · [Reference tables](appendix/reference-tables.md) (ASCII, format specifiers, precedence, limits) · [Errors and debugging guide](appendix/errors-and-debugging.md) · [Glossary](appendix/glossary.md)

**Where each slide deck went**

| Slide deck | Chapter |
|---|---|
| `00 Intro to Programming.pdf` | Chapter 0 |
| `01 C Basics.pdf` | Chapter 1 |
| `02 Variables  Datatypes.pdf` | Chapter 2 |
| `03 Operators.pdf` | Chapter 3 |
| `04 Data Input and Output.pdf` | Chapter 4 |
| `05 Flow of Control.pdf` | Chapter 5 |
| `06 Functions.pdf` | Chapter 6 |
| `07 Arrays.pdf` | Chapter 7 |
| `08 Pointers and Strings.pdf` | Chapter 8 |

Every slide topic is covered, including the items your lecturer set as "further reading" or "assignment": printf width/precision, the conditional and bitwise operators, `sizeof`, 3D arrays, function pointers, `strrchr`, `fgets`/`fputs` and *why `gets` is risky*.

---

## 2. How every chapter is organised

1. **What you will learn** — the goals.
2. **The lesson** — small steps, with a program for each idea, its output, pictures, and "common mistakes".
3. **Key takeaways** — the chapter in ten lines.
4. **Exercises**, always in the same six parts:

| Part | Type | What it trains |
|---|---|---|
| **A** | Quick check | definitions, true/false, concepts |
| **B** | Predict the output | reading and tracing code like a computer |
| **C** | Find and fix the bugs | debugging — the skill employers care about |
| **D** | Write the program | graded from easy to hard |
| **E** | Challenges and mini-projects | problem-solving |
| **F** | Research tasks | the "further reading" your lecturer asks for |

5. **Solutions** in a separate file — numbering matches exactly (**Ex 5.67** is solved under **Ex 5.67**).

---

## 3. How to study (the method that works)

1. **Read** a section, then **type the example programs yourself** (do not copy-paste) and run them.
2. **Change them** — break them on purpose and see what the compiler says.
3. Do the exercises **in order**, **on paper first** for Parts A–C.
4. For Part D, **write the algorithm in pseudocode** (Chapter 0!) before the C code.
5. **Struggle for at least 10 minutes** before opening a solution. Then compare — and try to write it again *without looking*.
6. Keep an **error diary** (Ex 1.43). Review it weekly.
7. After each chapter, redo three exercises from memory a few days later.

**Suggested schedule** (about 10 weeks, 6–8 hours a week)

| Week | Chapters | Goal |
|---|---|---|
| 1 | 0, 1 | install a compiler; Hello World; think like a programmer |
| 2 | 2, 3 | variables, types, operators |
| 3 | 4 | input and output; first interactive programs |
| 4–5 | 5 | decisions and loops — **take your time here** |
| 6 | 6 | functions and recursion |
| 7 | 7 | arrays (1D, then 2D) |
| 8–9 | 8 | pointers, then strings |
| 10 | 9 | projects, then the mock exam under real conditions |

---

## 4. Setting up your compiler

You need a C **compiler** and a place to type code. Any one of these works:

| Option | How |
|---|---|
| **Code::Blocks** with MinGW (the IDE in your lecture) | install *codeblocks-…mingw-setup*; create a *Console application → C* project; press **Build and Run** (F9) |
| **VS Code** + GCC | install VS Code, the *C/C++* extension, and a compiler (MSYS2 → `pacman -S mingw-w64-ucrt-x86_64-gcc`); compile in the terminal |
| **GCC on the command line** | `gcc prog.c -o prog` then run `prog` (Windows) or `./prog` (Linux/macOS). Recommended flags: `gcc -Wall -Wextra prog.c -o prog` |
| **Microsoft C compiler** (Visual Studio Build Tools) | open the *x64 Native Tools Command Prompt* and run `cl prog.c` then `prog.exe` |
| **Online** (no installation) | OnlineGDB, Programiz, or similar online C compilers |

Test your setup with the Hello World of Chapter 1. If `math.h` functions like `sqrt` fail to link on Linux/macOS, add `-lm`.

---

## 5. Conventions used in the files

- Code blocks show **complete programs** you can copy into a `.c` file. Most are followed by an **output block** showing exactly what the program prints.
- For interactive programs, the **text the user types is shown in the output** right after its prompt, as it appears in a terminal.
- Boxed notes: 💡 tips · ⚠️ common mistakes · 📝 **"Note on the slide"** — places where this course gently corrects or extends a slide.
- Tab-separated outputs are shown with spaces; the exact spacing depends on your terminal.

---

## 6. Where this course differs from the slides (and why)

Slides are summaries and a few contain slips. Wherever the course differs, it says so in a 📝 note. For the record:

| Slide says | The course says | Chapter |
|---|---|---|
| `float` has 6 digits of precision, `double` 14 | about 6–7 and 15–16 (the idea is the same) | 2 |
| The precedence table lists `<<=` `>>=` on their own row and omits `<` `<=` `>` `>=` | the full correct table | 3 |
| The slide for the comma operator shows `int a, c = 5, d;` | that is a declaration list; the real comma operator is explained separately | 3 |
| `Int main()` (capital I) | `int main(void)` | 1, 6 |
| `while` example "output `9 8 76`" | really `9 8 7 6` (the tab spaces were lost) | 5 |
| 2D-array "Method 2" has no outer braces | `{ {0,1,2,3}, {4,5,6,7}, {8,9,10,11} }` | 7 |
| `myArray[2][1]` "refers to the element 8" | it is **9** (8 is `myArray[2][0]`) | 7 |
| `scanf("%s", &fullname)` | `scanf("%s", fullname)` — no `&` for an array | 4, 8 |
| `gets()` to read strings | `gets` is unsafe and was removed in C11 → `fgets` | 4, 8 |
| `strcmp` prints `0 111 -32 32` | only the **sign** is guaranteed (other compilers print `0 1 -1 1`) | 8 |
| `strdup` without `free` | the copy must be freed | 8 |
| `strstr(mainString,'ello')` with single quotes | the second argument is a string: `"ello"` | 8 |
| Stack described as "first-in-last-out" | the usual name is **LIFO** (last in, first out) | 0 |

---

## 7. A note on correctness

Every complete program in the lessons and the solutions was **compiled and run**, and its output was compared automatically with the output printed in the text (about **580 programs** across the 10 chapters), and the "predict the output" answers were checked the same way. Errors found this way were corrected before publication — for example a miscounted vowel total and an impossible bank-withdrawal scenario.

Two things to keep in mind:

- The programs were checked with **GCC 14.2 (MinGW-w64, the compiler bundled with Code::Blocks)** *and* with Microsoft's C compiler, on 64-bit Windows. In this setup `int` is 4 bytes, `long` is 4 bytes and `double` is 8 bytes. On 64-bit Linux and macOS `long` is 8 bytes; the lessons point this out wherever it matters (Chapter 2). A few lines depend on the machine and are marked as such (memory addresses, `strcmp` raw values, random numbers).
- The deliberately **broken** programs in the "find and fix the bugs" exercises were also compiled, to confirm that each one really fails (or misbehaves) in the way the exercise says.

---

## 8. After this course

You now know the whole core of C. Natural next steps: **structures** (`struct`), **file input/output**, **dynamic data structures** (linked lists, stacks, queues — Chapter 0's list), **bit manipulation for embedded systems**, then **C++** or **Python** with a much easier time. Build the project ideas in Chapter 9 — they are the best preparation.

---

## 9. For maintainers: rebuilding the website

The pages in the `docs/` folder are generated from the Markdown files in `lessons/`, `solutions/` and `appendix/`. After editing any Markdown file, rebuild and commit:

```
pip install -r tools/requirements.txt
python tools/build_site.py
```

GitHub Pages serves the `docs/` folder of the `main` branch. (The small HTML comments such as `<!--in: 5-->` in the Markdown are invisible test markers; the site builder removes them.)

*Good luck — and remember: think first, code in small steps, test, and read the error messages.*
