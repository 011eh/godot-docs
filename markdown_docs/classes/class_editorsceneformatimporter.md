# EditorSceneFormatImporter

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorSceneFormatImporterBlend](class_editorsceneformatimporterblend.md#class-editorsceneformatimporterblend), [EditorSceneFormatImporterFBX2GLTF](class_editorsceneformatimporterfbx2gltf.md#class-editorsceneformatimporterfbx2gltf), [EditorSceneFormatImporterGLTF](class_editorsceneformatimportergltf.md#class-editorsceneformatimportergltf), [EditorSceneFormatImporterUFBX](class_editorsceneformatimporterufbx.md#class-editorsceneformatimporterufbx)

Imports scenes from third-parties' 3D files.

## Description

**EditorSceneFormatImporter** allows to define an importer script for a third-party 3D format.

To use **EditorSceneFormatImporter**, register it using the [EditorPlugin.add_scene_format_importer_plugin()](class_editorplugin.md#class-editorplugin-method-add-scene-format-importer-plugin) method first.

## Methods

| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | \_get_extensions()                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                           | \_get_import_options(path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                     |
| [Variant](class_variant.md#class-variant)                                 | \_get_option_visibility(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))                                                                                                                                                                                                                              |
| [Object](class_object.md#class-object)                                    | \_import_scene(path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int), options: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                              |
|                                                                           | add_import_option(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                               |
|                                                                           | add_import_option_advanced(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6) |

---

## Enumerations

flags **ImportFlags**:

ImportFlags **IMPORT_SCENE** = `1`

Unused flag (this has no effect when enabled).

ImportFlags **IMPORT_ANIMATION** = `2`

Import animations from the 3D scene. When importing a scene as an [AnimationLibrary](class_animationlibrary.md#class-animationlibrary), this flag is always enabled.

ImportFlags **IMPORT_FAIL_ON_MISSING_DEPENDENCIES** = `4`

Unused flag (this has no effect when enabled).

ImportFlags **IMPORT_GENERATE_TANGENT_ARRAYS** = `8`

If `true`, generate vertex tangents using [Mikktspace](http://www.mikktspace.com/) if the input meshes don't have tangent data. When possible, it's recommended to let the 3D modeling software generate tangents on export instead of relying on this option. Tangents are required for correct display of normal and height maps, along with any material/shader features that require tangents.

If you don't need material features that require tangents, disabling this can reduce output file size and speed up importing if the source 3D file doesn't contain tangents.

ImportFlags **IMPORT_USE_NAMED_SKIN_BINDS** = `16`

If checked, use named [Skin](class_skin.md#class-skin)s for animation. The [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) node contains 3 properties of relevance here: a skeleton [NodePath](class_nodepath.md#class-nodepath) pointing to the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node (usually `..`), a mesh, and a skin:

- The [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node contains a list of bones with names, their pose and rest, a name, and a parent bone.
- The mesh is all of the raw vertex data needed to display a mesh. In terms of the mesh, it knows how vertices are weight-painted and uses some internal numbering often imported from 3D modeling software.
- The skin contains the information necessary to bind this mesh onto this Skeleton3D. For each of the internal bone IDs chosen by the 3D modeling software, it contains two things. Firstly, a matrix known as the Bind Pose Matrix, Inverse Bind Matrix, or IBM for short. Secondly, the [Skin](class_skin.md#class-skin) contains each bone's name (if this flag is enabled), or the bone's index within the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) list (if this flag is disabled).

Together, this information is enough to tell Godot how to use the bone poses in the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node to render the mesh from each [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d). Note that each [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) may share binds, as is common in models exported from Blender, or each [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) may use a separate [Skin](class_skin.md#class-skin) object, as is common in models exported from other tools such as Maya.

ImportFlags **IMPORT_DISCARD_MESHES_AND_MATERIALS** = `32`

Ignore meshes and materials on import. When importing a scene as an [AnimationLibrary](class_animationlibrary.md#class-animationlibrary), this flag is always enabled.

ImportFlags **IMPORT_FORCE_DISABLE_MESH_COMPRESSION** = `64`

If `true`, mesh compression will not be used. Consider enabling if you notice blocky artifacts in your mesh normals or UVs, or if you have meshes that are larger than a few thousand meters in each direction.

---

## Method Descriptions

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_extensions**()

Return supported file extensions for this scene importer.

---

 **\_get_import_options**(path: [String](class_string.md#class-string))

Override to add general import options. These will appear in the main import dock on the editor. Add options via add_import_option() and add_import_option_advanced().

**Note:** All **EditorSceneFormatImporter** and [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin) instances will add options for all files. It is good practice to check the file extension when `path` is non-empty.

When the user is editing project settings, `path` will be empty. It is recommended to add all options when `path` is empty to allow the user to customize Import Defaults.

---

[Variant](class_variant.md#class-variant) **\_get_option_visibility**(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

[Object](class_object.md#class-object) **\_import_scene**(path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int), options: [Dictionary](class_dictionary.md#class-dictionary))

Perform the bulk of the scene import logic here, for example using [GLTFDocument](class_gltfdocument.md#class-gltfdocument) or [FBXDocument](class_fbxdocument.md#class-fbxdocument).

---

 **add_import_option**(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))

Add a specific import option (name and default value only). This function can only be called from \_get_import_options().

---

 **add_import_option_advanced**(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6)

Add a specific import option. This function can only be called from \_get_import_options().
