# Technique SCR38: Creating a conforming alternate version for a web page designed with progressive enhancement

## About this Technique

This technique is not referenced from any Understanding document.

This technique applies to HTML with scripting.

## Description

This objective of this technique is to offer a conforming alternate version for a web page designed with progressive enhancement. The technique demonstrates how to use a scripting technique to accomplish this by:

1. Storing the initial pre-enhanced version of the web page so that it can act as a "conforming alternate version" for any later enhanced versions of the content; and
2. Inserting a mechanism into all enhanced versions of the web page which allows a user to revert the content back to the stored pre-enhanced Alternate Version.

Web pages designed with progressive enhancement detect features in the web-enabled accessing device (size, capability and software) to allow those supported web technologies to be applied in layers on top of an HTML foundation. The basic content and functionality of such a web page are available through the HTML foundation to anyone using a more simple web-enabled accessing device, whilst enhanced versions of the page are created to suit the different features in more advanced accessing devices.

The current guidance for web pages delivered in alternate versions reads: "Note 4: Alternate versions may be provided to accommodate different technology environments or user groups. Each version should be as conformant as possible. One version would need to be fully conformant in order to meet conformance requirement 1." With regard to web pages designed with progressive enhancement this leaves the problem of which version to select as the one fully conformant version - all whilst trying to ensure that no set of users is disadvantaged by that choice.

One solution to this challenge is to select the pre-enhanced version of the web page (e.g. the DOM state created solely from the HTML in the source code in the absence of support for scripts, styles or non-HTML plugins) as the "fully conformant version", due to its broad reach, with regard to support, across all the possible web-enabled devices accessing the content.

Note

This technique removes all scripts, styles, and plugins, but it is important to state that this is not required for conformance with WCAG 2.x. An author could use a similar technique, but retain a reduced set of styles and scripts in the "pre-enhanced" version.

While this technique offers a way to base conformance claims on a single version, authors should continue to work to ensure that each enhanced version of the web page is as conformant as possible.

## Examples

### Example 1: Using JavaScript

The example uses JavaScript in the "accToggle.js" file to store the initial pre-enhanced version of the web page, created solely from the HTML in the source code, so that it can act as a "conforming alternate version" for any later enhanced versions of the web page; and inserts a toggle link into all enhanced versions of the web page which allows a user to revert the web page back to the stored pre-enhanced "Conforming Alternate Version". Note: The "sayhello.js" file is simply there as an example payload external file, and is to be replaced by any other external scripts which are desired.

The script in the acctoggle.js file stores the pre-enhanced version - assigning the version the url postfix #accessible. Clicking the "WCAG 2 conforming alternate version" link (inserted as the first child of the body element in any enhanced versions) changes the url to include the postfix "#accessible" which then resets the html located in the body element and the head element to pre-enhanced code. The pre-enhanced state can be reached from the link, or directly from a url typed into the browser. In addition, a link is inserted into the pre-enhanced "Conforming Alternate Version" which allows the user to re-enhance the web page (something which can also be done using the web browser's back button).

#### acctoggle.js JavaScript:

```javascript
window.onload = function(event) {

// store pre-enhanced element content
var initialHead = document.head.innerHTML;
var initialBody = document.body.innerHTML;
var initialURL = location.href;
				
var runOnce = function() {
  // payload you want to run per page call - e.g. analytics code
}

var setup = function() {
  // create conforming alternate version link

  var toggleEnhanced = document.querySelector("#toggle_enhanced");
  if (toggleEnhanced) {
    toggleEnhanced.outerHTML = "";
  }

  var nel = document.createElement("a");
  nel.id = "acctoggle";
  nel.setAttribute("href", "#accessible");
  nel.innerHTML = "WCAG 2 conforming alternate version";
  document.body.insertBefore(nel, document.body.firstChild);

  // payload
  var s = document.createElement("SCRIPT");
  s.setAttribute("src", "sayhello.js");
  document.querySelector("HEAD").appendChild(s);   
}
					
setup();
runOnce();

window.onpopstate = function(event) {
  if (location.href.indexOf("#accessible") != -1) {
  
  // revert element contents to pre-enhanced version
  document.head.innerHTML = initialHead;
  document.body.innerHTML = initialBody;

  // create enhanced version link
  var el = document.createElement("a");
  el.id = "toggle_enhanced";
  el.setAttribute("href", "");
  el.innerHTML = "Enhanced version";
  var back = function(e) {
    e.preventDefault();
    window.history.back();
  }
  el.addEventListener("click", back, false);
  document.body.insertBefore(el, document.body.firstChild);
}

if (location.href == initialURL) {
  setup();
}
};
}
```

#### HTML web page source code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Evaluera Ltd</title>
    <meta charset="UTF-8">
    <script src="accSwitch.js"></script>
  </head>
  <body> 
    <h1>Test Page</h1>
    <p>Say: <span id="change">Goodbye</span></p>
  </body>
</html>
```

#### sayhello.js source code

```javascript
var change = document.querySelector("#change");
change.innerText = "Hello";
```

## Related Resources

No endorsement implied.

* [Using Cookies](../css/C29#using-cookies)
* [Progressive Enhancement and Unobtrusive JavaScript](../css/C29#progressive-enhancement-and-unobtrusive-javascript)

## Related Techniques

* [G136: Providing a link at the beginning of a nonconforming web page that points to a conforming alternate version](../general/G136)
* [C29: Using a style switcher to provide a conforming alternate version](../css/C29)
* [SVR4: Allowing users to provide preferences for the display of conforming alternate versions](../server-side-script/SVR4)

## Tests

### Procedure

1. Check enhanced versions of the web page contain a link to the "Conforming Alternate Version".
2. Check that the alternate version is a [conforming alternate version](https://www.w3.org/TR/WCAG22/#dfn-conforming-alternate-versions) of the original page and that it conforms to WCAG 2 at the claimed conformance level.

### Expected Results

* Checks #1 and #2 are true.
