# OpenXRInteractionProfileEditorBase

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRInteractionProfileEditor](class_openxrinteractionprofileeditor.md#class-openxrinteractionprofileeditor)

Base class for editing interaction profiles.

## Description

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.

## Methods

|    | setup(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile))   |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

 **setup**(action_map: [OpenXRActionMap](class_openxractionmap.md#class-openxractionmap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile))

Setup this editor for the provided `action_map` and `interaction_profile`.
