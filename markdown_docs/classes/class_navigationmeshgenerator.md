# NavigationMeshGenerator

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:** [Object](class_object.md#class-object)

Helper class for creating and clearing navigation meshes.

## Description

This class is responsible for creating and clearing 3D navigation meshes used as [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources inside [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d). The **NavigationMeshGenerator** has very limited to no use for 2D as the navigation mesh baking process expects 3D node types and 3D source geometry to parse.

The entire navigation mesh baking is best done in a separate thread as the voxelization, collision tests and mesh optimization steps involved are very slow and performance-intensive operations.

Navigation mesh baking happens in multiple steps and the result depends on 3D source geometry and properties of the [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resource. In the first step, starting from a root node and depending on [NavigationMesh](class_navigationmesh.md#class-navigationmesh) properties all valid 3D source geometry nodes are collected from the [SceneTree](class_scenetree.md#class-scenetree). Second, all collected nodes are parsed for their relevant 3D geometry data and a combined 3D mesh is build. Due to the many different types of parsable objects, from normal [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)s to [CSGShape3D](class_csgshape3d.md#class-csgshape3d)s or various [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)s, some operations to collect geometry data can trigger [RenderingServer](class_renderingserver.md#class-renderingserver) and [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) synchronizations. Server synchronization can have a negative effect on baking time or framerate as it often involves [Mutex](class_mutex.md#class-mutex) locking for thread security. Many parsable objects and the continuous synchronization with other threaded Servers can increase the baking time significantly. On the other hand only a few but very large and complex objects will take some time to prepare for the Servers which can noticeably stall the next frame render. As a general rule the total number of parsable objects and their individual size and complexity should be balanced to avoid framerate issues or very long baking times. The combined mesh is then passed to the Recast Navigation Object to test the source geometry for walkable terrain suitable to [NavigationMesh](class_navigationmesh.md#class-navigationmesh) agent properties by creating a voxel world around the meshes bounding area.

The finalized navigation mesh is then returned and stored inside the [NavigationMesh](class_navigationmesh.md#class-navigationmesh) for use as a resource inside [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d) nodes.

**Note:** Using meshes to not only define walkable surfaces but also obstruct navigation baking does not always work. The navigation baking has no concept of what is a geometry "inside" when dealing with mesh source geometry and this is intentional. Depending on current baking parameters, as soon as the obstructing mesh is large enough to fit a navigation mesh area inside, the baking will generate navigation mesh areas that are inside the obstructing source geometry mesh.

## Tutorials

- [Using NavigationMeshes](../tutorials/navigation/navigation_using_navigationmeshes.md)

## Methods

|    | bake(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), root_node: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                    |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | bake_from_source_geometry_data(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d), callback: [Callable](class_callable.md#class-callable) = Callable())                                      |
|    | clear(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh))                                                                                                                                                                                                                                                                                                               |
|    | parse_source_geometry_data(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d), root_node: [Node](class_node.md#class-node), callback: [Callable](class_callable.md#class-callable) = Callable()) |

---

## Method Descriptions

 **bake**(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), root_node: [Node](class_node.md#class-node))

**Deprecated:** This method is deprecated due to core threading changes. To upgrade existing code, first create a [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d) resource. Use this resource with parse_source_geometry_data() to parse the [SceneTree](class_scenetree.md#class-scenetree) for nodes that should contribute to the navigation mesh baking. The [SceneTree](class_scenetree.md#class-scenetree) parsing needs to happen on the main thread. After the parsing is finished use the resource with bake_from_source_geometry_data() to bake a navigation mesh.

Bakes the `navigation_mesh` with source geometry collected starting from the `root_node`.

---

 **bake_from_source_geometry_data**(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d), callback: [Callable](class_callable.md#class-callable) = Callable())

Bakes the provided `navigation_mesh` with the data from the provided `source_geometry_data`. After the process is finished the optional `callback` will be called.

---

 **clear**(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh))

Removes all polygons and vertices from the provided `navigation_mesh` resource.

---

 **parse_source_geometry_data**(navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class-navigationmeshsourcegeometrydata3d), root_node: [Node](class_node.md#class-node), callback: [Callable](class_callable.md#class-callable) = Callable())

Parses the [SceneTree](class_scenetree.md#class-scenetree) for source geometry according to the properties of `navigation_mesh`. Updates the provided `source_geometry_data` resource with the resulting data. The resource can then be used to bake a navigation mesh with bake_from_source_geometry_data(). After the process is finished the optional `callback` will be called.

**Note:** This function needs to run on the main thread or with a deferred call as the SceneTree is not thread-safe.

**Performance:** While convenient, reading data arrays from [Mesh](class_mesh.md#class-mesh) resources can affect the frame rate negatively. The data needs to be received from the GPU, stalling the [RenderingServer](class_renderingserver.md#class-renderingserver) in the process. For performance prefer the use of e.g. collision shapes or creating the data arrays entirely in code.
