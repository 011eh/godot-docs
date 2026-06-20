# ColorPicker

**Inherits:** [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A widget that provides an interface for selecting or modifying a color.

## Description

A widget that provides an interface for selecting or modifying a color. It can optionally provide functionalities like a color sampler (eyedropper), color modes, and presets.

**Note:** This control is the color picker widget itself. You can use a [ColorPickerButton](class_colorpickerbutton.md#class-colorpickerbutton) instead if you need a button that brings up a **ColorPicker** in a popup.

## Tutorials

- [Tween Interpolation Demo](https://godotengine.org/asset-library/asset/2733)

## Properties

| [bool](class_bool.md#class-bool)                     | can_add_swatches       | `true`              |
|------------------------------------------------------|------------------------------------------------------------------------|---------------------|
| [Color](class_color.md#class-color)                  | color                             | `Color(1, 1, 1, 1)` |
| ColorModeType     | color_mode                   | `0`                 |
| [bool](class_bool.md#class-bool)                     | color_modes_visible | `true`              |
| [bool](class_bool.md#class-bool)                     | deferred_mode             | `false`             |
| [bool](class_bool.md#class-bool)                     | edit_alpha                   | `true`              |
| [bool](class_bool.md#class-bool)                     | edit_intensity           | `true`              |
| [bool](class_bool.md#class-bool)                     | hex_visible                 | `true`              |
| PickerShapeType | picker_shape               | `0`                 |
| [bool](class_bool.md#class-bool)                     | presets_visible         | `true`              |
| [bool](class_bool.md#class-bool)                     | sampler_visible         | `true`              |
| [bool](class_bool.md#class-bool)                     | sliders_visible         | `true`              |

## Methods

|                                                                      | add_preset(color: [Color](class_color.md#class-color))                   |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
|                                                                      | add_recent_preset(color: [Color](class_color.md#class-color))     |
|                                                                      | erase_preset(color: [Color](class_color.md#class-color))               |
|                                                                      | erase_recent_preset(color: [Color](class_color.md#class-color)) |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | get_presets()                                                           |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | get_recent_presets()                                             |

## Theme Properties

| [Color](class_color.md#class-color)             | focused_not_editing_cursor_color   | `Color(1, 1, 1, 0.275)`   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------|
| [int](class_int.md#class-int)                   | center_slider_grabbers                    | `1`                       |
| [int](class_int.md#class-int)                   | h_width                                                  | `30`                      |
| [int](class_int.md#class-int)                   | label_width                                          | `10`                      |
| [int](class_int.md#class-int)                   | margin                                                    | `4`                       |
| [int](class_int.md#class-int)                   | sv_height                                              | `256`                     |
| [int](class_int.md#class-int)                   | sv_width                                                | `256`                     |
| [Texture2D](class_texture2d.md#class-texture2d) | add_preset                                                |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | bar_arrow                                                  |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | color_copy                                                |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | color_hue                                                  |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | color_script                                            |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | expanded_arrow                                        |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | folded_arrow                                            |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_option                                              |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | overbright_indicator                            |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | picker_cursor                                          |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | picker_cursor_bg                                    |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | sample_bg                                                  |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | sample_revert                                          |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | screen_picker                                          |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | shape_circle                                            |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | shape_rect                                                |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | shape_rect_wheel                                    |                           |
| [StyleBox](class_stylebox.md#class-stylebox)    | picker_focus_circle                             |                           |
| [StyleBox](class_stylebox.md#class-stylebox)    | picker_focus_rectangle                       |                           |
| [StyleBox](class_stylebox.md#class-stylebox)    | sample_focus                                           |                           |

---

## Signals

**color_changed**(color: [Color](class_color.md#class-color))

Emitted when the color is changed.

---

**preset_added**(color: [Color](class_color.md#class-color))

Emitted when a preset is added.

---

**preset_removed**(color: [Color](class_color.md#class-color))

Emitted when a preset is removed.

---

## Enumerations

enum **ColorModeType**:

ColorModeType **MODE_RGB** = `0`

Allows editing the color with Red/Green/Blue sliders in sRGB color space.

ColorModeType **MODE_HSV** = `1`

Allows editing the color with Hue/Saturation/Value sliders.

ColorModeType **MODE_RAW** = `2`

**Deprecated:** This is replaced by MODE_LINEAR.

ColorModeType **MODE_LINEAR** = `2`

Allows editing the color with Red/Green/Blue sliders in linear color space.

ColorModeType **MODE_OKHSL** = `3`

Allows editing the color with Hue/Saturation/Lightness sliders.

OKHSL is a new color space similar to HSL but that better match perception by leveraging the Oklab color space which is designed to be simple to use, while doing a good job at predicting perceived lightness, chroma and hue.

[Okhsv and Okhsl color spaces](https://bottosson.github.io/posts/colorpicker/)

---

enum **PickerShapeType**:

PickerShapeType **SHAPE_HSV_RECTANGLE** = `0`

HSV Color Model rectangle color space.

PickerShapeType **SHAPE_HSV_WHEEL** = `1`

HSV Color Model rectangle color space with a wheel.

PickerShapeType **SHAPE_VHS_CIRCLE** = `2`

HSV Color Model circle color space. Use Saturation as a radius.

PickerShapeType **SHAPE_OKHSL_CIRCLE** = `3`

HSL OK Color Model circle color space.

PickerShapeType **SHAPE_NONE** = `4`

The color space shape and the shape select button are hidden. Can't be selected from the shapes popup.

PickerShapeType **SHAPE_OK_HS_RECTANGLE** = `5`

OKHSL Color Model rectangle with constant lightness.

PickerShapeType **SHAPE_OK_HL_RECTANGLE** = `6`

OKHSL Color Model rectangle with constant saturation.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **can_add_swatches** = `true`

-  **set_can_add_swatches**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_swatches_enabled**()

If `true`, it's possible to add presets under Swatches. If `false`, the button to add presets is disabled.

---

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)`

-  **set_pick_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_pick_color**()

The currently selected color.

---

ColorModeType **color_mode** = `0`

-  **set_color_mode**(value: ColorModeType)
- ColorModeType **get_color_mode**()

The currently selected color mode.

---

[bool](class_bool.md#class-bool) **color_modes_visible** = `true`

-  **set_modes_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_modes_visible**()

If `true`, the color mode buttons are visible.

---

[bool](class_bool.md#class-bool) **deferred_mode** = `false`

-  **set_deferred_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deferred_mode**()

If `true`, the color will apply only after the user releases the mouse button, otherwise it will apply immediately even in mouse motion event (which can cause performance issues).

---

[bool](class_bool.md#class-bool) **edit_alpha** = `true`

-  **set_edit_alpha**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_alpha**()

If `true`, shows an alpha channel slider (opacity).

---

[bool](class_bool.md#class-bool) **edit_intensity** = `true`

-  **set_edit_intensity**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_intensity**()

If `true`, shows an intensity slider. The intensity is applied as follows: convert the color to linear encoding, multiply it by `2 ** intensity`, and then convert it back to nonlinear sRGB encoding.

---

[bool](class_bool.md#class-bool) **hex_visible** = `true`

-  **set_hex_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hex_visible**()

If `true`, the hex color code input field is visible.

---

PickerShapeType **picker_shape** = `0`

-  **set_picker_shape**(value: PickerShapeType)
- PickerShapeType **get_picker_shape**()

The shape of the color space view.

---

[bool](class_bool.md#class-bool) **presets_visible** = `true`

-  **set_presets_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_presets_visible**()

If `true`, the Swatches and Recent Colors presets are visible.

---

[bool](class_bool.md#class-bool) **sampler_visible** = `true`

-  **set_sampler_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_sampler_visible**()

If `true`, the color sampler and color preview are visible.

---

[bool](class_bool.md#class-bool) **sliders_visible** = `true`

-  **set_sliders_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_sliders_visible**()

If `true`, the color sliders are visible.

---

## Method Descriptions

 **add_preset**(color: [Color](class_color.md#class-color))

Adds the given color to a list of color presets. The presets are displayed in the color picker and the user will be able to select them.

**Note:** The presets list is only for *this* color picker.

---

 **add_recent_preset**(color: [Color](class_color.md#class-color))

Adds the given color to a list of color recent presets so that it can be picked later. Recent presets are the colors that were picked recently, a new preset is automatically created and added to recent presets when you pick a new color.

**Note:** The recent presets list is only for *this* color picker.

---

 **erase_preset**(color: [Color](class_color.md#class-color))

Removes the given color from the list of color presets of this color picker.

---

 **erase_recent_preset**(color: [Color](class_color.md#class-color))

Removes the given color from the list of color recent presets of this color picker.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_presets**()

Returns the list of colors in the presets of the color picker.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_recent_presets**()

Returns the list of colors in the recent presets of the color picker.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **focused_not_editing_cursor_color** = `Color(1, 1, 1, 0.275)`

Color of rectangle or circle drawn when a picker shape part is focused but not editable via keyboard or joypad. Displayed *over* the picker shape, so a partially transparent color should be used to ensure the picker shape remains visible.

---

[int](class_int.md#class-int) **center_slider_grabbers** = `1`

Overrides the [Slider.center_grabber](class_slider.md#class-slider-theme-constant-center-grabber) theme property of the sliders.

---

[int](class_int.md#class-int) **h_width** = `30`

The width of the hue selection slider.

---

[int](class_int.md#class-int) **label_width** = `10`

The minimum width of the color labels next to sliders.

---

[int](class_int.md#class-int) **margin** = `4`

The margin around the **ColorPicker**.

---

[int](class_int.md#class-int) **sv_height** = `256`

The height of the saturation-value selection box.

---

[int](class_int.md#class-int) **sv_width** = `256`

The width of the saturation-value selection box.

---

[Texture2D](class_texture2d.md#class-texture2d) **add_preset**

The icon for the "Add Preset" button.

---

[Texture2D](class_texture2d.md#class-texture2d) **bar_arrow**

The texture for the arrow grabber.

---

[Texture2D](class_texture2d.md#class-texture2d) **color_copy**

The icon for the button that copies the color in text format to the clipboard.

---

[Texture2D](class_texture2d.md#class-texture2d) **color_hue**

Custom texture for the hue selection slider on the right.

---

[Texture2D](class_texture2d.md#class-texture2d) **color_script**

The icon for the button that switches color text to hexadecimal.

---

[Texture2D](class_texture2d.md#class-texture2d) **expanded_arrow**

The icon for color preset drop down menu when expanded.

---

[Texture2D](class_texture2d.md#class-texture2d) **folded_arrow**

The icon for color preset drop down menu when folded.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_option**

The icon for color preset option menu.

---

[Texture2D](class_texture2d.md#class-texture2d) **overbright_indicator**

The indicator used to signalize that the color value is outside the 0-1 range.

---

[Texture2D](class_texture2d.md#class-texture2d) **picker_cursor**

The image displayed over the color box/circle (depending on the picker_shape), marking the currently selected color.

---

[Texture2D](class_texture2d.md#class-texture2d) **picker_cursor_bg**

The fill image displayed behind the picker cursor.

---

[Texture2D](class_texture2d.md#class-texture2d) **sample_bg**

Background panel for the color preview box (visible when the color is translucent).

---

[Texture2D](class_texture2d.md#class-texture2d) **sample_revert**

The icon for the revert button (visible on the middle of the "old" color when it differs from the currently selected color). This icon is modulated with a dark color if the "old" color is bright enough, so the icon should be bright to ensure visibility in both scenarios.

---

[Texture2D](class_texture2d.md#class-texture2d) **screen_picker**

The icon for the screen color picker button.

---

[Texture2D](class_texture2d.md#class-texture2d) **shape_circle**

The icon for circular picker shapes.

---

[Texture2D](class_texture2d.md#class-texture2d) **shape_rect**

The icon for rectangular picker shapes.

---

[Texture2D](class_texture2d.md#class-texture2d) **shape_rect_wheel**

The icon for rectangular wheel picker shapes.

---

[StyleBox](class_stylebox.md#class-stylebox) **picker_focus_circle**

The [StyleBox](class_stylebox.md#class-stylebox) used when the circle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **picker_focus_rectangle**

The [StyleBox](class_stylebox.md#class-stylebox) used when the rectangle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **sample_focus**

The [StyleBox](class_stylebox.md#class-stylebox) used for the old color sample part when it is focused. Displayed *over* the sample, so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
