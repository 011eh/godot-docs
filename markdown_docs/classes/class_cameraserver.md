# CameraServer

**Inherits:** [Object](class_object.md#class-object)

Server keeping track of different cameras accessible in Godot.

## Description

The **CameraServer** keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no [CameraFeed](class_camerafeed.md#class-camerafeed)s will be available. To get a [CameraFeed](class_camerafeed.md#class-camerafeed) on iOS, enable [EditorExportPlatformIOS.modules/camera](class_editorexportplatformios.md#class-editorexportplatformios-property-modules-camera).

## Properties

| [bool](class_bool.md#class-bool)   | monitoring_feeds   | `false`   |
|------------------------------------|---------------------------------------------------------------------|-----------|

## Methods

|                                                                                         | add_feed(feed: [CameraFeed](class_camerafeed.md#class-camerafeed))       |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[CameraFeed](class_camerafeed.md#class-camerafeed)] | feeds()                                                                     |
| [CameraFeed](class_camerafeed.md#class-camerafeed)                                      | get_feed(index: [int](class_int.md#class-int))                           |
| [int](class_int.md#class-int)                                                           | get_feed_count()                                                   |
|                                                                                         | remove_feed(feed: [CameraFeed](class_camerafeed.md#class-camerafeed)) |

---

## Signals

**camera_feed_added**(id: [int](class_int.md#class-int))

Emitted when a [CameraFeed](class_camerafeed.md#class-camerafeed) is added (e.g. a webcam is plugged in).

---

**camera_feed_removed**(id: [int](class_int.md#class-int))

Emitted when a [CameraFeed](class_camerafeed.md#class-camerafeed) is removed (e.g. a webcam is unplugged).

---

**camera_feeds_updated**()

Emitted when camera feeds are updated.

---

## Enumerations

enum **FeedImage**:

FeedImage **FEED_RGBA_IMAGE** = `0`

The RGBA camera image.

FeedImage **FEED_YCBCR_IMAGE** = `0`

The [YCbCr](https://en.wikipedia.org/wiki/YCbCr) camera image.

FeedImage **FEED_Y_IMAGE** = `0`

The Y component camera image.

FeedImage **FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **monitoring_feeds** = `false`

-  **set_monitoring_feeds**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_monitoring_feeds**()

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you're actively accessing the camera.

**Note:** After setting it to `true`, you can receive updated camera feeds through the camera_feeds_updated signal.

GDScript

```gdscript
func _ready():
    CameraServer.camera_feeds_updated.connect(_on_camera_feeds_updated)
    CameraServer.monitoring_feeds = true

func _on_camera_feeds_updated():
    var feeds = CameraServer.feeds()
```

C#

```csharp
public override void _Ready()
{
    CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated;
    CameraServer.MonitoringFeeds = true;
}

void OnCameraFeedsUpdated()
{
    var feeds = CameraServer.Feeds();
}
```

---

## Method Descriptions

 **add_feed**(feed: [CameraFeed](class_camerafeed.md#class-camerafeed))

Adds the camera `feed` to the camera server.

---

[Array](class_array.md#class-array)[[CameraFeed](class_camerafeed.md#class-camerafeed)] **feeds**()

Returns an array of [CameraFeed](class_camerafeed.md#class-camerafeed)s.

---

[CameraFeed](class_camerafeed.md#class-camerafeed) **get_feed**(index: [int](class_int.md#class-int))

Returns the [CameraFeed](class_camerafeed.md#class-camerafeed) corresponding to the camera with the given `index`.

---

[int](class_int.md#class-int) **get_feed_count**()

Returns the number of [CameraFeed](class_camerafeed.md#class-camerafeed)s registered.

---

 **remove_feed**(feed: [CameraFeed](class_camerafeed.md#class-camerafeed))

Removes the specified camera `feed`.
