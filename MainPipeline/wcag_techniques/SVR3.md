# Technique SVR3: Using HTTP referer to ensure that the only way to access non-conforming content is from conforming content

## About this Technique

This technique is not referenced from any Understanding document.

This technique applies to content created using server-side scripting where a conforming version of content is provided as an alternative to a non-conforming version based on HTTP Referer.

## Description

The objective of this technique is to ensure that users can obtain an accessible version of content where both non-conforming and conforming versions are provided.

[Conformance Requirement 1](https://www.w3.org/WAI/WCAG22/Understanding/conformance#conf-req1) allows non-conforming pages to be included within the scope of conformance as long as they have a [conforming alternate version](https://www.w3.org/TR/WCAG22/#dfn-conforming-alternate-versions). It is not always possible for authors to include accessibility supported links to conforming content from within non-conforming content. Therefore, authors may need to rely on the use of Server Side Scripting technologies (ex. PHP, ASP, JSP) to ensure that the non-conforming version can only be reached from a conforming page.

This technique describes how to use information provided by the HTTP referer to ensure that non-conforming content can only be reached from a conforming page. The HTTP referer header is set by the user agent and contains the URI of the page (if any) which referred the user agent to the non-conforming page.

To implement this technique, an author identifies the URI for the conforming version of the content, for each non-conforming page. When a request for the non-conforming version of a page is received, the server compares the value of the HTTP referer header against the URI of the conforming version to determine whether the link to the non-conforming version came from the conforming version. The non-conforming version is only served if the HTTP referer matches the URI of the non-conforming version. Otherwise, the user is redirected to the conforming version of the content. Note that when comparing the URI in the HTTP referer header, non-relevant variations in the URI, such as in the query and target, should be taken into account.

## Examples

### Example 1: Interactive demonstrations of physical processes

An online physics course uses a proprietary modeling language to provide interactive demonstrations of physical processes. The user agent for the modeling language is not compatible with assistive technology. The site includes a script that uses the HTTP referer to ensure that unless users attempt to access the interactive demonstration from a page that contains a conforming description of the process and models, the server redirects the request to a conforming page which contains a link to the non-conforming version. Students may choose to access the non-conforming, interactive version, but those who do not are still able to learn about the process.

### Example 2: Using HTTP referer in PHP

The following example illustrates how this technique can be used in PHP. It includes two files, conforming.php and non-conforming.php which work together to ensure that the only way to access non-conforming content is from conforming content.

#### Conforming PHP

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Conforming Content</title>
</head>
<body>
  <h1>This is a conforming page</h1>
  <p>From here, you can visit the <a href="non-conforming.php">non-conforming 
    page</a>.</p>
</body>
</html>
```

#### Non-conforming PHP

```php-template
<?php 
// if the request comes from a file that contains the string "conforming.php" 
// then render the page
  if(stristr($_SERVER['HTTP_REFERER'], "conforming.php")) {
?>	
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Non-Conforming Content</title>
</head>
<body>
  <h1>This is a non-conforming page</h1>
  <p>Because you came from <?php echo $_SERVER['HTTP_REFERER']; ?>, 
   you are able to view the content on this page.</p>
</body>
</html>
<?php
 }
// if the referring page is not conforming.php, then redirect the user to 
// the conforming version
else  {
header("Location: conforming.php");
}
?>
```

A working example, [Conforming content](../../working-examples/server-referrer-access-nonconforming/non-conforming.php), is available.

## Related Techniques

* [G136: Providing a link at the beginning of a nonconforming web page that points to a conforming alternate version](../general/G136)
* [G190: Providing a link adjacent to or associated with a non-conforming object that links to a conforming alternate version](../general/G190)
* [SVR2: Using .htaccess to ensure that the only way to access non-conforming content is from conforming content](../server-side-script/SVR2)
* [SVR4: Allowing users to provide preferences for the display of conforming alternate versions](../server-side-script/SVR4)
* [C29: Using a style switcher to provide a conforming alternate version](../css/C29)

## Tests

### Procedure

Where WCAG-conforming alternatives are provided for non-conforming content:

1. Identify pages that do not conform to WCAG at the conformance Level claimed where accessible alternatives are served based on HTTP Referrer.
2. Visit the URI of the non-conforming content.
3. Verify that the resulting page is one of the following:

### Expected Results

* Check #3.1 or #3.2 is true.
