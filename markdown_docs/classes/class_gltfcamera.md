# GLTFCamera

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF camera.

## Description

Represents a camera as defined by the base glTF spec.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [glTF camera detailed specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera)
- [glTF camera spec and example file](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md)

## Properties

| [float](class_float.md#class-float)   | depth_far     | `4000.0`    |
|---------------------------------------|-------------------------------------------------------|-------------|
| [float](class_float.md#class-float)   | depth_near   | `0.05`      |
| [float](class_float.md#class-float)   | fov                 | `1.3089969` |
| [bool](class_bool.md#class-bool)      | perspective | `true`      |
| [float](class_float.md#class-float)   | size_mag       | `0.5`       |

## Methods

| GLTFCamera                    | from_dictionary(dictionary: [Dictionary](class_dictionary.md#class-dictionary))    |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| GLTFCamera                    | from_node(camera_node: [Camera3D](class_camera3d.md#class-camera3d))                     |
| [Dictionary](class_dictionary.md#class-dictionary) | to_dictionary()                                                                      |
| [Camera3D](class_camera3d.md#class-camera3d)       | to_node()                                                                                  |

---

## Property Descriptions

[float](class_float.md#class-float) **depth_far** = `4000.0`

-  **set_depth_far**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_far**()

The distance to the far culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `zfar` property.

---

[float](class_float.md#class-float) **depth_near** = `0.05`

-  **set_depth_near**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_near**()

The distance to the near culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `znear` property.

---

[float](class_float.md#class-float) **fov** = `1.3089969`

-  **set_fov**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fov**()

The FOV of the camera. This class and glTF define the camera FOV in radians, while Godot uses degrees. This maps to glTF's `yfov` property. This value is only used for perspective cameras, when perspective is `true`.

---

[bool](class_bool.md#class-bool) **perspective** = `true`

-  **set_perspective**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_perspective**()

If `true`, the camera is in perspective mode. Otherwise, the camera is in orthographic/orthogonal mode. This maps to glTF's camera `type` property. See [Camera3D.projection](class_camera3d.md#class-camera3d-property-projection) and the glTF spec for more information.

---

[float](class_float.md#class-float) **size_mag** = `0.5`

-  **set_size_mag**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_size_mag**()

The size of the camera. This class and glTF define the camera size magnitude as a radius in meters, while Godot defines it as a diameter in meters. This maps to glTF's `ymag` property. This value is only used for orthographic/orthogonal cameras, when perspective is `false`.

---

## Method Descriptions

GLTFCamera **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary))

Creates a new GLTFCamera instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary).

---

GLTFCamera **from_node**(camera_node: [Camera3D](class_camera3d.md#class-camera3d))

Create a new GLTFCamera instance from the given Godot [Camera3D](class_camera3d.md#class-camera3d) node.

---

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**()

Serializes this GLTFCamera instance into a [Dictionary](class_dictionary.md#class-dictionary).

---

[Camera3D](class_camera3d.md#class-camera3d) **to_node**()

Converts this GLTFCamera instance into a Godot [Camera3D](class_camera3d.md#class-camera3d) node.
