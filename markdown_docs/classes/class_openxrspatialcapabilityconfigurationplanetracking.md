# OpenXRSpatialCapabilityConfigurationPlaneTracking

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for plane tracking.

## Description

Configuration header for plane tracking. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context with plane tracking capabilities.

## Methods

| [PackedInt64Array](class_packedint64array.md#class-packedint64array)   | get_enabled_components()    |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                       | supports_labels()                  |
| [bool](class_bool.md#class-bool)                                       | supports_mesh_2d()                |
| [bool](class_bool.md#class-bool)                                       | supports_polygons()              |

---

## Method Descriptions

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**()

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.

---

[bool](class_bool.md#class-bool) **supports_labels**()

Returns `true` if we support the plane semantic label component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist) data object.

---

[bool](class_bool.md#class-bool) **supports_mesh_2d**()

Returns `true` if we support the mesh 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist) data object.

---

[bool](class_bool.md#class-bool) **supports_polygons**()

Returns `true` if we support the polygon 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist) data object.
