# Shape2D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CapsuleShape2D](class_capsuleshape2d.md#class-capsuleshape2d), [CircleShape2D](class_circleshape2d.md#class-circleshape2d), [ConcavePolygonShape2D](class_concavepolygonshape2d.md#class-concavepolygonshape2d), [ConvexPolygonShape2D](class_convexpolygonshape2d.md#class-convexpolygonshape2d), [RectangleShape2D](class_rectangleshape2d.md#class-rectangleshape2d), [SegmentShape2D](class_segmentshape2d.md#class-segmentshape2d), [SeparationRayShape2D](class_separationrayshape2d.md#class-separationrayshape2d), [WorldBoundaryShape2D](class_worldboundaryshape2d.md#class-worldboundaryshape2d)

Abstract base class for 2D shapes used for physics collision.

## Description

Abstract base class for all 2D shapes, intended for use in physics.

**Performance:** Primitive shapes, especially [CircleShape2D](class_circleshape2d.md#class-circleshape2d), are fast to check collisions against. [ConvexPolygonShape2D](class_convexpolygonshape2d.md#class-convexpolygonshape2d) is slower, and [ConcavePolygonShape2D](class_concavepolygonshape2d.md#class-concavepolygonshape2d) is the slowest.

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

## Properties

| [float](class_float.md#class-float)   | custom_solver_bias   | `0.0`   |
|---------------------------------------|--------------------------------------------------------------------|---------|

## Methods

| [bool](class_bool.md#class-bool)                                           | collide(local_xform: [Transform2D](class_transform2d.md#class-transform2d), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | collide_and_get_contacts(local_xform: [Transform2D](class_transform2d.md#class-transform2d), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                           | collide_with_motion(local_xform: [Transform2D](class_transform2d.md#class-transform2d), local_motion: [Vector2](class_vector2.md#class-vector2), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d), shape_motion: [Vector2](class_vector2.md#class-vector2))                                   |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | collide_with_motion_and_get_contacts(local_xform: [Transform2D](class_transform2d.md#class-transform2d), local_motion: [Vector2](class_vector2.md#class-vector2), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d), shape_motion: [Vector2](class_vector2.md#class-vector2)) |
|                                                                            | draw(canvas_item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                          |
| [Rect2](class_rect2.md#class-rect2)                                        | get_rect()                                                                                                                                                                                                                                                                                                                                                        |

---

## Property Descriptions

[float](class_float.md#class-float) **custom_solver_bias** = `0.0`

-  **set_custom_solver_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_custom_solver_bias**()

The shape's custom solver bias. Defines how much bodies react to enforce contact separation when this shape is involved.

When set to `0`, the default value from [ProjectSettings.physics/2d/solver/default_contact_bias](class_projectsettings.md#class-projectsettings-property-physics-2d-solver-default-contact-bias) is used.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **collide**(local_xform: [Transform2D](class_transform2d.md#class-transform2d), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d))

Returns `true` if this shape is colliding with another.

This method needs the transformation matrix for this shape (`local_xform`), the shape to check collisions with (`with_shape`), and the transformation matrix of that shape (`shape_xform`).

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **collide_and_get_contacts**(local_xform: [Transform2D](class_transform2d.md#class-transform2d), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d))

Returns a list of contact point pairs where this shape touches another.

If there are no collisions, the returned list is empty. Otherwise, the returned list contains contact points arranged in pairs, with entries alternating between points on the boundary of this shape and points on the boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with `(B - A).normalized()`, and the collision depth with `(B - A).length()`. This information is typically used to separate shapes, particularly in collision solvers.

This method needs the transformation matrix for this shape (`local_xform`), the shape to check collisions with (`with_shape`), and the transformation matrix of that shape (`shape_xform`).

---

[bool](class_bool.md#class-bool) **collide_with_motion**(local_xform: [Transform2D](class_transform2d.md#class-transform2d), local_motion: [Vector2](class_vector2.md#class-vector2), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d), shape_motion: [Vector2](class_vector2.md#class-vector2))

Returns whether this shape would collide with another, if a given movement was applied.

This method needs the transformation matrix for this shape (`local_xform`), the movement to test on this shape (`local_motion`), the shape to check collisions with (`with_shape`), the transformation matrix of that shape (`shape_xform`), and the movement to test onto the other object (`shape_motion`).

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **collide_with_motion_and_get_contacts**(local_xform: [Transform2D](class_transform2d.md#class-transform2d), local_motion: [Vector2](class_vector2.md#class-vector2), with_shape: Shape2D, shape_xform: [Transform2D](class_transform2d.md#class-transform2d), shape_motion: [Vector2](class_vector2.md#class-vector2))

Returns a list of contact point pairs where this shape would touch another, if a given movement was applied.

If there would be no collisions, the returned list is empty. Otherwise, the returned list contains contact points arranged in pairs, with entries alternating between points on the boundary of this shape and points on the boundary of `with_shape`.

A collision pair A, B can be used to calculate the collision normal with `(B - A).normalized()`, and the collision depth with `(B - A).length()`. This information is typically used to separate shapes, particularly in collision solvers.

This method needs the transformation matrix for this shape (`local_xform`), the movement to test on this shape (`local_motion`), the shape to check collisions with (`with_shape`), the transformation matrix of that shape (`shape_xform`), and the movement to test onto the other object (`shape_motion`).

---

 **draw**(canvas_item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Draws a solid shape onto a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API filled with the specified `color`. The exact drawing method is specific for each shape and cannot be configured.

---

[Rect2](class_rect2.md#class-rect2) **get_rect**()

Returns a [Rect2](class_rect2.md#class-rect2) representing the shapes boundary.
