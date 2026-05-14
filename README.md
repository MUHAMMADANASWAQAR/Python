# Python Practice

This repository contains Python practice files covering core programming concepts, object-oriented programming, file handling, async programming, JSON, and Pydantic.

## Topics Covered

- Hello world and basic syntax
- Strings, variables, naming conventions, and operators
- Conditional statements and match-case
- Loops and functions
- Lists, tuples, dictionaries, and sets
- Classes, constructors, inheritance, abstraction, encapsulation, and polymorphism
- File handling and exception handling
- List comprehension
- JSON serialization and deserialization
- Async programming with `asyncio`
- Pydantic models and validation

## Learning Path

Start with the numbered files from `01_hello_world.py` through `12_sets.py` to cover Python fundamentals. Then move into the object-oriented examples from `13_class.py` through `18_polymorphism.py`. The final files introduce practical topics such as file handling, JSON, async programming, and Pydantic validation.

## Project Files

The files are numbered in learning order:

```text
01_hello_world.py
02_strings_and_naming.py
03_operators_masterclass.py
...
24_pydantic.py
```

## Setup

This project includes Poetry configuration.

```powershell
poetry install
```

You can also run individual files directly with Python:

```powershell
python 01_hello_world.py
python 24_pydantic.py
```

## Notes

Some examples create or read local files such as `data.json`. Image files are included only where they support a specific lesson.
