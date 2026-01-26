# Technique SVR2: Using .htaccess to ensure that the only way to access non-conforming content is from conforming content

## About this Technique

This technique is not referenced from any Understanding document.

This technique applies to content residing on a web server that supports .htaccess (typically Apache) where a conforming version of content is provided as an alternative to a non-conforming version.

## Description

The objective of this technique is to ensure that users can always access an accessible version of the content when non-conforming versions are also available. Whenever content is provided in a format that does not conform to WCAG, the site as a whole can still conform if alternate versions of the inaccessible content are provided. Conformance Requirement 4 requires that alternate versions can be derived from the nonconforming content or from its URI.

Since it is not always possible to provide an accessible link from within non-conforming content, this technique describes how authors can use Apache's Module "mod_access" to ensure that non-conforming content can only be accessed from URIs that serve as alternate versions to the non-conforming content or from pages that include links to both the non-conforming version and the alternative version.

## Examples

### Example 1: Using Apache's mod_redirect module to redirect requests

The following .htaccess file uses Apache's mod_redirect module to redirect requests for "inaccessible.html" to "accessible.html" unless the request comes from "accessible.html".

```apache
# If the request for inaccessible content comes from a file 
# called accessible.html, then set an environment variable that 
# allows the inaccessible version to be displayed.
SetEnvIf Referer .*(accessible.html)$ let_me_in
<FilesMatch ^(inaccessible.html)$>
  Order Deny,Allow
  Deny from all
  Allow from env=let_me_in
</FilesMatch>

# If the request comes from anyplace but accessible.html, then 
# redirect the error condition to a location where the accessible 
# version resides
ErrorDocument 403 /example_directory/accessible.html
```

### Example 2: Redirecting direct requests for files

This example assumes a directory structure where documents are available in multiple formats. One of the formats does not meet WCAG at the level claimed and uses the file extension "jna" (Just Not Accessible). All of these files are stored in a folder called "jna" with an .htaccess file which ensures that any direct request for a file with the .jna extension from pages where inaccessible versions are not already available is redirected to an index page that lists all of the available formats.

```apache
# If the request for inaccessible content comes from a file at 
# https://example.com/documents/index.html, then set an environment 
# variable that allows the inaccessible version to be displayed.
SetEnvIf Referer ^https://example.com/documents/index.html$ let_me_in
<FilesMatch ^(.*\.jna)$>
  Order Deny,Allow
  Deny from all
  Allow from env=let_me_in
</FilesMatch>

# If the request comes from anyplace but https://example.com/documents/index.html, then 
# redirect the error condition to a location where a link the accessible 
# version resides
ErrorDocument 403 https://example.com/documents/index.html
```

## Related Resources

No endorsement implied.

* [Apache Module mod_env](https://httpd.apache.org/docs/2.4/mod/mod_env.html)
* [Authentication, Authorization and Access Control](https://httpd.apache.org/docs/2.4/howto/auth.html)
* [Apache Tutorial: .htaccess files](https://httpd.apache.org/docs/2.4/howto/htaccess.html)

## Related Techniques

* [G136: Providing a link at the beginning of a nonconforming web page that points to a conforming alternate version](../general/G136)
* [G190: Providing a link adjacent to or associated with a non-conforming object that links to a conforming alternate version](../general/G190)
* [SVR3: Using HTTP referer to ensure that the only way to access non-conforming content is from conforming content](../server-side-script/SVR3)
* [SVR4: Allowing users to provide preferences for the display of conforming alternate versions](../server-side-script/SVR4)
* [C29: Using a style switcher to provide a conforming alternate version](../css/C29)

## Tests

### Procedure

1. Identify pages that do not conform to WCAG at the conformance Level claimed where accessible alternatives are served based on the use of .htaccess files.
2. Visit the URI of the non-conforming content.
3. Verify that the resulting page is one of the following:

### Expected Results

* Check #3.1 or #3.2 is true.
