#### 01. Data Related Terms

- **Data Structures**

    - Arrangement or collection of data items do that operations can be performed on them efficiently in main memeory during execution of program.

    - Efficiency is the key. Without data-structures we cannot develop any applications

- **Database and Data Warehouse**
    - Relational data is stored in hard-disk
    - Data has to be brought to main-memory for operations
    - Commercial data can be categorized into two
        - i. Operational data (Used daily)
        - ii. Legacy data (Historical data - 10 years of data)
            - Large collection of legacy data is called *data warehouse*

- **Big Data**
    Day by day, large amount of data is generated. Storing and utilizing this data is called *Big Data.*

#### 02. Stack vs Heap memory

- A. Main memory
- B. How program uses memory
- C. Static allocation
- D. Dynamic allocation

- Memory 
    - Memory is divided into smaller addressable units called *bytes*. 
    - Every byte has an address
    - Addresses are single dimensional - Linear
    ```
                            65535 65536
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        [][][][][][][][][][][][][][]
        0 1 2 3
    ```

    > Total bytes = `65536` bytes = 64 * 1024 = `64kb` 

    - If we have lage main-memory RAM - 2GB or 4GB, Entire memory isn't used as a single unit but it is divided into managable pieces called ***Segments*** 

    > In our discussion let a segment be 64kb

    ```

                        +----------------------+
                        |                      |
                        |        CPU           |
                        |                      |
                        +----------------------+
                                ^  |
                                |  |
                                |  V
                        [-----[Main Memory------] 65535
                        +-----------------------+ -------
                        |                       |    |
                        |                       |  [Heap-memory-section]
                        |                       |    |
                        +-----------------------+ -------
                        |                       |    | 
                        |                       |    |
    +-------+           +                       +    |
    | Prog..|           |                       |  [Stack-memory-section]
    | ......|<--------->|                       |    |
    | ......|           |                       |    |
    +-------+           +-----------------------+ --------
    HDD                 |                       |    |
    Hard Disk           |                       |    |
                        |   <machie-code>       |    |
                        |   copied              |    | 
                        |   and loaded          |    |
                        |   here right after    |    |
                        |   after compilation   |    |
                        |                       |  [Code-memory-section]
                        |                       |    |
                       0|                       |    |
                        +-----------------------+ --------
                        [-----[Main Memory------]
    ```

#### A. Static Memory Allocation (How memory is allocated and destroyed in stack-memory)

- Consider this program:
    
    ```
    int main()
    {
        int a; // 2 bytes ( Let us assume for example)
        float b; // 4 bytes ( Let us assume for example)
    }
    ```

- Static Memory Allocation
    - For above program, `2 + 4 = 4bytes` is allocated in *stack-memory*
    > Note: Sizes or bytes to be allocated to data-types can only be decided by COMPILER
    - Strictly speaking, it is allocated in *stack-frame* (or *activation record*) of main main() function inside *stack-memory*
    - Size of memory to be allocated was decided during **compile time** - Hence called "**Static Memory Allocation**"

- If there is a sequence of function calls; How is memory allocated?
    - Memory is automatically created in *stack-section* and destroyed when function ends.
    - Example, consider this example (sequence of function calls)
        ```
                                    func2(int i) <--------------+
                                    {                           |
                                        int a;                  | 
                                        ....                    |
                step 3                  ....                    |
                +--------------<<-- }                           |
                |                                               |  
                |                   func1() <---------------+   |   
                |                   {                       |   |  
                |                       int x;              |   |  
                +---------------------> func2(); -->>-----------+ step 2     
                    +----------<<-- }                       |
                    |                                       |
                    |               int main()              |
                    |               {                       |
                    |                   int a;              |
                    |                   float b;            |
                    |                   ...                 |
                    |                   ...                 |
            step 4 +-----------------> func1(); -->>-------+ step 1
                                    }
        ```
    - > Note: step 1/2/3/4 is in chronologocal order 
        
        - Before `func1();` call
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |                                         |  | 
                            |         <not-yet-allocated>             |  |
                            |                                         |  |
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |                                         |  | 
                            |         <not-yet-allocated>             |  |
                            |                                         |  |
                            |                                         |  |
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |     a           b                       |  |
                            |   +----+      +----+----+               |  |
                            |   |    |      |    |    |               |  |
                            |   +----+      +----+----+               |  |  
                            |   200/201      202/205                  |  |
                            +=============+=============+=============+ ----
            ```

        - Before `func2();` call
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |                                         |  | 
                            |         <not-yet-allocated>             |  |
                            |                                         |  |
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |     x                                   |  | 
                            |   +----+                                |  |
                            |   |    |                                |  |
                            |   +----+                                |  |
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |     a           b                       |  |
                            |   +----+      +----+----+               |  |
                            |   |    |      |    |    |               |  |
                            |   +----+      +----+----+               |  |  
                            |   200/201      202/205                  |  |
                            +=============+=============+=============+ ----
            ```

        - Before `func2();` ends
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |     a           i                       |  |
                            |   +----+      +----+                    |  |
                            |   |    |      |    |                    |  |
                            |   +----+      +----+                    |  |  
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |     x                                   |  | 
                            |   +----+                                |  |
                            |   |    |                                |  |
                            |   +----+                                |  |
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |     a           b                       |  |
                            |   +----+      +----+----+               |  |
                            |   |    |      |    |    |               |  |
                            |   +----+      +----+----+               |  |  
                            |   200/201      202/205                  |  |
                            +=============+=============+=============+ ----
            ```
        
        - When `func2();` exec ends
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |                                         |  |
                            |             <destroyed>                 |  |  
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |     x                                   |  | 
                            |   +----+                                |  |
                            |   |    |                                |  |
                            |   +----+                                |  |
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |     a           b                       |  |
                            |   +----+      +----+----+               |  |
                            |   |    |      |    |    |               |  |
                            |   +----+      +----+----+               |  |  
                            |   200/201      202/205                  |  |
                            +=============+=============+=============+ ----
            ```

        - When `func1();` exec ends
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |             <destroyed>                 |  |  
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |             <destroyed>                 |  | 
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |     a           b                       |  |
                            |   +----+      +----+----+               |  |
                            |   |    |      |    |    |               |  |
                            |   +----+      +----+----+               |  |  
                            |   200/201      202/205                  |  |
                            +=============+=============+=============+ ----
            ```
        
        - When `main();` exec ends
            ```
                            +=============+=============+=============+
                            |                <heap>                   |
                            |                                         |
                            +=============+=============+=============+ ----
            func2()         |                                         |  |
            stack-frame     |             <destroyed>                 |  |  
                            |                                         |  |
                            |-----------------------------------------| <stack>
            func1()         |                                         |  |
            stack-frame     |             <destroyed>                 |  | 
                            |-----------------------------------------| <stack>
            main()          |                                         |  |
            stack-frame     |             <destroyed>                 |  |  
                            |                                         |  |
                            +=============+=============+=============+ ----
            ```

    > **Note: Memory is allocated and delocated exactly like in STACK. Hence called *Stack-memory* section of main memory**

    > Amount of memory to be allocated is decided by compiler.

#### B. Dynaminc Allocation (How memory is allocated and destroyed in heap-memory)

- Heap: If things are simply piled up or kept randomly, we call it *a heap*

- Heap memory is used in two cases
    - *Organized* pile of heap
    - *Unorganized* pile of heap

- *Resource*
    - For example, printer or keyboard is a resource. 
    - Use a resource when needed and after use, *release*(deallocate) it so that others can use the resource

- *stack-section* and *code-section* can be accessed directly but *heap-section* of main-memory cannot vbe accessed dorectly.
    - Use pointer to access it indirectly
    - We must explicitly allocate and delocate the memory. 
    - Example
        - Allocation
            - create a pointer
                ```
                    int *p; // declare address variable
                ```
            - allocate memory in heap and make the pointer cling to it
                ```
                p = (int *) malloc( 5 * sizeof(int) ); // C
                ```
                ```
                p = new int[5]; // C++
                ```
        - Delocation
            - can we simply write `p = NULL` to delocate memory? **No!** it will set pointer variable to null but the memory created by `malloc` or `new` still stays the same in heap-memory. It must be explicitly `delete`d
            - both in C/C++
                - Delete memory. `[]` means array-data-type
                ```
                delete []p;  
                ```
                - now, nullify pointer variable
                ```
                p = NULL;
                ```
            
- **Memory Leak:** 
    - If we dont delocate the memory, *the memory stays the same allocated for our program*.
    - This causes loss of memory

- Things to note
    - a. Here, heap memory is **unorganized**
    - b. Heap memory must be treated as *Resource* (explicit alloaction and deallocation)
    - c. Heap memory cannot be accessed directly