# Glossary

> Short, plain-English definitions of the words used in this course. Each entry points to the chapter where the idea is taught.

**Address** — The number that identifies where a variable lives in memory (usually written in hexadecimal). `&x` gives the address of `x`. *(Ch 8)*

**Algorithm** — A finite sequence of steps that solves a problem. *(Ch 0)*

**Argument** — The actual value supplied when a function is called, e.g. the `3` in `square(3)`. *(Ch 6)*

**Array** — A fixed-size collection of elements of the same type stored side by side under one name; elements are reached by index. *(Ch 7)*

**ASCII** — The code that assigns a number to each character (`'A'` = 65, `'a'` = 97, `'0'` = 48). *(Ch 2)*

**Assembly language** — A low-level language with short abbreviations for machine instructions. *(Ch 0)*

**Assignment** — Storing a value in a variable with `=`. *(Ch 2, 3)*

**Associativity** — The direction (left-to-right or right-to-left) in which operators of the same precedence are evaluated. *(Ch 3)*

**Base case** — The condition in a recursive function that stops the recursion. *(Ch 6)*

**Binary** — The base-2 number system using only 0 and 1; how computers store everything. *(Ch 3)*

**Bit** — A single binary digit (0 or 1). A **byte** is 8 bits. *(Ch 3)*

**Bitwise operator** — An operator that works on individual bits: `& | ^ ~ << >>`. *(Ch 3)*

**Block** — A group of statements inside `{ }`. Variables declared in a block exist only there. *(Ch 5, 6)*

**Break** — A statement that leaves a loop or `switch` immediately. *(Ch 5)*

**Buffer overflow** — Writing beyond the end of an array or string, damaging other memory — a common crash and security bug (cause of the `gets` ban). *(Ch 4, 8)*

**Bug** — A mistake in a program. **Debugging** is finding and fixing bugs. *(Ch 0, Appendix)*

**Call (function call)** — Running a function by writing its name and arguments. *(Ch 6)*

**Call by reference / pass by reference** — Passing the *address* of a variable so a function can change the original. *(Ch 8)*

**Call by value / pass by value** — Passing a *copy* of a value; the function can't change the caller's variable. *(Ch 6)*

**Call stack** — The pile of active function calls; each call is pushed when made and popped when it returns. *(Ch 6)*

**Case** — One labelled alternative inside a `switch`. *(Ch 5)*

**Cast** — Explicitly converting a value to another type: `(double) x`. *(Ch 2)*

**Character** — A single letter, digit or symbol; type `char`, written in single quotes. *(Ch 2)*

**Code** — The written instructions of a program. *(Ch 0)*

**Comment** — Text in the code ignored by the compiler: `// …` or `/* … */`. *(Ch 1)*

**Compiler** — A program that translates an entire source program into machine code. C is compiled. *(Ch 0)*

**Condition** — An expression that is true (non-zero) or false (0), used in `if` and loops. *(Ch 5)*

**Constant** — A value that never changes: a literal (`25`), a `const` variable, or a `#define` name. *(Ch 2)*

**Continue** — A statement that skips the rest of the current loop iteration. *(Ch 5)*

**Control statement** — A statement that changes the order of execution: decisions and loops. *(Ch 5)*

**Data structure** — A way of arranging data (array, list, stack, queue, tree…). *(Ch 0)*

**Data type** — The kind and size of data a variable holds (`int`, `char`, `float`, `double`…). *(Ch 2)*

**Declaration** — Introducing a name (variable or function) and its type to the compiler. *(Ch 2, 6)*

**Default** — The `switch` alternative that runs when no case matches. *(Ch 5)*

**Definition (function)** — The code that actually performs a function's task. *(Ch 6)*

**Dereference** — Following a pointer to reach the variable it points to, with `*p`. *(Ch 8)*

**Divide and conquer** — Solving a problem by splitting it into smaller sub-problems. *(Ch 0)*

**Double** — A decimal type with about 15 significant digits (8 bytes). *(Ch 2)*

**Element** — One item of an array. *(Ch 7)*

**Escape sequence** — A backslash code with a special meaning in text, e.g. `\n`. *(Ch 1)*

**Expression** — Anything that has a value: `3 + 4`, `x > 5`, `f(2)`. *(Ch 3)*

**Flow of control** — The order in which statements run. *(Ch 5)*

**Float** — A decimal type with about 6–7 significant digits (4 bytes). *(Ch 2)*

**Format specifier** — A `%`-code in `printf`/`scanf` such as `%d` or `%f`. *(Ch 4)*

**Function** — A named group of statements that performs one task and can be called repeatedly. *(Ch 6)*

**Function pointer** — A pointer that holds the address of a function. *(Ch 8)*

**Global variable** — A variable declared outside all functions, visible everywhere. *(Ch 6)*

**Header file** — A file (like `stdio.h`) that declares library functions; included with `#include`. *(Ch 1)*

**Hexadecimal** — The base-16 number system (digits 0–9 and A–F). *(Ch 8)*

**Identifier** — The name of a variable, function, etc. *(Ch 1)*

**Index** — The position number of an array element, starting from 0. *(Ch 7)*

**Infinite loop** — A loop that never ends. *(Ch 5)*

**Initialise** — Give a variable its first value. *(Ch 2)*

**Input buffer** — The "waiting room" holding typed characters until the program reads them. *(Ch 4)*

**Integer** — A whole number (type `int`). *(Ch 2)*

**Interpreter** — A program that translates and runs source code one line at a time. *(Ch 0)*

**Iteration** — One pass through the body of a loop. *(Ch 5)*

**Keyword** — A reserved word with a special meaning (`int`, `if`, `while`…). *(Ch 1)*

**Library** — A collection of ready-made functions. *(Ch 6)*

**Local variable** — A variable declared inside a function or block; it exists only there. *(Ch 6)*

**Logic error** — The program runs but gives the wrong result. *(Ch 0)*

**Loop** — A statement that repeats a block while a condition holds. *(Ch 5)*

**Machine language** — The binary instructions the CPU understands directly. *(Ch 0)*

**`main`** — The function where every C program starts executing. *(Ch 1)*

**Memory leak** — Memory obtained with `malloc` that is never returned with `free`. *(Ch 8)*

**Nested** — Placed inside another statement of the same kind (a loop in a loop, an `if` in a loop). *(Ch 5)*

**Null character (`'\0'`)** — The character with code 0 that marks the end of a string. *(Ch 8)*

**`NULL`** — The pointer value meaning "points to nothing". *(Ch 8)*

**Operand** — A value an operator works on. **Operator** — a symbol such as `+` that acts on operands. *(Ch 3)*

**Overflow** — A value too large for its type, which wraps around or misbehaves. *(Ch 2)*

**Paradigm** — A style of programming (procedural, object-oriented, functional, logic). *(Ch 0)*

**Parameter** — A variable in a function's definition that receives an argument. *(Ch 6)*

**Pointer** — A variable that stores the address of another variable. *(Ch 8)*

**Pointer arithmetic** — Adding/subtracting integers to pointers to move between elements. *(Ch 8)*

**Precedence** — Which operator is evaluated first when several are mixed. *(Ch 3)*

**Preprocessor** — The step before compilation that handles lines starting with `#` (`#include`, `#define`). *(Ch 1)*

**Problem definition** — Stating *what* must be solved, before deciding *how*. *(Ch 0)*

**Program** — A set of instructions that a computer can execute. *(Ch 0)*

**Prototype** — A function declaration: return type, name and parameter types, ending with `;`. *(Ch 6)*

**Pseudocode** — Informal, English-like description of an algorithm. *(Ch 0)*

**Qualifier** — A keyword that modifies a type: `short`, `long`, `signed`, `unsigned`, `const`. *(Ch 2)*

**Queue** — A first-in, first-out data structure. *(Ch 0)*

**Recursion** — A function calling itself. *(Ch 6)*

**Return value** — The value a function sends back with `return`. *(Ch 6)*

**Runtime error** — A failure while the program is running (crash, division by zero). *(Ch 0)*

**Scope** — The part of the program where a name is visible. *(Ch 6)*

**Short-circuit evaluation** — `&&` and `||` stop evaluating once the result is known. *(Ch 3)*

**`sizeof`** — An operator giving the size in bytes of a type or variable. *(Ch 3)*

**Source code** — The program as written by the programmer, in a `.c` file. *(Ch 0)*

**Stack (data structure)** — A last-in, first-out structure. *(Ch 0)*

**Statement** — One complete instruction, usually ending with `;`. *(Ch 1)*

**Static variable** — A local variable that keeps its value between function calls. *(Ch 6)*

**String** — An array of characters ending with `'\0'`. *(Ch 8)*

**String literal** — Text in double quotes, such as `"Kumasi"`. *(Ch 1, 8)*

**Syntax error** — A violation of the language's grammar, caught by the compiler. *(Ch 0, 1)*

**Ternary operator** — The conditional operator `condition ? a : b`. *(Ch 3)*

**Trace table** — A table that records the values of variables step by step while you run a program by hand. *(Ch 0)*

**Type casting** — Converting a value from one type to another (implicit or explicit). *(Ch 2)*

**Undefined behaviour** — Code whose result the C standard does not define (out-of-bounds access, signed overflow…): anything may happen. *(Ch 7)*

**Unsigned** — A type that stores only zero and positive values. *(Ch 2)*

**Variable** — A named storage space in memory that holds a value that can change. *(Ch 2)*

**`void`** — "No type": a function that returns nothing, or a generic pointer (`void *`). *(Ch 6, 8)*

**Whitespace** — Spaces, tabs and newlines. *(Ch 1, 4)*
