# pyctype_tree-sitter
It's tree-sitter implementation of [pyctype](https://github.com/S4Plus/pyctype). 

✔ PyCType_tree-sitter is no longer need to config C head files that used in the project.  
✔ PyCType_tree-sitter improves the original analysis process, such as analyzing the return statement in the C implementation. if return statement
What is returned is a variable, and only the types of all assignment statements (Assign) for this variable will be extracted. According to the correct analysis logic, the assignment statement before and closest to the return statement should be analyzed. This study improved the analysis process and made the analysis results more accurate.  
✔ PyCType_tree-sitter drastically reduces runtime.

# uage
run `PyCType_tree-sitter` with:
```python
python evaluate.py path-to-project
```
`path-to-project` is the path of the project (or a file) to be analyzed and should be replaced with absolute path.

# output
likes [pyctype](https://github.com/S4Plus/pyctype#usage).

