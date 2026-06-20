# GLTFNode

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

glTF node class.

## Description

Represents a glTF node. glTF nodes may have names, transforms, children (other glTF nodes), and more specialized properties (represented by their own classes).

glTF nodes generally exist inside of [GLTFState](class_gltfstate.md#class-gltfstate) which represents all data of a glTF file. Most of GLTFNode's properties are indices of other data in the glTF file. You can extend a glTF node with additional properties by using get_additional_data() and set_additional_data().

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [glTF scene and node spec](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_004_ScenesNodes.md")

## Properties

| [int](class_int.md#class-int)                                        | camera               | `-1`                                              |
|----------------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------|
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | children           | `PackedInt32Array()`                              |
| [int](class_int.md#class-int)                                        | height               | `-1`                                              |
| [int](class_int.md#class-int)                                        | light                 | `-1`                                              |
| [int](class_int.md#class-int)                                        | mesh                   | `-1`                                              |
| [String](class_string.md#class-string)                               | original_name | `""`                                              |
| [int](class_int.md#class-int)                                        | parent               | `-1`                                              |
| [Vector3](class_vector3.md#class-vector3)                            | position           | `Vector3(0, 0, 0)`                                |
| [Quaternion](class_quaternion.md#class-quaternion)                   | rotation           | `Quaternion(0, 0, 0, 1)`                          |
| [Vector3](class_vector3.md#class-vector3)                            | scale                 | `Vector3(1, 1, 1)`                                |
| [int](class_int.md#class-int)                                        | skeleton           | `-1`                                              |
| [int](class_int.md#class-int)                                        | skin                   | `-1`                                              |
| [bool](class_bool.md#class-bool)                                     | visible             | `true`                                            |
| [Transform3D](class_transform3d.md#class-transform3d)                | xform                 | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

## Methods

|                                              | append_child_index(child_index: [int](class_int.md#class-int))                                                                                       |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Variant](class_variant.md#class-variant)    | get_additional_data(extension_name: [StringName](class_stringname.md#class-stringname))                                                             |
| [NodePath](class_nodepath.md#class-nodepath) | get_scene_node_path(gltf_state: [GLTFState](class_gltfstate.md#class-gltfstate), handle_skeletons: [bool](class_bool.md#class-bool) = true)         |
|                                              | set_additional_data(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |

---

## Property Descriptions

[int](class_int.md#class-int) **camera** = `-1`

-  **set_camera**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_camera**()

If this glTF node is a camera, the index of the [GLTFCamera](class_gltfcamera.md#class-gltfcamera) in the [GLTFState](class_gltfstate.md#class-gltfstate) that describes the camera's properties. If `-1`, this node is not a camera.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **children** = `PackedInt32Array()`

-  **set_children**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_children**()

The indices of the child nodes in the [GLTFState](class_gltfstate.md#class-gltfstate). If this glTF node has no children, this will be an empty array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[int](class_int.md#class-int) **height** = `-1`

-  **set_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_height**()

How deep into the node hierarchy this node is. A root node will have a height of 0, its children will have a height of 1, and so on. If -1, the height has not been calculated.

---

[int](class_int.md#class-int) **light** = `-1`

-  **set_light**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_light**()

If this glTF node is a light, the index of the [GLTFLight](class_gltflight.md#class-gltflight) in the [GLTFState](class_gltfstate.md#class-gltfstate) that describes the light's properties. If -1, this node is not a light.

---

[int](class_int.md#class-int) **mesh** = `-1`

-  **set_mesh**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mesh**()

If this glTF node is a mesh, the index of the [GLTFMesh](class_gltfmesh.md#class-gltfmesh) in the [GLTFState](class_gltfstate.md#class-gltfstate) that describes the mesh's properties. If -1, this node is not a mesh.

---

[String](class_string.md#class-string) **original_name** = `""`

-  **set_original_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_name**()

The original name of the node.

---

[int](class_int.md#class-int) **parent** = `-1`

-  **set_parent**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_parent**()

The index of the parent node in the [GLTFState](class_gltfstate.md#class-gltfstate). If -1, this node is a root node.

---

[Vector3](class_vector3.md#class-vector3) **position** = `Vector3(0, 0, 0)`

-  **set_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_position**()

The position of the glTF node relative to its parent.

---

[Quaternion](class_quaternion.md#class-quaternion) **rotation** = `Quaternion(0, 0, 0, 1)`

-  **set_rotation**(value: [Quaternion](class_quaternion.md#class-quaternion))
- [Quaternion](class_quaternion.md#class-quaternion) **get_rotation**()

The rotation of the glTF node relative to its parent.

---

[Vector3](class_vector3.md#class-vector3) **scale** = `Vector3(1, 1, 1)`

-  **set_scale**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_scale**()

The scale of the glTF node relative to its parent.

---

[int](class_int.md#class-int) **skeleton** = `-1`

-  **set_skeleton**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skeleton**()

If this glTF node has a skeleton, the index of the [GLTFSkeleton](class_gltfskeleton.md#class-gltfskeleton) in the [GLTFState](class_gltfstate.md#class-gltfstate) that describes the skeleton's properties. If -1, this node does not have a skeleton.

---

[int](class_int.md#class-int) **skin** = `-1`

-  **set_skin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skin**()

If this glTF node has a skin, the index of the [GLTFSkin](class_gltfskin.md#class-gltfskin) in the [GLTFState](class_gltfstate.md#class-gltfstate) that describes the skin's properties. If -1, this node does not have a skin.

---

[bool](class_bool.md#class-bool) **visible** = `true`

-  **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_visible**()

If `true`, the GLTF node is visible. If `false`, the GLTF node is not visible. This is converted to the [Node3D.visible](class_node3d.md#class-node3d-property-visible) property in the Godot scene, and is exported to `KHR_node_visibility` when `false`.

---

[Transform3D](class_transform3d.md#class-transform3d) **xform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

-  **set_xform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_xform**()

The transform of the glTF node relative to its parent. This property is usually unused since the position, rotation, and scale properties are preferred.

---

## Method Descriptions

 **append_child_index**(child_index: [int](class_int.md#class-int))

Appends the given child node index to the children array.

---

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname))

Gets additional arbitrary data in this **GLTFNode** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_scene_node_path**(gltf_state: [GLTFState](class_gltfstate.md#class-gltfstate), handle_skeletons: [bool](class_bool.md#class-bool) = true)

Returns the [NodePath](class_nodepath.md#class-nodepath) that this GLTF node will have in the Godot scene tree after being imported. This is useful when importing glTF object model pointers with [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class-gltfobjectmodelproperty), for handling extensions such as `KHR_animation_pointer` or `KHR_interactivity`.

If `handle_skeletons` is `true`, paths to skeleton bone glTF nodes will be resolved properly. For example, a path that would be `^"A/B/C/Bone1/Bone2/Bone3"` if `false` will become `^"A/B/C/Skeleton3D:Bone3"`.

---

 **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant))

Sets additional arbitrary data in this **GLTFNode** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
