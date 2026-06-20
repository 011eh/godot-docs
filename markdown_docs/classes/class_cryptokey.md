# CryptoKey

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A cryptographic key (RSA or elliptic-curve).

## Description

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other [Resource](class_resource.md#class-resource).

They can be used to generate a self-signed [X509Certificate](class_x509certificate.md#class-x509certificate) via [Crypto.generate_self_signed_certificate()](class_crypto.md#class-crypto-method-generate-self-signed-certificate) and as private key in [StreamPeerTLS.accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream) along with the appropriate certificate.

## Tutorials

- [SSL certificates](../tutorials/networking/ssl_certificates.md)

## Methods

| [bool](class_bool.md#class-bool)                      | is_public_only()                                                                                                              |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error) | load(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false)                               |
| [Error](class_@globalscope.md#enum-globalscope-error) | load_from_string(string_key: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false) |
| [Error](class_@globalscope.md#enum-globalscope-error) | save(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false)                               |
| [String](class_string.md#class-string)                | save_to_string(public_only: [bool](class_bool.md#class-bool) = false)                                                         |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_public_only**()

Returns `true` if this CryptoKey only has the public part, and not the private one.

---

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false)

Loads a key from `path`. If `public_only` is `true`, only the public key will be loaded.

**Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---

[Error](class_@globalscope.md#enum-globalscope-error) **load_from_string**(string_key: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false)

Loads a key from the given `string_key`. If `public_only` is `true`, only the public key will be loaded.

---

[Error](class_@globalscope.md#enum-globalscope-error) **save**(path: [String](class_string.md#class-string), public_only: [bool](class_bool.md#class-bool) = false)

Saves a key to the given `path`. If `public_only` is `true`, only the public key will be saved.

**Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.

---

[String](class_string.md#class-string) **save_to_string**(public_only: [bool](class_bool.md#class-bool) = false)

Returns a string containing the key in PEM format. If `public_only` is `true`, only the public key will be included.
