### Introduction

#### 01. Arrays 

- Collection of similar data elements
```
// Create a 5-ints space.
// If 1 int takes 2 bytes, total 10 bytes space is allocated

int A[5];
```
This array will be created in `code section` of `main memory` and will be directly accessible to the `main` function. 

- Main memory is divided into 3 main sections
    - Heap
    - Stack
    - Code Section
```
------[Main Memory------]
|-----------------------| -------
|                       |    |
|                       |  [Heap]
|                       |    |
|-----------------------| -------
|                       |    | 
|                       |    |
|-----------------------|    |
|                       |  [Stack]
|         Main          |    |
|-----------------------| --------
|                       |    |
|                       |    |
|    main .........     |    |
|    ..............     |  [Code]
|    ..............     |    |
|                       |    |
|-----------------------| --------
------[Main Memory------]
```

- i. Declaration
    ```
    int a[5];
    ```

- ii. Initatialisation
    ```
    int B[5] = {2, 9, 6, 3, 10}
    ```

- iii. Accessing
    ```
    for (int i=0; i<5; i++)
        printf("%d", B[i]);
    ```


#### 02. Stucture

- Collection of related data-items under one name
- User Defined Data Type 

example snippet 1:
```
// This is a definition.

struc rectangle 
{
    int length; // let 2 bytes
    float breadth; // let 4 bytes
}
```

example snippet 2:
```
// This is a definition.

struc Rectangle 
{
    int length; // let 2 bytes
    float breadth; // let 4 bytes
}

int main()
{
    // i. Declaration
    // ---------------
    struct Rectangle r;

    // ii. Declaration & Initialisation
    // Note: Created inside `stack` section
    // of main memory 
    // ---------------------------------
    struct Rectange r = {10, 5}

    // iii. Access or Modify
    // ---------------------
    r.length = 15;
    r.breadth = 10;

    // eg. Area
    printf( r.length * r. breadth)
}
```

**Memory consumed:**
    
    - Snippet 1: `0 bytes`
    - Snippet 2: `6 bytes`

*Definitions do not consume any memory(eg. Above code)! If we create variable of that defn. memory is consumed.*


Example, `Complex number`, `Student`, `Book`, `Playing cards` etc.

-  Array of structures
```
struct Card deck[52];
```
This creates 52 cards, each of type `Card`.

```
// i. Initialize
// -------------
struct Card deck[52] = {
    {1, 0, 0}, // {face, shape, color}
    {2, 0, 0},
    {2, 1, 0},
    .
    .
    . 
    // upto 52 cards
}

// ii. Access
// ----------
printf( deck[33].face )
```

#### 03. Pointers

- Stores address of data. Used to access data *indirectly*.

*But why access indirectly?* 

our *program* can access **both** `code section` and `stack section` but **cannot** access `heap section` of main memory. 

*To access heap memory we need pointers! Pointers are used to access resources that that are outside our program.* 

*Another example is a file in hard-disk or a keyboard or a mouse or even Internet!!!.*

- **Main uses of Pointers**

    - Access Heap
    - Access External Resources
    - Parameter Passing

- **How to use Pointers**

    - i. Declaration
    - ii. Initialisation
    - iii. Dereferencing
    - iv. Dynamic Allocation

Consider this code:
```
int main(){
    
    int a = 10; // data variable
    int *p;     // address variable
}
```

**Note:** `p` is called address variable if there is `*` infront of it during initialisation. 

This creates storage space for `a` and `p` in main memory. Both are int so let us take 2 bytes each –

```
------[Main Memory------]
+-----------------------+ -------
|                       |    |
|                       |  [Heap]
|                       |    |
+-----------------------+ -------
|                       |    | 
|                       |    |
+-----------------------+    |
|      a         p      |  [Stack]
|     [10]      [ ]     |    |
|   200/201   210/211   |    |
+-----------------------+ --------
|                       |    |
|                       |    |
|    main .........     |    |
|    ..............     |  [Code]
|    ..............     |    |
|                       |    |
+-----------------------+ --------
------[Main Memory------]
```

```
               a
        +------+------+
        |      |      | Data: 10
        |      |      |
        +------+------+
        200    201



               p
        +------+------+
        |      |      | Data: <garbage>
        |      |      |
        +------+------+
        210    211
```

Both data variable and address variable (differentiated by `*`) are treated the EXACTLY the same way and allocated space in main section of stack.

But when we write
```
p = & a; 
```
Something interesting happens –

**Note the syntax**
```
              a
       +------+------+
+----->|      |      | Data: 10
|      |      |      |
|      +------+------+
|       200    201
|
|
| (&)
|              p
|      +------+------+
+------|      |      | Data: 200 (Note!) 
       |      |      | 
       +------+------+  
        210    211       

        `200` is allocated because `p = &a` means pointing p to a's address
```

Hence, the terms are
```
int main(){   
    
    int a = 10; // data variable - Declaration
    int *p;     // addr variable - Declaration

    p = &a      // Assignment (or) Initialisation

    printf(*p)  // `*p` is dereferencing.
}
```

**Note The Syntax:** `*` is used for two very different things – one, `initialision` and two, `dereferencing`. While declaring and dereferencing we HAVE TO use `*` but while assignment or initialisation or *updatation* we can directly use `p` in our syntax.


(more pointers to take care)