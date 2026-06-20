# XRCamera3D

**Inherits:** [Camera3D](class_camera3d.md#class-camera3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A camera node which automatically positions itself based on XR tracking data.

## Description

A camera node which automatically positions itself based on XR tracking data.

In contrast to [XRController3D](class_xrcontroller3d.md#class-xrcontroller3d), the render thread has access to more up-to-date tracking data, and the location of the **XRCamera3D** node can lag a few milliseconds behind what is used for rendering.

**Note:** If [Viewport.use_xr](class_viewport.md#class-viewport-property-use-xr) is `true`, most of the camera properties are overridden by the active [XRInterface](class_xrinterface.md#class-xrinterface). The only properties that can be trusted are the near and far planes.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| [PhysicsInterpolationMode](class_node.md#enum-node-physicsinterpolationmode)   | physics_interpolation_mode   | `2` (overrides [Node](class_node.md#class-node-property-physics-interpolation-mode))   |
|--------------------------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------|
