# RID

A handle for a [Resource](class_resource.md#class-resource)'s unique identifier.

## Description

The RID [Variant](class_variant.md#class-variant) type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as [DisplayServer](class_displayserver.md#class-displayserver), [RenderingServer](class_renderingserver.md#class-renderingserver), [TextServer](class_textserver.md#class-textserver), etc.

A low-level resource may correspond to a high-level [Resource](class_resource.md#class-resource), such as [Texture](class_texture.md#class-texture) or [Mesh](class_mesh.md#class-mesh).

**Note:** RIDs are only useful during the current session. It won't correspond to a similar resource if sent over a network, or loaded from a file at a later time.

**Note:** In a boolean context, an RID will evaluate to `false` if it has the invalid ID `0`. Otherwise, an RID will always evaluate to `true`. This is equivalent to calling is_valid().

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Constructors

| RID   | RID()                        |
|---------------------|------------------------------------------------------------|
| RID   | RID(from: RID) |

## Methods

| [int](class_int.md#class-int)    | get_id()     |
|----------------------------------|------------------------------------------|
| [bool](class_bool.md#class-bool) | is_valid() |

## Operators

| [bool](class_bool.md#class-bool)   | operator !=(right: RID)   |
|------------------------------------|------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | operator <(right: RID)     |
| [bool](class_bool.md#class-bool)   | operator <=(right: RID)   |
| [bool](class_bool.md#class-bool)   | operator ==(right: RID)    |
| [bool](class_bool.md#class-bool)   | operator >(right: RID)     |
| [bool](class_bool.md#class-bool)   | operator >=(right: RID)   |

---

## Constructor Descriptions

RID **RID**()

Constructs an empty **RID** with the invalid ID `0`.

---

RID **RID**(from: RID)

Constructs an **RID** as a copy of the given **RID**.

---

## Method Descriptions

[int](class_int.md#class-int) **get_id**()

Returns the ID of the referenced low-level resource.

---

[bool](class_bool.md#class-bool) **is_valid**()

Returns `true` if the **RID** is not `0`.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: RID)

Returns `true` if the **RID**s are not equal.

---

[bool](class_bool.md#class-bool) **operator <**(right: RID)

Returns `true` if the **RID**'s ID is less than `right`'s ID.

---

[bool](class_bool.md#class-bool) **operator <=**(right: RID)

Returns `true` if the **RID**'s ID is less than or equal to `right`'s ID.

---

[bool](class_bool.md#class-bool) **operator ==**(right: RID)

Returns `true` if both **RID**s are equal, which means they both refer to the same low-level resource.

---

[bool](class_bool.md#class-bool) **operator >**(right: RID)

Returns `true` if the **RID**'s ID is greater than `right`'s ID.

---

[bool](class_bool.md#class-bool) **operator >=**(right: RID)

Returns `true` if the **RID**'s ID is greater than or equal to `right`'s ID.
