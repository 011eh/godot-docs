# X509Certificate

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An X509 certificate (e.g. for TLS).

## Description

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other [Resource](class_resource.md#class-resource).

They can be used as the server certificate in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream) (along with the proper [CryptoKey](class_cryptokey.md#class-cryptokey)), and to specify the only certificate that should be accepted when connecting to a TLS server via [StreamPeerTLS.connect_to_stream()](class_streampeertls.md#class-streampeertls-method-connect-to-stream).

## Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | load(path: [String](class_string.md#class-string))                           |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | load_from_string(string: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error)   | save(path: [String](class_string.md#class-string))                           |
| [String](class_string.md#class-string)                  | save_to_string()                                                   |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string))

Loads a certificate from `path` ("\*.crt" file).

---

[Error](class_@globalscope.md#enum-globalscope-error) **load_from_string**(string: [String](class_string.md#class-string))

Loads a certificate from the given `string`.

---

[Error](class_@globalscope.md#enum-globalscope-error) **save**(path: [String](class_string.md#class-string))

Saves a certificate to the given `path` (should be a "\*.crt" file).

---

[String](class_string.md#class-string) **save_to_string**()

Returns a string representation of the certificate, or an empty string if the certificate is invalid.
