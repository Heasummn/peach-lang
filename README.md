# peach-lang

## Declaring Variable

```
let snoopy: Dog = new Snoopy()
var snoopy = new Snoopy()
```

Like in Swift, `let` is Peach is the javascript `const`, and `var` is the javascript `let`. There is no consensus of the javascript `var`.
Variable types can be explicitly defined like in the example `let snoopy: Dog` or type inferred like `var snoopy = new Snoopy()`.

## Primitive Data Types

```
let type1: Int = 2
let type2: Double = 2.0
let type3: Bool = true
let type4: Char = 'A'
```

## Characters and String

Declaring strings using double quotation marks (`"string literal"`) is not valid. Use ES6 style templating strings with backticks instead.

```
let name: String = `John Doe`
```

An example with string interpolation

```
let name = `John Doe`
let greetings = `Hello! \(name)`

```

## Data Structures

Array, Map, Set, Tuples


## Control Flow

#### For loops

```
for i in 1...10 {
	log(`we have looped \(i) times`)
} 
```

```
for object in objects {
	log(`printing \(object)`)
} 
```

##### While loops

```
while true {
	log(`forever`)
}
```

There are no do while loops.

#### If statements

```
if name == `snoopy` {
	return true
}
```

There are no switch statements.

## Functions

```
func add(a: Int, b: Int) -> Int {
	return a + b
}
```

```
func greet() -> Void {
    print("Hello!")
}
```

## Anonymous functions

```
let doSomething = function() -> void {
	print("Do something")
}
```

There is no arrow functions. Instead of ES6 arrow functions, regular functions will be scoped like arrow functions.

## Async

```
async function() -> Void {
  let foo = await someAsyncFunction()
  console.log("At this point, foo is assigned a value")
}
```

