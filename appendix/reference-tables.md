# Reference Tables

> Quick-look tables for the whole course. For explanations, see the chapters.

---

## 1. The 32 keywords of standard C

| | | | | |
|---|---|---|---|---|
| `auto` | `break` | `case` | `char` | `const` |
| `continue` | `default` | `do` | `double` | `else` |
| `enum` | `extern` | `float` | `for` | `goto` |
| `if` | `int` | `long` | `register` | `return` |
| `short` | `signed` | `sizeof` | `static` | `struct` |
| `switch` | `typedef` | `union` | `unsigned` | `void` |
| `volatile` | `while` | | | |

(Newer standards add `inline`, `restrict`, `_Bool` and a few others.)

---

## 2. Escape sequences

| Sequence | Meaning |
|---|---|
| `\n` | newline |
| `\t` | horizontal tab |
| `\\` | backslash |
| `\"` | double quote |
| `\'` | single quote |
| `\?` | question mark |
| `\0` | null character (ends a string) |
| `\a` | alert (beep) |
| `\b` | backspace |
| `\f` | form feed |
| `\r` | carriage return (back to the start of the line) |
| `\v` | vertical tab |
| `%%` | (in a `printf` format) a percent sign |

---

## 3. `printf` format specifiers

| Specifier | Prints | Example |
|---|---|---|
| `%d` / `%i` | signed decimal integer | `392` |
| `%u` | unsigned decimal integer | `7235` |
| `%o` | unsigned octal | `610` |
| `%x` / `%X` | unsigned hexadecimal (lower / upper case) | `7fa` / `7FA` |
| `%f` | decimal floating point | `392.650000` |
| `%e` / `%E` | scientific notation | `3.926500e+02` |
| `%g` / `%G` | 6 significant digits; `%f` style, or `%e` style for very large/small numbers; no trailing zeros | `392.65` |
| `%a` / `%A` | hexadecimal floating point | `-0xc.90fep-2` |
| `%c` | a character | `a` |
| `%s` | a string | `sample` |
| `%p` | a pointer (address) | `0061FE1C` |
| `%n` | prints nothing; stores the count of characters printed so far | |
| `%%` | a literal `%` | `%` |

**Shape of a specifier:** `%[flags][width][.precision][length]type`

| Part | Options | Example → result |
|---|---|---|
| flags | `-` left-align · `0` zero-pad · `+` show sign · (space) | `%-5d` → `42···` · `%05d` → `00042` · `%+d` → `+42` |
| width | minimum field width | `%5d` → `···42` |
| precision | digits after `.` (floats) or max characters (strings) | `%.2f` → `3.14` · `%.3s` → `Kum` |
| length | `h` short · `l` long (and `double` in `scanf`) · `ll` long long · `z` size_t | `%ld` · `%lld` · `%lf` · `%zu` |
| `*` | width/precision taken from an argument | `%*d` with `(8, 42)` → `······42` |

---

## 4. `scanf` format specifiers (differences to remember)

| Type | `scanf` | Note |
|---|---|---|
| `int` | `%d` | needs `&x` |
| `unsigned` | `%u` | |
| `long` / `long long` | `%ld` / `%lld` | |
| `float` | `%f` | |
| **`double`** | **`%lf`** | not `%f`! |
| `char` | `" %c"` | the space skips leftover whitespace |
| word | `%s` / `%49s` | no `&`; stops at whitespace |
| line | `%[^\n]` | everything up to the newline (prefer `fgets`) |

`scanf` returns the number of items successfully read.

---

## 5. Operator precedence and associativity

| Level | Operators | Associativity |
|---|---|---|
| 1 (highest) | `()` `[]` `.` `->` postfix `++` `--` | left → right |
| 2 | prefix `++` `--`, unary `+` `-`, `!`, `~`, `(type)`, `*` (dereference), `&` (address-of), `sizeof` | right → left |
| 3 | `*` `/` `%` | left → right |
| 4 | `+` `-` | left → right |
| 5 | `<<` `>>` | left → right |
| 6 | `<` `<=` `>` `>=` | left → right |
| 7 | `==` `!=` | left → right |
| 8 | `&` | left → right |
| 9 | `^` | left → right |
| 10 | `\|` | left → right |
| 11 | `&&` | left → right |
| 12 | `\|\|` | left → right |
| 13 | `?:` | right → left |
| 14 | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `\|=` | right → left |
| 15 (lowest) | `,` | left → right |

---

## 6. Typical limits (`<limits.h>`, 4-byte `int`)

| Constant | Value |
|---|---|
| `CHAR_BIT` | 8 |
| `SCHAR_MIN` / `SCHAR_MAX` | −128 / 127 |
| `UCHAR_MAX` | 255 |
| `SHRT_MIN` / `SHRT_MAX` | −32 768 / 32 767 |
| `USHRT_MAX` | 65 535 |
| `INT_MIN` / `INT_MAX` | −2 147 483 648 / 2 147 483 647 |
| `UINT_MAX` | 4 294 967 295 |
| `LLONG_MIN` / `LLONG_MAX` | −9 223 372 036 854 775 808 / 9 223 372 036 854 775 807 |

(`LONG_MAX` is the same as `INT_MAX` on Windows, but 9 223 372 036 854 775 807 on 64-bit Linux/macOS — **never assume**, use the constants.)

---

## 7. ASCII table (printable characters)

Every character is stored as a number. A few facts worth remembering: `'0'` = 48 · `'A'` = 65 · `'a'` = 97 · a lowercase letter is its uppercase partner **+ 32** · `'\0'` = 0 · `'\n'` = 10 · `' '` = 32.

| Dec | Char | Hex | | Dec | Char | Hex | | Dec | Char | Hex | | Dec | Char | Hex |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 32 | (space) | 20 | | 56 | `8` | 38 | | 80 | `P` | 50 | | 104 | `h` | 68 |
| 33 | `!` | 21 | | 57 | `9` | 39 | | 81 | `Q` | 51 | | 105 | `i` | 69 |
| 34 | `"` | 22 | | 58 | `:` | 3A | | 82 | `R` | 52 | | 106 | `j` | 6A |
| 35 | `#` | 23 | | 59 | `;` | 3B | | 83 | `S` | 53 | | 107 | `k` | 6B |
| 36 | `$` | 24 | | 60 | `<` | 3C | | 84 | `T` | 54 | | 108 | `l` | 6C |
| 37 | `%` | 25 | | 61 | `=` | 3D | | 85 | `U` | 55 | | 109 | `m` | 6D |
| 38 | `&` | 26 | | 62 | `>` | 3E | | 86 | `V` | 56 | | 110 | `n` | 6E |
| 39 | `'` | 27 | | 63 | `?` | 3F | | 87 | `W` | 57 | | 111 | `o` | 6F |
| 40 | `(` | 28 | | 64 | `@` | 40 | | 88 | `X` | 58 | | 112 | `p` | 70 |
| 41 | `)` | 29 | | 65 | `A` | 41 | | 89 | `Y` | 59 | | 113 | `q` | 71 |
| 42 | `*` | 2A | | 66 | `B` | 42 | | 90 | `Z` | 5A | | 114 | `r` | 72 |
| 43 | `+` | 2B | | 67 | `C` | 43 | | 91 | `[` | 5B | | 115 | `s` | 73 |
| 44 | `,` | 2C | | 68 | `D` | 44 | | 92 | `\` | 5C | | 116 | `t` | 74 |
| 45 | `-` | 2D | | 69 | `E` | 45 | | 93 | `]` | 5D | | 117 | `u` | 75 |
| 46 | `.` | 2E | | 70 | `F` | 46 | | 94 | `^` | 5E | | 118 | `v` | 76 |
| 47 | `/` | 2F | | 71 | `G` | 47 | | 95 | `_` | 5F | | 119 | `w` | 77 |
| 48 | `0` | 30 | | 72 | `H` | 48 | | 96 | `` ` `` | 60 | | 120 | `x` | 78 |
| 49 | `1` | 31 | | 73 | `I` | 49 | | 97 | `a` | 61 | | 121 | `y` | 79 |
| 50 | `2` | 32 | | 74 | `J` | 4A | | 98 | `b` | 62 | | 122 | `z` | 7A |
| 51 | `3` | 33 | | 75 | `K` | 4B | | 99 | `c` | 63 | | 123 | `{` | 7B |
| 52 | `4` | 34 | | 76 | `L` | 4C | | 100 | `d` | 64 | | 124 | `\|` | 7C |
| 53 | `5` | 35 | | 77 | `M` | 4D | | 101 | `e` | 65 | | 125 | `}` | 7D |
| 54 | `6` | 36 | | 78 | `N` | 4E | | 102 | `f` | 66 | | 126 | `~` | 7E |
| 55 | `7` | 37 | | 79 | `O` | 4F | | 103 | `g` | 67 | |  |  |  |

Control characters: 0 `\0` (null) · 7 `\a` (bell) · 8 `\b` (backspace) · 9 `\t` (tab) · 10 `\n` (newline) · 13 `\r` (carriage return) · 27 ESC · 127 DEL.

---

## 8. Number systems

| Decimal | Binary | Octal | Hex |
|---|---|---|---|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

Powers of two: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 (= 2¹⁰), 65 536 (= 2¹⁶).

---

## 9. Library functions used in this course

**`<string.h>`**

| Function | Purpose |
|---|---|
| `strlen(s)` | length of a string |
| `strcpy(d, s)` / `strncpy(d, s, n)` | copy |
| `strcat(d, s)` / `strncat(d, s, n)` | append |
| `strcmp(a, b)` / `strncmp(a, b, n)` | compare (0 = equal) |
| `strchr(s, c)` / `strrchr(s, c)` | first / last occurrence of a character |
| `strstr(s, sub)` | first occurrence of a substring |
| `strdup(s)` | allocated copy (free it!) |
| `strcspn(s, set)` | length of the initial part with no character from `set` |
| `memcpy(d, s, n)` / `memset(p, v, n)` | copy / fill raw bytes |

**`<math.h>`:** `sqrt(x)`, `pow(x, y)`, `fabs(x)`, `ceil(x)`, `floor(x)`, `round(x)`, `fmod(x, y)`, `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `log10(x)`, `exp(x)` (angles in radians).

**`<ctype.h>`:** `isalpha`, `isdigit`, `isalnum`, `isspace`, `isupper`, `islower`, `toupper`, `tolower`.

**`<stdlib.h>`:** `malloc`, `calloc`, `realloc`, `free`, `abs`, `rand`, `srand`, `exit`, `atoi`, `atof`, `qsort`.

**`<stdio.h>`:** `printf`, `scanf`, `sprintf`, `snprintf`, `sscanf`, `getchar`, `putchar`, `puts`, `fgets`, `fputs`.
