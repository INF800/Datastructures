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
                    |                       |  [Heap]
                    |                       |    |
                    +-----------------------+ -------
                    |                       |    | 
                    |                       |    |
+-------+           +                       +    |
| Prog..|           |                       |  [Stack]
| ......|<--------->|                       |    |
| ......|           |                       |    |
+-------+           +-----------------------+ --------
  HDD               |                       |    |
  Hard Disk         |                       |    |
                    |      <machie-code>    |    |
                    |       loaded here     |    |
                    |                       |  [Code]
                    |                       |    |
                   0|                       |    |
                    +-----------------------+ --------
                    [-----[Main Memory------]
```

