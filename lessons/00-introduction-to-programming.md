# Chapter 0 — Introduction to Programming

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `00 Intro to Programming.pdf`  
> **Solutions:** [Solutions to Chapter 0](../solutions/00-introduction-to-programming.md)

---

## What you will learn

By the end of this chapter you will be able to:

1. Explain what programming (coding) is, in your own words.
2. Tell the difference between low-level and high-level languages, and between a compiler and an interpreter.
3. Name the main programming paradigms and say where C belongs.
4. Explain why choosing the right **data structure** matters.
5. Use simple **problem-solving strategies** (examples, similarities, working backwards, divide and conquer) to attack a problem *before* writing any code.
6. Write a simple **algorithm** in pseudocode and trace it by hand.

You will not write much C in this chapter. That is on purpose. A good programmer thinks first and types second.

---

## 0.1 What is computer programming?

A computer is an incredibly fast machine that has **no common sense**. It does *exactly* what it is told — nothing more, nothing less.

**Computer programming** is the art of telling a computer what to do through a set of instructions. Those written instructions are called **computer code**, or just **code**. That is why programming is also called **coding**.

Think of a recipe for jollof rice:

```
1. Heat the oil.
2. Fry the onions for 3 minutes.
3. Add tomato paste and stir.
4. Add rice and water.
5. Cover and cook for 25 minutes.
```

A cook can follow this recipe. A computer program is the same idea: **a list of clear steps**. The difference is that the computer needs the steps to be *far* more precise. If you tell a human "add some salt", they understand. If you tell a computer "add some salt", it freezes — *how much is "some"?*

> 💡 **Remember:** The computer is not clever. **You** are the clever one. Your job is to break a problem into steps so simple that even a machine with no common sense can follow them.

To write code you need a **programming language** — a language the computer can be made to understand. In this course the language is **C**.

---

## 0.2 Programming languages

A **programming language** is a language that lets us write detailed instructions for a computer. With it we create programs that carry out **algorithms**.

> **Algorithm** = a *finite* sequence of steps that, when followed, solves a particular problem.

"Finite" means it must *end*. A recipe that says "keep stirring forever" is not an algorithm.

Programming languages fall into two big families.

### 1. Low-level languages

These are close to what the hardware understands.

| Type | What it is | Example of how it looks |
|------|------------|-------------------------|
| **Machine language** | Strings of binary codes (0s and 1s) that the CPU understands *directly*. Not meant for humans to read. | `10110000 01100001` |
| **Assembly language** | A short list of basic instructions using abbreviations (called *mnemonics*). Easier than machine code, but still hard to read. | `MOV AL, 61h` |

### 2. High-level languages

These are designed for **humans**. You write with words and symbols that look a bit like English and mathematics. Example, in C:

```c
total = price * quantity;
```

Even a beginner can guess what that line does.

The slides ask you to research examples of high-level languages. Here is a starter list: **C, C++, Java, Python, JavaScript, C#, PHP, Go, Rust, Swift, Kotlin**.

### The translation problem

The CPU only understands machine language. So code written in a high-level language **must be translated** into machine language before it can run. There are two ways to translate:

| | **Compiler** | **Interpreter** |
|---|---|---|
| How it works | Translates the **whole program** at once, then you run the result. | Translates and runs the program **one line at a time**. |
| Real-life comparison | Translating an entire book, then handing the finished book to readers. | A translator standing next to two people, translating each sentence as it is spoken. |
| Speed of the finished program | Usually **faster** | Usually slower |
| Error messages | You see errors from the whole program *before* it runs. | You see an error only when the interpreter reaches that line. |
| Examples | **C**, C++, Rust, Go | Python, JavaScript, PHP (and many others) |

**C is a compiled language.** The flow looks like this:

```
  your code          compiler            executable file         output
┌───────────┐     ┌──────────────┐     ┌────────────────┐     ┌───────────────┐
│ hello.c   │ ──▶ │ gcc / cl     │ ──▶ │ hello.exe      │ ──▶ │ Hello, World! │
│ (source)  │     │ (translator) │     │ (machine code) │     │               │
└───────────┘     └──────────────┘     └────────────────┘     └───────────────┘
```

Generally, compiled languages are used to build software applications (operating systems, games, device software), while interpreted languages are often used for scripts, such as those that generate the content of dynamic websites. Real life has many exceptions — some languages do a bit of both — so treat this as a rule of thumb, not a law.

---

## 0.3 Programming paradigms

A **programming paradigm** is a *style* of solving problems — a family of tools and techniques that follow a similar approach. The paradigm decides how your code is structured, how it runs, and how it handles data.

There are two main paradigms.

**Imperative** — you tell the computer **how** to do it, step by step, by changing the state (the values) of variables. Focus: *how the program operates.*

**Declarative** — you tell the computer **what** you want, and let the language figure out how. Focus: *what must be done*.

```
                        Programming Paradigms
                 ┌──────────────┴──────────────┐
            Imperative                     Declarative
         ┌───────┴───────┐              ┌───────┴───────┐
    Procedural     Object-Oriented    Functional        Logic
    (routines)     (objects/classes)  (math functions)  (logical problems)
    e.g. C, Pascal  e.g. Java, Python  e.g. Lisp         e.g. Prolog
```

**C is a procedural language** (part of the imperative family). You organise your program into **procedures** — in C we call them **functions** — and run them one after another. You will meet functions in Chapter 6.

> 💡 **Analogy.** *Imperative:* "Go straight, turn left at the junction, walk 200 metres, enter the blue gate." *Declarative:* "Take me to Kumasi Central Market." In the first you give every step; in the second you only say where you want to end up.

---

## 0.4 Data structures

Every program works with **data**: names, prices, scores, temperatures. How you *arrange* that data has a huge effect on how simple and fast your solution is.

| Inappropriate choice leads to… | Appropriate choice leads to… |
|---|---|
| Clumsiness | Simplicity |
| Difficulty (code that is hard to follow) | Transparency (code that is easy to understand) |
| Inefficiency (slow, wasteful) | Efficiency |

When choosing a data structure, ask yourself:

- Can intermediate results be arranged so I can reach them quickly and avoid repeating calculations?
- Can I **search** and **update** the data easily?
- How much **memory** does it need?
- Does the problem look like a *common* data structure I already know?
- Can I recover data from earlier steps if I need it?

### Common data structures

| Structure | Idea | Everyday picture |
|-----------|------|------------------|
| **Array** | Many items of the **same type**, side by side, each with a position number | A row of numbered lockers |
| **Linked list** | Items linked to each other by **pointers** (each item knows where the next one is) | A treasure hunt: each clue tells you where the next clue is |
| **Stack** | **Last in, first out (LIFO).** The last item added is the first removed | A pile of plates — you take the top plate first |
| **Queue** | **First in, first out (FIFO).** The first item added is the first removed | People lining up at a bank: first to arrive is first served |
| **Tree** | **Hierarchical** structure — a parent with children | A family tree, or folders inside folders |

> 📝 **Note on the slides.** The slides write the stack rule as "first-in-last-out". It is the same rule viewed from the other side: the *first* plate you put down ends up at the bottom and is the *last* to leave. The usual name is **LIFO — last in, first out**.

In this course you will actually build with **arrays** (Chapter 7). The others come in later courses.

---

## 0.5 Problem-solving

Here is an uncomfortable truth: **problem-solving cannot be turned into a machine-like recipe.** There is no single universal method. Different strategies work for different people in different situations.

But there *are* strategies that help. And the most important ingredient of all is **practice**.

### Step 1 — Define the problem

Before anything else, make sure you understand what you are being asked. The **problem definition** phase focuses on *what must be done*, **not how**.

```
              Problem Statement
              /       |       \
          Task 1    Task 2    Task 3
```

A big problem statement is usually a bundle of small tasks.

**Example from the slides:** *"Write an algorithm to determine if an integer has 3 digits."*

Ask clarifying questions:

- What is the **input**? An integer.
- What is the **output**? A yes/no answer.
- Are negative numbers allowed? Is `-456` a 3-digit number? (Let us say yes: the digits are 4, 5, 6.)
- What about `0`, `99`, `1000`? (They do **not** have exactly 3 digits.)

Only now are we ready to think about *how*.

### Strategy A — Use specific examples

Pick real numbers and solve the problem by hand. To find the maximum of a set, take `{12, 7, 25, 9}` and just find it. You will notice what *you* do: you keep the biggest so far and compare it with each new number. That is the mechanism of your algorithm.

### Strategy B — Find similarities with problems you have solved

"Have I seen something like this before?" Summing the numbers 1 to 10 is very close to multiplying the numbers 1 to 10 (factorial). Change `+` to `×` and you are almost done.

> ⚠️ **Caution:** Do not let past experience make you lazy. Sometimes a problem *looks* like an old one but has a twist. Look at a problem from several angles.

### Strategy C — Work backwards from the solution

Start from the answer and undo the steps. Or guess an answer and test whether it fits.

*Example:* "I think of a number, multiply it by 3, subtract 4, and get 20." Work backwards: `20 + 4 = 24`, then `24 ÷ 3 = 8`. The number was **8**.

### Strategy D — Divide and conquer

Break the original problem into **smaller sub-problems** that are easier to solve, then combine the answers. Big programs are built this way — each small piece becomes a *function* (Chapter 6). The idea is used heavily in sorting, searching and selection algorithms.

> *Example:* Building a student-results program. Sub-problems: (1) read the scores, (2) calculate the average, (3) assign a grade, (4) print the report. Each is simple on its own.

### Always write things down

Whatever strategy you try, **take notes** so you do not go around in circles. Document the path you took to solve the problem; it will be of enormous benefit later. Keep a "programming notebook".

---

## 0.6 Writing an algorithm

We usually write an algorithm *before* the code, in one of two forms.

### Pseudocode

Informal, English-like steps. There is no strict grammar — it just has to be clear. We use words like `START`, `INPUT`, `SET`, `IF … THEN … ELSE`, `WHILE`, `PRINT`, `END`.

**Algorithm: does an integer have 3 digits?**

```
START
  INPUT n
  IF n < 0 THEN
      SET n = -n              (make it positive)
  END IF
  IF n >= 100 AND n <= 999 THEN
      PRINT "Yes, 3 digits"
  ELSE
      PRINT "No"
  END IF
END
```

**Algorithm: find the maximum of a list of numbers**

```
START
  INPUT the first number
  SET max = that number
  WHILE there are more numbers:
      INPUT next number
      IF next number > max THEN
          SET max = next number
      END IF
  END WHILE
  PRINT max
END
```

### Flowcharts

A flowchart draws the same logic with shapes and arrows.

| Shape | Meaning |
|-------|---------|
| Rounded box (oval) | **Start / End** |
| Parallelogram | **Input / Output** |
| Rectangle | **Process** (a calculation or assignment) |
| Diamond | **Decision** (yes/no question) |
| Arrows | The **flow** (order of steps) |

```
        ( START )
            │
      /  INPUT n  /
            │
        ◇ n < 0 ? ◇───Yes──▶ [ n = -n ]
            │ No                   │
            ◀──────────────────────┘
            │
   ◇ n >= 100 AND n <= 999 ?◇
      │Yes              │No
 /PRINT "Yes"/      /PRINT "No"/
      │                 │
      └───────┬─────────┘
          ( END )
```

### Tracing an algorithm by hand

A **trace table** is how you *test* an algorithm with real numbers before coding it. Each row is one step; each column is a variable.

Algorithm: *sum the numbers 1 to 4*

```
1. SET total = 0
2. SET count = 1
3. WHILE count <= 4
       total = total + count
       count = count + 1
4. PRINT total
```

| pass | count at the test | count <= 4 ? | total = total + count | count = count + 1 |
|------|-------|--------------|----------------------|-------------------|
| 1 | 1 | yes | 0 + 1 = **1** | 2 |
| 2 | 2 | yes | 1 + 2 = **3** | 3 |
| 3 | 3 | yes | 3 + 3 = **6** | 4 |
| 4 | 4 | yes | 6 + 4 = **10** | 5 |
| 5 | 5 | **no**, so stop | (not done) | (not done) |

Output: `10`. ✔ Notice that the test runs **five** times but the body runs only **four** times. The last test is the one that fails and ends the loop.

### A sneak peek: from pseudocode to C

Do not worry about the C syntax yet — you will learn every piece in the coming chapters. But look how closely the C version follows the pseudocode. This is how the "3 digits" algorithm looks as a real program:

<!--in: 456-->
```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n < 0)
        n = -n;                    /* make it positive first */

    if (n >= 100 && n <= 999)
        printf("Yes, 3 digits\n");
    else
        printf("No\n");

    return 0;
}
```
```output
Enter an integer: 456
Yes, 3 digits
```

Run it again with `-99`, `1000`, `-100` and `0` and compare with what *you* predicted from the pseudocode. (Results: `No`, `No`, `Yes`, `No`.)

---

## 0.7 The programming process

Real programmers follow a loop like this:

```
 1. Understand the problem  ──▶ 2. Plan (algorithm)  ──▶ 3. Write the code
          ▲                                                       │
          │                                                       ▼
 6. Fix (debug) ◀── 5. Test with many inputs ◀── 4. Compile & run
```

You will meet three kinds of mistakes ("bugs"):

| Error type | When you meet it | Example |
|---|---|---|
| **Syntax error** | At compile time. The compiler refuses to build your program. | Missing semicolon |
| **Runtime error** | While the program is running. It crashes. | Dividing by zero |
| **Logic error** | The program runs but gives the **wrong answer**. The hardest to find. | Using `+` where you needed `-` |

> 💡 The best defence against logic errors is what you just learned: **trace your algorithm by hand with real numbers before and after you code it.**

---

## 0.8 Why programming matters in engineering

Programming lets computers solve problems and perform tasks efficiently. In engineering it is used to:

- **Automate tasks** — e.g. a script that processes 10,000 sensor readings.
- **Model systems** — e.g. simulate a bridge under load before building it.
- **Build applications** — e.g. mobile apps, control software.

Typical application areas: **software engineering, artificial intelligence, embedded systems, simulations, databases**, and more.

---

## Key takeaways

- Programming = giving a computer a precise list of instructions (code) in a programming language.
- An **algorithm** is a finite, ordered list of steps that solves a problem.
- **Low-level** = machine and assembly. **High-level** = human-friendly (C, Python, Java…).
- **Compiler** translates the whole program first (C is compiled). **Interpreter** translates line by line.
- C is **procedural**, which is part of the **imperative** paradigm.
- A good **data structure** makes a solution simple and efficient: arrays, linked lists, stacks (LIFO), queues (FIFO), trees.
- Problem-solving: **define → use examples → look for similarities → work backwards → divide and conquer.** Write notes. Practise.
- Pseudocode and flowcharts let you design and test on paper *before* coding.
- Three kinds of bugs: syntax, runtime, logic.

---

# Exercises — Chapter 0

*Try each one on paper before looking at the solutions. No computer is needed in this chapter.*

## Part A — Quick check

**Ex 0.1** In one sentence, what is computer programming?

**Ex 0.2** What is an algorithm? Why does it have to be *finite*?

**Ex 0.3** Match each term (1–5) with its description (a–e).

| | Term | | Description |
|---|---|---|---|
| 1 | Machine language | a | Translates a whole program at once |
| 2 | Assembly language | b | Closest to human language; written with words and symbols |
| 3 | High-level language | c | Binary codes the CPU understands directly |
| 4 | Compiler | d | Translates and runs a program one line at a time |
| 5 | Interpreter | e | Short abbreviations (like `MOV`, `ADD`) for basic instructions |

**Ex 0.4** True or false? Give a reason for each *false* answer.

1. Machine language is designed to be easy for humans to read.
2. A program written in a high-level language can run directly on the CPU without any translation.
3. C is an interpreted language.
4. An interpreter translates the whole program before running it.
5. Programs written in compiled languages usually run faster than interpreted ones.
6. C is a procedural language.
7. In a declarative language you focus on *how* each step is done.
8. A stack removes the item that was added **first**.

**Ex 0.5** Name two other compiled languages and two interpreted languages (besides C).

**Ex 0.6** Put each language in a paradigm box (procedural / object-oriented / functional / logic): **C, Java, Lisp, Prolog, Pascal, Python.**

**Ex 0.7** Which data structure fits best?

1. The "undo" button in a text editor.
2. Customers waiting to be served at a pharmacy.
3. The marks of 60 students in one test.
4. The folders and sub-folders on your laptop.
5. A music playlist where every song stores *which song plays next*.

**Ex 0.8** List three questions you should ask when choosing a data structure.

**Ex 0.9** The slides say the *problem-definition* phase focuses on *what* must be done and not *how*. Why is it a bad idea to jump straight to "how"?

**Ex 0.10** Name the four problem-solving strategies from this chapter, and give a one-line meaning for each.

## Part B — Trace the algorithm

**Ex 0.11** Trace this algorithm and give the output.

```
1. SET a = 2
2. SET b = 5
3. SET a = a + b
4. SET b = a - b
5. SET a = a - b
6. PRINT a, b
```

**Ex 0.12** Trace this algorithm with the input list `7, 12, 5, 20, 9`. Fill in a trace table and say what the algorithm finds.

```
1. INPUT first number; SET m = first number
2. FOR each remaining number x:
       IF x > m THEN SET m = x
3. PRINT m
```

**Ex 0.13** Trace with `n = 4096` and state what the algorithm computes.

```
1. SET count = 0
2. WHILE n > 0:
       SET n = n DIV 10        (DIV = whole-number division, e.g. 4096 DIV 10 = 409)
       SET count = count + 1
3. PRINT count
```

**Ex 0.14** Trace with `x = 17`. What does this algorithm compute? (Hint: think of what is left over.)

```
1. WHILE x >= 5:
       SET x = x - 5
2. PRINT x
```

**Ex 0.15** Trace with `n = 6`. What famous list of numbers does it print?

```
1. SET a = 0
2. SET b = 1
3. REPEAT n times:
       PRINT a
       SET temp = a + b
       SET a = b
       SET b = temp
```

## Part C — Find the bug (in algorithms)

**Ex 0.16** The algorithm should output the **average** of three numbers but gives wrong answers. Find the mistake and correct it.

```
INPUT a, b, c
SET average = a + b + c / 3
PRINT average
```

**Ex 0.17** This algorithm should find the **largest** number in a list. It fails for the list `-8, -3, -15`. Why? Fix it.

```
SET max = 0
FOR each number x in the list:
    IF x > max THEN SET max = x
PRINT max
```

**Ex 0.18** This algorithm should sum 1 to N but it never ends. Why? Fix it.

```
INPUT N
SET total = 0
SET i = 1
WHILE i <= N:
    SET total = total + i
PRINT total
```

**Ex 0.19** This algorithm should say whether `n` is even. It is wrong. Find the problem.

```
INPUT n
IF n / 2 = 0 THEN
    PRINT "even"
ELSE
    PRINT "odd"
```

## Part D — Write the algorithm (pseudocode)

**Ex 0.20** Read a temperature in °C and print it in °F. (`F = C × 9 / 5 + 32`)

**Ex 0.21** Read three numbers and print the **largest**.

**Ex 0.22** Read a year and say whether it is a **leap year**. (Leap if divisible by 4, except century years, which must be divisible by 400. So 2024 and 2000 are leap; 1900 and 2023 are not.)

**Ex 0.23** Read `N` and print the sum `1 + 2 + … + N`.

**Ex 0.24** Read `N` and print `N!` (N factorial = 1 × 2 × … × N).

**Ex 0.25** Read an integer `n > 1` and say whether it is **prime**.

**Ex 0.26** Read a positive integer and print its digits **reversed** (`1234` → `4321`).

**Ex 0.27** A shop gives a **10% discount** when the total bill is more than GH₵200. Read the total and print the amount to pay.

**Ex 0.28** Read an exam score (0–100) and print the grade: A (80–100), B (70–79), C (60–69), D (50–59), F (below 50).

**Ex 0.29** Write the steps (with decisions) for a person withdrawing cash from an ATM.

**Ex 0.30** Draw a flowchart for Ex 0.21 (largest of three numbers).

## Part E — Challenges

**Ex 0.31 (Divide and conquer)** You have 8 coins that look identical. One is **lighter** than the rest. You have a balance scale (no weights). What is the *smallest* number of weighings that always finds the light coin? Describe your method.

**Ex 0.32 (Divide and conquer)** I am thinking of a whole number between 1 and 100. After each guess I tell you "higher", "lower" or "correct". Describe a strategy that **always** wins in at most 7 guesses.

**Ex 0.33 (Work backwards)** I think of a number, add 9, multiply by 4, subtract 6, and the result is 58. What was my number?

**Ex 0.34 (Similarities)** You already have an algorithm that adds the numbers 1 to N. Explain how you would change it (in as few words as possible) to (a) multiply the numbers 1 to N, and (b) add only the **even** numbers from 1 to N.

## Part F — Research tasks (from the slides' "further reading")

**Ex 0.35** Research and list **five** examples of high-level languages and say for each whether it is usually compiled or interpreted.

**Ex 0.36** Write half a page on the differences between a compiler and an interpreter. Include one advantage and one disadvantage of each.

**Ex 0.37** Find **two** real-world products or systems (a phone OS, a game console, a car, a hospital machine…) that rely on C code. Say what part of the system C is used for.

---

*End of Chapter 0. Next: [Chapter 1 — C Basics](01-c-basics.md)*
