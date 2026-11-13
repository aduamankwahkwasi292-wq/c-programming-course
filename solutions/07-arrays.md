# Solutions — Chapter 7: Arrays

> Back to the lesson: [Chapter 7 lesson](../lessons/07-arrays.md)

---

## Part A — Quick check

**Ex 7.1** An **array** stores a fixed-size, sequential collection of elements of the **same type** under **one name**. With 60 separate variables you would need 60 names and 60 separate statements to read, add or print them; with an array a single loop handles them all.

**Ex 7.2**
```c
int marks[10];
double prices[5];
char letters[26];
```

**Ex 7.3** The first element has index **0**. The last element of `int a[8]` has index **7**.

**Ex 7.4** It reads/writes memory **outside** the array (out-of-bounds): undefined behaviour — a crash, garbage, or silent corruption of another variable. **No**, the compiler does not stop you; C does not check indices.

**Ex 7.5** (a) `1 2 0 0 0` (the rest are filled with 0). (b) `0 0 0`. (c) **garbage** — unpredictable values (never rely on them).

**Ex 7.6** It computes the **number of elements** (total bytes ÷ bytes of one element). It is better than hard-coding the size because if you later change the declaration (`int a[5]` → `int a[8]`) every loop adjusts automatically.

**Ex 7.7** `int t[4][5]`: 4 × 5 = **20** elements = 80 bytes. `float x[3][4][2]`: 3 × 4 × 2 = **24** elements.

**Ex 7.8** The **first** index `i` is the **row**; the second index `j` is the **column**.

**Ex 7.9** **No** to both: `b = a;` does not compile for arrays, and `a == b` compiles but compares the **addresses** of the arrays, not their contents. Use a **loop** to copy or compare element by element.

**Ex 7.10** **Yes** — the function receives the address of the original array, so changes affect the original. You should also pass the **size** (number of elements).

**Ex 7.11**
```
          col 0  col 1  col 2
   row 0    1      2      3
   row 1    4      5      6
```
`m[1][2]` = **6**; `m[0][1]` = **2**.

**Ex 7.12** In `int x[5];` the **5 is the size** (a declaration — "5 integers"). In `x[4] = 9;` the **4 is an index** (selects the fifth element).

**Ex 7.13** Valid indices are `0 … n−1`. With `i <= n` the last pass uses `a[n]`, which is one past the end (out-of-bounds).

**Ex 7.14**
1. **False** — all elements have the same type.
2. **False** — the first element is `a[0]`.
3. **True.**
4. **False** — too many initialisers (6 values for 5 slots).
5. **True.**
6. **False** — rows are 0, 1, 2 only; `m[3][0]` is out-of-bounds.

---

## Part B — Predict the output

**Ex 7.15** `10 30 50`

**Ex 7.16** `1 5 3 5` — `a[1] = 1 + 4 = 5`, then `a[3]` goes 4 → 5.

**Ex 7.17** `7 8 0 0 0 0`

**Ex 7.18** `80 28 12` — 10 × 8 bytes, 7 × 4 bytes, and 12 elements.

**Ex 7.19** `9` — it adds the elements at indices 0, 2, 4: 3 + 1 + 5.

**Ex 7.20** `2 4 0`
`a[a[0]]` = `a[4]` = 2. `a[a[1]]` = `a[0]` = 4. `a[a[a[2]]]`: `a[2]` = 3 → `a[3]` = 1 → `a[1]` = 0.

**Ex 7.21** `9 1` — the maximum is 9, found at index 1.

**Ex 7.22** `2 3 4 5 5` — every element is replaced by its right-hand neighbour (the last stays 5).

**Ex 7.23** `5 4 3 2 1`

**Ex 7.24** `11 12 13` — the function receives the **original** array.

**Ex 7.25** `1 2 3` — a single element is passed **by value**.

**Ex 7.26** `3 4 6`

**Ex 7.27** `6 15` — row sums.

**Ex 7.28** `1 4 2 5 3 6` — it walks down each *column* (the outer loop is the column).

**Ex 7.29**
```output
1 5 9
3 5 7
```

**Ex 7.30**
```output
1 0 0
4 5 0
```
Missing elements in each row group become 0.

**Ex 7.31** `2 5` — a flat list fills row by row: row 0 = 1 2 3, row 1 = 4 5 6; `m[0][1]` = 2, `m[1][1]` = 5.

**Ex 7.32** `48 16 4` — 12 ints × 4 bytes = 48; one row has 4 ints = 16 bytes; one element = 4 bytes.

**Ex 7.33** `3 6 8`

**Ex 7.34** `1 4 2 5 8` — the first bubble pass: (5,1) swap, (5,4) swap, (5,2) swap, (5,8) no swap. The 5 has moved right.

**Ex 7.35** `1:2 2:1 3:3` — `count[d]` is how many times `d` appears.

**Ex 7.36** `2 6 12 20 30` — each element becomes the sum of itself and the (already updated) previous element: a **cumulative sum**.

---

## Part C — Find and fix the bugs

**Ex 7.37** `i <= 5` writes `a[5]`, which doesn't exist (valid indices are 0–4). Use `<`:
```c
for (int i = 0; i < 5; i++)
    a[i] = i * i;
```

**Ex 7.38** The array size must be a **constant**; `n` is a variable. (C99 allows "variable-length arrays" but they are optional in later standards, unsupported by some compilers, and risky.) Use a constant:
```c
#define N 5
int a[N];
```

**Ex 7.39** Arrays cannot be assigned. Copy element by element:
```c
for (int i = 0; i < 3; i++)
    b[i] = a[i];
```

**Ex 7.40** `a == b` compares the **addresses** where the two arrays live — which are different — not their contents. Compare in a loop:
```c
#include <stdio.h>

int main(void)
{
    int a[3] = {1, 2, 3};
    int b[3] = {1, 2, 3};
    int same = 1;

    for (int i = 0; i < 3; i++)
        if (a[i] != b[i])
        {
            same = 0;
            break;
        }

    if (same)
        printf("same\n");
    else
        printf("different\n");
    return 0;
}
```
```output
same
```

**Ex 7.41** Inside the function, `arr` is only an **address**, so `sizeof(arr)` is the size of an address (8 bytes on a 64-bit machine) and `sizeof(arr) / sizeof(arr[0])` is 2 (or 1 on 32-bit). Pass the size:
```c
void printAll(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
}
/* call: printAll(numbers, 6); */
```

**Ex 7.42** `count` was never initialised, so it starts with garbage. Fix: `int count[5] = {0};`.

**Ex 7.43** The loop bounds are swapped. The matrix has **2 rows and 3 columns**, but the loops treat `i` (the row) as going to 3 and `j` (the column) to 2 — reading outside the array. Fix: `i < 2` and `j < 3`.

**Ex 7.44** When an array is a parameter, only the **first** dimension may be left empty; the compiler needs the **column count** to compute where each row starts: `void printMatrix(int m[][3], int rows)` (or `int m[][COLS]`).

**Ex 7.45** `scanf` needs the **address** of each element: `scanf("%d", &a[i]);`.

**Ex 7.46** The sum is divided by `MAX` (100, the array's *capacity*) instead of `n` (3, the number of values actually entered). Divide by `n`.

**Ex 7.47** Without braces the inner `for` is the only statement in the outer loop; the `printf("\n")` runs once at the very end. Add braces:
```c
for (int i = 0; i < 2; i++)
{
    for (int j = 0; j < 3; j++)
        printf("%d ", m[i][j]);
    printf("\n");
}
```

**Ex 7.48** When `j` reaches `n − 1`, the comparison uses `a[j + 1]` = `a[n]` (out of bounds). The inner loop must stop earlier: `j < n - 1` (or `j < n - 1 - pass`).

**Ex 7.49** The last valid index is `n - 1`, not `n`. Use `arr[n - 1]`.

---

## Part D1 — One-dimensional arrays

**Ex 7.50**
<!--in: 10 20 30 40 50-->
```c
#include <stdio.h>

#define SIZE 5

int main(void)
{
    int a[SIZE];

    printf("Enter %d integers: ", SIZE);
    for (int i = 0; i < SIZE; i++)
        scanf("%d", &a[i]);

    printf("In reverse: ");
    for (int i = SIZE - 1; i >= 0; i--)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
Enter 5 integers: 10 20 30 40 50
In reverse: 50 40 30 20 10
```

**Ex 7.51**
<!--in: 5 70 85 91 60 73-->
```c
#include <stdio.h>

#define MAX 20

int main(void)
{
    int a[MAX], n, sum = 0;

    printf("How many numbers (max %d)? ", MAX);
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        sum += a[i];
    }

    printf("Sum = %d, Average = %.2f\n", sum, (double) sum / n);
    return 0;
}
```
```output
How many numbers (max 20)? 5 70 85 91 60 73
Sum = 379, Average = 75.80
```

**Ex 7.52**
<!--in: 6 12 -5 40 7 0 33-->
```c
#include <stdio.h>

#define MAX 20

int main(void)
{
    int a[MAX], n;

    printf("How many numbers? ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    int maxIdx = 0, minIdx = 0;
    for (int i = 1; i < n; i++)
    {
        if (a[i] > a[maxIdx]) maxIdx = i;
        if (a[i] < a[minIdx]) minIdx = i;
    }

    printf("Largest : %d at index %d\n", a[maxIdx], maxIdx);
    printf("Smallest: %d at index %d\n", a[minIdx], minIdx);
    return 0;
}
```
```output
How many numbers? 6 12 -5 40 7 0 33
Largest : 40 at index 2
Smallest: -5 at index 1
```
Tip: remembering the **index** is more useful than remembering the value (you can always get the value from the index).

**Ex 7.53**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {4, -2, 0, 7, -9, 0, 3, -1};
    int n = sizeof(a) / sizeof(a[0]);
    int pos = 0, neg = 0, zero = 0;

    for (int i = 0; i < n; i++)
    {
        if (a[i] > 0)
            pos++;
        else if (a[i] < 0)
            neg++;
        else
            zero++;
    }

    printf("Positive: %d, negative: %d, zero: %d\n", pos, neg, zero);
    return 0;
}
```
```output
Positive: 3, negative: 3, zero: 2
```

**Ex 7.54**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {12, 7, 8, 3, 20, 15, 4};
    int n = sizeof(a) / sizeof(a[0]);
    int evens = 0, odds = 0;

    printf("Even: ");
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0)
        {
            printf("%d ", a[i]);
            evens++;
        }

    printf("(%d)\nOdd : ", evens);
    for (int i = 0; i < n; i++)
        if (a[i] % 2 != 0)
        {
            printf("%d ", a[i]);
            odds++;
        }
    printf("(%d)\n", odds);
    return 0;
}
```
```output
Even: 12 8 20 4 (4)
Odd : 7 3 15 (3)
```

**Ex 7.55** *(Using `-1` as "not found" works because no valid index is negative.)*
<!--in: 7-->
```c
#include <stdio.h>

int main(void)
{
    int a[] = {4, 9, 7, 1, 8, 7};
    int n = sizeof(a) / sizeof(a[0]);
    int key, index = -1;

    printf("Search for: ");
    scanf("%d", &key);

    for (int i = 0; i < n; i++)
        if (a[i] == key)
        {
            index = i;
            break;
        }

    if (index == -1)
        printf("%d not found\n", key);
    else
        printf("First occurrence of %d is at index %d\n", key, index);
    return 0;
}
```
```output
Search for: 7
First occurrence of 7 is at index 2
```

**Ex 7.56**
<!--in: 3-->
```c
#include <stdio.h>

int main(void)
{
    int a[] = {3, 7, 3, 9, 3, 1, 7};
    int n = sizeof(a) / sizeof(a[0]);
    int key, count = 0;

    printf("Value to count: ");
    scanf("%d", &key);

    for (int i = 0; i < n; i++)
        if (a[i] == key)
            count++;

    printf("%d occurs %d time(s)\n", key, count);
    return 0;
}
```
```output
Value to count: 3
3 occurs 3 time(s)
```

**Ex 7.57** We track the largest value and the largest value that is **smaller** than it, in a single pass.
```c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    int a[] = {12, 45, 7, 45, 30};
    int n = sizeof(a) / sizeof(a[0]);
    int first = a[0], second = INT_MIN;

    for (int i = 1; i < n; i++)
    {
        if (a[i] > first)
        {
            second = first;
            first = a[i];
        }
        else if (a[i] != first && a[i] > second)
        {
            second = a[i];
        }
    }

    printf("Largest: %d, second largest: %d\n", first, second);
    return 0;
}
```
```output
Largest: 45, second largest: 30
```
(`a[i] != first` ensures a repeated maximum is not counted as the "second" largest.)

**Ex 7.58**
```c
#include <stdio.h>

void printArray(const int a[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void reverse(int a[], int n)
{
    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

int main(void)
{
    int a[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Before: ");
    printArray(a, n);
    reverse(a, n);
    printf("After : ");
    printArray(a, n);
    return 0;
}
```
```output
Before: 1 2 3 4 5 6
After : 6 5 4 3 2 1
```

**Ex 7.59**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int b[5];

    for (int i = 0; i < n; i++)
        b[i] = a[n - 1 - i];

    for (int i = 0; i < n; i++)
        printf("%d ", b[i]);
    printf("\n");
    return 0;
}
```
```output
5 4 3 2 1
```

**Ex 7.60**
```c
#include <stdio.h>

int isSorted(const int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
        if (a[i] > a[i + 1])
            return 0;               /* one pair out of order is enough */
    return 1;
}

int main(void)
{
    int x[] = {1, 3, 5, 7};
    int y[] = {1, 3, 2, 7};

    printf("x sorted? %d\n", isSorted(x, 4));
    printf("y sorted? %d\n", isSorted(y, 4));
    return 0;
}
```
```output
x sorted? 1
y sorted? 0
```

**Ex 7.61** Compare each element with its mirror image; only go as far as the middle.
```c
#include <stdio.h>

int isPalindrome(const int a[], int n)
{
    for (int i = 0; i < n / 2; i++)
        if (a[i] != a[n - 1 - i])
            return 0;
    return 1;
}

int main(void)
{
    int x[] = {1, 2, 3, 2, 1};
    int y[] = {1, 2, 3, 4};

    printf("x palindrome? %d\n", isPalindrome(x, 5));
    printf("y palindrome? %d\n", isPalindrome(y, 4));
    return 0;
}
```
```output
x palindrome? 1
y palindrome? 0
```

**Ex 7.62** For descending order, only the comparison changes (`<` instead of `>`).
```c
#include <stdio.h>

void bubbleSort(int a[], int n, int ascending)
{
    for (int pass = 0; pass < n - 1; pass++)
        for (int j = 0; j < n - 1 - pass; j++)
        {
            int outOfOrder = ascending ? (a[j] > a[j + 1]) : (a[j] < a[j + 1]);
            if (outOfOrder)
            {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
}

void printArray(const int a[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(a) / sizeof(a[0]);

    bubbleSort(a, n, 1);
    printf("Ascending : ");
    printArray(a, n);

    bubbleSort(a, n, 0);
    printf("Descending: ");
    printArray(a, n);
    return 0;
}
```
```output
Ascending : 11 12 22 25 34 64 90
Descending: 90 64 34 25 22 12 11
```

**Ex 7.63**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {29, 10, 14, 37, 13};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < n - 1; i++)
    {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)         /* find the smallest of the rest */
            if (a[j] < a[minIdx])
                minIdx = j;

        int temp = a[i];                        /* put it in position i */
        a[i] = a[minIdx];
        a[minIdx] = temp;

        printf("after pass %d: ", i + 1);
        for (int k = 0; k < n; k++)
            printf("%d ", a[k]);
        printf("\n");
    }
    return 0;
}
```
```output
after pass 1: 10 29 14 37 13
after pass 2: 10 13 14 37 29
after pass 3: 10 13 14 37 29
after pass 4: 10 13 14 29 37
```
Selection sort does at most `n − 1` swaps; bubble sort may do many more.

**Ex 7.64**
<!--in: 23-->
```c
#include <stdio.h>

int main(void)
{
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(a) / sizeof(a[0]);
    int key, low = 0, high = n - 1, found = -1, steps = 0;

    printf("Search for: ");
    scanf("%d", &key);

    while (low <= high)
    {
        int mid = (low + high) / 2;
        steps++;
        if (a[mid] == key)
        {
            found = mid;
            break;
        }
        else if (a[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    if (found >= 0)
        printf("Found %d at index %d after %d step(s)\n", key, found, steps);
    else
        printf("%d not found (%d step(s))\n", key, steps);
    return 0;
}
```
```output
Search for: 23
Found 23 at index 5 after 3 step(s)
```

**Ex 7.65**
<!--in: 2 25-->
```c
#include <stdio.h>

#define CAPACITY 10

int main(void)
{
    int a[CAPACITY] = {10, 20, 30, 40, 50};
    int n = 5, pos, value;

    printf("Position and value to insert: ");
    scanf("%d %d", &pos, &value);

    for (int i = n; i > pos; i--)          /* shift right, starting from the end */
        a[i] = a[i - 1];
    a[pos] = value;
    n++;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
Position and value to insert: 2 25
10 20 25 30 40 50
```
(A real program should first check that `n < CAPACITY` and that `0 <= pos <= n`.)

**Ex 7.66**
<!--in: 1-->
```c
#include <stdio.h>

int main(void)
{
    int a[] = {10, 20, 30, 40, 50};
    int n = 5, pos;

    printf("Position to delete: ");
    scanf("%d", &pos);

    for (int i = pos; i < n - 1; i++)      /* shift left, starting from the front */
        a[i] = a[i + 1];
    n--;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
Position to delete: 1
10 30 40 50
```

**Ex 7.67** Duplicates of a sorted array are next to each other. Keep a write position `k`; copy an element only if it differs from the last one kept.
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 1, 2, 2, 2, 3, 5, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int k = 1;

    for (int i = 1; i < n; i++)
        if (a[i] != a[k - 1])
            a[k++] = a[i];

    for (int i = 0; i < k; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
1 2 3 5
```

**Ex 7.68** Walk through both arrays, always taking the smaller front element.
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 4, 7, 10};
    int b[] = {2, 3, 8, 9, 11};
    int na = 4, nb = 5;
    int c[9];
    int i = 0, j = 0, k = 0;

    while (i < na && j < nb)
    {
        if (a[i] <= b[j])
            c[k++] = a[i++];
        else
            c[k++] = b[j++];
    }
    while (i < na)                       /* leftovers of a */
        c[k++] = a[i++];
    while (j < nb)                       /* leftovers of b */
        c[k++] = b[j++];

    for (int x = 0; x < k; x++)
        printf("%d ", c[x]);
    printf("\n");
    return 0;
}
```
```output
1 2 3 4 7 8 9 10 11
```

**Ex 7.69**
<!--in: 1223334444-->
```c
#include <stdio.h>

int main(void)
{
    int n, count[10] = {0};

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    while (n > 0)
    {
        count[n % 10]++;
        n /= 10;
    }

    for (int d = 0; d < 10; d++)
        if (count[d] > 0)
            printf("digit %d: %d\n", d, count[d]);
    return 0;
}
```
```output
Enter a positive integer: 1223334444
digit 1: 1
digit 2: 2
digit 3: 3
digit 4: 4
```

**Ex 7.70** `mark / 10` gives the band number (0–9); a mark of 100 would give 10, so we fold it into the last band.
```c
#include <stdio.h>

int main(void)
{
    int marks[] = {45, 67, 89, 92, 100, 55, 61, 78, 83, 99, 12, 67};
    int n = sizeof(marks) / sizeof(marks[0]);
    int band[10] = {0};

    for (int i = 0; i < n; i++)
    {
        int b = marks[i] / 10;
        if (b > 9)
            b = 9;
        band[b]++;
    }

    for (int b = 0; b < 10; b++)
    {
        printf("%3d-%-3d: ", b * 10, (b == 9) ? 100 : b * 10 + 9);
        for (int s = 0; s < band[b]; s++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
  0-9  : 
 10-19 : *
 20-29 : 
 30-39 : 
 40-49 : *
 50-59 : *
 60-69 : ***
 70-79 : *
 80-89 : **
 90-100: ***
```

**Ex 7.71**
<!--in: 37-->
```c
#include <stdio.h>

int main(void)
{
    int n, bits[32], count = 0;

    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    if (n == 0)
        bits[count++] = 0;
    while (n > 0)
    {
        bits[count++] = n % 2;     /* remainders come out last bit first */
        n /= 2;
    }

    printf("Binary: ");
    for (int i = count - 1; i >= 0; i--)
        printf("%d", bits[i]);
    printf("\n");
    return 0;
}
```
```output
Enter a non-negative integer: 37
Binary: 100101
```

**Ex 7.72**
```c
#include <stdio.h>

int main(void)
{
    int bits[] = {1, 0, 1, 1, 0, 1};
    int n = sizeof(bits) / sizeof(bits[0]);
    int value = 0;

    for (int i = 0; i < n; i++)
        value = value * 2 + bits[i];          /* shift left and add the next bit */

    printf("Decimal value = %d\n", value);
    return 0;
}
```
```output
Decimal value = 45
```
(Check: 32 + 8 + 4 + 1 = 45.)

**Ex 7.73**
```c
#include <stdio.h>

#define N 10

int main(void)
{
    int fib[N], sum = 0;

    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i < N; i++)
        fib[i] = fib[i - 1] + fib[i - 2];

    for (int i = 0; i < N; i++)
    {
        printf("%d ", fib[i]);
        sum += fib[i];
    }
    printf("\nSum = %d\n", sum);
    return 0;
}
```
```output
0 1 1 2 3 5 8 13 21 34
Sum = 88
```

**Ex 7.74** Start by assuming every number is prime; for each prime found, cross out its multiples.
```c
#include <stdio.h>

#define LIMIT 50

int main(void)
{
    int isPrime[LIMIT + 1];

    for (int i = 0; i <= LIMIT; i++)
        isPrime[i] = 1;
    isPrime[0] = isPrime[1] = 0;

    for (int p = 2; p * p <= LIMIT; p++)
        if (isPrime[p])
            for (int multiple = p * p; multiple <= LIMIT; multiple += p)
                isPrime[multiple] = 0;

    for (int i = 2; i <= LIMIT; i++)
        if (isPrime[i])
            printf("%d ", i);
    printf("\n");
    return 0;
}
```
```output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

**Ex 7.75** Rotating by `k` is just rotating by one, `k` times.
```c
#include <stdio.h>

void rotateLeftOnce(int a[], int n)
{
    int first = a[0];
    for (int i = 0; i < n - 1; i++)
        a[i] = a[i + 1];
    a[n - 1] = first;
}

void rotateLeft(int a[], int n, int k)
{
    for (int r = 0; r < k; r++)
        rotateLeftOnce(a, n);
}

void printArray(const int a[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int a[] = {1, 2, 3, 4, 5};
    int b[] = {1, 2, 3, 4, 5};

    rotateLeftOnce(a, 5);
    printf("by 1: ");
    printArray(a, 5);

    rotateLeft(b, 5, 2);
    printf("by 2: ");
    printArray(b, 5);
    return 0;
}
```
```output
by 1: 2 3 4 5 1
by 2: 3 4 5 1 2
```

**Ex 7.76**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {70, 85, 60, 85, 90, 75, 85, 60};
    int n = sizeof(a) / sizeof(a[0]);
    int sum = 0;

    for (int i = 0; i < n; i++)
        sum += a[i];
    double mean = (double) sum / n;

    /* sort (bubble sort) to find the median */
    for (int pass = 0; pass < n - 1; pass++)
        for (int j = 0; j < n - 1 - pass; j++)
            if (a[j] > a[j + 1])
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
    double median = (n % 2 == 1) ? a[n / 2] : (a[n / 2 - 1] + a[n / 2]) / 2.0;

    /* mode: the value with the highest count */
    int mode = a[0], bestCount = 0;
    for (int i = 0; i < n; i++)
    {
        int count = 0;
        for (int j = 0; j < n; j++)
            if (a[j] == a[i])
                count++;
        if (count > bestCount)
        {
            bestCount = count;
            mode = a[i];
        }
    }

    printf("Mean   = %.2f\n", mean);
    printf("Median = %.1f\n", median);
    printf("Mode   = %d (appears %d times)\n", mode, bestCount);
    return 0;
}
```
```output
Mean   = 76.25
Median = 80.0
Mode   = 85 (appears 3 times)
```

**Ex 7.77**
```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double x[] = {2, 4, 4, 4, 5, 5, 7, 9};
    int n = sizeof(x) / sizeof(x[0]);
    double sum = 0, squares = 0;

    for (int i = 0; i < n; i++)
        sum += x[i];
    double mean = sum / n;

    for (int i = 0; i < n; i++)
        squares += (x[i] - mean) * (x[i] - mean);

    printf("Mean = %.2f, standard deviation = %.2f\n", mean, sqrt(squares / n));
    return 0;
}
```
```output
Mean = 5.00, standard deviation = 2.00
```

**Ex 7.78**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {3, 1, 4, 1, 5, 9};
    int n = sizeof(a) / sizeof(a[0]);
    int c[6];

    c[0] = a[0];
    for (int i = 1; i < n; i++)
        c[i] = c[i - 1] + a[i];

    for (int i = 0; i < n; i++)
        printf("%d ", c[i]);
    printf("\n");
    return 0;
}
```
```output
3 4 8 9 14 23
```

**Ex 7.79**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 2, 3};
    int b[] = {4, 5, 6};
    int n = 3, sum[3], dot = 0;

    for (int i = 0; i < n; i++)
    {
        sum[i] = a[i] + b[i];
        dot += a[i] * b[i];
    }

    printf("Sum vector: ");
    for (int i = 0; i < n; i++)
        printf("%d ", sum[i]);
    printf("\nDot product: %d\n", dot);
    return 0;
}
```
```output
Sum vector: 5 7 9
Dot product: 32
```

**Ex 7.80** Two nested loops: `j` starts at `i + 1` so every pair is tried once.
```c
#include <stdio.h>

int main(void)
{
    int a[] = {2, 7, 11, 15, 1, 8};
    int n = sizeof(a) / sizeof(a[0]);
    int target = 9;

    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] + a[j] == target)
                printf("a[%d] + a[%d] = %d + %d = %d\n", i, j, a[i], a[j], target);
    return 0;
}
```
```output
a[0] + a[1] = 2 + 7 = 9
a[4] + a[5] = 1 + 8 = 9
```

**Ex 7.81** Copy the non-zero elements to the front (keeping their order), then fill the rest with zeros.
```c
#include <stdio.h>

int main(void)
{
    int a[] = {0, 3, 0, 5, 1};
    int n = sizeof(a) / sizeof(a[0]);
    int k = 0;

    for (int i = 0; i < n; i++)
        if (a[i] != 0)
            a[k++] = a[i];
    while (k < n)
        a[k++] = 0;

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
3 5 1 0 0
```

---

## Part D2 — Two-dimensional arrays

**Ex 7.82**
```c
#include <stdio.h>

int main(void)
{
    int t[3][4];
    int count = 0;

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 4; j++)
            t[i][j] = count++;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
            printf("%4d", t[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
   0   1   2   3
   4   5   6   7
   8   9  10  11
```

**Ex 7.83**
<!--in: 1 2 3 4 5 6 7 8 9-->
```c
#include <stdio.h>

int main(void)
{
    int m[3][3], total = 0;

    printf("Enter the 9 elements row by row: ");
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
        {
            scanf("%d", &m[i][j]);
            total += m[i][j];
        }

    printf("Sum of all elements: %d\n", total);

    for (int i = 0; i < 3; i++)
    {
        int rowSum = 0;
        for (int j = 0; j < 3; j++)
            rowSum += m[i][j];
        printf("Row %d sum: %d\n", i, rowSum);
    }

    for (int j = 0; j < 3; j++)
    {
        int colSum = 0;
        for (int i = 0; i < 3; i++)
            colSum += m[i][j];
        printf("Column %d sum: %d\n", j, colSum);
    }
    return 0;
}
```
```output
Enter the 9 elements row by row: 1 2 3 4 5 6 7 8 9
Sum of all elements: 45
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24
Column 0 sum: 12
Column 1 sum: 15
Column 2 sum: 18
```

**Ex 7.84**
```c
#include <stdio.h>

int main(void)
{
    int m[2][3] = { {7, 8, 9}, {10, 11, 12} };
    int t[3][2];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 3; j++)
            t[j][i] = m[i][j];

    printf("Original:\n");
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
            printf("%4d", m[i][j]);
        printf("\n");
    }

    printf("Transpose:\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
            printf("%4d", t[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
Original:
   7   8   9
  10  11  12
Transpose:
   7  10
   8  11
   9  12
```

**Ex 7.85**
```c
#include <stdio.h>

int main(void)
{
    int a[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int b[3][3] = { {1, 0, 0}, {0, 1, 0}, {0, 0, 1} };
    int c[3][3];

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            c[i][j] = a[i][j] + b[i][j];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
            printf("%4d", c[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
   2   2   3
   4   6   6
   7   8  10
```

**Ex 7.86**
```c
#include <stdio.h>

int main(void)
{
    int a[2][3] = { {2, 0, 1}, {1, 3, 2} };
    int b[3][2] = { {1, 2}, {0, 1}, {4, 0} };
    int c[2][2];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
        {
            c[i][j] = 0;
            for (int k = 0; k < 3; k++)
                c[i][j] += a[i][k] * b[k][j];
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
   6   4
   9   5
```
The number of **columns of A** must equal the number of **rows of B** (3 = 3); the result has the rows of A and the columns of B (2 × 2).

**Ex 7.87**
```c
#include <stdio.h>

#define N 3

int isSymmetric(int m[][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (m[i][j] != m[j][i])
                return 0;
    return 1;
}

int main(void)
{
    int a[N][N] = { {1, 2, 3}, {2, 5, 6}, {3, 6, 9} };
    int b[N][N] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int mainDiag = 0, secondDiag = 0;

    for (int i = 0; i < N; i++)
    {
        mainDiag += a[i][i];
        secondDiag += a[i][N - 1 - i];
    }

    printf("Main diagonal sum      = %d\n", mainDiag);
    printf("Secondary diagonal sum = %d\n", secondDiag);
    printf("a symmetric? %d\n", isSymmetric(a));
    printf("b symmetric? %d\n", isSymmetric(b));
    return 0;
}
```
```output
Main diagonal sum      = 15
Secondary diagonal sum = 11
a symmetric? 1
b symmetric? 0
```

**Ex 7.88**
```c
#include <stdio.h>

#define N 4

int isIdentity(int m[][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            int expected = (i == j) ? 1 : 0;
            if (m[i][j] != expected)
                return 0;
        }
    return 1;
}

int main(void)
{
    int id[N][N];
    int other[N][N] = {0};

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            id[i][j] = (i == j);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            printf("%d ", id[i][j]);
        printf("\n");
    }

    printf("id is identity?    %d\n", isIdentity(id));
    printf("other is identity? %d\n", isIdentity(other));
    return 0;
}
```
```output
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
id is identity?    1
other is identity? 0
```

**Ex 7.89**
```c
#include <stdio.h>

int main(void)
{
    int m[3][3] = { {3, 8, 1}, {9, 4, 7}, {2, 6, 5} };
    int best = m[0][0], bestRow = 0, bestCol = 0;

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (m[i][j] > best)
            {
                best = m[i][j];
                bestRow = i;
                bestCol = j;
            }

    printf("Largest = %d at row %d, column %d\n", best, bestRow, bestCol);
    return 0;
}
```
```output
Largest = 9 at row 1, column 0
```

**Ex 7.90**
```c
#include <stdio.h>

int main(void)
{
    int m[3][3] = { {3, 8, 1}, {9, 4, 7}, {2, 6, 5} };
    int bestRow = 0, bestSum = -1;

    for (int i = 0; i < 3; i++)
    {
        int sum = 0;
        for (int j = 0; j < 3; j++)
            sum += m[i][j];
        printf("row %d sum = %d\n", i, sum);
        if (sum > bestSum)
        {
            bestSum = sum;
            bestRow = i;
        }
    }
    printf("Row %d has the largest sum (%d)\n", bestRow, bestSum);
    return 0;
}
```
```output
row 0 sum = 12
row 1 sum = 20
row 2 sum = 13
Row 1 has the largest sum (20)
```

**Ex 7.91**
```c
#include <stdio.h>

#define STUDENTS 4
#define COURSES 3

int main(void)
{
    int marks[STUDENTS][COURSES] = {
        {70, 80, 90},
        {60, 75, 85},
        {95, 85, 90},
        {50, 65, 55}
    };
    double bestAvg = -1;
    int best = 0;

    for (int s = 0; s < STUDENTS; s++)
    {
        int sum = 0;
        for (int c = 0; c < COURSES; c++)
            sum += marks[s][c];
        double avg = (double) sum / COURSES;
        printf("Student %d average: %.2f\n", s + 1, avg);
        if (avg > bestAvg)
        {
            bestAvg = avg;
            best = s;
        }
    }

    for (int c = 0; c < COURSES; c++)
    {
        int sum = 0;
        for (int s = 0; s < STUDENTS; s++)
            sum += marks[s][c];
        printf("Course %d average: %.2f\n", c + 1, (double) sum / STUDENTS);
    }

    printf("Best student: Student %d (%.2f)\n", best + 1, bestAvg);
    return 0;
}
```
```output
Student 1 average: 80.00
Student 2 average: 73.33
Student 3 average: 90.00
Student 4 average: 56.67
Course 1 average: 68.75
Course 2 average: 76.25
Course 3 average: 80.00
Best student: Student 3 (90.00)
```

**Ex 7.92**
```c
#include <stdio.h>

int isMagic(int m[3][3])
{
    int target = m[0][0] + m[0][1] + m[0][2];        /* the first row's sum */
    int d1 = 0, d2 = 0;

    for (int i = 0; i < 3; i++)
    {
        int row = 0, col = 0;
        for (int j = 0; j < 3; j++)
        {
            row += m[i][j];
            col += m[j][i];
        }
        if (row != target || col != target)
            return 0;
        d1 += m[i][i];
        d2 += m[i][2 - i];
    }
    return d1 == target && d2 == target;
}

int main(void)
{
    int a[3][3] = { {2, 7, 6}, {9, 5, 1}, {4, 3, 8} };
    int b[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };

    printf("a is magic? %d\n", isMagic(a));
    printf("b is magic? %d\n", isMagic(b));
    return 0;
}
```
```output
a is magic? 1
b is magic? 0
```

**Ex 7.93**
```c
#include <stdio.h>

char winner(char b[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        if (b[i][0] != ' ' && b[i][0] == b[i][1] && b[i][1] == b[i][2])
            return b[i][0];                                   /* row i */
        if (b[0][i] != ' ' && b[0][i] == b[1][i] && b[1][i] == b[2][i])
            return b[0][i];                                   /* column i */
    }
    if (b[1][1] != ' ' && b[0][0] == b[1][1] && b[1][1] == b[2][2])
        return b[1][1];                                       /* main diagonal */
    if (b[1][1] != ' ' && b[0][2] == b[1][1] && b[1][1] == b[2][0])
        return b[1][1];                                       /* other diagonal */
    return ' ';
}

int main(void)
{
    char board[3][3] = { {'X', 'O', 'X'},
                         {'O', 'X', 'O'},
                         {' ', ' ', 'X'} };

    for (int i = 0; i < 3; i++)
    {
        printf(" %c | %c | %c\n", board[i][0], board[i][1], board[i][2]);
        if (i < 2)
            printf("---+---+---\n");
    }

    char w = winner(board);
    if (w == ' ')
        printf("No winner yet\n");
    else
        printf("Winner: %c\n", w);
    return 0;
}
```
```output
 X | O | X
---+---+---
 O | X | O
---+---+---
   |   | X
Winner: X
```

**Ex 7.94**
```c
#include <stdio.h>

#define ROWS 6

int main(void)
{
    int p[ROWS][ROWS] = {0};

    for (int i = 0; i < ROWS; i++)
    {
        p[i][0] = 1;                                  /* every row starts with 1 */
        for (int j = 1; j <= i; j++)
            p[i][j] = p[i - 1][j - 1] + p[i - 1][j];  /* sum of the two above */
    }

    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j <= i; j++)
            printf("%d ", p[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```
(For `j = i`, `p[i-1][j]` is outside the used part of the previous row, but the array was initialised with zeros, so it adds 0 — that is why we wrote `= {0}`.)

**Ex 7.95**
```c
#include <stdio.h>

#define BRANCHES 3
#define QUARTERS 4

int main(void)
{
    int sales[BRANCHES][QUARTERS] = {
        {120, 150,  90, 200},
        { 80, 110, 130,  95},
        {140, 100, 160, 180}
    };
    int bestBranch = 0, bestBranchTotal = -1;
    int bestQuarter = 0, bestQuarterTotal = -1;

    for (int b = 0; b < BRANCHES; b++)
    {
        int total = 0;
        for (int q = 0; q < QUARTERS; q++)
            total += sales[b][q];
        printf("Branch %d total: %d\n", b + 1, total);
        if (total > bestBranchTotal)
        {
            bestBranchTotal = total;
            bestBranch = b;
        }
    }

    for (int q = 0; q < QUARTERS; q++)
    {
        int total = 0;
        for (int b = 0; b < BRANCHES; b++)
            total += sales[b][q];
        printf("Quarter %d total: %d\n", q + 1, total);
        if (total > bestQuarterTotal)
        {
            bestQuarterTotal = total;
            bestQuarter = q;
        }
    }

    printf("Best branch : %d (%d)\n", bestBranch + 1, bestBranchTotal);
    printf("Best quarter: %d (%d)\n", bestQuarter + 1, bestQuarterTotal);
    return 0;
}
```
```output
Branch 1 total: 560
Branch 2 total: 415
Branch 3 total: 580
Quarter 1 total: 340
Quarter 2 total: 360
Quarter 3 total: 380
Quarter 4 total: 475
Best branch : 3 (580)
Best quarter: 4 (475)
```

**Ex 7.96**
```c
#include <stdio.h>

#define N 3

int main(void)
{
    int m[N][N] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int r[N][N];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            r[j][N - 1 - i] = m[i][j];

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            printf("%3d", r[i][j]);
        printf("\n");
    }
    return 0;
}
```
```output
  7  4  1
  8  5  2
  9  6  3
```
The first row `1 2 3` has become the last column.

**Ex 7.97** For every row and column, keep a "seen" flag for each of the numbers 1–4.
```c
#include <stdio.h>

#define N 4

int isLatinSquare(int g[][N])
{
    for (int i = 0; i < N; i++)
    {
        int rowSeen[N + 1] = {0};
        int colSeen[N + 1] = {0};

        for (int j = 0; j < N; j++)
        {
            int r = g[i][j];          /* value in row i  */
            int c = g[j][i];          /* value in column i */
            if (r < 1 || r > N || c < 1 || c > N)
                return 0;
            if (rowSeen[r] || colSeen[c])
                return 0;             /* a repeat */
            rowSeen[r] = 1;
            colSeen[c] = 1;
        }
    }
    return 1;
}

int main(void)
{
    int good[N][N] = { {1, 2, 3, 4}, {2, 3, 4, 1}, {3, 4, 1, 2}, {4, 1, 2, 3} };
    int bad[N][N]  = { {1, 2, 3, 4}, {2, 3, 4, 1}, {3, 4, 1, 2}, {4, 1, 3, 2} };

    printf("good: %d\n", isLatinSquare(good));
    printf("bad : %d\n", isLatinSquare(bad));
    return 0;
}
```
```output
good: 1
bad : 0
```

---

## Part D3 — Three-dimensional arrays

**Ex 7.98** Using `page * 100 + row * 10 + col` as the value makes it easy to see which element is which.
```c
#include <stdio.h>

int main(void)
{
    int cube[2][3][4];

    for (int p = 0; p < 2; p++)
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 4; c++)
                cube[p][r][c] = p * 100 + r * 10 + c;

    for (int p = 0; p < 2; p++)
    {
        printf("Page %d:\n", p);
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 4; c++)
                printf("%5d", cube[p][r][c]);
            printf("\n");
        }
    }
    return 0;
}
```
```output
Page 0:
    0    1    2    3
   10   11   12   13
   20   21   22   23
Page 1:
  100  101  102  103
  110  111  112  113
  120  121  122  123
```

**Ex 7.99**
```c
#include <stdio.h>

int main(void)
{
    int marks[2][3][2] = {
        { {70, 80}, {60, 90}, {85, 75} },        /* class 0: 3 students x 2 tests */
        { {50, 65}, {95, 85}, {40, 60} }         /* class 1 */
    };

    for (int c = 0; c < 2; c++)
    {
        int classTotal = 0;
        for (int s = 0; s < 3; s++)
        {
            int total = 0;
            for (int t = 0; t < 2; t++)
                total += marks[c][s][t];
            printf("Class %d, student %d total: %d\n", c + 1, s + 1, total);
            classTotal += total;
        }
        printf("Class %d average mark: %.2f\n", c + 1, classTotal / 6.0);
    }
    return 0;
}
```
```output
Class 1, student 1 total: 150
Class 1, student 2 total: 150
Class 1, student 3 total: 160
Class 1 average mark: 76.67
Class 2, student 1 total: 115
Class 2, student 2 total: 180
Class 2, student 3 total: 100
Class 2 average mark: 65.83
```

**Ex 7.100**
```c
#include <stdio.h>

int main(void)
{
    int temp[2][3][4] = {
        { {20, 22, 25, 23}, {19, 21, 24, 22}, {21, 23, 26, 24} },     /* city 0 */
        { {30, 32, 35, 33}, {29, 31, 34, 32}, {31, 33, 36, 34} }      /* city 1 */
    };
    int hottest = temp[0][0][0], hc = 0, hd = 0, hr = 0;

    for (int city = 0; city < 2; city++)
        for (int day = 0; day < 3; day++)
        {
            int sum = 0;
            for (int r = 0; r < 4; r++)
            {
                sum += temp[city][day][r];
                if (temp[city][day][r] > hottest)
                {
                    hottest = temp[city][day][r];
                    hc = city;
                    hd = day;
                    hr = r;
                }
            }
            printf("City %d, day %d: average %.2f\n", city + 1, day + 1, sum / 4.0);
        }

    printf("Hottest reading: %d (city %d, day %d, reading %d)\n", hottest, hc + 1, hd + 1, hr + 1);
    return 0;
}
```
```output
City 1, day 1: average 22.50
City 1, day 2: average 21.50
City 1, day 3: average 23.50
City 2, day 1: average 32.50
City 2, day 2: average 31.50
City 2, day 3: average 33.50
Hottest reading: 36 (city 2, day 3, reading 3)
```

---

## Part E — Challenges and mini-projects

**Ex 7.101**
<!--in: 5 78 45 91 60 85-->
```c
#include <stdio.h>

#define MAX 30

double average(const int marks[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += marks[i];
    return (double) sum / n;
}

int highest(const int marks[], int n)
{
    int h = marks[0];
    for (int i = 1; i < n; i++)
        if (marks[i] > h)
            h = marks[i];
    return h;
}

int lowest(const int marks[], int n)
{
    int l = marks[0];
    for (int i = 1; i < n; i++)
        if (marks[i] < l)
            l = marks[i];
    return l;
}

char gradeOf(int mark)
{
    if (mark >= 80) return 'A';
    if (mark >= 70) return 'B';
    if (mark >= 60) return 'C';
    if (mark >= 50) return 'D';
    return 'F';
}

void printReport(const int marks[], int n)
{
    double avg = average(marks, n);

    printf("\n%-8s %5s %5s\n", "Student", "Mark", "Grade");
    for (int i = 0; i < n; i++)
        printf("%-8d %5d %5c\n", i + 1, marks[i], gradeOf(marks[i]));

    printf("\nAverage: %.2f   Highest: %d   Lowest: %d\n", avg, highest(marks, n), lowest(marks, n));
    printf("Above average: ");
    for (int i = 0; i < n; i++)
        if (marks[i] > avg)
            printf("student %d  ", i + 1);
    printf("\n");
}

int main(void)
{
    int marks[MAX], n;

    printf("Number of students (max %d): ", MAX);
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Mark %d: ", i + 1);
        scanf("%d", &marks[i]);
    }

    printReport(marks, n);
    return 0;
}
```
```output
Number of students (max 30): 5
Mark 1: 78
Mark 2: 45
Mark 3: 91
Mark 4: 60
Mark 5: 85

Student   Mark Grade
1           78     B
2           45     F
3           91     A
4           60     C
5           85     A

Average: 71.80   Highest: 91   Lowest: 45
Above average: student 1  student 3  student 5
```

**Ex 7.102**
```c
#include <stdio.h>

int det2(int m[2][2])
{
    return m[0][0] * m[1][1] - m[0][1] * m[1][0];
}

int det3(int m[3][3])
{
    return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
         - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
         + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
}

int main(void)
{
    int a[2][2] = { {3, 8}, {4, 6} };
    int b[3][3] = { {6, 1, 1}, {4, -2, 5}, {2, 8, 7} };

    printf("det(a) = %d\n", det2(a));
    printf("det(b) = %d\n", det3(b));
    return 0;
}
```
```output
det(a) = -14
det(b) = -306
```

**Ex 7.103**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {1, 3, 5, 2, 4, 6, 8, 9, 1};
    int n = sizeof(a) / sizeof(a[0]);
    int longest = 1, current = 1;

    for (int i = 1; i < n; i++)
    {
        if (a[i] > a[i - 1])
            current++;                  /* the run continues */
        else
            current = 1;                /* the run is broken: start again */
        if (current > longest)
            longest = current;
    }

    printf("Longest increasing run: %d\n", longest);
    return 0;
}
```
```output
Longest increasing run: 5
```

**Ex 7.104**
```c
#include <stdio.h>

int main(void)
{
    int a[] = {3, 2, 3, 3, 5, 2};
    int n = sizeof(a) / sizeof(a[0]);
    int value = 3, k = 0;

    for (int i = 0; i < n; i++)
        if (a[i] != value)
            a[k++] = a[i];              /* keep only the elements that are not 'value' */

    printf("New length: %d\n", k);
    for (int i = 0; i < k; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
New length: 3
2 5 2
```

**Ex 7.105** (Kadane's algorithm) `current` is the best sum of a stretch **ending** at the present element: either extend the previous stretch, or start fresh here — whichever is larger.
```c
#include <stdio.h>

int main(void)
{
    int a[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(a) / sizeof(a[0]);
    int current = a[0], best = a[0];

    for (int i = 1; i < n; i++)
    {
        current = (current + a[i] > a[i]) ? current + a[i] : a[i];
        if (current > best)
            best = current;
    }

    printf("Maximum sub-array sum: %d\n", best);
    return 0;
}
```
```output
Maximum sub-array sum: 6
```
(The best stretch is `4 −1 2 1`.)

**Ex 7.106** Keep four boundaries (`top`, `bottom`, `left`, `right`) and shrink them as each side is printed.
```c
#include <stdio.h>

#define N 4

int main(void)
{
    int m[N][N], value = 1;
    int top = 0, bottom = N - 1, left = 0, right = N - 1;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            m[i][j] = value++;

    while (top <= bottom && left <= right)
    {
        for (int j = left; j <= right; j++)        /* top row, left to right */
            printf("%d ", m[top][j]);
        top++;

        for (int i = top; i <= bottom; i++)        /* right column, top to bottom */
            printf("%d ", m[i][right]);
        right--;

        if (top <= bottom)
        {
            for (int j = right; j >= left; j--)    /* bottom row, right to left */
                printf("%d ", m[bottom][j]);
            bottom--;
        }
        if (left <= right)
        {
            for (int i = bottom; i >= top; i--)    /* left column, bottom to top */
                printf("%d ", m[i][left]);
            left++;
        }
    }
    printf("\n");
    return 0;
}
```
```output
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
```

**Ex 7.107** We use the *high* bits of the generator (`state >> 16`): the lowest bits of this kind of generator are not very random.
```c
#include <stdio.h>

unsigned int nextRandom(void)
{
    static unsigned int state = 12345;
    state = (state * 1103515245u + 12345u) & 0x7fffffffu;
    return state >> 16;
}

int main(void)
{
    int count[7] = {0};                 /* count[1..6]; index 0 unused */

    for (int i = 0; i < 600; i++)
        count[nextRandom() % 6 + 1]++;

    for (int face = 1; face <= 6; face++)
    {
        printf("%d: %3d ", face, count[face]);
        for (int s = 0; s < count[face] / 5; s++)       /* one star per 5 rolls */
            printf("*");
        printf("\n");
    }
    return 0;
}
```
```output
1: 112 **********************
2: 104 ********************
3: 102 ********************
4:  83 ****************
5: 101 ********************
6:  98 *******************
```
Each face should appear about 100 times (600 ÷ 6). Small differences are normal — that's what "random" looks like.

**Ex 7.108** Add from the **least significant** bit (index 0), carrying to the next position.
```c
#include <stdio.h>

#define BITS 4

int main(void)
{
    int a[BITS] = {1, 1, 0, 1};          /* 1011 = 11 (least significant bit first) */
    int b[BITS] = {0, 1, 1, 0};          /* 0110 = 6 */
    int sum[BITS + 1];
    int carry = 0;

    for (int i = 0; i < BITS; i++)
    {
        int s = a[i] + b[i] + carry;
        sum[i] = s % 2;
        carry = s / 2;
    }
    sum[BITS] = carry;

    printf("Result: ");
    for (int i = BITS; i >= 0; i--)
        printf("%d", sum[i]);
    printf("\n");
    return 0;
}
```
```output
Result: 10001
```
(11 + 6 = 17 = `10001` in binary ✔.)

---

## Part F — Research tasks (sample answers)

**Ex 7.109** When you pass an array to a function, C passes only the **address of its first element**; inside the function, the parameter `arr` is just a pointer variable. `sizeof(arr)` therefore returns the size of a *pointer* (8 bytes on 64-bit machines), not of the whole array. `sizeof` can only see the true size where the array is *declared*.
```c
#include <stdio.h>

void show(int arr[])
{
    printf("inside the function: %zu bytes\n", sizeof(arr));
}

int main(void)
{
    int a[5] = {1, 2, 3, 4, 5};

    printf("in main            : %zu bytes\n", sizeof(a));
    show(a);
    return 0;
}
```
```output
in main            : 20 bytes
inside the function: 8 bytes
```
(On a 32-bit system the second line prints 4.)

**Ex 7.110** A **variable-length array** is an array whose size is a *run-time* value: `int n; scanf("%d", &n); int a[n];`. It was introduced in **C99**, became *optional* in C11, and some compilers (e.g. Microsoft's) never supported it. Programmers avoid it because a large `n` can overflow the stack and crash the program with no warning, and because the code is not portable. Alternatives: a fixed maximum size (as in this chapter), or **dynamic memory** with `malloc` (a later topic).

**Ex 7.111** `qsort(array, count, size_of_one_element, compare)`. The comparison function receives two **addresses** and returns a negative number, zero or a positive number.
```c
#include <stdio.h>
#include <stdlib.h>

int compareInts(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    return (x > y) - (x < y);            /* -1, 0 or 1 */
}

int main(void)
{
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), compareInts);

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
```output
11 12 22 25 34 64 90
```
(The `const void *` and `*(const int *)p` syntax is pointers — Chapter 8. `compareInts` is passed as a **function pointer**.)

**Ex 7.112** It means the array's name is really the **address of its first element**, and `a[i]` is just a notation for "go `i` elements past that address and take what is there". Arrays and pointers are two faces of the same idea.
```c
#include <stdio.h>

int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};

    printf("%d %d\n", a[2], *(a + 2));
    return 0;
}
```
```output
30 30
```

---

*Next: [Chapter 8 solutions](08-pointers-and-strings.md)*
