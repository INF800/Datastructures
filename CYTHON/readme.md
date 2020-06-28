source : https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

- `pip3 install cython`
- Write your python source-code in `.pyx` file
- Use cython to create to `.so` and `.c` file using the below script `setup.py`
    ```
    from setuptools import setup
    from Cython.Build import cythonize

    setup(
        ext_modules = cythonize("filename.pyx")
    )
    ```
    ```
    python setup.py build_ext --inplace
    ```
    
- In **cur dir**, you can import your *C-Powered* python code using --
    ```
    import filename
    ```

    **NOTE:**
    >   - Not only `.so` file is important, to use `.so` file, you have to build it in target machine
    >   - Name of `.so` file should be atleast `filename.so` as in `filename.pyx` python module or something like `filename.cpython-37m-darwin.so`
    >   - Paste `.so` file in your main(any) dir to be able to import viz. `import filename` in any py-module located in same dir as `.so` file
