# scripts
- `dual.py` -- conversion between primal and dual LP problems

# todo
- `dual.py`
    - negatives don't work
    - all variables are always in the form of x_1, x_2, etc.; find a way to generalize this
    - generalize parsing variable terms from operators because right now it assumes that there's always a space between variables and operators
    - let 1 be parsed as a coefficient even if it's not specified
    - generalize constraint format so that it can be `[variables] [inequality] [value]` or `[value] [inequality] [variable]`
    - only takes primal (minimization) problem as input
    - input takes constraints first, then variables, and differentiates using the b-value; generalize this
    - improvement in output formatting
    - look into using a library to help with input parsing or writing my own