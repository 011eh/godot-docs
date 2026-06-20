# RenderSceneBuffers

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [RenderSceneBuffersExtension](class_renderscenebuffersextension.md#class-renderscenebuffersextension), [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class-renderscenebuffersrd)

Abstract scene buffers object, created for each viewport for which 3D rendering is done.

## Description

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class-renderscenebuffersrd).

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

## Methods

|    | configure(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration))   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

 **configure**(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration))

This method is called by the rendering server when the associated viewport's configuration is changed. It will discard the old buffers and recreate the internal buffers used.
