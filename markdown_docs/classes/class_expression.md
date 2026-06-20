# Expression

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A class that stores an expression you can execute.

## Description

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

An example expression text using the built-in math functions could be `sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a [LineEdit](class_lineedit.md#class-lineedit) node to write our expression and show the result.

GDScript

```gdscript
var expression = Expression.new()

func _ready():
    $LineEdit.text_submitted.connect(self._on_text_submitted)

func _on_text_submitted(command):
    var error = expression.parse(command)
    if error != OK:
        print(expression.get_error_text())
        return
    var result = expression.execute()
    if not expression.has_execute_failed():
        $LineEdit.text = str(result)
```

C#

```csharp
private Expression _expression = new Expression();

public override void _Ready()
{
    GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
}

private void OnTextEntered(string command)
{
    Error error = _expression.Parse(command);
    if (error != Error.Ok)
    {
        GD.Print(_expression.GetErrorText());
        return;
    }
    Variant result = _expression.Execute();
    if (!_expression.HasExecuteFailed())
    {
        GetNode<LineEdit>("LineEdit").Text = result.ToString();
    }
}
```

## Tutorials

- [Evaluating Expressions](../tutorials/scripting/evaluating_expressions.md)

## Methods

| [Variant](class_variant.md#class-variant)             | execute(inputs: [Array](class_array.md#class-array) = [], base_instance: [Object](class_object.md#class-object) = null, show_error: [bool](class_bool.md#class-bool) = true, const_calls_only: [bool](class_bool.md#class-bool) = false)   |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                | get_error_text()                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                      | has_execute_failed()                                                                                                                                                                                                            |
| [Error](class_@globalscope.md#enum-globalscope-error) | parse(expression: [String](class_string.md#class-string), input_names: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray())                                                                        |

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **execute**(inputs: [Array](class_array.md#class-array) = [], base_instance: [Object](class_object.md#class-object) = null, show_error: [bool](class_bool.md#class-bool) = true, const_calls_only: [bool](class_bool.md#class-bool) = false)

Executes the expression that was previously parsed by parse() and returns the result. Before you use the returned object, you should check if the method failed by calling has_execute_failed().

If you defined input variables in parse(), you can specify their values in the inputs array, in the same order.

---

[String](class_string.md#class-string) **get_error_text**()

Returns the error text if parse() or execute() has failed.

---

[bool](class_bool.md#class-bool) **has_execute_failed**()

Returns `true` if execute() has failed.

---

[Error](class_@globalscope.md#enum-globalscope-error) **parse**(expression: [String](class_string.md#class-string), input_names: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray())

Parses the expression and returns an [Error](class_@globalscope.md#enum-globalscope-error) code.

You can optionally specify names of variables that may appear in the expression with `input_names`, so that you can bind them when it gets executed.
