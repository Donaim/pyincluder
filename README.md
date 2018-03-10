# PyIncluder
Includes some preprocessor magic to your project.

## Currently available:
- `#include <target>`  
    Just copies the content of target file.  
    Hovewer there are some improvements over std c include:
    - `at (destination)` option  
        Allows to copy content at specific location in source file (based on labels)
    - `if (condition)` option  
        If condition is not satisfied, skips `#include` instruction  
- `#label (name)`  
    Defines _target-point_ for both `#include` and `#moveat`.
    Supports `if` option, which is going to ingore the label if condition is not met.  
- `#moveat (destination)`  
    Treats text below, as if it was from included file.  
    Does not allow for repeated code at destination (in contrast to `#include`)  

# To do
- [x] `if` option for `#moveat`
- [ ] `at` option for `#label`
- [ ] new `#template <var>` instruction (simmilar to c++ templates)
- [ ] improve conditions for `if` option (mb even up to python.compile)
- [ ] improve typesystem. i.e. connect `#moveat` and `#include`

## Details
`if` option currently only checks if **pyincluder.py** has (or hasn't with '!' prefix) _**condition**_ in its stdin args.  