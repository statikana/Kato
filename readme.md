Silly language, work in progess. It basically just uses scopes. Basic example script:
```
{
    let favorite_number = 13;
    let age = {
        let name = "ryan";
        if (name) {
            emit 10000;
        } else {
            emit 3;
        };
    };
    emit favorite_number/age;
};
```
`emit` sets the value of the scope, but continues executing. like `b = { emit 'b'; }`. `return` is also implemented basically just exits the program. When functions etc. are implemented, `return` will serve a more useful purpose. I am considering implementing an in-between keyword which immedietly exits the current scope and also sets the value of it, but then at that point just do `emit value; return;` or something.

Unimplemented stuff:
- Comparisons / reassignment (e.g. var += 1, a == b)
- Array types
- In-place if-statements (a = true? 'x' : 'y';)? idk
- Typed boolean values