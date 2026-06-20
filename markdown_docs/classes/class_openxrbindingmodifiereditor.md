# OpenXRBindingModifierEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class-panelcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Binding modifier editor.

## Description

This is the default binding modifier editor used in the OpenXR action map.

## Methods

| [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier)   | get_binding_modifier()                                                                                                                                                       |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                       | setup(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier)) |

---

## Signals

**binding_modifier_removed**(binding_modifier_editor: [Object](class_object.md#class-object))

Signal emitted when the user presses the delete binding modifier button for this modifier.

---

## Method Descriptions

[OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) **get_binding_modifier**()

Returns the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) currently being edited.

---

 **setup**(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier))

Setup this editor for the provided `action_map` and `binding_modifier`.
