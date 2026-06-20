# Light2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [DirectionalLight2D](class_directionallight2d.md#class-directionallight2d), [PointLight2D](class_pointlight2d.md#class-pointlight2d)

Casts light in a 2D environment.

## Description

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

## Properties

| BlendMode       | blend_mode                       | `0`                 |
|--------------------------------------------|------------------------------------------------------------------------|---------------------|
| [Color](class_color.md#class-color)        | color                                 | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool)           | editor_only                     | `false`             |
| [bool](class_bool.md#class-bool)           | enabled                             | `true`              |
| [float](class_float.md#class-float)        | energy                               | `1.0`               |
| [int](class_int.md#class-int)              | range_item_cull_mask   | `1`                 |
| [int](class_int.md#class-int)              | range_layer_max             | `0`                 |
| [int](class_int.md#class-int)              | range_layer_min             | `0`                 |
| [int](class_int.md#class-int)              | range_z_max                     | `1024`              |
| [int](class_int.md#class-int)              | range_z_min                     | `-1024`             |
| [Color](class_color.md#class-color)        | shadow_color                   | `Color(0, 0, 0, 0)` |
| [bool](class_bool.md#class-bool)           | shadow_enabled               | `false`             |
| ShadowFilter | shadow_filter                 | `0`                 |
| [float](class_float.md#class-float)        | shadow_filter_smooth   | `0.0`               |
| [int](class_int.md#class-int)              | shadow_item_cull_mask | `1`                 |

## Methods

| [float](class_float.md#class-float)   | get_height()                                            |
|---------------------------------------|---------------------------------------------------------------------------------------------|
|                                       | set_height(height: [float](class_float.md#class-float)) |

---

## Enumerations

enum **ShadowFilter**:

ShadowFilter **SHADOW_FILTER_NONE** = `0`

No filter applies to the shadow map. This provides hard shadow edges and is the fastest to render. See shadow_filter.

ShadowFilter **SHADOW_FILTER_PCF5** = `1`

Percentage closer filtering (5 samples) applies to the shadow map. This is slower compared to hard shadow rendering. See shadow_filter.

ShadowFilter **SHADOW_FILTER_PCF13** = `2`

Percentage closer filtering (13 samples) applies to the shadow map. This is the slowest shadow filtering mode, and should be used sparingly. See shadow_filter.

---

enum **BlendMode**:

BlendMode **BLEND_MODE_ADD** = `0`

Adds the value of pixels corresponding to the Light2D to the values of pixels under it. This is the common behavior of a light.

BlendMode **BLEND_MODE_SUB** = `1`

Subtracts the value of pixels corresponding to the Light2D to the values of pixels under it, resulting in inversed light effect.

BlendMode **BLEND_MODE_MIX** = `2`

Mix the value of pixels corresponding to the Light2D to the values of pixels under it by linear interpolation.

---

## Property Descriptions

BlendMode **blend_mode** = `0`

-  **set_blend_mode**(value: BlendMode)
- BlendMode **get_blend_mode**()

The Light2D's blend mode.

---

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The Light2D's [Color](class_color.md#class-color).

---

[bool](class_bool.md#class-bool) **editor_only** = `false`

-  **set_editor_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editor_only**()

If `true`, Light2D will only appear when editing the scene.

---

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, Light2D will emit light.

---

[float](class_float.md#class-float) **energy** = `1.0`

-  **set_energy**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy**()

The Light2D's energy value. The larger the value, the stronger the light.

---

[int](class_int.md#class-int) **range_item_cull_mask** = `1`

-  **set_item_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_cull_mask**()

The layer mask. Only objects with a matching [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask) will be affected by the Light2D. See also shadow_item_cull_mask, which affects which objects can cast shadows.

**Note:** range_item_cull_mask is ignored by [DirectionalLight2D](class_directionallight2d.md#class-directionallight2d), which will always light a 2D node regardless of the 2D node's [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask).

---

[int](class_int.md#class-int) **range_layer_max** = `0`

-  **set_layer_range_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layer_range_max**()

Maximum layer value of objects that are affected by the Light2D.

---

[int](class_int.md#class-int) **range_layer_min** = `0`

-  **set_layer_range_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layer_range_min**()

Minimum layer value of objects that are affected by the Light2D.

---

[int](class_int.md#class-int) **range_z_max** = `1024`

-  **set_z_range_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_range_max**()

Maximum `z` value of objects that are affected by the Light2D.

---

[int](class_int.md#class-int) **range_z_min** = `-1024`

-  **set_z_range_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_range_min**()

Minimum `z` value of objects that are affected by the Light2D.

---

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0)`

-  **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

[Color](class_color.md#class-color) of shadows cast by the Light2D.

---

[bool](class_bool.md#class-bool) **shadow_enabled** = `false`

-  **set_shadow_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shadow_enabled**()

If `true`, the Light2D will cast shadows.

---

ShadowFilter **shadow_filter** = `0`

-  **set_shadow_filter**(value: ShadowFilter)
- ShadowFilter **get_shadow_filter**()

Shadow filter type.

---

[float](class_float.md#class-float) **shadow_filter_smooth** = `0.0`

-  **set_shadow_smooth**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_shadow_smooth**()

Smoothing value for shadows. Higher values will result in softer shadows, at the cost of visible streaks that can appear in shadow rendering. shadow_filter_smooth only has an effect if shadow_filter is SHADOW_FILTER_PCF5 or SHADOW_FILTER_PCF13.

---

[int](class_int.md#class-int) **shadow_item_cull_mask** = `1`

-  **set_item_shadow_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_shadow_cull_mask**()

The shadow mask. Used with [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) to cast shadows. Only occluders with a matching [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask) will cast shadows. See also range_item_cull_mask, which affects which objects can *receive* the light.

---

## Method Descriptions

[float](class_float.md#class-float) **get_height**()

Returns the light's height, which is used in 2D normal mapping. See [PointLight2D.height](class_pointlight2d.md#class-pointlight2d-property-height) and [DirectionalLight2D.height](class_directionallight2d.md#class-directionallight2d-property-height).

---

 **set_height**(height: [float](class_float.md#class-float))

Sets the light's height, which is used in 2D normal mapping. See [PointLight2D.height](class_pointlight2d.md#class-pointlight2d-property-height) and [DirectionalLight2D.height](class_directionallight2d.md#class-directionallight2d-property-height).
