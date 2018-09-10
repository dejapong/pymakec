Pymakec is a python library for generating C header and source files.

It's easy to use and read. The following is an example of a python script which creates the C source code for Hello World:

```python

from pymakec import *

cf = cfile([
    cinclude("stdio.h"),
    cfunction("int", "main", ["int argc", "const char** argv"], [
        ccomment("Call the printf function"),
        ccall("printf", "%s\n", cstring("Hello World")),
        "/* Any string can be added too */"
        creturn(0)
    ]),
])

# Print the C file
print(cf.generate())

```

The list passed to the `cfile` constructor is called an items list. Any block element can be constructed by passing an items list to it, at the end of any positional arguments. The items list argument is a named argument called `items`.

The `add` method accepts an items list, and returns a transformed list of items (strings will be indented). This method is useful for non-sequential builds, such as follows:

```python
from pymakec import *

cf = cfile([
    cinclude("stdio.h"),
])

mainf = cf.add([
    cfunction("int", "main", ["int argc", "const char** argv"], [
        ccall("sayHello", "Hello World"),
        creturn(0)
    ]),
])[0]

sayHello = cf.add([
    cfunction("void", "sayHello", ["const char* msg"], [
        ccall("printf", "%s\n", "msg"),
    ]),
])

# Add a function declaration before the main method, where it's called
cf.add(sayHello.declaration(), before=mainf)

# Print the C file
print(cf.generate())

```

I'd like to add the following features before calling this done, but the library is usable right now. Any missing features can be supplemented by the fact that bare strings can be added to an items list. Features I'm working on include:

* Variables
* Typedefs
* Switch
* Break, continue
* Do loops
* While Loops
* Enums
* Unions
* Structs
* Array and struct initializers
* Get function pointers from function object
