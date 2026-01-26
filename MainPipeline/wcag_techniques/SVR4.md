# Technique SVR4: Allowing users to provide preferences for the display of conforming alternate versions

## About this Technique

This technique is not referenced from any Understanding document.

This technique applies to content created using server-side scripting to store preferences.

## Description

The objective of this technique is to provide a mechanism for users to select a preference for an alternate conforming version of a web page.

Providing preferences to allow users to view conforming alternate versions can be accomplished in several ways. One common method is to provide a link which triggers a server-side process that sets a session or persistent cookie that the web server uses to modify the page or redirect the user to the alternate version. Other methods include providing user-specific choices that are stored as part of the user's login information for a system where users sign in to access a web page or service.

Users requiring an alternate version will need the mechanism provided in the non-conforming page to be accessible in order to find and use it. The mechanism itself should conform to the accessibility level being claimed.

## Examples

### Example 1: Setting a session or persistent cookie to store a user preference

A website offers a link to a "preferences" page on pages within the site. On this page, there is an option to view an alternate version of the site. There may be various aspects of the page that are affected, or the user may be opting to view an entirely alternate version of the site. The preference may be to display a version of the site where video included on the site displays captioning, or it may be offered because the primary site contains accessibility conformance issues that are addressed only via the alternative.

A web page author may choose to handle this preference via a cookie, which may be handled via a server-side scripting language such as PHP.

The preferences page may be offered as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Site Preferences</title>
</head>
<body>
  <h1>Site Preferences</h1>
  <form id="form1" name="site_prefs" method="post" action="pref.php">
    <fieldset>
      <legend>Which version of the site do you want to view?</legend>
      <input type="radio" name="site_pref" id="site_pref_reg" value="reg">
      <label for="site_pref_reg">Main version of site</label>
      <input type="radio" name="site_pref" id="site_pref_axx" value="axx">
      <label for="site_pref_axx">Accessibility-conforming version</label>
    </fieldset> 
  </form>
</body>
</html>
```

The form is submitted to the pref.php file for processing. A cookie is set, and in this simple example the user's browser is directed to the site home page.

#### pref.php

```php-template
<?php
if(isset($site_pref)) {
setcookie("site_pref",$site_pref, time() + (86400 * 30)); //set for 30 days
header("location: http://www.example.com"); //redirects to home page
}
?>
```

The home page starts with code that implements the user's preference.

#### index.php

```php-template
<?php
if(isset($site_pref)) {
  if($site_pref="axx") {
    header("location: ./accessible/index.php");
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  ...
```

For a login-based system, the preference is stored in the user's database record and referred to by the server-side script generating the pages for the user to view.

## Related Resources

No endorsement implied.

* [Setting and using cookies in PHP](https://php.net/setcookie)

## Related Techniques

* [G136: Providing a link at the beginning of a nonconforming web page that points to a conforming alternate version](../general/G136)
* [G190: Providing a link adjacent to or associated with a non-conforming object that links to a conforming alternate version](../general/G190)
* [SCR38: Creating a conforming alternate version for a web page designed with progressive enhancement](../client-side-script/SCR38)
* [SVR2: Using .htaccess to ensure that the only way to access non-conforming content is from conforming content](../server-side-script/SVR2)
* [SVR3: Using HTTP referer to ensure that the only way to access non-conforming content is from conforming content](../server-side-script/SVR3)
* [C29: Using a style switcher to provide a conforming alternate version](../css/C29)

## Tests

### Procedure

1. Change a preference for how pages on the site are displayed.
2. Check that the preference itself or a link to that page where it can be set can be reached from each non-conforming page.
3. Check that web pages are displayed according to the selected preference.
4. Check that when the preference(s) are set, the web page conforms as claimed.
5. Verify that the resulting page is a conforming alternate version for the original page.

### Expected Results

* Checks #2 and #3 are true.
