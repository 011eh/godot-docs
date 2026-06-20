# GDScript

**Inherits:** [Script](class_script.md#class-script) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A script implemented in the GDScript programming language.

## Description

A script implemented in the GDScript programming language, saved with the `.gd` extension. The script extends the functionality of all objects that instantiate it.

Calling new() creates a new instance of the script. [Object.set_script()](class_object.md#class-object-method-set-script) extends an existing object, if that object's class matches one of the script's base classes.

If you are looking for GDScript's built-in functions, see [@GDScript](class_@gdscript.md#class-gdscript) instead.

## Tutorials

- [GDScript documentation index](../tutorials/scripting/gdscript/index.md)

## Methods

| [Variant](class_variant.md#class-variant)   | new(...)    |
|---------------------------------------------|-------------------------------------------|

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **new**(...)

Returns a new instance of the script.

```gdscript
var MyClass = load("myclass.gd")
var instance = MyClass.new()
print(instance.get_script() == MyClass) # Prints true
```
