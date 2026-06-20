# OpenXRSpatialContextPersistenceConfig

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for spatial persistence.

## Description

Configuration header for spatial persistence. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) as the next parameter to create a spatial context with spatial persistence capabilities.

## Methods

|                                     | add_persistence_context(persistence_context: [RID](class_rid.md#class-rid))       |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array) | get_persistence_contexts()                                                       |
|                                     | remove_persistence_context(persistence_context: [RID](class_rid.md#class-rid)) |

---

## Method Descriptions

 **add_persistence_context**(persistence_context: [RID](class_rid.md#class-rid))

Adds a persistence context to this configuration. You must add at least one persistence context to create a valid configuration. You can create a persistence context by calling [OpenXRSpatialAnchorCapability.create_persistence_context()](class_openxrspatialanchorcapability.md#class-openxrspatialanchorcapability-method-create-persistence-context).

---

[Array](class_array.md#class-array) **get_persistence_contexts**()

Gets the persistence context(s) (as [RID](class_rid.md#class-rid)s) received by add_persistence_context().

---

 **remove_persistence_context**(persistence_context: [RID](class_rid.md#class-rid))

Removes a persistence context.
