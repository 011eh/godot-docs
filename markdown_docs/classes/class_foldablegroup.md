# FoldableGroup

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A group of foldable containers that doesn't allow more than one container to be expanded at a time.

## Description

A group of [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)-derived nodes. Only one container can be expanded at a time.

## Properties

| [bool](class_bool.md#class-bool)   | allow_folding_all   | `false`                                                                                          |
|------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | resource_local_to_scene                                                | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

## Methods

| [Array](class_array.md#class-array)[[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)]   | get_containers()                 |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)                                        | get_expanded_container() |

---

## Signals

**expanded**(container: [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer))

Emitted when one of the containers of the group is expanded.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_folding_all** = `false`

-  **set_allow_folding_all**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_folding_all**()

If `true`, it is possible to fold all containers in this FoldableGroup.

---

## Method Descriptions

[Array](class_array.md#class-array)[[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)] **get_containers**()

Returns an [Array](class_array.md#class-array) of [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer)s that have this as their FoldableGroup (see [FoldableContainer.foldable_group](class_foldablecontainer.md#class-foldablecontainer-property-foldable-group)). This is equivalent to [ButtonGroup](class_buttongroup.md#class-buttongroup) but for FoldableContainers.

---

[FoldableContainer](class_foldablecontainer.md#class-foldablecontainer) **get_expanded_container**()

Returns the current expanded container.
