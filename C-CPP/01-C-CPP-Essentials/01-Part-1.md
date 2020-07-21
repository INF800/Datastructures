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

*But why access indirectly? And why use pointers at all??* 

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

    printf(*p)  //`10`. `*p` is called dereferencing.
}
```

**Note The Syntax:** `*` is used for two very different things – one, `initialision` and two, `dereferencing`. While declaring and dereferencing we HAVE TO use `*` but while assignment or initialisation or *updatation* we can directly use `p` in our syntax. `&` can be read as *"Address of"* can be used for **Referencing** discussed below.

(more pointers to take care)

- **Access Heap Memory using Pointers**

    - i. Declare address variable
    ```
    int *p;
    ```
    *whenever you declare something, memory is allocated definitly inside `stack-section` of main memory.*
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
        |          p            |  [Stack]
        |         [ ]           |    |
        |       210/211         |    |
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

    - ii. Create an Array   - In `heap-section` of main memory
    
    **(C Language)**
    
    use: `malloc` available in `#include<stdlib.h>`

    ```
    // syntax: malloc(<size-to-be-alocated>)
    // we will let compiler decide how much size space has to be allocated
    // size-to-be-alocated = <number-of-elements> * sizeof(<data-type>)

    malloc ( 5 * sizeof(int)); // 5 * 2
    ```
    ```
        ------[Main Memory------]
        +-----------------------+ -------
        |                       |    |
        |     [][][][][]        |  [Heap]
        |      0 1 2 3 4        |    |
        |      addr: 5000       |    |
        +-----------------------+ -------
        |                       |    | 
        |                       |    |
        +-----------------------+    |
        |          p            |  [Stack]
        |         [ ]           |    |
        |       210/211         |    |
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

    `malloc()` will allocate space in `heap-memory` but to access it we need pointers. malloc returns `void-pointer` type so we have to `typecast` it into our desired data-type i.e use `(int *)` as shown below

    ```
    p = (int *) malloc (5 * sizeof(int));
    ```
    ```
        ------[Main Memory------]
        +-----------------------+ -------
        |                       |    |
    +----------[][][][][]       |  [Heap]
    |   |      0 1 2 3 4        |    |
    |   |      addr: 5000       |    |
    |   +-----------------------+ -------
    |   |                       |    | 
    |   |                       |    |
    |   +-----------------------+    |
    |   |           p           |  [Stack]
    +------------>[5000] (NOTE!)|    |
        |        210/211        |    |
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

    *Note how pointer clings to the heap memory address*

    **(C++ Language)** 
    
    *It is a lot more simple*
    ```
    p = new int[5]; // just one line
    ```

#### 04. References

- **Not** present in C Language. It is available only in C++

- It is a nickname or alias given to a variable

Symbol Before Variable Initialisation | Type of Variable | Declaration Example | Declaration with Initialisation | Accessing variable | Updating variable | Read As |
---|---| ---| --- | --- | --- | --- |
|`<nothing>` | Data variable | `int x ;` | `int x = 10 ;` | `a` | `a = 5 ;` | na |
|`*` | Address variable | `int *x ;` | ? | ? | ? | *"value at"* |
|`&` | Reference variable | `int &x ;` | ? | ? | ? | *"address of"* |

Usage:
```
int main()
{
    int a = 10; // data variable
}
```
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
|      a                |  [Stack]
|     [10]              |    |
|   200/201             |    |
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

if I write,
```
int main()
{
    int a = 10; // data variable

    int &r = a; declare and initialize ref. variable
}
```
our *reference-variable* `r` will now point to *data-variable* `a`. Note that we can read `&` as adderess of - which forms a basis for pointers as well as references!
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
|    a(or)r (Note!)     |  [Stack]
|     [10]              |    |
|   200/201             |    |
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
            a (or) r
        +------+------+
        |      |      | Data: 10
        |      |      | Addr: 200
        +------+------+
        200    201

```
**Note:** Both `a` and `r` are SAME as they have same address. changing `r` changes `a`.

eg.
```
int main()
{
    int a = 10; // data variable
    int &r = a; declare and initialize ref. variable

    cout << a; // `10` 
    r++;
    cout << r; // `11`
    cout << a; // `11` Changes itself as `a` and `r` both refers to same address. thanks to `&`
}
```

**Why do you need another name for same variable if you already have one? Why `Reference`?**

>It is used in *parameter passing* - we use references instead of pointers to write smaller functions. Useful feature of C++. More will be discussed in *Functions* section of this guide.

#### 05. Pointer to Structure

Consider this example,
```
struct Rectangle
{
    int length; // 2 bytes
    int bredth; // 2 bytes
};

int main()
{
    struct Rectangle r = { 10, 5 } // 2 + 2 = 4 bytes
}
```

```
               r
        +------+------+
        |      10     | r.length 
        |             | 
        +------+------+
        |      05     | r.breadth
        |             | 
        +------+------+
```
we can change the value if we want using
```
r.length = 15;
```

Let us initalize a pointer now. Whatever data-type a pointer may point to, it **always occupies space as of the size-of-int in any compiler. (Here 2 bytes)**

Why? Because it holds just the address!
eg.
```
int main()
{
    struct Rectangle r = { 10, 5 } // 2 + 2 = 4 bytes
    
    // pointer declare
    struct Rectangle *p; // 2bytes only. Even if `Rectangle` occupies 4 bytes

    // pointer declare and initialize
    struct Rectangle *p = &r; // 2 bytes only
}
```
when `struct Rectangle *p = &r;` is called in above code, 
```
+----------------+
|                |
|                |
|                V
|                r
|        +------+------+
|     200|      10     | r.length (2 bytes)
|     201|             | 
|        +------+------+
|     202|      05     | r.breadth (2 bytes)
|     203|             | 
|        +------+------+
|
| (&)
|              p
|       +------+------+
--------|     200     | (2 bytes)
        |             | 
        +------+------+      
```

**So, how to access Rectangle `r` using poiniter `p` ?**

- `p.length` (wrong!) `p` stores address of `r` not `r` itself 

- `*p.length` (wrong!) Higher precedence is for `.` operator. So, it will try to find `p.address` first i.e same as `*(p.address)`

- `(*p).length` (correct!)

- `p -> length = 20` (correct) special syntax in C++

**Create object dynamically in Heap using pointer**
```
int main(){
    
    struct Rectangle *p; // declare pointer. Note the type.
    
    // malloc( sizeof(struct Rectangle) ) // void-pointer. type cast it.

    p = (struct Rectangle *) malloc( sizeof(struct Rectangle *) )
}
```
Note: `malloc()` only allocates memory space. It doesn't attach a "identifier" to the space. 

For example,  `(struct Rectangle *) malloc( sizeof(struct Rectangle *) ) ` creates space but it has no "identifier" but only address. We are storing that address in a pointer `p` (which will be used as the "identifier"). We are using the created memory's address to "identifier" it ourselves .
```
        ------[Main Memory------]
        +-----------------------+ -------
        |      Rectangle        |    |
    +----------[][][][]         |  [Heap]
    |   |      0 1 2 3          |    |
    |   |  addr: 5000/01/02/03  |    |
    |   +-----------------------+ -------
    |   |                       |    | 
    |   |                       |    |
    |   +-----------------------+    |
    |   |           p           |  [Stack]
    +------------>[5000] (NOTE!)|    |
        |        210/211        |    |
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

Note: `p` is a pointer not Rectangle. Rectangle is present in Heap!

We can now access the created Rectangle in `heap-memory` using our Rectangle pointer `p`
```
p -> length = 10;
p -> breadth = 5;
```

