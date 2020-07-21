## Types of Recursion

1. TAIL RECURSION
2. HEAD RECURSION
3. TREE RECURSION
4. INDIRECT RECURSION
5. NESTED RECURSION


#### 01. Tail Recursion

- If the function is calling itself, it is called a *recursive-call*
- If *recursive-call* is the last-most statement of a recursive function, it is called a recursive function.
- After that call, it should perform nothing. Example,
    ```
    void func (int n)
    {
        if(n>0)
        {
            printf("%d", n);
            ....
            ....
            ....
            func(n-1); // last-most statement
        }
    }
    ```
    ```
    func(3)
    ```
- All actions are performed at *call-time* (ascending) not *return-time* (descending). For example, this examle is **not** a tail recursion as `func(n-1) + n` happens at *return-time*
    ```
    void func (int n)
    {
        if(n>0)
        {
            printf("%d", n);
            ....
            ....
            ....
            func(n-1) + n; // last-most statement
        }
    }
    ```
    ```
    func(3)
    ```

**Tail Recursion converted into Loops**

- Every recursion can be converted in loop and vice versa!

- For example,
    ```
    void func (int n)
    {
        if(n>0)
        {
            printf("%d", n);
            ....
            ....
            ....
            func(n-1); // last-most statement
        }
    }
    ```
    ```
    func(3)
    ```
    
    is same as
    
    ```
    void func (int n)
    {
        while(n>0)
        {
            printf("%d", n);
            ....
            ....
            n--;
        }
    }
    ```
    ```
    func(3)
    ```

- Let's compare

| Type | Time Complexity | Space Complexity |
| --- | --- | --- |
| Tail Recursion | **`O(n)`** | **`O(n)`** | 
| Loop | **`O(n)`** | **`O(1)`** |

> For tail recursion, `n` activation records are created for every `n-th` recursive call. But, for a loop, single activation record is maintained.

- **Hence, if there is a tail recursion in your code, try to convert it into a loop! To reduce space complexity**

> Note: Not all recursions can be written as loop but *tail-recursions* can be!

#### 02. Head Recursion

 - No statement/execution is present before *recursive-call*
 - Example
    ```
    void func (int n)
    {
        if(n>0)
        {
            func(n-1); // first-most statement
            ....
            ....
            ....
            printf("%d", n);
        }
    }
    ```
    ```
    func(3)
    ```
- It performs all it's execution at *returning-time* (descending). Not while *calling-time* (ascending)

**Head Recursion converted into Loops**

- It cannot be easily(*as-it-is*) converted into loop. But it can be converted!
- For example
    ```
    void func (int n)
    {
        if(n>0)
        {
            func(n-1); // first-most statement
            ....
            ....
            ....
            printf("%d", n);
        }
    }
    ```
    ```
    func(3) //123
    ```
    
    cannot be converted as intutively as tail-recursion. But the loop-code below is same as the head-recursion
    ```
    void func(int n)
    {
        int i=1;
        while(i<n)
        {
            printf("%d", n);
            i++;           
        }
    }
    ```
    ```
    func(3) //123
    ```
    Note: It is a complex conversion! But is do-able.


#### 03. Tree Recursion

- More than one *recursive-call*s to itself in the function body
- Example,
    ```
    func(n)
    {
        if (n>0)
        {
            ....
            ....
            func(n-1); //recursive call 1
            ....
            ....
            func(n-1); //recursive call 2
            ....
            ....
            func(n-1); //recursive call 3
            ....
            ....
        }
    }
    ```

**Tracing tree for Tree Recursion**

- Let us consider this function
    ```
    void func (int n)
    {
        if (n>0)
        {
            printf("%d", n); // line 0
            func(n-1);       // line 1 
            func(n-1);       // line 2
        }
    }
    ```
    ```
    func(3);
    ```

Whole recursion looks like this. Let us go step by step. Note that this recursion uses `4 activation records`(stack-framses)
```

                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 func(2)
                                            |                                       |
                        +---------------------------------------+     +---------------------------------------+
                        |                   |                   |     |                  |                    |
                        V                   V                   V     V                  V                    V
                        2                 func(1)           func(1)   2                func(1)              func(1)
                                            |                   |                        |                    |
                                +----------------------+  +----------------------+  +----------------------+  +----------------------+
                                |           |          |  |           |          |  |           |          |  |           |          |
                                V           V          V  V           V          V  V           V          V  V           V          V
                                1      func(0)   func(0)  1      func(0)   func(0)  1      func(0)   func(0)  1      func(0)   func(0)
                                            |         |               |         |               |         |               |         |
                                           [x]       [x]             [x]       [x]             [x]       [x]             [x]       [x]

```     

- Recursive call 1 `func(3)` where `n = 3`. Recursive call in *line 2* will wait until this recursive call reaches it's base condition! (Same happens recursively)
> `waiting-n` will be processed in **descending order**

    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
    ```

    ```
    +---------------------------+
    | n[3]                      | <stack> func(3)
    +---------------------------+
    ```

- Recursive call 2 `func(2)`
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           waiting-1
    ```
    ```
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Recursive call 3 `func(1)`
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           waiting-1
                                            |                
                                +----------------------+  
                                |           |          | 
                                V           V          V 
                                1      func(0)   waiting-2 
    ```
    ```
    +---------------------------+
    | n[1]                      | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Recursive call 4 `func(0)`
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           waiting-1
                                            |                
                                +----------------------+  
                                |           |          | 
                                V           V          V 
                                1      func(0)   waiting-2 
                                            |  
                                           [x]  
    ```
    ```
    +---------------------------+
    | n[0]                      | <stack-frame> func(0)
    +---------------------------+
    | n[1]                      | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

> Note: For 4 recursive calls. 4 activation records are created

- Recursive call 4 end. waiting 2 processing; `n=1` `func(n-1) = func(0)`. Memory related to recursive call 4 (`func(0)`) will be deallocated
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           waiting-1  
                                            |                                     
                                +----------------------+  
                                |           |          | 
                                V           V          V  
                                1      func(0)   func(0)  
                                            |         |                            
                                           [x]       [x]             
    ```
    ```
    +---------------------------+
    | n[x] n[0]                 | <stack-frame> func(0) 
    +---------------------------+
    | n[1]                      | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Waiting-2 processing ends as func(0) reaches base condition. 
- Waiting-1 processing. 
- `n=2` => `func(n-1) = func(1)`
- Memory related to previous `func(0)` call deallocated as the function ends. With the end of `fucn(0)`, parent recursive func `func(1)` ends as well. As a result,
memory related to it is also deallocated and waiting-1 is processed!
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           func(1)  
                                            |                   |                    
                                +----------------------+  +----------------------+  
                                |           |          |  |           |          |  
                                V           V          V  V           V          V  
                                1      func(0)   func(0)  1      func(0)   waiting-3  
                                            |         |                            
                                           [x]       [x]             
    ```
    ```
    +---------------------------+
    | n[x] n[x]                 | <stack-frame> func(0) 
    +---------------------------+
    | n[x] n[1]                 | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Recursive call for `func(0)` reaches base condition
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           func(1)  
                                            |                   |                    
                                +----------------------+  +----------------------+  
                                |           |          |  |           |          |  
                                V           V          V  V           V          V  
                                1      func(0)   func(0)  1      func(0)   waiting-3  
                                            |         |               |                        
                                           [x]       [x]             [x]          
    ```
    ```
    +---------------------------+
    | n[x] n[x] n[0]            | <stack-frame> func(0) 
    +---------------------------+
    | n[x] n[1]                 | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Memory related to previous `func(0)` is deallocated. Waiting-3 processed - `func(0`
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 waiting-0
                                            |                        
                        +---------------------------------------+  
                        |                   |                   |
                        V                   V                   V   
                        2                 func(1)           func(1)  
                                            |                   |                    
                                +----------------------+  +----------------------+  
                                |           |          |  |           |          |  
                                V           V          V  V           V          V  
                                1      func(0)   func(0)  1      func(0)   func(0)  
                                            |         |               |                              
                                           [x]       [x]             [x]              
    ```
    ```
    +---------------------------+
    | n[x] n[x] n[x] n[0]       | <stack-frame> func(0) 
    +---------------------------+
    | n[x] n[1]                 | <stack-frame> func(1)
    +---------------------------+
    | n[2]                      | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- Memory related to previous `func(0)` is deallocated as it reaches base condition. 
- With `func(0)`, parent `func(1)` ends as well - whose memory is also deallocated
- With `func(1)`, parent `func(2)` ends as well - whose memory is also deallocated
- waiting-0 processed. `n=3` => `func(n-1) = func(2)`
    ```
                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 func(2)
                                            |                                       |
                        +---------------------------------------+     +---------------------------------------+
                        |                   |                   |     |                  |                    |
                        V                   V                   V     V                  V                    V
                        2                 func(1)           func(1)   2                func(1)          waitng-5
                                            |                   |                    
                                +----------------------+  +----------------------+  
                                |           |          |  |           |          |  
                                V           V          V  V           V          V  
                                1      func(0)   func(0)  1      func(0)   func(0)  
                                            |         |               |         |                             
                                           [x]       [x]             [x]       [x]                
    ```
    ```
    +---------------------------+
    | n[x] n[x] n[x] n[x]       | <stack-frame> func(0) 
    +---------------------------+
    | n[x] n[x]                 | <stack-frame> func(1)
    +---------------------------+
    | n[x] n[2]                 | <stack-frame> func(2)
    +---------------------------+
    | n[3]                      | <stack-frame> func(3)
    +---------------------------+
    ```

- **Similarly `func1` is processed after it's recursive end, waiting-5 is processed**

>  Note: Atmost `4-stack-frames` are used. 

> `Number of recursive calls = Noumber of activation records created (and deleted)` i.e **15 Times**

Output
```
3211211
```

- Finally, tree looks like
```

                                          func(3)
                                            |
    +-------------------------------------------------------------------------------+
    |                                       |                                       |
    V                                       V                                       V
    3                                     func(2)                                 func(2)
                                            |                                       |
                        +---------------------------------------+     +---------------------------------------+
                        |                   |                   |     |                  |                    |
                        V                   V                   V     V                  V                    V
                        2                 func(1)           func(1)   2                func(1)              func(1)
                                            |                   |                        |                    |
                                +----------------------+  +----------------------+  +----------------------+  +----------------------+
                                |           |          |  |           |          |  |           |          |  |           |          |
                                V           V          V  V           V          V  V           V          V  V           V          V
                                1      func(0)   func(0)  1      func(0)   func(0)  1      func(0)   func(0)  1      func(0)   func(0)
                                            |         |               |         |               |         |               |         |
                                           [x]       [x]             [x]       [x]             [x]       [x]             [x]       [x]

```     

**Let us mark the order of calls**

```
                                                                                                                        LEVEL-WISE NUMBER OF CALLS 
                                            ①                                                                                               
                                          func(3)                                                                                         [1]  2^0
                                            |                                                                                                   
    +-------------------------------------------------------------------------------+                                                              
    |                                       |                                       |                                                           
    V                                       V ②                                    V⑨                                                           
    3                                     func(2)                                 func(2)                                                 [2]  2^1    
                                            |                                       |                                                                            
                        +---------------------------------------+     +---------------------------------------+                                             
                        |                   |                   |     |                  |                    |                                         
                        V                   V ③              ⑥ V     V                ⑩V                  ⑬V                                    
                        2                 func(1)           func(1)   2                func(1)              func(1)                       [4]  2^2
                                            |                   |                        |                    |                                 
                                +----------------------+  +----------------------+  +----------------------+  +----------------------+
                                |           |          |  |           |          |  |           |          |  |           |          |
                                V           V          V  V         ⑦V         ⑧V  V         ⑪V        ⑫V  V         ⑭ V        ⑮V
                                1     ④func(0) ⑤func(0)  1      func(0)   func(0)  1      func(0)   func(0)  1      func(0)   func(0)    [8]  2^3
                                            |         |               |         |               |         |               |         |
                                           [x]       [x]             [x]       [x]             [x]       [x]             [x]       [x]

```  

- Time complexity depends on the number of calls and count level-wise number of calls
- `func` is printing in each call 
- Let us calculate time complexity,
    - for `n=3`
        - `4` levels
        - for level `i`, number of calls in the level = `2^i` (i starts from 0)
        - i.e
            - Total number of calls = `2^0 + 2^1 + 2^2 + 2^3` = `15`
    - for `n=4`
        - `2^0 + 2^1 + 2^2 + 2^3 + 2^4` = `31`
    - for `n`
        - `2^0 + 2^1 + ... + 2^n` (sum of GP)
            ```
             2^0 + 2^1 + ... + 2^n` =  ( 2^(n+1) ) - 1
            ```
        - `( 2^(n+1) ) - 1` number of calls
        - Hence, time complexity: **`O(2^n)`**
- Space complexity
    - for `n=3`
        - 4 stack-framses
    - for `n=4`
        - 5 stack-framses
    - for `n`
        - `n+1` stack-frames
    - Space complexity: **`O(n)`**

- For this tree recursion function
    - Time Complexity: **`O(2^n)`**
    - Space Complexity: **`O(n)`**
