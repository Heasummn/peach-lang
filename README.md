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
    print(`Hello!`)
}
```

```
func yell() {
    print(`HELLO!`)
}
```

Void return type is optional to write.

#### Anonymous functions

```
let doSomething = function() {
	print(`Do something`)
}
```

There is no arrow functions. Instead of ES6 arrow functions, regular functions will be scoped like arrow functions.

#### Async functions

```
async function() {
  let foo = await someAsyncFunction()
  console.log(`At this point, foo is assigned a value`)
}
```

Async fucntions work the same as ES7 async.

## Classes

```
class HighClass {
	let a: Int
	let b: Int
	
	constructor(a: Int, b: Int) {
		self.a = a
		self.b = b
	}

	func getA() -> Int {
		return a
	}

	func getB() -> Int {
		return b
	}
}
```

There is no inheritence in Peach.

## Javascript Object

```
let object = {
	type: "A", 
	size: "200", 
	color: "white"
}

assert(object.color == `white`)
```

Javscript objects are directly compatible in Peach.


## Compilation
PeachLang is pretty small right now, but to get the current code up and running, install the requirements.txt and run `python3 peach_lang/main.py`

## Development
To develop the parser, use antlr4 upon the `peach_lang/PeachLang.g4` file.
Make sure that the output directory is set to `peach_lang/parser`, and that you only build a visitor.
I recommend using an IDE such as PyCharm and the Antlr4 plugin to handle development.