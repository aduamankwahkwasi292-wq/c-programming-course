# Chapter 7 — Arrays

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Based on slides:** `07 Arrays.pdf`  
> **Solutions:** [Solutions to Chapter 7](../solutions/07-arrays.md)

---

## What you will learn

1. What an **array** is and how to **declare** and **initialise** one.
2. How **indexing** works (it starts at **0**!).
3. How to **traverse** an array with a `for` loop.
4. The classic array algorithms: sum, maximum, search, reverse, sort…
5. How to **pass arrays to functions**.
6. **Multi-dimensional arrays** (tables and cubes): 2D and 3D.

---

## 7.1 Why do we need arrays?

Suppose you must store the marks of 60 students. Do you declare 60 variables — `mark1`, `mark2`, … `mark60`? And how would you add them up? You'd need 60 separate additions!

An **array** solves this. It is a **data structure** (Chapter 0) that stores a **fixed-size, sequential collection of elements of the same data type** under **one name**.

> 💡 **Analogy.** A row of numbered lockers in a school corridor. The whole row has one name ("the lockers"); each locker has a **number** (its *index*) and holds one item. To use locker 7, you just say *"locker 7"*.

```
   marks   ┌────┬────┬────┬────┬────┐
           │ 78 │ 85 │ 91 │ 60 │ 73 │      one name: marks
           └────┴────┴────┴────┴────┘      five boxes, side by side in memory
  index      0    1    2    3    4
```

In C, arrays can be **1-dimensional** (a list), **2-dimensional** (a table with rows and columns) or **3-dimensional** (a stack of tables).

---

## 7.2 Declaring an array

```c
datatype arrayName[size];
```

- `datatype` — the type of **every** element (`int`, `double`, `char`…).
- `size` — how many elements. It must be an **integer constant greater than zero**.

```c
int months[12];          // room for 12 integers
double prices[5];        // room for 5 decimals
char letters[26];        // room for 26 characters
```

Use a named constant for the size, so you can change it in one place:

```c
#define SIZE 5
int marks[SIZE];
```

The elements sit **next to each other** in memory. An `int` array of 5 elements takes `5 × 4 = 20` bytes.

---

## 7.3 Indexing — counting starts at 0

Each element is reached by its **index** (a position number) inside square brackets: `arrayName[index]`.

> 🔑 **The first element has index `0`. The last element of an array of size `n` has index `n − 1`.**

```
   int a[5]:     a[0]  a[1]  a[2]  a[3]  a[4]
                  ▲                       ▲
              first element          last element (size − 1)
```

**Careful with the two different meanings of the brackets** (your slide stresses this):

```c
int myArray[5];     // here 5 is the SIZE — it is part of a declaration
myArray[4] = 9;     // here 4 is an INDEX — it picks one element
```

When a name is written **without** a data type in front, the number inside the brackets is an **index**, not a size.

You can use an element like any variable:

```c
a[2] = 40;                     // store
int x = a[2] + 1;              // read
a[i] = a[i - 1] + a[i - 2];    // the index can be any integer expression
```

> ⚠️ **C does NOT check the index!** If you write `a[5]` for a 5-element array, the compiler usually says nothing, and the program touches memory that is **not yours** — it may crash, silently corrupt another variable, or "seem to work". This is the **#1 array bug**. It is called an **out-of-bounds** access (or buffer overflow). *You* must keep the index between `0` and `size − 1`.

---

## 7.4 Initialising an array

To **initialise** an array is to fill it with values. There are two ways (from your slide): **at declaration** and **with a loop**.

### Way 1 — values at declaration

```c
int age[4] = {28, 29, 40, 38};
float size[5] = {56.3, 61.5, 29.3, 60.7, 45.2};
```

```
   age     ┌────┬────┬────┬────┐
           │ 28 │ 29 │ 40 │ 38 │
           └────┴────┴────┴────┘
  indices    0    1    2    3
```

Useful variations:

```c
#include <stdio.h>

int main(void)
{
    int a[6] = {7, 8};                  /* fewer values: the rest become 0 */
    int zeros[4] = {0};                 /* a quick way to fill with zeros  */
    int b[] = {4, 8, 15, 16, 23, 42};   /* size left out: the compiler counts -> 6 */

    for (int i = 0; i < 6; i++)
        printf("%d ", a[i]);
    printf("\n");

    for (int i = 0; i < 4; i++)
        printf("%d ", zeros[i]);
    printf("\n");

    printf("b has %zu elements\n", sizeof(b) / sizeof(b[0]));
    return 0;
}
```
```output
7 8 0 0 0 0
0 0 0 0
b has 6 elements
```

> ⚠️ **Uninitialised local arrays contain garbage** (whatever was in memory before) — just like uninitialised variables. And giving **more** values than the size (`int a[3] = {1,2,3,4};`) is not allowed: some compilers refuse it, and GCC warns `excess elements in array initializer` and throws the extra values away.

### Way 2 — with a loop

```c
int myArray[5];
int n = 0;
for (n = 0; n < sizeof(myArray) / sizeof(myArray[0]); n++)
{
    myArray[n] = n;
}
```

### The `sizeof` trick — finding the array length

`sizeof` (Chapter 3) gives the size in **bytes**. For the array `int myArray[5]`:

- `sizeof(myArray)` → `20` bytes (5 integers × 4 bytes)
- `sizeof(myArray[0])` → `4` bytes (one integer)
- **length** = `sizeof(myArray) / sizeof(myArray[0])` = `20 / 4` = **5**

This way the loop adapts automatically if you change the size.

```
At declaration:           After initialisation:

   0    1    2    3    4        0    1    2    3    4
 ┌────┬────┬────┬────┬────┐   ┌────┬────┬────┬────┬────┐
 │ ?  │ ?  │ ?  │ ?  │ ?  │   │ 0  │ 1  │ 2  │ 3  │ 4  │
 └────┴────┴────┴────┴────┘   └────┴────┴────┴────┴────┘
```

Putting it together (printing while initialising — from your slide):

```c
#include <stdio.h>

int main(void)
{
    int myArray[5];
    int n = 0;

    for (n = 0; n < sizeof(myArray) / sizeof(myArray[0]); n++)
    {
        myArray[n] = n;
        printf("%d\t", myArray[n]);
    }
    return 0;
}
```
```output
0       1       2       3       4
```

### Changing one element

```c
myArray[0] = 5;
myArray[1] = 6;
myArray[2] = 7;
myArray[3] = 8;
myArray[4] = 9;
```

```
After initialisation:   0  1  2  3  4
After values change:    5  6  7  8  9
```

> ⚠️ `sizeof(array) / sizeof(array[0])` works **only in the same function where the array was declared**. Inside a function that *received* the array as a parameter it does **not** work (section 7.7).

---

## 7.5 Traversing an array

**Traversing** means visiting every element, one by one. The tool is the `for` loop (Chapter 5), with the standard pattern:

```c
for (i = 0; i < n; i++)          /* i = 0, 1, ..., n-1 */
{
    /* use a[i] */
}
```

> 💡 Use `i < n`, **never `i <= n`** — `a[n]` is one past the end!

### Reading values from the user, and printing them

<!--in: 70 85 91 60 73-->
```c
#include <stdio.h>

#define SIZE 5

int main(void)
{
    int marks[SIZE];

    printf("Enter %d marks: ", SIZE);
    for (int i = 0; i < SIZE; i++)
        scanf("%d", &marks[i]);              /* note the & before each element */

    printf("You entered: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", marks[i]);
    printf("\n");
    return 0;
}
```
```output
Enter 5 marks: 70 85 91 60 73
You entered: 70 85 91 60 73
```

### Classic task 1 — sum and average

```c
#include <stdio.h>

int main(void)
{
    int a[] = {70, 85, 91, 60, 73};
    int n = sizeof(a) / sizeof(a[0]);
    int sum = 0;

    for (int i = 0; i < n; i++)
        sum += a[i];

    printf("Sum = %d, average = %.2f\n", sum, (double) sum / n);
    return 0;
}
```
```output
Sum = 379, average = 75.80
```

### Classic task 2 — largest and smallest (and where they are)

Start with the **first** element as the best so far, then compare the rest:

```c
#include <stdio.h>

int main(void)
{
    int a[] = {12, -5, 40, 7, 0, 33};
    int n = sizeof(a) / sizeof(a[0]);
    int max = a[0], min = a[0], maxIndex = 0;

    for (int i = 1; i < n; i++)
    {
        if (a[i] > max)
        {
            max = a[i];
            maxIndex = i;
        }
        if (a[i] < min)
            min = a[i];
    }

    printf("max = %d at index %d, min = %d\n", max, maxIndex, min);
    return 0;
}
```
```output
max = 40 at index 2, min = -5
```

### Classic task 3 — linear search

Look at each element until you find the key:

<!--in: 7-->
```c
#include <stdio.h>

int main(void)
{
    int a[] = {4, 9, 7, 1, 8};
    int n = sizeof(a) / sizeof(a[0]);
    int key, found = -1;

    printf("Search for: ");
    scanf("%d", &key);

    for (int i = 0; i < n; i++)
    {
        if (a[i] == key)
        {
            found = i;
            break;                     /* stop at the first match */
        }
    }

    if (found >= 0)
        printf("%d found at index %d\n", key, found);
    else
        printf("%d not found\n", key);
    return 0;
}
```
```output
Search for: 7
7 found at index 2
```

### Classic task 4 — reverse an array in place

Swap the first with the last, the second with the second-last… and stop at the middle:

```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
5 4 3 2 1
```

### Classic task 5 — counting with an array (frequency)

Use the *values* as **indices** into a counting array. Count how often each digit appears in a list of digits:

```c
#include <stdio.h>

int main(void)
{
    int digits[] = {1, 3, 2, 3, 3, 1, 0, 9, 3};
    int n = sizeof(digits) / sizeof(digits[0]);
    int count[10] = {0};                      /* count[d] = how many times d appears */

    for (int i = 0; i < n; i++)
        count[digits[i]]++;

    for (int d = 0; d < 10; d++)
        if (count[d] > 0)
            printf("digit %d appears %d time(s)\n", d, count[d]);
    return 0;
}
```
```output
digit 0 appears 1 time(s)
digit 1 appears 2 time(s)
digit 2 appears 1 time(s)
digit 3 appears 4 time(s)
digit 9 appears 1 time(s)
```

### Classic task 6 — sorting (bubble sort)

**Bubble sort**: sweep through the array repeatedly, swapping neighbours that are in the wrong order. After each full sweep the largest remaining value has "bubbled" to its final place at the end.

```
 start:       5  1  4  2  8
 sweep 1:     1  4  2  5  8      (the 8 is already in place)
 sweep 2:     1  2  4  5  8      (the 5 is in place)
 sweep 3:     1  2  4  5  8      (nothing swapped: done)
```

```c
#include <stdio.h>

int main(void)
{
    int a[] = {5, 1, 4, 2, 8};
    int n = sizeof(a) / sizeof(a[0]);

    for (int pass = 0; pass < n - 1; pass++)
    {
        for (int j = 0; j < n - 1 - pass; j++)     /* the last 'pass' elements are already sorted */
        {
            if (a[j] > a[j + 1])
            {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
1 2 4 5 8
```

### Classic task 7 — binary search (on a *sorted* array)

If the array is sorted, you can do far better than linear search: look at the **middle** element and throw away half the array each time (Chapter 0, Ex 0.32).

```c
#include <stdio.h>

int main(void)
{
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(a) / sizeof(a[0]);
    int key = 23, low = 0, high = n - 1, found = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (a[mid] == key)
        {
            found = mid;
            break;
        }
        else if (a[mid] < key)
            low = mid + 1;               /* key must be in the right half */
        else
            high = mid - 1;              /* key must be in the left half  */
    }

    printf("index = %d\n", found);
    return 0;
}
```
```output
index = 5
```

A list of 1 000 000 items needs at most 20 steps this way (linear search: up to a million).

### Classic task 8 — inserting and deleting (shifting)

An array has a fixed size, so to **insert** you must first **shift** the later elements one place right; to **delete**, shift them left.

```c
#include <stdio.h>

int main(void)
{
    int a[10] = {10, 20, 30, 40, 50};
    int n = 5;                                 /* number of elements actually used */
    int pos = 2, value = 25;

    for (int i = n; i > pos; i--)              /* shift right, starting from the END */
        a[i] = a[i - 1];
    a[pos] = value;
    n++;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");

    pos = 0;                                   /* now delete the element at index 0 */
    for (int i = pos; i < n - 1; i++)          /* shift left, starting from the FRONT */
        a[i] = a[i + 1];
    n--;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
10 20 25 30 40 50
20 25 30 40 50
```

Remember: the array's *size* (10) never changes. We keep a separate variable `n` for **how many slots are in use**.

---

## 7.6 Things you cannot do with whole arrays

An array name stands for the *whole block*, and C has few operations for that:

| You can't write… | Do this instead |
|---|---|
| `b = a;` (copy an array) | copy **element by element** with a loop |
| `if (a == b)` (compare arrays) | compare element by element with a loop |
| `printf("%d", a);` (print an array) | loop and print each element |
| `scanf("%d", a);` (read an array) | loop and read each element |

(`a == b` *does* compile, but it compares the **addresses** of the two arrays, not their contents — almost never what you want.)

---

## 7.7 Arrays and functions

A function can **receive an array** as a parameter. Write the array parameter with **empty brackets** and pass the **size separately**:

```c
void printArray(int arr[], int n);       /* prototype */
```

```c
#include <stdio.h>

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int sumArray(int arr[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr[i];
    return sum;
}

int main(void)
{
    int a[] = {4, 8, 15, 16, 23, 42};
    int n = sizeof(a) / sizeof(a[0]);

    printArray(a, n);
    printf("sum = %d\n", sumArray(a, n));
    return 0;
}
```
```output
4 8 15 16 23 42
sum = 108
```

### The surprise: the function CAN change the original array

Remember "pass by value" from Chapter 6: ordinary variables are *copied*. **Arrays are different.** When you pass an array, C does **not** copy all its elements; it passes the **address of the first element** (the array "decays" to a pointer — Chapter 8 explains). So the function works on the **original** array:

```c
#include <stdio.h>

void addTen(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        arr[i] += 10;                    /* changes the ORIGINAL array */
}

void change(int x)
{
    x = 99;                              /* changes only a copy */
}

int main(void)
{
    int a[3] = {1, 2, 3};

    addTen(a, 3);
    printf("%d %d %d\n", a[0], a[1], a[2]);

    change(a[1]);                        /* a single element IS passed by value */
    printf("%d %d %d\n", a[0], a[1], a[2]);
    return 0;
}
```
```output
11 12 13
11 12 13
```

- Whole array → the function can modify the original.
- A single element (`a[1]`) → just a copy of its value, like any variable.

If a function should **only read** the array, say so with `const` — the compiler will then stop accidental changes:

```c
int sumArray(const int arr[], int n);
```

### The `sizeof` trap

Inside `printArray`, `sizeof(arr) / sizeof(arr[0])` does **not** give the number of elements — `arr` is really just an address there, so `sizeof(arr)` is the size of an address (4 or 8 bytes). **Always pass the size as an extra parameter** (`int n`).

### Functions cannot return arrays

A function cannot return a whole array. Instead, the **caller** creates the array and passes it in for the function to **fill**:

```c
void fillSquares(int arr[], int n)       /* fills arr[i] with i*i */
{
    for (int i = 0; i < n; i++)
        arr[i] = i * i;
}
```

---

## 7.8 Multi-dimensional arrays

A **multi-dimensional array** is an **array of arrays**. A 2D array stores data in **tabular form** — rows and columns. A 3D array is a stack of such tables.

```
  Array_name   col 0   col 1   ...   col N
   row 0      [ ]     [ ]     ...   [ ]
   row 1      [ ]     [ ]     ...   [ ]
   ...
   row N      [ ]     [ ]     ...   [ ]
```

The general form for an **N-dimensional** array:

```c
datatype arrayName[size1][size2]...[sizeN];
```

```c
int myTwoD[2][3];          // two-dimensional:   2 rows, 3 columns
int myThreeD[2][3][4];     // three-dimensional: 2 tables, each 3 rows x 4 columns
```

**Total size = the product of all the dimensions:**

- `int myArray[2][3]` stores `2 × 3 = 6` elements.
- `int thatArray[5][6][3]` stores `5 × 6 × 3 = 90` elements.

---

## 7.9 Two-dimensional arrays

```c
datatype arrayName[x][y];
```

An element is written `arrayName[i][j]` where **`i` is the row number** and **`j` is the column number** (rows first!). Both start at 0.

For `int myArray[3][3];`:

```
              Column 0        Column 1        Column 2
   Row 0     myArray[0][0]   myArray[0][1]   myArray[0][2]
   Row 1     myArray[1][0]   myArray[1][1]   myArray[1][2]
   Row 2     myArray[2][0]   myArray[2][1]   myArray[2][2]
```

### Initialising a 2D array

**Method 1 — one flat list.** The values fill the array **row by row**:

```c
int myArray[3][4] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
```

**Method 2 — one brace group per row** (easier to read — and recommended):

```c
int myArray[3][4] = { {0, 1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10, 11} };
```

> 📝 **Note on the slide.** The slide shows Method 2 without the **outer** braces. The correct form has braces around the whole thing *and* around each row, as above.

Both give the same table:

```
              Column 0  Column 1  Column 2  Column 3
   Row 0         0         1         2         3
   Row 1         4         5         6         7
   Row 2         8         9        10        11
```

Missing values are filled with 0, and the **first** dimension may be left out when you initialise: `int m[][3] = {{1,2,3},{4,5,6}};` makes a 2×3 array.

### Accessing elements

`myArray[2][1]` means *row 2, column 1* — which is **`9`**.

> ⚠️ Your slide says `myArray[2][1]` refers to "the element 8". Look at the table above: row 2 is `8 9 10 11`, and column 1 is the second number, so it is **9**. (Element `8` is `myArray[2][0]`.) A good reminder to *always trace by hand*!

### Traversing a 2D array — nested `for` loops

The **outer** loop goes through the **rows**; the **inner** loop goes through the **columns** of that row.

```c
#include <stdio.h>

int main(void)
{
    int myArray[3][4];
    int i, j, size = -1;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            myArray[i][j] = ++size;
            printf("Element at myArray[%d][%d] is %d\n", i, j, myArray[i][j]);
        }
    }
    return 0;
}
```
```output
Element at myArray[0][0] is 0
Element at myArray[0][1] is 1
Element at myArray[0][2] is 2
Element at myArray[0][3] is 3
Element at myArray[1][0] is 4
Element at myArray[1][1] is 5
Element at myArray[1][2] is 6
Element at myArray[1][3] is 7
Element at myArray[2][0] is 8
Element at myArray[2][1] is 9
Element at myArray[2][2] is 10
Element at myArray[2][3] is 11
```

(`++size` increases `size` first, then uses it — prefix, Chapter 3 — so the values are 0, 1, 2, …)

To print it as a **table**, add a `printf("\n")` at the end of each row — take note of the **nested for loops**:

```c
#include <stdio.h>

int main(void)
{
    int myArray[3][4];
    int i, j, size = -1;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            myArray[i][j] = ++size;
            printf("%d\t", myArray[i][j]);
        }
        printf("\n");                        /* new line after each row */
    }
    return 0;
}
```
```output
0       1       2       3
4       5       6       7
8       9       10      11
```

### How a 2D array sits in memory

Memory is one long line, so C stores a 2D array **row after row** ("row-major order"): `0 1 2 3 | 4 5 6 7 | 8 9 10 11`. This is why the **column count** matters to the compiler when you pass a 2D array to a function.

### 2D arrays and functions

When you pass a 2D array, you must give **all dimensions except the first**:

```c
void printMatrix(int m[][3], int rows)        /* the column count (3) is required */
```

```c
#include <stdio.h>

#define COLS 3

void printMatrix(int m[][COLS], int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < COLS; j++)
            printf("%4d", m[i][j]);
        printf("\n");
    }
}

int main(void)
{
    int a[2][COLS] = { {1, 2, 3}, {4, 5, 6} };

    printMatrix(a, 2);
    return 0;
}
```
```output
   1   2   3
   4   5   6
```

### Classic 2D tasks

**Row sums and column sums:**

```c
#include <stdio.h>

int main(void)
{
    int m[2][3] = { {1, 2, 3}, {4, 5, 6} };

    for (int i = 0; i < 2; i++)                 /* sum of each row */
    {
        int rowSum = 0;
        for (int j = 0; j < 3; j++)
            rowSum += m[i][j];
        printf("row %d sum = %d\n", i, rowSum);
    }

    for (int j = 0; j < 3; j++)                 /* sum of each column */
    {
        int colSum = 0;
        for (int i = 0; i < 2; i++)
            colSum += m[i][j];
        printf("column %d sum = %d\n", j, colSum);
    }
    return 0;
}
```
```output
row 0 sum = 6
row 1 sum = 15
column 0 sum = 5
column 1 sum = 7
column 2 sum = 9
```

**Transpose** (rows become columns): `t[j][i] = m[i][j]`.

```c
#include <stdio.h>

int main(void)
{
    int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
    int t[3][2];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 3; j++)
            t[j][i] = m[i][j];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
            printf("%d ", t[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
1 4
2 5
3 6
```

**Matrix multiplication:** `c[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j] + …` — "row of A times column of B".

```c
#include <stdio.h>

int main(void)
{
    int a[2][3] = { {1, 2, 3}, {4, 5, 6} };
    int b[3][2] = { {7, 8}, {9, 10}, {11, 12} };
    int c[2][2];

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            c[i][j] = 0;
            for (int k = 0; k < 3; k++)
                c[i][j] += a[i][k] * b[k][j];
        }
    }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
            printf("%4d", c[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
  58  64
 139 154
```

(Check `c[0][0]`: `1×7 + 2×9 + 3×11 = 7 + 18 + 33 = 58` ✔.)

---

## 7.10 Three-dimensional arrays (assignment from your slides)

A 3D array is a **stack of 2D tables**. Think of a book: the first index is the **page**, the second the **row** on that page, the third the **column**.

```c
int cube[2][3][4];       /* 2 pages, each with 3 rows and 4 columns = 24 elements */
```

Access with three indices — `cube[page][row][col]` — and traverse with **three nested loops**:

```c
#include <stdio.h>

int main(void)
{
    int cube[2][3][4];
    int count = 1;

    for (int p = 0; p < 2; p++)
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 4; c++)
                cube[p][r][c] = count++;

    for (int p = 0; p < 2; p++)
    {
        printf("Page %d:\n", p);
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 4; c++)
                printf("%3d", cube[p][r][c]);
            printf("\n");
        }
    }
    printf("cube[1][2][3] = %d\n", cube[1][2][3]);
    return 0;
}
```
```output
Page 0:
  1  2  3  4
  5  6  7  8
  9 10 11 12
Page 1:
 13 14 15 16
 17 18 19 20
 21 22 23 24
cube[1][2][3] = 24
```

Initialising with braces nests one level deeper:

```c
int c[2][2][2] = { { {1, 2}, {3, 4} },
                   { {5, 6}, {7, 8} } };
```

**Real example:** `temp[city][day][reading]` — 3 cities × 7 days × 4 readings per day.

---

## 7.11 Common array mistakes

| Mistake | Result |
|---|---|
| Index `= size` (e.g. `a[5]` in a 5-element array) | out-of-bounds: crash or silent corruption |
| `for (i = 0; i <= n; i++)` | off by one → touches `a[n]` |
| Forgetting to initialise (`count[10]` without `= {0}`) | garbage in the counters |
| Size is a variable | not allowed in standard C89 (VLAs exist in C99, but avoid them) |
| `b = a;` or `a == b` | doesn't copy / compare contents |
| `sizeof(arr)` inside a function | gives the size of an address, not the array |
| Swapping row and column (`m[j][i]`) | wrong element, or out-of-bounds if not square |
| `scanf("%d", a[i])` | missing `&` |
| Dividing by the array's size when fewer values were entered | wrong average |

---

## Key takeaways

- An **array** holds a fixed number of values of the **same type** under one name.
- Declare: `type name[size];` — `size` is a **constant**. Index from **0** to **size − 1**.
- **C does not check the index.** Out-of-bounds access is a serious bug.
- Initialise with `{...}` (missing values become 0) or with a loop. `sizeof(a)/sizeof(a[0])` gives the length.
- Use `for (i = 0; i < n; i++)` to traverse. Typical algorithms: sum, max/min, search, reverse, count, sort.
- You cannot copy or compare whole arrays with `=` / `==` — use loops.
- Pass an array to a function with `type name[]` **and** its size; the function works on the **original** array.
- **2D arrays:** `type name[rows][cols]`; `m[i][j]` = row `i`, column `j`; nested loops; stored row after row.
- **3D arrays:** `type name[pages][rows][cols]`; three nested loops.
- Total size = product of the dimensions.

---

# Exercises — Chapter 7

## Part A — Quick check

**Ex 7.1** What is an array? Why is it better to use an array than 60 separate variables for 60 marks?

**Ex 7.2** Declare: (a) an array `marks` of 10 integers; (b) an array `prices` of 5 doubles; (c) an array `letters` of 26 characters.

**Ex 7.3** What is the index of the first element of an array? What is the index of the last element of `int a[8]`?

**Ex 7.4** What happens if you access `a[8]` when `int a[8]`? Does the compiler stop you?

**Ex 7.5** What values do these arrays hold? (a) `int a[5] = {1, 2};` (b) `int b[3] = {0};` (c) `int c[4];` declared inside `main` with no initialiser.

**Ex 7.6** What does `sizeof(arr) / sizeof(arr[0])` compute? Why is it better than writing the size by hand in every loop?

**Ex 7.7** How many elements can `int t[4][5]` hold? How many does `float x[3][4][2]` hold? How many bytes does `int t[4][5]` occupy if an `int` is 4 bytes?

**Ex 7.8** In `m[i][j]`, which index is the row and which is the column?

**Ex 7.9** Can you copy an array with `b = a;`? Can you compare two arrays with `==`? What should you do instead?

**Ex 7.10** When an array is passed to a function, can the function change the original elements? What extra piece of information should you also pass?

**Ex 7.11** Draw `int m[2][3] = { {1, 2, 3}, {4, 5, 6} };` as a table. What is `m[1][2]`? What is `m[0][1]`?

**Ex 7.12** In `int x[5];` and in `x[4] = 9;` what does the `5` mean and what does the `4` mean?

**Ex 7.13** Why is the standard loop for an array of `n` elements `for (i = 0; i < n; i++)` and not `i <= n`?

**Ex 7.14** True or false?
1. The elements of an array may have different types.
2. The first element is `a[1]`.
3. An array of size `n` has a last index of `n − 1`.
4. `int a[5] = {1, 2, 3, 4, 5, 6};` is valid.
5. The size of a multidimensional array is the product of its dimensions.
6. In a 2D array `m[3][4]`, `m[3][0]` is a valid element.

## Part B — Predict the output

*(Assume `<stdio.h>` is included and the code is inside `main`. Trace on paper.)*

**Ex 7.15**
```c
int a[5] = {10, 20, 30, 40, 50};
printf("%d %d %d\n", a[0], a[2], a[4]);
```

**Ex 7.16**
```c
int a[4] = {1, 2, 3, 4};
a[1] = a[0] + a[3];
a[3]++;
for (int i = 0; i < 4; i++)
    printf("%d ", a[i]);
```

**Ex 7.17**
```c
int a[6] = {7, 8};
for (int i = 0; i < 6; i++)
    printf("%d ", a[i]);
```

**Ex 7.18**
```c
double d[10];
int n[7];
char c[12];
printf("%zu %zu %zu\n", sizeof(d), sizeof(n), sizeof(c) / sizeof(c[0]));
```
*(Assume `double` = 8 bytes and `int` = 4 bytes.)*

**Ex 7.19**
```c
int a[] = {3, 8, 1, 9, 5};
int sum = 0;
for (int i = 0; i < 5; i += 2)
    sum += a[i];
printf("%d\n", sum);
```

**Ex 7.20**
```c
int a[5] = {4, 0, 3, 1, 2};
printf("%d %d %d\n", a[a[0]], a[a[1]], a[a[a[2]]]);
```

**Ex 7.21**
```c
int a[6] = {4, 9, 2, 7, 5, 1};
int max = a[0], idx = 0;
for (int i = 1; i < 6; i++)
    if (a[i] > max)
    {
        max = a[i];
        idx = i;
    }
printf("%d %d\n", max, idx);
```

**Ex 7.22**
```c
int a[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 4; i++)
    a[i] = a[i + 1];
for (int i = 0; i < 5; i++)
    printf("%d ", a[i]);
```

**Ex 7.23**
```c
int a[5] = {1, 2, 3, 4, 5};
for (int i = 0, j = 4; i < j; i++, j--)
{
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
}
for (int i = 0; i < 5; i++)
    printf("%d ", a[i]);
```

**Ex 7.24**
```c
#include <stdio.h>
void bump(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        arr[i] += 10;
}
int main(void)
{
    int a[3] = {1, 2, 3};
    bump(a, 3);
    printf("%d %d %d\n", a[0], a[1], a[2]);
    return 0;
}
```

**Ex 7.25**
```c
#include <stdio.h>
void change(int x)
{
    x = 99;
}
int main(void)
{
    int a[3] = {1, 2, 3};
    change(a[1]);
    printf("%d %d %d\n", a[0], a[1], a[2]);
    return 0;
}
```

**Ex 7.26**
```c
int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
printf("%d %d %d\n", m[0][2], m[1][0], m[1][2]);
```

**Ex 7.27**
```c
int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
for (int i = 0; i < 2; i++)
{
    int s = 0;
    for (int j = 0; j < 3; j++)
        s += m[i][j];
    printf("%d ", s);
}
```

**Ex 7.28**
```c
int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
for (int j = 0; j < 3; j++)
    for (int i = 0; i < 2; i++)
        printf("%d ", m[i][j]);
```

**Ex 7.29**
```c
int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
for (int i = 0; i < 3; i++)
    printf("%d ", m[i][i]);
printf("\n");
for (int i = 0; i < 3; i++)
    printf("%d ", m[i][2 - i]);
```

**Ex 7.30**
```c
int m[2][3] = { {1}, {4, 5} };
for (int i = 0; i < 2; i++)
{
    for (int j = 0; j < 3; j++)
        printf("%d ", m[i][j]);
    printf("\n");
}
```

**Ex 7.31**
```c
int m[2][3] = {1, 2, 3, 4, 5, 6};
printf("%d %d\n", m[0][1], m[1][1]);
```

**Ex 7.32**
```c
int t[3][4];
printf("%zu %zu %zu\n", sizeof(t), sizeof(t[0]), sizeof(t[0][0]));
```
*(`int` = 4 bytes.)*

**Ex 7.33**
```c
int c[2][2][2] = { { {1, 2}, {3, 4} }, { {5, 6}, {7, 8} } };
printf("%d %d %d\n", c[0][1][0], c[1][0][1], c[1][1][1]);
```

**Ex 7.34** One pass of bubble sort:
```c
int a[5] = {5, 1, 4, 2, 8};
for (int i = 0; i < 4; i++)
    if (a[i] > a[i + 1])
    {
        int t = a[i];
        a[i] = a[i + 1];
        a[i + 1] = t;
    }
for (int i = 0; i < 5; i++)
    printf("%d ", a[i]);
```

**Ex 7.35** Counting array:
```c
int data[] = {1, 3, 2, 3, 3, 1};
int count[4] = {0};
for (int i = 0; i < 6; i++)
    count[data[i]]++;
for (int d = 1; d <= 3; d++)
    printf("%d:%d ", d, count[d]);
```

**Ex 7.36** Running total:
```c
int a[5] = {2, 4, 6, 8, 10};
for (int i = 1; i < 5; i++)
    a[i] += a[i - 1];
for (int i = 0; i < 5; i++)
    printf("%d ", a[i]);
```

## Part C — Find and fix the bugs

**Ex 7.37** The program writes beyond the array. Find and fix the mistake.
```c
int a[5];
for (int i = 0; i <= 5; i++)
    a[i] = i * i;
```

**Ex 7.38** Why is this a problem in standard C (and with some compilers, an error)? Fix it.
```c
int n = 5;
int a[n];
```

**Ex 7.39** This does not compile. Fix it.
```c
int a[3] = {1, 2, 3}, b[3];
b = a;
```

**Ex 7.40** The program claims two identical arrays are different. Why? Fix it.
```c
int a[3] = {1, 2, 3};
int b[3] = {1, 2, 3};
if (a == b)
    printf("same\n");
else
    printf("different\n");
```

**Ex 7.41** The function prints only one or two numbers. Why? Fix it.
```c
void printAll(int arr[])
{
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
        printf("%d ", arr[i]);
}
/* called as: printAll(numbers); where numbers has 6 elements */
```

**Ex 7.42** Some counts are huge and wrong. Fix it.
```c
int count[5];
int data[] = {1, 2, 2, 4, 4, 4};
for (int i = 0; i < 6; i++)
    count[data[i]]++;
```

**Ex 7.43** This loop is meant to print a 2 × 3 matrix. Find the mistake.
```c
int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 2; j++)
        printf("%d ", m[i][j]);
```

**Ex 7.44** The compiler complains about the function declaration. Fix it.
```c
void printMatrix(int m[][], int rows, int cols);
```

**Ex 7.45** Find the mistake in the input loop.
```c
int a[5];
for (int i = 0; i < 5; i++)
    scanf("%d", a[i]);
```

**Ex 7.46** The user enters 3 marks, but the average printed is far too small. Why?
```c
#define MAX 100
int marks[MAX];
int n = 3, sum = 0;
/* ... the user entered 3 marks into marks[0..2] ... */
for (int i = 0; i < n; i++)
    sum += marks[i];
printf("Average: %.2f\n", (double) sum / MAX);
```

**Ex 7.47** The matrix prints on one long line. Fix the braces.
```c
int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
for (int i = 0; i < 2; i++)
    for (int j = 0; j < 3; j++)
        printf("%d ", m[i][j]);
        printf("\n");
```

**Ex 7.48** Bubble sort touches an element beyond the array. Fix the inner loop.
```c
int a[5] = {5, 1, 4, 2, 8};
int n = 5;
for (int pass = 0; pass < n - 1; pass++)
    for (int j = 0; j < n; j++)
        if (a[j] > a[j + 1])
        {
            int t = a[j];
            a[j] = a[j + 1];
            a[j + 1] = t;
        }
```

**Ex 7.49** What is wrong with this "swap ends" function?
```c
void swapEnds(int arr[], int n)
{
    int temp = arr[0];
    arr[0] = arr[n];
    arr[n] = temp;
}
```

## Part D1 — One-dimensional arrays

*(Use `#define` for array sizes. Use functions where it makes the program cleaner.)*

**Ex 7.50** Read 5 integers and print them in **reverse order**.

**Ex 7.51** Read `N` (at most 20) and then `N` numbers. Print their **sum** and **average**.

**Ex 7.52** Read `N` numbers and print the **largest** and **smallest** with their **positions** (indices).

**Ex 7.53** Count how many elements of an array are **positive**, **negative** and **zero**.

**Ex 7.54** Print the **even** elements and the **odd** elements of an array separately, and how many of each.

**Ex 7.55** **Linear search:** read a key and print the index of its first occurrence (or `not found`).

**Ex 7.56** Read a value and count **how many times** it occurs in the array.

**Ex 7.57** Find the **second largest** element without sorting.

**Ex 7.58** **Reverse** an array **in place** (no second array). Print it before and after.

**Ex 7.59** **Copy** an array into a second array in **reverse order**.

**Ex 7.60** Check whether an array is **sorted in ascending order**.

**Ex 7.61** Check whether an array is a **palindrome** (reads the same forwards and backwards).

**Ex 7.62** **Bubble sort** an array in ascending order, then show how to change it for descending order.

**Ex 7.63** **Selection sort:** repeatedly find the smallest remaining element and swap it into place.

**Ex 7.64** **Binary search** on a sorted array. Also print how many comparisons were needed.

**Ex 7.65** **Insert** a value at a given position, shifting the others right.

**Ex 7.66** **Delete** the element at a given position, shifting the others left.

**Ex 7.67** Remove the **duplicates** from a **sorted** array (so `1 1 2 2 2 3` becomes `1 2 3`).

**Ex 7.68** **Merge** two sorted arrays into one sorted array.

**Ex 7.69** Read an integer and count how many times each **digit** 0–9 occurs in it (use a counting array).

**Ex 7.70** A **histogram** of marks: given 12 marks between 0 and 100, count how many fall into 0–9, 10–19, … 90–100, and print one `*` per student for each band.

**Ex 7.71** Convert a decimal number to **binary** by storing the remainders in an array and printing them in reverse.

**Ex 7.72** Given an array of bits such as `{1, 0, 1, 1, 0, 1}` (most significant bit first), compute the **decimal value**.

**Ex 7.73** Store the first `N` **Fibonacci** numbers in an array, then print them and their sum.

**Ex 7.74** **Sieve of Eratosthenes:** list all primes up to 50 by crossing out multiples in an array of flags.

**Ex 7.75** **Rotate** an array left by one position, and then write a version that rotates left by `k` positions.

**Ex 7.76** For an array of marks, compute the **mean**, the **median** (middle value after sorting) and the **mode** (most frequent value).

**Ex 7.77** Compute the **standard deviation** of an array of numbers: `sqrt( Σ(x − mean)² / n )`.

**Ex 7.78** Build a **cumulative sum** array: `c[i] = a[0] + a[1] + … + a[i]`.

**Ex 7.79** Given two vectors (arrays) of equal length, compute their **sum vector** and their **dot product**.

**Ex 7.80** Given an array and a target number, find **two elements** whose sum equals the target (print their indices).

**Ex 7.81** Move all the **zeros** to the end of an array, keeping the order of the other elements (`0 3 0 5 1` → `3 5 1 0 0`).

## Part D2 — Two-dimensional arrays

**Ex 7.82** Fill a 3 × 4 array with the values 0 to 11 and print it as a table.

**Ex 7.83** Read a 3 × 3 matrix. Print the **sum of all elements**, the **sum of each row** and the **sum of each column**.

**Ex 7.84** Compute the **transpose** of a 2 × 3 matrix.

**Ex 7.85** **Add** two 2 × 2 (or 3 × 3) matrices.

**Ex 7.86** **Multiply** a 2 × 3 matrix by a 3 × 2 matrix.

**Ex 7.87** For a square matrix compute the sum of the **main diagonal** and of the **secondary diagonal**, and check whether the matrix is **symmetric** (`m[i][j] == m[j][i]`).

**Ex 7.88** Print the **n × n identity matrix**, and write a function that checks whether a given matrix is an identity matrix.

**Ex 7.89** Find the **largest element** of a matrix and its **row and column**.

**Ex 7.90** Find the **row with the largest sum**.

**Ex 7.91** A table holds the marks of 4 students in 3 courses. Print each student's **average**, each course's **average**, and the **best student**.

**Ex 7.92** Check whether a 3 × 3 matrix is a **magic square** (all rows, all columns and both diagonals have the same sum).

**Ex 7.93** A 3 × 3 **tic-tac-toe** board holds `'X'`, `'O'` or `' '`. Print the board and decide whether **X** or **O** has won (three in a row, column or diagonal).

**Ex 7.94** Store **Pascal's triangle** (6 rows) in a 2D array using `p[i][j] = p[i-1][j-1] + p[i-1][j]`, and print it.

**Ex 7.95** A company has 3 branches and the sales for 4 quarters. Print the **total per branch**, the **total per quarter**, the **best quarter** and the **best branch**.

**Ex 7.96** **Rotate** a square matrix by 90° clockwise (`r[j][n-1-i] = m[i][j]`).

**Ex 7.97** A 4 × 4 grid should contain the numbers 1–4 **exactly once in every row and every column** (a *Latin square*). Write a program that checks this.

## Part D3 — Three-dimensional arrays

**Ex 7.98** Declare `int cube[2][3][4]`, fill it with consecutive numbers starting at 1, and print it page by page.

**Ex 7.99** `marks[2][3][2]` holds the marks of **2 classes**, **3 students** each, in **2 tests**. Print each student's **total**, and the **average mark of each class**.

**Ex 7.100** `temp[2][3][4]` holds the temperature readings: 2 cities, 3 days, 4 readings per day. Print the **average temperature per day for each city**, and the **hottest reading** of all.

## Part E — Challenges and mini-projects

**Ex 7.101 (class grade book)** Read the number of students (at most 30) and their marks. Write functions to compute the **average**, **highest**, **lowest**, a **grade** for a mark, and a function that prints a report listing every student's mark and grade, plus the students who are **above average**.

**Ex 7.102 (determinant)** Compute the **determinant** of a 2 × 2 and of a 3 × 3 matrix.

**Ex 7.103 (longest run)** Find the length of the **longest strictly increasing run** of consecutive elements (e.g. `1 3 5 2 4 6 8 9 1` → 5 for `2 4 6 8 9`).

**Ex 7.104 (remove value)** Remove **all occurrences** of a given value from an array **in place** and report the new length.

**Ex 7.105 (best stretch)** Find the **maximum sum of consecutive elements** (a sub-array) in an array containing positive and negative numbers (e.g. `-2 1 -3 4 -1 2 1 -5 4` → 6).

**Ex 7.106 (spiral)** Print a 4 × 4 matrix in **spiral order** (right across the top row, down the last column, left along the bottom row, up the first column, then the inner square).

**Ex 7.107 (dice)** Simulate rolling a die **600 times** using a small pseudo-random generator (like Ex 6.74), count how many times each face appears in an array, and print a histogram.

**Ex 7.108 (binary adder)** Add two binary numbers stored as arrays of bits (least significant bit first), with carry, and print the result.

## Part F — Research tasks

**Ex 7.109** Read more about the `sizeof` operator. Explain why `sizeof(arr)` inside a function that received `arr` as a parameter does not give the array's size.

**Ex 7.110** What is a **variable-length array (VLA)**? Which C standard introduced it, and why do many programmers avoid it?

**Ex 7.111** Look up `qsort` in `<stdlib.h>`. Use it to sort an array of integers (you will need to write a *comparison function*).

**Ex 7.112** Read ahead: in C, `a[i]` is exactly the same as `*(a + i)`. What do you think this means for the relationship between arrays and pointers? (You will confirm it in Chapter 8.)

---

*End of Chapter 7. Next: [Chapter 8 — Pointers and Strings](08-pointers-and-strings.md)*
