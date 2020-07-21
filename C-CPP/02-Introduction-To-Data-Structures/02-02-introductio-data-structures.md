#### 01. Physical Datastructures - Introduction

- There are two main physical data structures
    - Arrays 
        ```
        +---+---+---+---+
        | 8 | 5 | 9 | 0 |
        +---+---+---+---+
        0   1   2   3   
        ```
    - Linked Listes
        ```
        +---+---+       +---+---+       +---+---+
        | 2 | --|------>| 4 | --|------>| 7 | / |
        +---+---+       +---+---+       +---+---+
        ```

> We can have more data structures by taking combination of these two

- **Why are they called physical?**
    - *They decide or define how memory is organized or allocated*
    - More related 

- Array
    - Contigous
    - fixed sized length (Static)
    - Can be created either in *Stack* or *Heap*
    - Use when length of data is already known

- Linked list
    - Dynamic datastructure
    - Collection of nodes (data and addr of next node)
    - length can grow/reduce dynamically
    -  Always created in *Heap* (*Head-pointer* may be available in *Stack* section)
    - Use when length of data isn't already known

#### 02. Logical Datastructures - Introduction

| Logical Datastructure | Physical Datastructure |
|---|---|
| Stack | Heap |
| Queues | Array |
| Trees | |
| Graph | |
| Hash Table | |

> These are basic logical datastructures. There are more subdivisions.

**Differences**

| Logical Datastructure | Physical Datastructure |
|---|---|
| Holds the data | Defines decipline how to manipulate data | 

| Logical Datastructure | Type |
|---|---|
| `Stack` `Queue` | Linear |
| `Tree` `Graph` | Non-Linear |
| `Hash Table` | Tabular/Linear |

- Logical datastrucures are actually used in application like algorithms
- For implementing these logical datastructures, we use physical datastuctures like arrays or linked lists or *combintion of both*

#### 03. ADT - Abstract Data Type

- A **Data-Type** is defined by
    1. *Representation of data* (How you store the data)
    2. *Operations allowed on the data*
    
    - Representation example 
        - `int x;` is stored as *2bytes* i.e *16bits* together in a single value or data. 
        - 1bit is reserved for sign and rest 15bits for data
    - Operations example
        - `int x;` supports `+ - * / % < > = ++ --`

> NOTE: `int` is *primitive-datatype* not *abstract-datatype* it is being used to define meaning of *abstract* and *data-type*

- **Abstract**
    - Hiding internal details
    - Do we need to know how data is stored or how operations are performed on it? No! Hide internal details from programmer. 
    
- **Abstract Data Type**
    - Related to OOPs
    - Using classes we can define our own data types that are abstract. (hide internal details)
    - Example,
        - Let us take a list - 
            ```
            8 ,3, 9, 4, 6, 10, 12
            ```
            with index values `0, 1, 3, 4, 5, 6`
        - How to create this list in our program?
            - We need *space* for storing elements
            - Need to know *maximum capacity*
            - Need to know *size* of list
        - Representation of the list can be done using 
            - *Array*
            - *Linked list*
        - Operations needed to be performed
            - add an elemnt
            - remove an element
            - search an element
    - **Abstract data type** define the data and operations on data together and let it to be used as data type by hiding internal details.
    - Very common in C++

#### 04. Operations on a list

- `add(ele)` / `append(ele)`:
    - Adding an element at the end of a list

- `add(index, ele)`/ `insert(ele)`:
    - Shift elemnts, created space and add

- `remove(index)`:
    - delete and shift elements

- `set(index, ele)` / `replace(index, ele)`:
    - Changing an element at a given index

- `search(key)` / `contains(key)`:
    - returns index or bool

- `sort()`
    - Arranges a list in ascending or descending order