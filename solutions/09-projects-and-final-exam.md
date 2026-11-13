# Solutions — Chapter 9: Final Exam

> Back to the exam: [lessons/09-projects-and-final-exam.md](../lessons/09-projects-and-final-exam.md)
>
> The four worked projects (Student Manager, Tic-Tac-Toe, Matrix Calculator, Mini Bank) are already fully solved inside the lesson. The **project ideas** are open-ended, so they have no fixed solution.

---

## Section A — Multiple choice (20 marks)

| Q | Answer | Why |
|---|---|---|
| A1 | **(c)** `total_sum` | letters, digits, underscore; not starting with a digit; not a keyword |
| A2 | **(b)** compiled | the whole program is translated to machine code before it runs |
| A3 | **(b)** 3 | integer ÷ integer = integer (the fraction is discarded) |
| A4 | **(b)** 0 | `5 > 3` is 1 but `2 > 4` is 0; `1 && 0` is 0 (and C prints `0`, not "false") |
| A5 | **(c)** 2 | `10 % 4` is the remainder 2 |
| A6 | **(c)** execution continues into the next case | this is "fall-through" |
| A7 | **(c)** `do … while` | its condition is tested *after* the body |
| A8 | **(b)** 3 | `i` takes the values 1, 4, 7 (then 10 fails `i < 10`) |
| A9 | **(b)** `int add(int, int);` | a prototype ends with a semicolon; parameter names are optional |
| A10 | **(c)** keeps its value between calls | initialised once, lives for the whole program |
| A11 | **(b)** the condition that stops the recursion | |
| A12 | **(c)** 0 to 7 | indices run from 0 to size − 1 |
| A13 | **(b)** 10 | 40 bytes ÷ 4 bytes per element |
| A14 | **(b)** row 1, column 2 | `m[row][column]`, counting from 0 |
| A15 | **(b)** the address of another variable | |
| A16 | **(c)** 5 | `*p` is the value `p` points to, i.e. `x` |
| A17 | **(b)** `fgets` | it takes the buffer size, so it can't overflow |
| A18 | **(b)** 5 | `strlen` does not count the `'\0'` |
| A19 | **(c)** `strcmp(a, b) == 0` | `==` compares addresses |
| A20 | **(b)** 3 | `'H'`, `'i'` and `'\0'` |

---

## Section B — Short answers (24 marks · 3 marks each)

*(Each answer is shown as a complete, tested program.)*

**B1.** *(2 marks for the output pair, 1 for a correct explanation.)*
```c
#include <stdio.h>

int main(void)
{
    int i, sum = 0;

    for (i = 1; i <= 10; i++)
    {
        if (i % 3 == 0)
            continue;
        if (i > 8)
            break;
        sum += i;
    }
    printf("%d %d\n", sum, i);
    return 0;
}
```
```output
27 10
```
`continue` skips 3, 6 and 9; the loop adds 1 + 2 + 4 + 5 + 7 + 8 = 27; at `i = 10` the second test `i > 8` triggers `break`, so `i` is still 10 afterwards.

**B2.**
```c
#include <stdio.h>

int g(int n)
{
    if (n == 0)
        return 0;
    return n % 10 + g(n / 10);
}

int main(void)
{
    printf("%d\n", g(2026));
    return 0;
}
```
```output
10
```
`g` returns the **sum of the digits**: 6 + 2 + 0 + 2 = 10.

**B3.** *(1 mark for the output, 1 for "it swaps", 1 for mentioning that it works through the pointers.)*
```c
#include <stdio.h>

void f(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    int x = 4, y = 9;

    f(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```
```output
9 4
```
`f` **swaps** the values of the two variables whose addresses it receives.

**B4.**
```c
#include <stdio.h>

int main(void)
{
    int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int s = 0;

    for (int i = 0; i < 3; i++)
        s += m[i][2 - i];
    printf("%d\n", s);
    return 0;
}
```
```output
15
```
It adds the **secondary diagonal**: `m[0][2] + m[1][1] + m[2][0]` = 3 + 5 + 7.

**B5.**
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[] = "KNUST";

    s[2] = '\0';
    printf("%s %zu %zu\n", s, strlen(s), sizeof(s));
    return 0;
}
```
```output
KN 2 6
```
Putting `'\0'` at index 2 ends the string after `KN` (length 2), but the array is still 6 bytes.

**B6.** *(1 mark for each definition, 1 for a correct example.)* In **pass by value** the function receives a **copy** of the argument, so changes to the parameter do not affect the caller's variable: `void f(int n) { n = 0; }` called as `f(x)` leaves `x` unchanged. In **pass by reference** the caller passes the variable's **address** (`&x`) and the function receives a pointer, so by writing `*p = 0;` it changes the caller's original variable: `void f(int *p) { *p = 0; }` called as `f(&x)` sets `x` to 0.

**B7.** *(1 mark for "string literal is read-only", 1 for "undefined behaviour/crash", 1 for the fix.)* `char *s = "hi";` makes `s` point to a **string literal**, which is stored in read-only memory; assigning to `s[0]` is **undefined behaviour** (usually a crash). The fix is to give the program its **own modifiable copy** in an array: `char s[] = "hi";`.

**B8.**
```c
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = i; j <= 3; j++)
            printf("%d", i * j);
        printf("-");
    }
    printf("\n");
    return 0;
}
```
```output
123-46-9-
```
Row `i = 1`: j = 1, 2, 3 → 1 2 3. Row `i = 2`: j = 2, 3 → 4 6. Row `i = 3`: j = 3 → 9.

---

## Section C — Debugging (10 marks)

**C1.** *(1 mark per mistake found **and** corrected.)*

1. `int average(...)` must return a **`double`** (the average is generally not a whole number).
2. `int sum;` is **uninitialised** → `int sum = 0;`.
3. The loop condition `i <= n` reads `a[n]`, **beyond the array** → `i < n`.
4. `sum / n` is **integer division** → `(double) sum / n`.
5. The call `average(marks)` is **missing the size argument** → `average(marks, 5)`.

Corrected program:
```c
#include <stdio.h>

double average(int a[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i];
    return (double) sum / n;
}

int main(void)
{
    int marks[5] = {60, 70, 80, 90, 100};
    printf("Average = %.2f\n", average(marks, 5));
    return 0;
}
```
```output
Average = 80.00
```

**C2.** *(1 mark per mistake found **and** fixed.)*

1. `char city[5] = "Accra";` — `"Accra"` needs **6** bytes (5 letters + `'\0'`) → `char city[] = "Accra";`.
2. `copy = city;` — **arrays cannot be assigned** → `strcpy(copy, city);`.
3. `city == "Accra"` — compares **addresses**, not text → `strcmp(city, "Accra") == 0`.
4. `int *p; *p = strlen(city);` — `p` is **uninitialised** (points nowhere) → make it point to a variable first: `int len; int *p = &len; *p = (int) strlen(city);` (or just `int len = (int) strlen(city);`).
5. `gets(copy);` — **unsafe** (no size limit; removed from C11) → `fgets(copy, sizeof(copy), stdin);`.

Corrected program:
<!--in: Kumasi-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char city[] = "Accra";
    char copy[10];

    strcpy(copy, city);
    if (strcmp(city, "Accra") == 0)
        printf("same\n");

    int len;
    int *p = &len;
    *p = (int) strlen(city);
    printf("length = %d\n", len);

    fgets(copy, sizeof(copy), stdin);
    printf("you typed: %s", copy);
    return 0;
}
```
```output
same
length = 5
Kumasi
you typed: Kumasi
```

---

## Section D — Programming (46 marks)

### D1 (8 marks)

**Marking scheme:** reading the line **safely** with `fgets` (2) · function loops until `'\0'` (2) · correct vowel test for upper *and* lower case (2) · `main` prints both counts, other = length − vowels (2).

<!--in: Programming in C-->
```c
#include <stdio.h>
#include <string.h>

int countVowels(const char *s)
{
    int count = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        switch (s[i])
        {
            case 'a': case 'e': case 'i': case 'o': case 'u':
            case 'A': case 'E': case 'I': case 'O': case 'U':
                count++;
        }
    }
    return count;
}

int main(void)
{
    char line[200];

    printf("Enter a line of text: ");
    fgets(line, sizeof(line), stdin);
    line[strcspn(line, "\n")] = '\0';             /* remove the final newline */

    int vowels = countVowels(line);
    printf("Vowels: %d\n", vowels);
    printf("Other characters: %d\n", (int) strlen(line) - vowels);
    return 0;
}
```
```output
Enter a line of text: Programming in C
Vowels: 4
Other characters: 12
```

### D2 (10 marks)

**Marking scheme:** reading `n` and the array (2) · `mean` (2) · `countAbove` (2) · `sortDescending` (3) · correct output (1).

<!--in: 6 40 85 62 91 55 78-->
```c
#include <stdio.h>

#define MAX 50

double mean(const int a[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i];
    return (double) sum / n;
}

int countAbove(const int a[], int n, double limit)
{
    int count = 0;
    for (int i = 0; i < n; i++)
        if (a[i] > limit)
            count++;
    return count;
}

void sortDescending(int a[], int n)
{
    for (int pass = 0; pass < n - 1; pass++)
        for (int j = 0; j < n - 1 - pass; j++)
            if (a[j] < a[j + 1])
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
}

int main(void)
{
    int a[MAX], n;

    printf("How many numbers (max %d)? ", MAX);
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    double m = mean(a, n);
    printf("Mean = %.2f\n", m);
    printf("Numbers above the mean: %d\n", countAbove(a, n, m));

    sortDescending(a, n);
    printf("Sorted: ");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
How many numbers (max 50)? 6 40 85 62 91 55 78
Mean = 68.50
Numbers above the mean: 3
Sorted: 91 85 78 62 55 40
```

### D3 (12 marks)

**Marking scheme:** parallel arrays for names/prices and a counter (2) · menu loop with `switch` and a sensible exit (3) · `addItem` with the two validations and the counter passed **by pointer** (3) · `listItems` (2) · `totalPrice` (2).

<!--in: 1 Rice 12.50\n1 Sugar 9.00\n1 Gari -3\n2\n3\n4-->
```c
#include <stdio.h>

#define MAX_ITEMS 10
#define NAME_LEN 30

void addItem(char names[][NAME_LEN], double prices[], int *count)
{
    char name[NAME_LEN];
    double price;

    scanf("%29s %lf", name, &price);

    if (*count == MAX_ITEMS)
    {
        printf("The list is full.\n");
        return;
    }
    if (price <= 0)
    {
        printf("The price must be positive.\n");
        return;
    }

    snprintf(names[*count], NAME_LEN, "%s", name);
    prices[*count] = price;
    (*count)++;
    printf("Item added.\n");
}

void listItems(char names[][NAME_LEN], const double prices[], int count)
{
    printf("\n%-4s %-15s %10s\n", "No.", "Item", "Price");
    for (int i = 0; i < count; i++)
        printf("%-4d %-15s %10.2f\n", i + 1, names[i], prices[i]);
}

double totalPrice(const double prices[], int count)
{
    double total = 0;
    for (int i = 0; i < count; i++)
        total += prices[i];
    return total;
}

int main(void)
{
    char names[MAX_ITEMS][NAME_LEN];
    double prices[MAX_ITEMS];
    int count = 0;
    int choice;

    do
    {
        printf("\n1) Add item  2) List items  3) Total price  4) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1: addItem(names, prices, &count); break;
            case 2: listItems(names, prices, count); break;
            case 3: printf("Total: GHS %.2f\n", totalPrice(prices, count)); break;
            case 4: printf("Goodbye!\n"); break;
            default: printf("Invalid choice.\n");
        }
    }
    while (choice != 4);

    return 0;
}
```
```output
1) Add item  2) List items  3) Total price  4) Exit
Choose: 1 Rice 12.50
Item added.

1) Add item  2) List items  3) Total price  4) Exit
Choose: 1 Sugar 9.00
Item added.

1) Add item  2) List items  3) Total price  4) Exit
Choose: 1 Gari -3
The price must be positive.

1) Add item  2) List items  3) Total price  4) Exit
Choose: 2

No.  Item                 Price
1    Rice                 12.50
2    Sugar                 9.00

1) Add item  2) List items  3) Total price  4) Exit
Choose: 3
Total: GHS 21.50

1) Add item  2) List items  3) Total price  4) Exit
Choose: 4
Goodbye!
```

### D4 (16 marks)

**Marking scheme**
- (a) `transpose` **in place** (4): loops over the **upper triangle only** (`j > i`) (2) and swaps `m[i][j]` with `m[j][i]` using a temporary (2). *(Swapping over the whole matrix would transpose it twice and change nothing — a common mistake, 0 for the logic.)*
- (b) `isSymmetric` (3): double loop (1), correct comparison (1), returns 0 as soon as a mismatch is found / 1 at the end (1).
- (c) `traceAndMax` (4): pointer parameters dereferenced correctly (2); trace over the diagonal (1); maximum over all elements (1).
- (d) recursive `gcd` (3): base case (1), recursive call `gcd(b, a % b)` (1), returns the result (1).
- (e) `main` (2): calls all four with sample data and prints.

```c
#include <stdio.h>

void printMatrix(int m[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
            printf("%3d", m[i][j]);
        printf("\n");
    }
}

void transpose(int m[3][3])
{
    for (int i = 0; i < 3; i++)
        for (int j = i + 1; j < 3; j++)          /* only above the diagonal */
        {
            int t = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = t;
        }
}

int isSymmetric(int m[3][3])
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (m[i][j] != m[j][i])
                return 0;
    return 1;
}

void traceAndMax(int m[3][3], int *trace, int *max)
{
    *trace = 0;
    *max = m[0][0];
    for (int i = 0; i < 3; i++)
    {
        *trace += m[i][i];
        for (int j = 0; j < 3; j++)
            if (m[i][j] > *max)
                *max = m[i][j];
    }
}

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main(void)
{
    int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int s[3][3] = { {1, 2, 3}, {2, 5, 6}, {3, 6, 9} };
    int trace, max;

    printf("m symmetric? %d\n", isSymmetric(m));
    printf("s symmetric? %d\n", isSymmetric(s));

    traceAndMax(m, &trace, &max);
    printf("trace = %d, max = %d\n", trace, max);

    transpose(m);
    printf("transpose of m:\n");
    printMatrix(m);

    printf("gcd(48, 18) = %d\n", gcd(48, 18));
    return 0;
}
```
```output
m symmetric? 0
s symmetric? 1
trace = 15, max = 9
transpose of m:
  1  4  7
  2  5  8
  3  6  9
gcd(48, 18) = 6
```

---

## Total and grading guide

| Section | Marks |
|---|---|
| A — Multiple choice | 20 |
| B — Short answers | 24 |
| C — Debugging | 10 |
| D — Programming | 46 |
| **Total** | **100** |

| Score | Meaning |
|---|---|
| 80–100 | Excellent — you have mastered the course. Start the project ideas! |
| 70–79 | Very good — review the sections where you lost marks. |
| 60–69 | Good — redo the exercises of the weakest chapters. |
| 50–59 | Pass — you know the basics; practise loops, arrays and pointers more. |
| below 50 | Go back through Chapters 5–8 slowly, **writing every program yourself**. Then retake the exam. |

> **A final word from your professor.** Nobody learns programming by reading. You learn it by **typing programs, breaking them, and fixing them**. If you do only one thing after this course: every day, write one small program from scratch. In a month you will not recognise yourself.

---

*Back to the course index: [README](../README.md)*
