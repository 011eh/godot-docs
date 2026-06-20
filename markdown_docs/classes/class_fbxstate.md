# FBXState

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFState](class_gltfstate.md#class-gltfstate) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

## Description

The FBXState handles the state data imported from FBX files.

## Properties

| [bool](class_bool.md#class-bool)   | allow_geometry_helper_nodes   | `false`   |
|------------------------------------|---------------------------------------------------------------------------------------|-----------|

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_geometry_helper_nodes** = `false`

-  **set_allow_geometry_helper_nodes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_geometry_helper_nodes**()

If `true`, the import process used auxiliary nodes called geometry helper nodes. These nodes help preserve the pivots and transformations of the original 3D model during import.
