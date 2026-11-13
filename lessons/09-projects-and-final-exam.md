# Chapter 9 — Projects and Final Exam

> **Course:** COE 281 — Programming and Problem-Solving 1  
> **Covers:** everything — Chapters 0 to 8  
> **Solutions to the exam:** [Exam solutions](../solutions/09-projects-and-final-exam.md)

---

## What you will do

1. Learn a **method** for building a bigger program without getting lost.
2. Study **four complete mini-projects**, each combining decisions, loops, functions, arrays, strings and pointers.
3. Pick **project ideas** to build on your own.
4. Sit a **mock final exam** (3 hours, 100 marks) with a full marking scheme.

---

# PART 1 — From problem to program

## 9.1 A method for building programs

Your slides (Chapter 0) taught you how to *think*: **define the problem, use examples, divide and conquer, write notes.** Now we apply it to code. Follow these steps every time:

| Step | What you do | Example (Student Manager) |
|---|---|---|
| **1. Understand** | Write what the program must do, in plain words. List **inputs** and **outputs**. | "Store up to 20 students with a mark; list them; show statistics; search; rank." |
| **2. Choose the data** | Decide which **variables / arrays** hold the information. (Chapter 0: data structures!) | Parallel arrays: `names[20][30]` and `marks[20]`, plus a counter. |
| **3. Divide** | Split into **functions**, one job each. Write only the **prototypes** first. | `addStudent`, `listStudents`, `showStats`, `searchStudent`, `showRanking`. |
| **4. Write `main` first** | `main` is a short menu loop calling the functions. | `do { menu; switch (choice) … } while (choice != 6);` |
| **5. Build one function at a time** | Write a function, **test it alone**, then add the next. | Test `addStudent` + `listStudents` before anything else. |
| **6. Test with tricky input** | Empty data, one item, a full array, wrong input, negative numbers… | "What if the list is empty?" |
| **7. Clean up** | Meaningful names, comments for *why*, no repeated code. | |

> 💡 **Never write 200 lines and then compile.** Write 10 lines, compile, test. Small steps → small bugs.

## 9.2 Passing the program's data around

Good programs avoid global variables, so functions receive what they need as **parameters**:

- An **array** is passed as its address (so the function can change it) — with its **size** (or a counter) as a separate parameter.
- A **counter** that a function must **change** (like "number of students") is passed **by pointer** (`int *count`).
- Things the function only **reads** are marked `const`.

You will see all three in the projects.

---

# PART 2 — Four worked projects

## Project 1 — Student Records Manager

**Goal.** Keep a class list (name + mark) for up to 20 students. A menu lets the teacher add students, list them, see statistics, search by name, and see a **ranking** (highest mark first).

**Design.**
- Data: `names[MAX][30]` (a 2D `char` array: one string per row), `marks[MAX]` and `count` (how many students are stored).
- To rank the students **without moving the names around**, we sort an array of **indices** (`order[]`): `order[0]` is the index of the best student, `order[1]` the second best, and so on. This is a very useful trick.

<!--in: 1 Kofi 72\n1 Ama 85\n1 Yaw 60\n2\n3\n4 Ama\n4 Esi\n5\n6-->
```c
#include <stdio.h>
#include <string.h>

#define MAX 20
#define NAME_LEN 30

void addStudent(char names[][NAME_LEN], int marks[], int *count);
void listStudents(char names[][NAME_LEN], const int marks[], int count);
void showStats(char names[][NAME_LEN], const int marks[], int count);
void searchStudent(char names[][NAME_LEN], const int marks[], int count);
void showRanking(char names[][NAME_LEN], const int marks[], int count);

int main(void)
{
    char names[MAX][NAME_LEN];
    int marks[MAX];
    int count = 0;
    int choice;

    do
    {
        printf("\n=== STUDENT MANAGER ===\n");
        printf("1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1: addStudent(names, marks, &count);      break;
            case 2: listStudents(names, marks, count);     break;
            case 3: showStats(names, marks, count);        break;
            case 4: searchStudent(names, marks, count);    break;
            case 5: showRanking(names, marks, count);      break;
            case 6: printf("Goodbye!\n");                  break;
            default: printf("Invalid choice.\n");
        }
    }
    while (choice != 6);

    return 0;
}

void addStudent(char names[][NAME_LEN], int marks[], int *count)
{
    if (*count == MAX)
    {
        printf("The class is full.\n");
        return;
    }
    printf("Name and mark: ");
    scanf("%29s %d", names[*count], &marks[*count]);
    (*count)++;                                    /* changes the caller's counter */
    printf("Student added.\n");
}

void listStudents(char names[][NAME_LEN], const int marks[], int count)
{
    printf("\n%-4s %-15s %5s\n", "No.", "Name", "Mark");
    for (int i = 0; i < count; i++)
        printf("%-4d %-15s %5d\n", i + 1, names[i], marks[i]);
}

void showStats(char names[][NAME_LEN], const int marks[], int count)
{
    if (count == 0)
    {
        printf("No students yet.\n");
        return;
    }

    int best = 0, worst = 0, sum = 0;
    for (int i = 0; i < count; i++)
    {
        sum += marks[i];
        if (marks[i] > marks[best])  best = i;
        if (marks[i] < marks[worst]) worst = i;
    }

    printf("Average: %.2f\n", (double) sum / count);
    printf("Highest: %s (%d)\n", names[best], marks[best]);
    printf("Lowest : %s (%d)\n", names[worst], marks[worst]);
}

void searchStudent(char names[][NAME_LEN], const int marks[], int count)
{
    char key[NAME_LEN];

    printf("Name to search: ");
    scanf("%29s", key);

    for (int i = 0; i < count; i++)
        if (strcmp(names[i], key) == 0)
        {
            printf("%s scored %d\n", names[i], marks[i]);
            return;
        }
    printf("%s was not found.\n", key);
}

void showRanking(char names[][NAME_LEN], const int marks[], int count)
{
    int order[MAX];

    for (int i = 0; i < count; i++)
        order[i] = i;                              /* start with 0, 1, 2, ... */

    for (int pass = 0; pass < count - 1; pass++)   /* bubble sort the INDICES by mark */
        for (int j = 0; j < count - 1 - pass; j++)
            if (marks[order[j]] < marks[order[j + 1]])
            {
                int t = order[j];
                order[j] = order[j + 1];
                order[j + 1] = t;
            }

    printf("\n%-5s %-15s %5s\n", "Rank", "Name", "Mark");
    for (int r = 0; r < count; r++)
        printf("%-5d %-15s %5d\n", r + 1, names[order[r]], marks[order[r]]);
}
```
```output
=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 1
Name and mark: Kofi 72
Student added.

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 1
Name and mark: Ama 85
Student added.

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 1
Name and mark: Yaw 60
Student added.

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 2

No.  Name            Mark
1    Kofi               72
2    Ama                85
3    Yaw                60

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 3
Average: 72.33
Highest: Ama (85)
Lowest : Yaw (60)

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 4
Name to search: Ama
Ama scored 85

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 4
Name to search: Esi
Esi was not found.

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 5

Rank  Name            Mark
1     Ama                85
2     Kofi               72
3     Yaw                60

=== STUDENT MANAGER ===
1) Add  2) List  3) Statistics  4) Search  5) Ranking  6) Exit
Choose: 6
Goodbye!
```

**What to notice**
- `main` is tiny: it only shows the menu and calls functions.
- `count` is passed **by pointer** to `addStudent` (so the function can add 1), and by value to the others (they only read it).
- The `const` on `marks[]` promises that listing/searching won't change the marks.
- Ranking sorts the *indices*, so `names` and `marks` stay in the original order.

**Extend it:** delete a student; edit a mark; grade letters; reject marks outside 0–100; stop adding when `MAX` is reached (already done!); count passes and failures.

---

## Project 2 — Tic-Tac-Toe (two players)

**Goal.** Two people take turns at the keyboard. Cells are numbered 1–9. The program must refuse illegal moves, detect a winner and detect a draw.

**Design.** The board is a **2D char array** `char board[3][3]`. Cell number `n` (1–9) is at row `(n − 1) / 3`, column `(n − 1) % 3`. Functions: `initBoard`, `printBoard`, `placeMark`, `winner`, `isFull`.

In the sample game below X plays 1, O plays 4, X plays 2, O tries 2 (**already taken!**), then plays 5, and X plays 3 to win the top row.

<!--in: 1 4 2 2 5 3-->
```c
#include <stdio.h>

void initBoard(char b[3][3]);
void printBoard(char b[3][3]);
int placeMark(char b[3][3], int cell, char player);
char winner(char b[3][3]);
int isFull(char b[3][3]);

int main(void)
{
    char board[3][3];
    char player = 'X';
    int cell;

    initBoard(board);

    while (1)
    {
        printBoard(board);
        printf("Player %c, choose a cell (1-9): ", player);
        scanf("%d", &cell);

        if (!placeMark(board, cell, player))
        {
            printf("Invalid move, try again.\n");
            continue;                                  /* same player tries again */
        }

        if (winner(board) != ' ')
        {
            printBoard(board);
            printf("Player %c wins!\n", player);
            break;
        }
        if (isFull(board))
        {
            printBoard(board);
            printf("It's a draw!\n");
            break;
        }

        player = (player == 'X') ? 'O' : 'X';          /* switch turns */
    }
    return 0;
}

void initBoard(char b[3][3])
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            b[i][j] = ' ';
}

void printBoard(char b[3][3])
{
    printf("\n");
    for (int i = 0; i < 3; i++)
    {
        printf(" %c | %c | %c\n", b[i][0], b[i][1], b[i][2]);
        if (i < 2)
            printf("---+---+---\n");
    }
    printf("\n");
}

int placeMark(char b[3][3], int cell, char player)
{
    if (cell < 1 || cell > 9)
        return 0;                                      /* outside the board */

    int row = (cell - 1) / 3;
    int col = (cell - 1) % 3;

    if (b[row][col] != ' ')
        return 0;                                      /* already taken */

    b[row][col] = player;
    return 1;
}

char winner(char b[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        if (b[i][0] != ' ' && b[i][0] == b[i][1] && b[i][1] == b[i][2])
            return b[i][0];                            /* a row */
        if (b[0][i] != ' ' && b[0][i] == b[1][i] && b[1][i] == b[2][i])
            return b[0][i];                            /* a column */
    }
    if (b[1][1] != ' ' && b[0][0] == b[1][1] && b[1][1] == b[2][2])
        return b[1][1];                                /* diagonal */
    if (b[1][1] != ' ' && b[0][2] == b[1][1] && b[1][1] == b[2][0])
        return b[1][1];                                /* other diagonal */
    return ' ';
}

int isFull(char b[3][3])
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (b[i][j] == ' ')
                return 0;
    return 1;
}
```
```output

   |   |
---+---+---
   |   |
---+---+---
   |   |

Player X, choose a cell (1-9): 1

 X |   |
---+---+---
   |   |
---+---+---
   |   |

Player O, choose a cell (1-9): 4

 X |   |
---+---+---
 O |   |
---+---+---
   |   |

Player X, choose a cell (1-9): 2

 X | X |
---+---+---
 O |   |
---+---+---
   |   |

Player O, choose a cell (1-9): 2
Invalid move, try again.

 X | X |
---+---+---
 O |   |
---+---+---
   |   |

Player O, choose a cell (1-9): 5

 X | X |
---+---+---
 O | O |
---+---+---
   |   |

Player X, choose a cell (1-9): 3

 X | X | X
---+---+---
 O | O |
---+---+---
   |   |

Player X wins!
```

**What to notice**
- `placeMark` **returns** 1 or 0 to say whether the move was legal — so `main` doesn't need to know *why* it failed.
- The `continue` statement restarts the loop *without* switching players.
- The turn switch uses the conditional operator: `player = (player == 'X') ? 'O' : 'X';`.
- All the "rules" live in small functions, which makes them easy to test (and to reuse for Ex 7.93).

**Extend it:** play against the computer (it picks the first empty cell, then a smarter move); ask "Play again?"; keep a score table over several games.

---

## Project 3 — Matrix Calculator

**Goal.** Read two 3 × 3 matrices **A** and **B**, then let the user add them, multiply them, transpose **A**, or compute the determinant of **A**.

**Design.** Matrices are `int m[3][3]`. Each operation is a function. Functions that *produce* a matrix take an extra **output** matrix parameter to fill (arrays can't be returned).

Input: **A** = `2 1 0 / 5 3 1 / 0 1 4`, **B** = `1 0 2 / 0 1 0 / 3 0 1`, then menu choices 1 (add), 2 (multiply), 3 (transpose A), 4 (determinant of A), 5 (exit).

<!--in: 2 1 0 5 3 1 0 1 4\n1 0 2 0 1 0 3 0 1\n1\n2\n3\n4\n5-->
```c
#include <stdio.h>

#define N 3

void readMatrix(int m[N][N], const char *name);
void printMatrix(int m[N][N], const char *title);
void addMatrices(int a[N][N], int b[N][N], int result[N][N]);
void multiplyMatrices(int a[N][N], int b[N][N], int result[N][N]);
void transpose(int a[N][N], int result[N][N]);
int determinant(int m[N][N]);

int main(void)
{
    int a[N][N], b[N][N], result[N][N];
    int choice;

    readMatrix(a, "A");
    readMatrix(b, "B");

    do
    {
        printf("\n1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                addMatrices(a, b, result);
                printMatrix(result, "A + B");
                break;
            case 2:
                multiplyMatrices(a, b, result);
                printMatrix(result, "A x B");
                break;
            case 3:
                transpose(a, result);
                printMatrix(result, "Transpose of A");
                break;
            case 4:
                printf("det(A) = %d\n", determinant(a));
                break;
            case 5:
                printf("Goodbye!\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    }
    while (choice != 5);

    return 0;
}

void readMatrix(int m[N][N], const char *name)
{
    printf("Enter the %d elements of %s, row by row: ", N * N, name);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            scanf("%d", &m[i][j]);
}

void printMatrix(int m[N][N], const char *title)
{
    printf("%s:\n", title);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            printf("%5d", m[i][j]);
        printf("\n");
    }
}

void addMatrices(int a[N][N], int b[N][N], int result[N][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            result[i][j] = a[i][j] + b[i][j];
}

void multiplyMatrices(int a[N][N], int b[N][N], int result[N][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            result[i][j] = 0;
            for (int k = 0; k < N; k++)
                result[i][j] += a[i][k] * b[k][j];
        }
}

void transpose(int a[N][N], int result[N][N])
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            result[j][i] = a[i][j];
}

int determinant(int m[N][N])
{
    return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
         - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
         + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
}
```
```output
Enter the 9 elements of A, row by row: 2 1 0 5 3 1 0 1 4
Enter the 9 elements of B, row by row: 1 0 2 0 1 0 3 0 1

1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit
Choose: 1
A + B:
    3    1    2
    5    4    1
    3    1    5

1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit
Choose: 2
A x B:
    2    1    4
    8    3   11
   12    1    4

1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit
Choose: 3
Transpose of A:
    2    5    0
    1    3    1
    0    1    4

1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit
Choose: 4
det(A) = 2

1) A + B  2) A x B  3) Transpose of A  4) Determinant of A  5) Exit
Choose: 5
Goodbye!
```

**Check one entry by hand:** `(A×B)[1][2]` = row 1 of A × column 2 of B = `5·2 + 3·0 + 1·1 = 11` ✔.

**Extend it:** let the user choose the matrix size (use a maximum size and pass the real size as a parameter); subtraction; scalar multiplication; inverse of a 2 × 2 matrix; detect when multiplication is impossible.

---

## Project 4 — Mini Bank (ATM) with a mini-statement

**Goal.** A customer logs in with a PIN (3 attempts), then can check the balance, deposit, withdraw and view a **mini-statement** of the last 5 transactions.

**Design.**
- The transaction history is a 2D char array: `history[5][40]`, one text line per transaction, built with `snprintf`.
- When the history is full, the oldest line is dropped (everything shifts up one row) — the same *shifting* idea you used to delete an element from an array.
- Input: PIN `1111` (wrong), `1234` (right); then deposit 500, withdraw 200, try to withdraw 1500 (refused — the balance is only 1300), see balance, see statement, exit.

<!--in: 1111\n1234\n2 500\n3 200\n3 1500\n1\n4\n5-->
```c
#include <stdio.h>
#include <string.h>

#define HISTORY 5
#define ENTRY 40
#define CORRECT_PIN 1234

void record(char history[][ENTRY], int *entries, const char *text)
{
    if (*entries == HISTORY)                       /* full: drop the oldest line */
    {
        for (int i = 1; i < HISTORY; i++)
            strcpy(history[i - 1], history[i]);
        (*entries)--;
    }
    snprintf(history[*entries], ENTRY, "%s", text);
    (*entries)++;
}

int login(void)
{
    int pin;

    for (int attempt = 1; attempt <= 3; attempt++)
    {
        printf("Enter PIN: ");
        scanf("%d", &pin);
        if (pin == CORRECT_PIN)
            return 1;
        printf("Wrong PIN (%d attempt(s) left)\n", 3 - attempt);
    }
    return 0;
}

void showStatement(char history[][ENTRY], int entries)
{
    printf("--- Mini statement ---\n");
    if (entries == 0)
        printf("(no transactions)\n");
    for (int i = entries - 1; i >= 0; i--)         /* newest first */
        printf("%s\n", history[i]);
}

int main(void)
{
    double balance = 1000.00;
    char history[HISTORY][ENTRY];
    int entries = 0;
    int choice;
    double amount;
    char line[ENTRY];

    if (!login())
    {
        printf("Card blocked.\n");
        return 0;
    }

    do
    {
        printf("\n1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Balance: GHS %.2f\n", balance);
                break;
            case 2:
            case 3:
                scanf("%lf", &amount);
                if (amount <= 0)
                {
                    printf("Amount must be positive.\n");
                }
                else if (choice == 2)
                {
                    balance += amount;
                    snprintf(line, sizeof(line), "Deposit   GHS %9.2f", amount);
                    record(history, &entries, line);
                    printf("Deposited GHS %.2f\n", amount);
                }
                else if (amount > balance)
                {
                    printf("Insufficient funds.\n");
                }
                else
                {
                    balance -= amount;
                    snprintf(line, sizeof(line), "Withdrawal GHS %9.2f", amount);
                    record(history, &entries, line);
                    printf("Please take your cash: GHS %.2f\n", amount);
                }
                break;
            case 4:
                showStatement(history, entries);
                break;
            case 5:
                printf("Thank you. Goodbye!\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    }
    while (choice != 5);

    return 0;
}
```
```output
Enter PIN: 1111
Wrong PIN (2 attempt(s) left)
Enter PIN: 1234

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 2 500
Deposited GHS 500.00

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 3 200
Please take your cash: GHS 200.00

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 3 1500
Insufficient funds.

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 1
Balance: GHS 1300.00

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 4
--- Mini statement ---
Withdrawal GHS    200.00
Deposit   GHS    500.00

1) Balance  2) Deposit  3) Withdraw  4) Statement  5) Exit
Choose: 5
Thank you. Goodbye!
```

**What to notice**
- `login()` returns `1` or `0` — a function that answers a yes/no question.
- `record` takes the entry counter **by pointer** because it changes it.
- The `case 2:` / `case 3:` fall-through shares the "read and validate the amount" code.
- Real banking software never stores money in `double` (rounding errors!) — it uses whole pesewas. Why is that safer? (Think of Ex 2.44.)

**Extend it:** several accounts (arrays) with a **transfer** function using pointers; PIN change; daily withdrawal limit; a `static` transaction counter.

---

# PART 3 — Project ideas for you

Pick **two** and build them using the method of section 9.1. Use arrays, functions and (where it fits) pointers and strings.

| # | Project | Skills it practises |
|---|---|---|
| 1 | **Inventory system** for a shop — add/sell items, warn when stock is low, total stock value | parallel arrays, menus, validation |
| 2 | **Payroll calculator** — read employees' hours and rates, compute overtime and tax bands, print payslips | decisions, loops, formatted output |
| 3 | **Library manager** — add books, borrow/return (a book can't be borrowed twice), list available books | arrays of strings, flags, search |
| 4 | **Parking-fee system** — enter/leave times as `hh:mm`, compute the fee with a daily maximum | time arithmetic, functions |
| 5 | **Temperature logger** — store 7 days × 4 readings, find the hottest day, averages, a text "graph" | 2D arrays, statistics, patterns |
| 6 | **Vigenère cipher** — encrypt/decrypt text with a keyword (a stronger Caesar cipher) | strings, `%` arithmetic |
| 7 | **Connect Four** — 6 × 7 board, gravity, win detection (4 in a row) | 2D arrays, nested loops |
| 8 | **Sudoku validator** — decide whether a filled 9 × 9 grid is a valid solution | 2D arrays, counting arrays |
| 9 | **Voting system** — candidates, votes stored in arrays, count, winner, tie detection, percentage bars | arrays, strings, sorting |
| 10 | **Bank with several accounts** — transfer between accounts using pointers, a log of the last transactions | pointers, functions, static |

---

# PART 4 — Mock final exam

> **Time:** 3 hours · **Total:** 100 marks · **Calculator:** not needed
> **Instructions:** Answer **all** questions. Write clear, indented C code. In programming questions, marks are awarded for **correct logic**, **good structure (functions)** and **meaningful names**, not only for the final output. Assume a typical system where `int` is 4 bytes.
>
> *Do the exam under real conditions first (on paper, no compiler!), then compare with the solutions and the marking scheme.*

## Section A — Multiple choice (20 marks · 1 mark each)

Choose the **one** best answer.

**A1.** Which of these is a **valid** C identifier?
(a) `2fast` (b) `my-var` (c) `total_sum` (d) `float`

**A2.** C is best described as a…
(a) interpreted language (b) compiled language (c) markup language (d) query language

**A3.** The value of `7 / 2` when both operands are `int` is…
(a) 3.5 (b) 3 (c) 4 (d) 3.0

**A4.** What is printed by `printf("%d", 5 > 3 && 2 > 4);`?
(a) 1 (b) 0 (c) 5 (d) true

**A5.** After `int x = 10; x %= 4;` the value of `x` is…
(a) 0 (b) 1 (c) 2 (d) 4

**A6.** In a `switch` statement, if `break` is omitted at the end of a matched case…
(a) the compiler reports an error (b) the program stops (c) execution continues into the next case (d) the `default` is skipped

**A7.** Which loop is guaranteed to run its body **at least once**?
(a) `for` (b) `while` (c) `do … while` (d) none of them

**A8.** How many times does the body of `for (i = 1; i < 10; i += 3)` run?
(a) 2 (b) 3 (c) 4 (d) 9

**A9.** Which is a correct function **prototype**?
(a) `int add(int a, int b)` (b) `int add(int, int);` (c) `add(int, int) int;` (d) `function int add(int, int);`

**A10.** A `static` local variable…
(a) is visible in all functions (b) cannot be changed (c) keeps its value between calls (d) is created fresh on every call

**A11.** In a recursive function, the **base case** is…
(a) the first call (b) the condition that stops the recursion (c) the largest input (d) the return type

**A12.** The valid indices of `int a[8]` are…
(a) 1 to 8 (b) 0 to 8 (c) 0 to 7 (d) 1 to 7

**A13.** For `int a[10];` (4-byte `int`), `sizeof(a) / sizeof(a[0])` equals…
(a) 4 (b) 10 (c) 40 (d) 1

**A14.** In `int m[3][4];`, the element `m[1][2]` is in…
(a) row 2, column 1 (b) row 1, column 2 (c) the 12th element counted from 1 (d) out of bounds

**A15.** A pointer is a variable that stores…
(a) a value of any type (b) the address of another variable (c) a function (d) a string

**A16.** If `int x = 5; int *p = &x;` then `*p` is…
(a) the address of `x` (b) the address of `p` (c) 5 (d) undefined

**A17.** Which function is the **safe** way to read a line of text?
(a) `gets` (b) `fgets` (c) `getchar` (d) `scanf("%d")`

**A18.** `strlen("Accra")` returns…
(a) 4 (b) 5 (c) 6 (d) 7

**A19.** To check whether two strings are equal you should use…
(a) `a == b` (b) `a = b` (c) `strcmp(a, b) == 0` (d) `strcpy(a, b)`

**A20.** How many bytes does `char s[] = "Hi";` occupy?
(a) 2 (b) 3 (c) 4 (d) 8

## Section B — Short answers (24 marks · 3 marks each)

**B1.** What is printed?
```c
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
```

**B2.** What is printed?
```c
int g(int n)
{
    if (n == 0)
        return 0;
    return n % 10 + g(n / 10);
}
/* in main: */
printf("%d\n", g(2026));
```

**B3.** What is printed? Explain in one sentence what `f` does.
```c
void f(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
/* in main: */
int x = 4, y = 9;
f(&x, &y);
printf("%d %d\n", x, y);
```

**B4.** What is printed?
```c
int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
int s = 0;
for (int i = 0; i < 3; i++)
    s += m[i][2 - i];
printf("%d\n", s);
```

**B5.** What is printed?
```c
char s[] = "KNUST";
s[2] = '\0';
printf("%s %zu %zu\n", s, strlen(s), sizeof(s));
```

**B6.** Explain, with a short example, the difference between **passing by value** and **passing by reference** in C.

**B7.** A student writes `char *s = "hi"; s[0] = 'H';`. What is the problem? How should the declaration be changed?

**B8.** What is printed?
```c
for (int i = 1; i <= 3; i++)
{
    for (int j = i; j <= 3; j++)
        printf("%d", i * j);
    printf("-");
}
```

## Section C — Debugging (10 marks · 5 marks each)

**C1.** The program below is supposed to print `Average = 80.00` for the five marks. It contains **five** mistakes. Find and correct them all.
<!--skip-->
```c
#include <stdio.h>

int average(int a[], int n)
{
    int sum;
    for (int i = 0; i <= n; i++)
        sum += a[i];
    return sum / n;
}

int main(void)
{
    int marks[5] = {60, 70, 80, 90, 100};
    printf("Average = %.2f\n", average(marks));
    return 0;
}
```

**C2.** The program below contains **five** mistakes involving strings and pointers. Find them and say how to fix each.
<!--skip-->
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char city[5] = "Accra";
    char copy[10];
    copy = city;
    if (city == "Accra")
        printf("same\n");
    int *p;
    *p = strlen(city);
    gets(copy);
    return 0;
}
```

## Section D — Programming (46 marks)

**D1. (8 marks)** Write a function `int countVowels(const char *s)` that returns the number of vowels (upper or lower case) in the string `s`. Then write a `main` that reads a line of text with a **safe** function and prints the number of vowels and the number of other characters (excluding the final newline).

**D2. (10 marks)** Write a program that:
1. reads `n` (at most 50) and then `n` integers into an array;
2. has a function `double mean(const int a[], int n)`;
3. has a function `int countAbove(const int a[], int n, double limit)` returning how many elements are greater than `limit`;
4. has a function `void sortDescending(int a[], int n)`;
5. prints the mean, how many numbers are above the mean, and the numbers sorted from largest to smallest.

**D3. (12 marks)** A small shop program keeps up to 10 items. Each item has a **name** (one word) and a **price**. Write a **menu-driven** program (loop until Exit) with the options **1) Add item**, **2) List items**, **3) Show total price of all items**, **4) Exit**. Use arrays, and put each option in its own function. Refuse to add an item when the shop list is full or the price is not positive.

**D4. (16 marks)** Write a **matrix toolkit** for 3 × 3 integer matrices:
- (a) `void transpose(int m[3][3])` — transposes the matrix **in place** (4 marks);
- (b) `int isSymmetric(int m[3][3])` — returns 1 if `m[i][j] == m[j][i]` for all `i`, `j` (3 marks);
- (c) `void traceAndMax(int m[3][3], int *trace, int *max)` — returns the **trace** (sum of the main diagonal) and the **largest element**, **using pointers** (4 marks);
- (d) a **recursive** function `int gcd(int a, int b)` (3 marks);
- (e) a `main` that tests all four functions with sample data and prints the results (2 marks).

---

*End of the exam. Compare your answers with [the solutions and marking scheme](../solutions/09-projects-and-final-exam.md).*

*Congratulations on reaching the end of the course! Keep the habit: **think first, code in small steps, test, and read the error messages.***
