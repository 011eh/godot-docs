# OpenXRSpatialCapabilityConfigurationAnchor

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class-openxrspatialcapabilityconfigurationbaseheader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration header for spatial anchors.

## Description

Configuration header for spatial anchors. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-create-spatial-context) to create a spatial context with spatial anchor capabilities.

## Methods

| [PackedInt64Array](class_packedint64array.md#class-packedint64array)   | get_enabled_components()    |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_enabled_components**()

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.
