# EditorExportPlatformVisionOS

**Inherits:** [EditorExportPlatformAppleEmbedded](class_editorexportplatformappleembedded.md#class-editorexportplatformappleembedded) **<** [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Exporter for visionOS.

## Tutorials

- [Exporting for iOS](../tutorials/export/exporting_for_ios.md)
- [iOS plugins documentation index](../tutorials/platform/ios/index.md)

## Properties

| [String](class_string.md#class-string)                                  | application/additional_plist_content                                                             |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | application/app_store_team_id                                                                           |
| [String](class_string.md#class-string)                                  | application/bundle_identifier                                                                           |
| [String](class_string.md#class-string)                                  | application/code_sign_identity_debug                                                             |
| [String](class_string.md#class-string)                                  | application/code_sign_identity_release                                                         |
| [bool](class_bool.md#class-bool)                                        | application/delete_old_export_files_unconditionally                               |
| [int](class_int.md#class-int)                                           | application/export_method_debug                                                                       |
| [int](class_int.md#class-int)                                           | application/export_method_release                                                                   |
| [bool](class_bool.md#class-bool)                                        | application/export_project_only                                                                       |
| [int](class_int.md#class-int)                                           | application/icon_interpolation                                                                         |
| [String](class_string.md#class-string)                                  | application/min_visionos_version                                                                     |
| [String](class_string.md#class-string)                                  | application/provisioning_profile_specifier_debug                                     |
| [String](class_string.md#class-string)                                  | application/provisioning_profile_specifier_release                                 |
| [String](class_string.md#class-string)                                  | application/provisioning_profile_uuid_debug                                               |
| [String](class_string.md#class-string)                                  | application/provisioning_profile_uuid_release                                           |
| [String](class_string.md#class-string)                                  | application/short_version                                                                                   |
| [String](class_string.md#class-string)                                  | application/signature                                                                                           |
| [String](class_string.md#class-string)                                  | application/version                                                                                               |
| [bool](class_bool.md#class-bool)                                        | architectures/arm64                                                                                               |
| [bool](class_bool.md#class-bool)                                        | capabilities/access_wifi                                                                                     |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | capabilities/additional                                                                                       |
| [bool](class_bool.md#class-bool)                                        | capabilities/performance_a12                                                                             |
| [bool](class_bool.md#class-bool)                                        | capabilities/performance_gaming_tier                                                             |
| [String](class_string.md#class-string)                                  | custom_template/debug                                                                                           |
| [String](class_string.md#class-string)                                  | custom_template/release                                                                                       |
| [String](class_string.md#class-string)                                  | entitlements/additional                                                                                       |
| [bool](class_bool.md#class-bool)                                        | entitlements/game_center                                                                                     |
| [bool](class_bool.md#class-bool)                                        | entitlements/increased_memory_limit                                                               |
| [String](class_string.md#class-string)                                  | entitlements/push_notifications                                                                       |
| [String](class_string.md#class-string)                                  | icons/icon_1024x1024                                                                                             |
| [String](class_string.md#class-string)                                  | icons/icon_1024x1024_dark                                                                                   |
| [String](class_string.md#class-string)                                  | icons/icon_1024x1024_tinted                                                                               |
| [bool](class_bool.md#class-bool)                                        | modules/camera                                                                                                         |
| [int](class_int.md#class-int)                                           | privacy/active_keyboard_access_reasons                                                         |
| [String](class_string.md#class-string)                                  | privacy/camera_usage_description                                                                     |
| [Dictionary](class_dictionary.md#class-dictionary)                      | privacy/camera_usage_description_localized                                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/advertising_data/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/advertising_data/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/advertising_data/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/advertising_data/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/audio_data/collected                                               |
| [int](class_int.md#class-int)                                           | privacy/collected_data/audio_data/collection_purposes                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/audio_data/linked_to_user                                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/audio_data/used_for_tracking                               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/browsing_history/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/browsing_history/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/browsing_history/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/browsing_history/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/coarse_location/collected                                     |
| [int](class_int.md#class-int)                                           | privacy/collected_data/coarse_location/collection_purposes                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/coarse_location/linked_to_user                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/coarse_location/used_for_tracking                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/contacts/collected                                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/contacts/collection_purposes                               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/contacts/linked_to_user                                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/contacts/used_for_tracking                                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/crash_data/collected                                               |
| [int](class_int.md#class-int)                                           | privacy/collected_data/crash_data/collection_purposes                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/crash_data/linked_to_user                                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/crash_data/used_for_tracking                               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/credit_info/collected                                             |
| [int](class_int.md#class-int)                                           | privacy/collected_data/credit_info/collection_purposes                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/credit_info/linked_to_user                                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/credit_info/used_for_tracking                             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/customer_support/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/customer_support/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/customer_support/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/customer_support/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/device_id/collected                                                 |
| [int](class_int.md#class-int)                                           | privacy/collected_data/device_id/collection_purposes                             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/device_id/linked_to_user                                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/device_id/used_for_tracking                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/email_address/collected                                         |
| [int](class_int.md#class-int)                                           | privacy/collected_data/email_address/collection_purposes                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/email_address/linked_to_user                               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/email_address/used_for_tracking                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/emails_or_text_messages/collected                     |
| [int](class_int.md#class-int)                                           | privacy/collected_data/emails_or_text_messages/collection_purposes |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/emails_or_text_messages/linked_to_user           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/emails_or_text_messages/used_for_tracking     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/environment_scanning/collected                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/environment_scanning/collection_purposes       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/environment_scanning/linked_to_user                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/environment_scanning/used_for_tracking           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/fitness/collected                                                     |
| [int](class_int.md#class-int)                                           | privacy/collected_data/fitness/collection_purposes                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/fitness/linked_to_user                                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/fitness/used_for_tracking                                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/gameplay_content/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/gameplay_content/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/gameplay_content/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/gameplay_content/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/hands/collected                                                         |
| [int](class_int.md#class-int)                                           | privacy/collected_data/hands/collection_purposes                                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/hands/linked_to_user                                               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/hands/used_for_tracking                                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/head/collected                                                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/head/collection_purposes                                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/head/linked_to_user                                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/head/used_for_tracking                                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/health/collected                                                       |
| [int](class_int.md#class-int)                                           | privacy/collected_data/health/collection_purposes                                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/health/linked_to_user                                             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/health/used_for_tracking                                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/name/collected                                                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/name/collection_purposes                                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/name/linked_to_user                                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/name/used_for_tracking                                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_contact_info/collected                               |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_contact_info/collection_purposes           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_contact_info/linked_to_user                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_contact_info/used_for_tracking               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_data_types/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_data_types/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_data_types/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_data_types/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_diagnostic_data/collected                         |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_diagnostic_data/collection_purposes     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_diagnostic_data/linked_to_user               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_diagnostic_data/used_for_tracking         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_financial_info/collected                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_financial_info/collection_purposes       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_financial_info/linked_to_user                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_financial_info/used_for_tracking           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_usage_data/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_usage_data/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_usage_data/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_usage_data/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_user_content/collected                               |
| [int](class_int.md#class-int)                                           | privacy/collected_data/other_user_content/collection_purposes           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_user_content/linked_to_user                     |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/other_user_content/used_for_tracking               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/payment_info/collected                                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/payment_info/collection_purposes                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/payment_info/linked_to_user                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/payment_info/used_for_tracking                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/performance_data/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/performance_data/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/performance_data/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/performance_data/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/phone_number/collected                                           |
| [int](class_int.md#class-int)                                           | privacy/collected_data/phone_number/collection_purposes                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/phone_number/linked_to_user                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/phone_number/used_for_tracking                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/photos_or_videos/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/photos_or_videos/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/photos_or_videos/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/photos_or_videos/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/physical_address/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/physical_address/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/physical_address/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/physical_address/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/precise_location/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/precise_location/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/precise_location/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/precise_location/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/product_interaction/collected                             |
| [int](class_int.md#class-int)                                           | privacy/collected_data/product_interaction/collection_purposes         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/product_interaction/linked_to_user                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/product_interaction/used_for_tracking             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/purchase_history/collected                                   |
| [int](class_int.md#class-int)                                           | privacy/collected_data/purchase_history/collection_purposes               |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/purchase_history/linked_to_user                         |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/purchase_history/used_for_tracking                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/search_history/collected                                       |
| [int](class_int.md#class-int)                                           | privacy/collected_data/search_history/collection_purposes                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/search_history/linked_to_user                             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/search_history/used_for_tracking                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/sensitive_info/collected                                       |
| [int](class_int.md#class-int)                                           | privacy/collected_data/sensitive_info/collection_purposes                   |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/sensitive_info/linked_to_user                             |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/sensitive_info/used_for_tracking                       |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/user_id/collected                                                     |
| [int](class_int.md#class-int)                                           | privacy/collected_data/user_id/collection_purposes                                 |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/user_id/linked_to_user                                           |
| [bool](class_bool.md#class-bool)                                        | privacy/collected_data/user_id/used_for_tracking                                     |
| [int](class_int.md#class-int)                                           | privacy/disk_space_access_reasons                                                                   |
| [int](class_int.md#class-int)                                           | privacy/file_timestamp_access_reasons                                                           |
| [String](class_string.md#class-string)                                  | privacy/microphone_usage_description                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                      | privacy/microphone_usage_description_localized                                         |
| [String](class_string.md#class-string)                                  | privacy/photolibrary_usage_description                                                         |
| [Dictionary](class_dictionary.md#class-dictionary)                      | privacy/photolibrary_usage_description_localized                                     |
| [int](class_int.md#class-int)                                           | privacy/system_boot_time_access_reasons                                                       |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | privacy/tracking_domains                                                                                     |
| [bool](class_bool.md#class-bool)                                        | privacy/tracking_enabled                                                                                     |
| [int](class_int.md#class-int)                                           | privacy/user_defaults_access_reasons                                                             |
| [bool](class_bool.md#class-bool)                                        | shader_baker/enabled                                                                                             |
| [bool](class_bool.md#class-bool)                                        | user_data/accessible_from_files_app                                                               |
| [bool](class_bool.md#class-bool)                                        | user_data/accessible_from_itunes_sharing                                                     |

---

## Property Descriptions

[String](class_string.md#class-string) **application/additional_plist_content**

Additional data added to the root `<dict>` section of the [Info.plist](https://developer.apple.com/documentation/bundleresources/information_property_list) file. The value should be an XML section with pairs of key-value elements, e.g.:

```text
<key>key_name</key>
<string>value</string>
```

---

[String](class_string.md#class-string) **application/app_store_team_id**

Apple Team ID, unique 10-character string. To locate your Team ID check "Membership details" section in your Apple developer account dashboard, or "Organizational Unit" of your code signing certificate. See [Locate your Team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

---

[String](class_string.md#class-string) **application/bundle_identifier**

Unique application identifier in a reverse-DNS format, can only contain alphanumeric characters (`A-Z`, `a-z`, and `0-9`), hyphens (`-`), and periods (`.`).

---

[String](class_string.md#class-string) **application/code_sign_identity_debug**

The "Full Name", "Common Name" or SHA-1 hash of the signing identity used for debug export.

---

[String](class_string.md#class-string) **application/code_sign_identity_release**

The "Full Name", "Common Name" or SHA-1 hash of the signing identity used for release export.

---

[bool](class_bool.md#class-bool) **application/delete_old_export_files_unconditionally**

If `true`, existing "project name" and "project name.xcodeproj" in the export destination directory will be unconditionally deleted during export.

---

[int](class_int.md#class-int) **application/export_method_debug**

Application distribution target (debug export).

---

[int](class_int.md#class-int) **application/export_method_release**

Application distribution target (release export).

---

[bool](class_bool.md#class-bool) **application/export_project_only**

If `true`, exports iOS project files without building an XCArchive or `.ipa` file. If `false`, exports iOS project files and builds an XCArchive and `.ipa` file at the same time. When combining Godot with Fastlane or other build pipelines, you may want to set this to `true`.

---

[int](class_int.md#class-int) **application/icon_interpolation**

Interpolation method used to resize application icon.

---

[String](class_string.md#class-string) **application/min_visionos_version**

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **application/provisioning_profile_specifier_debug**

Name of the provisioning profile. Sets XCode PROVISIONING_PROFILE_SPECIFIER for debug. [Used for manual provisioning](https://developer.apple.com/documentation/xcode/build-settings-reference#Provisioning-Profile).

Can be overridden with the environment variable `GODOT_APPLE_PLATFORM_PROFILE_SPECIFIER_DEBUG`.

---

[String](class_string.md#class-string) **application/provisioning_profile_specifier_release**

Name of the provisioning profile. Sets XCode PROVISIONING_PROFILE_SPECIFIER for release. [Used for manual provisioning](https://developer.apple.com/documentation/xcode/build-settings-reference#Provisioning-Profile).

Can be overridden with the environment variable `GODOT_APPLE_PLATFORM_PROFILE_SPECIFIER_RELEASE`.

---

[String](class_string.md#class-string) **application/provisioning_profile_uuid_debug**

UUID of the provisioning profile. If left empty, Xcode will download or create a provisioning profile automatically. See [Edit, download, or delete provisioning profiles](https://developer.apple.com/help/account/manage-profiles/edit-download-or-delete-profiles).

Can be overridden with the environment variable `GODOT_APPLE_PLATFORM_PROVISIONING_PROFILE_UUID_DEBUG`.

---

[String](class_string.md#class-string) **application/provisioning_profile_uuid_release**

UUID of the provisioning profile. If left empty, Xcode will download or create a provisioning profile automatically. See [Edit, download, or delete provisioning profiles](https://developer.apple.com/help/account/manage-profiles/edit-download-or-delete-profiles).

Can be overridden with the environment variable `GODOT_APPLE_PLATFORM_PROVISIONING_PROFILE_UUID_RELEASE`.

---

[String](class_string.md#class-string) **application/short_version**

Application version visible to the user. Can only contain numeric characters (`0-9`) and periods (`.`). Falls back to [ProjectSettings.application/config/version](class_projectsettings.md#class-projectsettings-property-application-config-version) if left empty.

**Note:** This value is used for the *Identity > Version* value in the generated Xcode project.

---

[String](class_string.md#class-string) **application/signature**

A four-character creator code that is specific to the bundle. Optional.

---

[String](class_string.md#class-string) **application/version**

Machine-readable application version in the `major.minor.patch` format. Can only contain numeric characters (`0-9`) and periods (`.`). This must be incremented with every new release pushed to the App Store. Falls back to [ProjectSettings.application/config/version](class_projectsettings.md#class-projectsettings-property-application-config-version) if left empty.

**Note:** This value is used for the *Identity > Build* value in the generated Xcode project.

---

[bool](class_bool.md#class-bool) **architectures/arm64**

If `true`, `arm64` binaries are included into exported project.

---

[bool](class_bool.md#class-bool) **capabilities/access_wifi**

If `true`, networking features related to Wi-Fi access are enabled. See [Required Device Capabilities](https://developer.apple.com/support/required-device-capabilities/).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **capabilities/additional**

Additional data added to the `UIRequiredDeviceCapabilities` array of the `Info.plist` file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[bool](class_bool.md#class-bool) **capabilities/performance_a12**

Requires the graphics performance and features of the A12 Bionic and later chips (devices supporting all Vulkan renderer features).

Enabling this option limits supported devices to: iPhone XS, iPhone XR, iPad Mini (5th gen.), iPad Air (3rd gen.), iPad (8th gen) and newer.

---

[bool](class_bool.md#class-bool) **capabilities/performance_gaming_tier**

Requires the graphics performance and features of the A17 Pro and later chips.

Enabling this option limits supported devices to: iPhone 15 Pro and newer.

---

[String](class_string.md#class-string) **custom_template/debug**

Path to the custom export template. If left empty, default template is used.

---

[String](class_string.md#class-string) **custom_template/release**

Path to the custom export template. If left empty, default template is used.

---

[String](class_string.md#class-string) **entitlements/additional**

Additional data added to the root `<dict>` section of the [.entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) file. The value should be an XML section with pairs of key-value elements, for example:

```text
<key>key_name</key>
<string>value</string>
```

---

[bool](class_bool.md#class-bool) **entitlements/game_center**

If `true`, allows access to Game Center features. See [com.apple.developer.game-center](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_game-center).

---

[bool](class_bool.md#class-bool) **entitlements/increased_memory_limit**

If `true`, hints that the app might perform better with a higher memory limit. See [com.apple.developer.kernel.increased-memory-limit](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_kernel_increased-memory-limit).

---

[String](class_string.md#class-string) **entitlements/push_notifications**

Environment for Apple Push Notification service. See [aps-environment](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment).

---

[String](class_string.md#class-string) **icons/icon_1024x1024**

Base application icon used to generate other icons. If left empty, it will fallback to [ProjectSettings.application/config/icon](class_projectsettings.md#class-projectsettings-property-application-config-icon). See [App icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

---

[String](class_string.md#class-string) **icons/icon_1024x1024_dark**

Base application icon used to generate other icons, dark version. See [App icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

---

[String](class_string.md#class-string) **icons/icon_1024x1024_tinted**

Base application icon used to generate other icons, tinted version. See [App icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

---

[bool](class_bool.md#class-bool) **modules/camera**

If `true`, [CameraServer](class_cameraserver.md#class-cameraserver) module is added to the exported project.

---

[int](class_int.md#class-int) **privacy/active_keyboard_access_reasons**

The reasons your app use active keyboard API. See [Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

---

[String](class_string.md#class-string) **privacy/camera_usage_description**

A message displayed when requesting access to the device's camera (in English).

---

[Dictionary](class_dictionary.md#class-dictionary) **privacy/camera_usage_description_localized**

A message displayed when requesting access to the device's camera (localized).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/advertising_data/collected**

Indicates whether your app collects advertising data.

---

[int](class_int.md#class-int) **privacy/collected_data/advertising_data/collection_purposes**

The reasons your app collects advertising data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/advertising_data/linked_to_user**

Indicates whether your app links advertising data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/advertising_data/used_for_tracking**

Indicates whether your app uses advertising data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/audio_data/collected**

Indicates whether your app collects audio data.

---

[int](class_int.md#class-int) **privacy/collected_data/audio_data/collection_purposes**

The reasons your app collects audio data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/audio_data/linked_to_user**

Indicates whether your app links audio data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/audio_data/used_for_tracking**

Indicates whether your app uses audio data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/browsing_history/collected**

Indicates whether your app collects browsing history.

---

[int](class_int.md#class-int) **privacy/collected_data/browsing_history/collection_purposes**

The reasons your app collects browsing history. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/browsing_history/linked_to_user**

Indicates whether your app links browsing history to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/browsing_history/used_for_tracking**

Indicates whether your app uses browsing history for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/coarse_location/collected**

Indicates whether your app collects coarse location data.

---

[int](class_int.md#class-int) **privacy/collected_data/coarse_location/collection_purposes**

The reasons your app collects coarse location data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/coarse_location/linked_to_user**

Indicates whether your app links coarse location data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/coarse_location/used_for_tracking**

Indicates whether your app uses coarse location data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/contacts/collected**

Indicates whether your app collects contacts.

---

[int](class_int.md#class-int) **privacy/collected_data/contacts/collection_purposes**

The reasons your app collects contacts. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/contacts/linked_to_user**

Indicates whether your app links contacts to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/contacts/used_for_tracking**

Indicates whether your app uses contacts for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/crash_data/collected**

Indicates whether your app collects crash data.

---

[int](class_int.md#class-int) **privacy/collected_data/crash_data/collection_purposes**

The reasons your app collects crash data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/crash_data/linked_to_user**

Indicates whether your app links crash data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/crash_data/used_for_tracking**

Indicates whether your app uses crash data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/credit_info/collected**

Indicates whether your app collects credit information.

---

[int](class_int.md#class-int) **privacy/collected_data/credit_info/collection_purposes**

The reasons your app collects credit information. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/credit_info/linked_to_user**

Indicates whether your app links credit information to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/credit_info/used_for_tracking**

Indicates whether your app uses credit information for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/customer_support/collected**

Indicates whether your app collects customer support data.

---

[int](class_int.md#class-int) **privacy/collected_data/customer_support/collection_purposes**

The reasons your app collects customer support data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/customer_support/linked_to_user**

Indicates whether your app links customer support data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/customer_support/used_for_tracking**

Indicates whether your app uses customer support data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/device_id/collected**

Indicates whether your app collects device IDs.

---

[int](class_int.md#class-int) **privacy/collected_data/device_id/collection_purposes**

The reasons your app collects device IDs. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/device_id/linked_to_user**

Indicates whether your app links device IDs to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/device_id/used_for_tracking**

Indicates whether your app uses device IDs for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/email_address/collected**

Indicates whether your app collects email address.

---

[int](class_int.md#class-int) **privacy/collected_data/email_address/collection_purposes**

The reasons your app collects email address. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/email_address/linked_to_user**

Indicates whether your app links email address to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/email_address/used_for_tracking**

Indicates whether your app uses email address for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/emails_or_text_messages/collected**

Indicates whether your app collects emails or text messages.

---

[int](class_int.md#class-int) **privacy/collected_data/emails_or_text_messages/collection_purposes**

The reasons your app collects emails or text messages. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/emails_or_text_messages/linked_to_user**

Indicates whether your app links emails or text messages to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/emails_or_text_messages/used_for_tracking**

Indicates whether your app uses emails or text messages for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/environment_scanning/collected**

Indicates whether your app collects environment scanning data.

---

[int](class_int.md#class-int) **privacy/collected_data/environment_scanning/collection_purposes**

The reasons your app collects environment scanning data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/environment_scanning/linked_to_user**

Indicates whether your app links environment scanning data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/environment_scanning/used_for_tracking**

Indicates whether your app uses environment scanning data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/fitness/collected**

Indicates whether your app collects fitness and exercise data.

---

[int](class_int.md#class-int) **privacy/collected_data/fitness/collection_purposes**

The reasons your app collects fitness and exercise data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/fitness/linked_to_user**

Indicates whether your app links fitness and exercise data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/fitness/used_for_tracking**

Indicates whether your app uses fitness and exercise data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/gameplay_content/collected**

Indicates whether your app collects gameplay content.

---

[int](class_int.md#class-int) **privacy/collected_data/gameplay_content/collection_purposes**

The reasons your app collects gameplay content. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/gameplay_content/linked_to_user**

Indicates whether your app links gameplay content to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/gameplay_content/used_for_tracking**

Indicates whether your app uses gameplay content for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/hands/collected**

Indicates whether your app collects user's hand structure and hand movements.

---

[int](class_int.md#class-int) **privacy/collected_data/hands/collection_purposes**

The reasons your app collects user's hand structure and hand movements. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/hands/linked_to_user**

Indicates whether your app links user's hand structure and hand movements to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/hands/used_for_tracking**

Indicates whether your app uses user's hand structure and hand movements for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/head/collected**

Indicates whether your app collects user's head movement.

---

[int](class_int.md#class-int) **privacy/collected_data/head/collection_purposes**

The reasons your app collects user's head movement. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/head/linked_to_user**

Indicates whether your app links user's head movement to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/head/used_for_tracking**

Indicates whether your app uses user's head movement for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/health/collected**

Indicates whether your app collects health and medical data.

---

[int](class_int.md#class-int) **privacy/collected_data/health/collection_purposes**

The reasons your app collects health and medical data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/health/linked_to_user**

Indicates whether your app links health and medical data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/health/used_for_tracking**

Indicates whether your app uses health and medical data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/name/collected**

Indicates whether your app collects user's name.

---

[int](class_int.md#class-int) **privacy/collected_data/name/collection_purposes**

The reasons your app collects user's name. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/name/linked_to_user**

Indicates whether your app links user's name to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/name/used_for_tracking**

Indicates whether your app uses user's name for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_contact_info/collected**

Indicates whether your app collects any other contact information.

---

[int](class_int.md#class-int) **privacy/collected_data/other_contact_info/collection_purposes**

The reasons your app collects any other contact information. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_contact_info/linked_to_user**

Indicates whether your app links any other contact information to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_contact_info/used_for_tracking**

Indicates whether your app uses any other contact information for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_data_types/collected**

Indicates whether your app collects any other data.

---

[int](class_int.md#class-int) **privacy/collected_data/other_data_types/collection_purposes**

The reasons your app collects any other data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_data_types/linked_to_user**

Indicates whether your app links any other data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_data_types/used_for_tracking**

Indicates whether your app uses any other data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_diagnostic_data/collected**

Indicates whether your app collects any other diagnostic data.

---

[int](class_int.md#class-int) **privacy/collected_data/other_diagnostic_data/collection_purposes**

The reasons your app collects any other diagnostic data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_diagnostic_data/linked_to_user**

Indicates whether your app links any other diagnostic data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_diagnostic_data/used_for_tracking**

Indicates whether your app uses any other diagnostic data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_financial_info/collected**

Indicates whether your app collects any other financial information.

---

[int](class_int.md#class-int) **privacy/collected_data/other_financial_info/collection_purposes**

The reasons your app collects any other financial information. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_financial_info/linked_to_user**

Indicates whether your app links any other financial information to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_financial_info/used_for_tracking**

Indicates whether your app uses any other financial information for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_usage_data/collected**

Indicates whether your app collects any other usage data.

---

[int](class_int.md#class-int) **privacy/collected_data/other_usage_data/collection_purposes**

The reasons your app collects any other usage data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_usage_data/linked_to_user**

Indicates whether your app links any other usage data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_usage_data/used_for_tracking**

Indicates whether your app uses any other usage data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_user_content/collected**

Indicates whether your app collects any other user generated content.

---

[int](class_int.md#class-int) **privacy/collected_data/other_user_content/collection_purposes**

The reasons your app collects any other user generated content. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_user_content/linked_to_user**

Indicates whether your app links any other user generated content to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/other_user_content/used_for_tracking**

Indicates whether your app uses any other user generated content for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/payment_info/collected**

Indicates whether your app collects payment information.

---

[int](class_int.md#class-int) **privacy/collected_data/payment_info/collection_purposes**

The reasons your app collects payment information. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/payment_info/linked_to_user**

Indicates whether your app links payment information to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/payment_info/used_for_tracking**

Indicates whether your app uses payment information for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/performance_data/collected**

Indicates whether your app collects performance data.

---

[int](class_int.md#class-int) **privacy/collected_data/performance_data/collection_purposes**

The reasons your app collects performance data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/performance_data/linked_to_user**

Indicates whether your app links performance data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/performance_data/used_for_tracking**

Indicates whether your app uses performance data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/phone_number/collected**

Indicates whether your app collects phone number.

---

[int](class_int.md#class-int) **privacy/collected_data/phone_number/collection_purposes**

The reasons your app collects phone number. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/phone_number/linked_to_user**

Indicates whether your app links phone number to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/phone_number/used_for_tracking**

Indicates whether your app uses phone number for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/photos_or_videos/collected**

Indicates whether your app collects photos or videos.

---

[int](class_int.md#class-int) **privacy/collected_data/photos_or_videos/collection_purposes**

The reasons your app collects photos or videos. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/photos_or_videos/linked_to_user**

Indicates whether your app links photos or videos to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/photos_or_videos/used_for_tracking**

Indicates whether your app uses photos or videos for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/physical_address/collected**

Indicates whether your app collects physical address.

---

[int](class_int.md#class-int) **privacy/collected_data/physical_address/collection_purposes**

The reasons your app collects physical address. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/physical_address/linked_to_user**

Indicates whether your app links physical address to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/physical_address/used_for_tracking**

Indicates whether your app uses physical address for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/precise_location/collected**

Indicates whether your app collects precise location data.

---

[int](class_int.md#class-int) **privacy/collected_data/precise_location/collection_purposes**

The reasons your app collects precise location data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/precise_location/linked_to_user**

Indicates whether your app links precise location data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/precise_location/used_for_tracking**

Indicates whether your app uses precise location data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/product_interaction/collected**

Indicates whether your app collects product interaction data.

---

[int](class_int.md#class-int) **privacy/collected_data/product_interaction/collection_purposes**

The reasons your app collects product interaction data. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/product_interaction/linked_to_user**

Indicates whether your app links product interaction data to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/product_interaction/used_for_tracking**

Indicates whether your app uses product interaction data for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/purchase_history/collected**

Indicates whether your app collects purchase history.

---

[int](class_int.md#class-int) **privacy/collected_data/purchase_history/collection_purposes**

The reasons your app collects purchase history. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/purchase_history/linked_to_user**

Indicates whether your app links purchase history to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/purchase_history/used_for_tracking**

Indicates whether your app uses purchase history for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/search_history/collected**

Indicates whether your app collects search history.

---

[int](class_int.md#class-int) **privacy/collected_data/search_history/collection_purposes**

The reasons your app collects search history. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/search_history/linked_to_user**

Indicates whether your app links search history to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/search_history/used_for_tracking**

Indicates whether your app uses search history for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/sensitive_info/collected**

Indicates whether your app collects sensitive user information.

---

[int](class_int.md#class-int) **privacy/collected_data/sensitive_info/collection_purposes**

The reasons your app collects sensitive user information. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/sensitive_info/linked_to_user**

Indicates whether your app links sensitive user information to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/sensitive_info/used_for_tracking**

Indicates whether your app uses sensitive user information for tracking.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/user_id/collected**

Indicates whether your app collects user IDs.

---

[int](class_int.md#class-int) **privacy/collected_data/user_id/collection_purposes**

The reasons your app collects user IDs. See [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

---

[bool](class_bool.md#class-bool) **privacy/collected_data/user_id/linked_to_user**

Indicates whether your app links user IDs to the user's identity.

---

[bool](class_bool.md#class-bool) **privacy/collected_data/user_id/used_for_tracking**

Indicates whether your app uses user IDs for tracking.

---

[int](class_int.md#class-int) **privacy/disk_space_access_reasons**

The reasons your app use free disk space API. See [Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

---

[int](class_int.md#class-int) **privacy/file_timestamp_access_reasons**

The reasons your app use file timestamp/metadata API. See [Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

---

[String](class_string.md#class-string) **privacy/microphone_usage_description**

A message displayed when requesting access to the device's microphone (in English).

---

[Dictionary](class_dictionary.md#class-dictionary) **privacy/microphone_usage_description_localized**

A message displayed when requesting access to the device's microphone (localized).

---

[String](class_string.md#class-string) **privacy/photolibrary_usage_description**

A message displayed when requesting access to the user's photo library (in English).

---

[Dictionary](class_dictionary.md#class-dictionary) **privacy/photolibrary_usage_description_localized**

A message displayed when requesting access to the user's photo library (localized).

---

[int](class_int.md#class-int) **privacy/system_boot_time_access_reasons**

The reasons your app use system boot time / absolute time API. See [Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **privacy/tracking_domains**

The list of internet domains your app connects to that engage in tracking. See [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[bool](class_bool.md#class-bool) **privacy/tracking_enabled**

Indicates whether your app uses data for tracking. See [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

---

[int](class_int.md#class-int) **privacy/user_defaults_access_reasons**

The reasons your app use user defaults API. See [Describing use of required reason API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

---

[bool](class_bool.md#class-bool) **shader_baker/enabled**

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ and Mobile renderers.

**Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.

---

[bool](class_bool.md#class-bool) **user_data/accessible_from_files_app**

If `true`, the app "Documents" folder can be accessed via "Files" app. See [LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/documentation/bundleresources/information_property_list/lssupportsopeningdocumentsinplace).

---

[bool](class_bool.md#class-bool) **user_data/accessible_from_itunes_sharing**

If `true`, the app "Documents" folder can be accessed via iTunes file sharing. See [UIFileSharingEnabled](https://developer.apple.com/documentation/bundleresources/information_property_list/uifilesharingenabled).
