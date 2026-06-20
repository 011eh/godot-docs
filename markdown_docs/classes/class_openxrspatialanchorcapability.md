# OpenXRSpatialAnchorCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

Implementation for handling spatial entity anchor logic.

## Description

This is an internal class that handles the OpenXR anchor spatial entity extension.

## Methods

| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)    | create_default_persistence_context(user_callback: [Callable](class_callable.md#class-callable) = Callable())                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker) | create_new_anchor(transform: [Transform3D](class_transform3d.md#class-transform3d), spatial_context: [RID](class_rid.md#class-rid) = RID(), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null)                                                                                                                                                                                                                                                                                               |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)    | create_persistence_context(scope: PersistenceScope, user_callback: [Callable](class_callable.md#class-callable) = Callable())                                                                                                                                                                                                                                                                                                                                        |
|                                                                               | do_entity_update(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null)                                                                                       |
|                                                                               | free_persistence_context(persistence_context: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                 | get_persistence_context_handle(persistence_context: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                              | is_persistence_scope_supported(scope: PersistenceScope)                                                                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                              | is_spatial_anchor_supported()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                              | is_spatial_persistence_supported()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)    | persist_anchor(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), persistence_context: [RID](class_rid.md#class-rid) = RID(), user_callback: [Callable](class_callable.md#class-callable) = Callable())                                                                                                                                                                                                                                                                                      |
|                                                                               | remove_anchor(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker))                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)    | start_entity_discovery(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable()) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult)    | unpersist_anchor(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), persistence_context: [RID](class_rid.md#class-rid) = RID(), user_callback: [Callable](class_callable.md#class-callable) = Callable())                                                                                                                                                                                                                                                                                  |

---

## Enumerations

enum **PersistenceScope**:

PersistenceScope **PERSISTENCE_SCOPE_SYSTEM_MANAGED** = `1`

Provides the application with read-only access (i.e. application cannot modify this scope) to spatial entities persisted and managed by the system. The application can use the UUID in the persistence component for this scope to correlate entities across spatial contexts and device reboots.

PersistenceScope **PERSISTENCE_SCOPE_LOCAL_ANCHORS** = `1000781000`

Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and same app (using persist_anchor() and unpersist_anchor() functions)

---

## Method Descriptions

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **create_default_persistence_context**(user_callback: [Callable](class_callable.md#class-callable) = Callable())

Calls create_persistence_context() with a configuration that likely works with the XR runtime.

`user_callback` is called when the context is created.

---

[OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker) **create_new_anchor**(transform: [Transform3D](class_transform3d.md#class-transform3d), spatial_context: [RID](class_rid.md#class-rid) = RID(), next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null)

Creates a new anchor that will be tracked by the XR runtime. The `transform` should be a transform in the local space of your [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) node. If `spatial_context` is not specified the default will be used, this requires [ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection](class_projectsettings.md#class-projectsettings-property-xr-openxr-extensions-spatial-entity-enable-builtin-anchor-detection) to be set. The returned tracker will track the location in case our reference space changes.

`next` must be a valid next object for the `XrSpatialAnchorCreateInfoEXT` chain.

---

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **create_persistence_context**(scope: PersistenceScope, user_callback: [Callable](class_callable.md#class-callable) = Callable())

Creates a new persistence context for storing persistent data.

**Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is the [RID](class_rid.md#class-rid) for our persistence context.

---

 **do_entity_update**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null)

Calls [OpenXRSpatialEntityExtension.update_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities) and [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot) with the anchor entities associated with `spatial_context`.

`component_data` are the [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)s to update for this anchor capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.update_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-update-spatial-entities).

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

---

 **free_persistence_context**(persistence_context: [RID](class_rid.md#class-rid))

Frees a persistence context previously created with create_persistence_context().

---

[int](class_int.md#class-int) **get_persistence_context_handle**(persistence_context: [RID](class_rid.md#class-rid))

Returns the internal handle for this persistence context.

**Note:** For GDExtension implementations.

---

[bool](class_bool.md#class-bool) **is_persistence_scope_supported**(scope: PersistenceScope)

Returns `true` if this persistence scope is supported by our spatial anchor capability.

**Note:** Only valid after an OpenXR instance has been created.

---

[bool](class_bool.md#class-bool) **is_spatial_anchor_supported**()

Returns `true` if spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

---

[bool](class_bool.md#class-bool) **is_spatial_persistence_supported**()

Returns `true` if persistent spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

---

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **persist_anchor**(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), persistence_context: [RID](class_rid.md#class-rid) = RID(), user_callback: [Callable](class_callable.md#class-callable) = Callable())

Changes this anchor into a persistent anchor. This means its location will be stored on the device and the anchor will be restored the next time your application starts. If `persistence_context` is not specified the default will be used, this requires [ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection](class_projectsettings.md#class-projectsettings-property-xr-openxr-extensions-spatial-entity-enable-builtin-anchor-detection) to be set.

**Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.

---

 **remove_anchor**(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker))

Remove an anchor previously created with create_new_anchor(). If this anchor was persistent you must first call unpersist_anchor() and await its callback.

---

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **start_entity_discovery**(spatial_context: [RID](class_rid.md#class-rid), component_data: [Array](class_array.md#class-array)[[OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)], next_snapshot_create: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, next_snapshot_query: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) = null, user_callback: [Callable](class_callable.md#class-callable) = Callable())

Calls [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities) and [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot) with the anchor entities associated with `spatial_context`.

`component_data` are the [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata)s to discover for this anchor capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

`user_callback`, when non-null, is called with two parameters usually twice. The first parameter is the [RID](class_rid.md#class-rid) of the discovery snapshot and the second parameter is a boolean where `false` indicates the discovery snapshot is about to be processed, and `true` indicates the discovery snapshot has been processed and `component_data` has valid data. The second call is skipped if an error was encountered.

The returned [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) is identical to the return from [OpenXRSpatialEntityExtension.discover_spatial_entities()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-discover-spatial-entities).

---

[OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) **unpersist_anchor**(anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), persistence_context: [RID](class_rid.md#class-rid) = RID(), user_callback: [Callable](class_callable.md#class-callable) = Callable())

Removes the persistent data from this anchor. The runtime will not recreate the anchor when your application restarts. If `persistence_context` is not specified the default will be used, this requires [ProjectSettings.xr/openxr/extensions/spatial_entity/enabled](class_projectsettings.md#class-projectsettings-property-xr-openxr-extensions-spatial-entity-enabled) to be set.

**Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class-openxrfutureresult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.
