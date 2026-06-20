# RenderSceneBuffersExtension

**Inherits:** [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

## Description

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

## Methods

|    | \_configure(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration))    |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | \_set_anisotropic_filtering_level(anisotropic_filtering_level: [int](class_int.md#class-int))                       |
|    | \_set_fsr_sharpness(fsr_sharpness: [float](class_float.md#class-float))                                                           |
|    | \_set_texture_mipmap_bias(texture_mipmap_bias: [float](class_float.md#class-float))                                         |
|    | \_set_use_debanding(use_debanding: [bool](class_bool.md#class-bool))                                                              |

---

## Method Descriptions

 **\_configure**(config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class-renderscenebuffersconfiguration))

Implement this in GDExtension to handle the (re)sizing of a viewport.

---

 **\_set_anisotropic_filtering_level**(anisotropic_filtering_level: [int](class_int.md#class-int))

Implement this in GDExtension to change the anisotropic filtering level.

---

 **\_set_fsr_sharpness**(fsr_sharpness: [float](class_float.md#class-float))

Implement this in GDExtension to record a new FSR sharpness value.

---

 **\_set_texture_mipmap_bias**(texture_mipmap_bias: [float](class_float.md#class-float))

Implement this in GDExtension to change the texture mipmap bias.

---

 **\_set_use_debanding**(use_debanding: [bool](class_bool.md#class-bool))

Implement this in GDExtension to react to the debanding flag changing.
