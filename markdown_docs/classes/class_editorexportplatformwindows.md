# EditorExportPlatformWindows

**Inherits:** [EditorExportPlatformPC](class_editorexportplatformpc.md#class-editorexportplatformpc) **<** [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Exporter for Windows.

## Description

The Windows exporter customizes how a Windows build is handled. In the editor's "Export" window, it is created when adding a new "Windows" preset.

## Tutorials

- [Exporting for Windows](../tutorials/export/exporting_for_windows.md)

## Properties

| [String](class_string.md#class-string)                                  | application/company_name                               |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | application/console_wrapper_icon               |
| [String](class_string.md#class-string)                                  | application/copyright                                     |
| [bool](class_bool.md#class-bool)                                        | application/d3d12_agility_sdk_multiarch |
| [int](class_int.md#class-int)                                           | application/export_angle                               |
| [int](class_int.md#class-int)                                           | application/export_d3d12                               |
| [String](class_string.md#class-string)                                  | application/file_description                       |
| [String](class_string.md#class-string)                                  | application/file_version                               |
| [String](class_string.md#class-string)                                  | application/icon                                               |
| [int](class_int.md#class-int)                                           | application/icon_interpolation                   |
| [bool](class_bool.md#class-bool)                                        | application/modify_resources                       |
| [String](class_string.md#class-string)                                  | application/product_name                               |
| [String](class_string.md#class-string)                                  | application/product_version                         |
| [String](class_string.md#class-string)                                  | application/trademarks                                   |
| [String](class_string.md#class-string)                                  | binary_format/architecture                           |
| [bool](class_bool.md#class-bool)                                        | binary_format/embed_pck                                 |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | codesign/custom_options                                 |
| [String](class_string.md#class-string)                                  | codesign/description                                       |
| [int](class_int.md#class-int)                                           | codesign/digest_algorithm                             |
| [bool](class_bool.md#class-bool)                                        | codesign/enable                                                 |
| [String](class_string.md#class-string)                                  | codesign/identity                                             |
| [int](class_int.md#class-int)                                           | codesign/identity_type                                   |
| [String](class_string.md#class-string)                                  | codesign/password                                             |
| [bool](class_bool.md#class-bool)                                        | codesign/timestamp                                           |
| [String](class_string.md#class-string)                                  | codesign/timestamp_server_url                     |
| [String](class_string.md#class-string)                                  | custom_template/debug                                     |
| [String](class_string.md#class-string)                                  | custom_template/release                                 |
| [int](class_int.md#class-int)                                           | debug/export_console_wrapper                       |
| [bool](class_bool.md#class-bool)                                        | shader_baker/enabled                                       |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/cleanup_script               |
| [bool](class_bool.md#class-bool)                                        | ssh_remote_deploy/enabled                             |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/extra_args_scp               |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/extra_args_ssh               |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/host                                   |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/port                                   |
| [String](class_string.md#class-string)                                  | ssh_remote_deploy/run_script                       |
| [bool](class_bool.md#class-bool)                                        | texture_format/etc2_astc                               |
| [bool](class_bool.md#class-bool)                                        | texture_format/s3tc_bptc                               |

---

## Property Descriptions

[String](class_string.md#class-string) **application/company_name**

Company that produced the application. Required. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **application/console_wrapper_icon**

Console wrapper icon file. If left empty, it will fallback to application/icon, then to [ProjectSettings.application/config/windows_native_icon](class_projectsettings.md#class-projectsettings-property-application-config-windows-native-icon), and lastly, [ProjectSettings.application/config/icon](class_projectsettings.md#class-projectsettings-property-application-config-icon).

---

[String](class_string.md#class-string) **application/copyright**

Copyright notice for the bundle visible to the user. Optional. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[bool](class_bool.md#class-bool) **application/d3d12_agility_sdk_multiarch**

If `true`, and application/export_d3d12 is set, the Agility SDK DLLs will be stored in arch-specific subdirectories.

---

[int](class_int.md#class-int) **application/export_angle**

If set to `1`, ANGLE libraries are exported with the exported application. If set to `0`, ANGLE libraries are exported only if [ProjectSettings.rendering/gl_compatibility/driver](class_projectsettings.md#class-projectsettings-property-rendering-gl-compatibility-driver) is set to `"opengl3_angle"`.

---

[int](class_int.md#class-int) **application/export_d3d12**

If set to `1`, the Direct3D 12 runtime libraries (Agility SDK, PIX) are exported with the exported application. If set to `0`, Direct3D 12 libraries are exported only if [ProjectSettings.rendering/rendering_device/driver](class_projectsettings.md#class-projectsettings-property-rendering-rendering-device-driver) is set to `"d3d12"`.

---

[String](class_string.md#class-string) **application/file_description**

File description to be presented to users. Required. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **application/file_version**

Version number of the file. Falls back to [ProjectSettings.application/config/version](class_projectsettings.md#class-projectsettings-property-application-config-version) if left empty. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **application/icon**

Application icon file. If left empty, it will fallback to [ProjectSettings.application/config/windows_native_icon](class_projectsettings.md#class-projectsettings-property-application-config-windows-native-icon), and then to [ProjectSettings.application/config/icon](class_projectsettings.md#class-projectsettings-property-application-config-icon).

---

[int](class_int.md#class-int) **application/icon_interpolation**

Interpolation method used to resize application icon.

---

[bool](class_bool.md#class-bool) **application/modify_resources**

If enabled, icon and metadata of the exported executable is set according to the other `application/*` values.

---

[String](class_string.md#class-string) **application/product_name**

Name of the application. Required. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **application/product_version**

Application version visible to the user. Falls back to [ProjectSettings.application/config/version](class_projectsettings.md#class-projectsettings-property-application-config-version) if left empty. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **application/trademarks**

Trademarks and registered trademarks that apply to the file. Optional. See [StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

---

[String](class_string.md#class-string) **binary_format/architecture**

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, and `arm64`.

---

[bool](class_bool.md#class-bool) **binary_format/embed_pck**

If `true`, project resources are embedded into the executable.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **codesign/custom_options**

Array of the additional command line arguments passed to the code signing tool. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[String](class_string.md#class-string) **codesign/description**

Description of the signed content. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

---

[int](class_int.md#class-int) **codesign/digest_algorithm**

Digest algorithm to use for creating signature. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

---

[bool](class_bool.md#class-bool) **codesign/enable**

If `true`, executable signing is enabled.

---

[String](class_string.md#class-string) **codesign/identity**

PKCS #12 certificate file used to sign executable or certificate SHA-1 hash (if codesign/identity_type is set to "Use certificate store"). See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY`.

---

[int](class_int.md#class-int) **codesign/identity_type**

Type of identity to use. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY_TYPE`.

---

[String](class_string.md#class-string) **codesign/password**

Password for the certificate file used to sign executable. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_PASSWORD`.

---

[bool](class_bool.md#class-bool) **codesign/timestamp**

If `true`, time-stamp is added to the signature. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

---

[String](class_string.md#class-string) **codesign/timestamp_server_url**

URL of the time stamp server. If left empty, the default server is used. See [Sign Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

---

[String](class_string.md#class-string) **custom_template/debug**

Path to the custom export template. If left empty, default template is used.

---

[String](class_string.md#class-string) **custom_template/release**

Path to the custom export template. If left empty, default template is used.

---

[int](class_int.md#class-int) **debug/export_console_wrapper**

If `true`, a console wrapper executable is exported alongside the main executable, which allows running the project with enabled console output.

---

[bool](class_bool.md#class-bool) **shader_baker/enabled**

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ and Mobile renderers.

**Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.

---

[String](class_string.md#class-string) **ssh_remote_deploy/cleanup_script**

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.
- `{archive_name}` - Name of the ZIP containing uploaded application.
- `{exe_name}` - Name of application executable.
- `{cmd_args}` - Array of the command line argument for the application.

---

[bool](class_bool.md#class-bool) **ssh_remote_deploy/enabled**

Enables remote deploy using SSH/SCP.

---

[String](class_string.md#class-string) **ssh_remote_deploy/extra_args_scp**

Array of the additional command line arguments passed to the SCP.

---

[String](class_string.md#class-string) **ssh_remote_deploy/extra_args_ssh**

Array of the additional command line arguments passed to the SSH.

---

[String](class_string.md#class-string) **ssh_remote_deploy/host**

Remote host SSH user name and address, in `user@address` format.

---

[String](class_string.md#class-string) **ssh_remote_deploy/port**

Remote host SSH port number.

---

[String](class_string.md#class-string) **ssh_remote_deploy/run_script**

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.
- `{archive_name}` - Name of the ZIP containing uploaded application.
- `{exe_name}` - Name of application executable.
- `{cmd_args}` - Array of the command line argument for the application.

---

[bool](class_bool.md#class-bool) **texture_format/etc2_astc**

If `true`, project textures are exported in the ETC2/ASTC format.

---

[bool](class_bool.md#class-bool) **texture_format/s3tc_bptc**

If `true`, project textures are exported in the S3TC/BPTC format.
