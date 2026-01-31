# Technique SCR2: Using redundant keyboard and mouse event handlers

## About this Technique

This technique relates to [2.1.1: Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard) (Sufficient when used with [G90: Providing keyboard-triggered event handlers](../general/G90)).

This technique applies to HTML with scripting support.

## Description

The objective of this technique is to demonstrate using device independent events to change a decorative image in response to a mouse or focus event. Use the onmouseover and onmouseout events to change a decorative image when the mouse moves on top of or away from an element on the page. Also, use the onfocus and onblur events to change the image when the element receives and loses focus.

The example below has a decorative image in front of an anchor element. When the user mouses over the anchor tag, the decorative image in front of the anchor is changed. When the mouse moves off of the anchor, the image is changed back to its original version. The same image change effect occurs when the user gives keyboard focus to the anchor element. When focus is received the image changes, when focus is lost the image is changed back. This is accomplished by attaching onmouseover, onmouseout, onfocus and onblur event handlers to the anchor element. The event handler is a JavaScript function called updateImage(), which changes the src attribute of the image. The updateImage() is called in response to the onmouseover, onmouseout, onfocus, and onblur events.

Each image is given a unique id. This unique id is passed to updateImage() along with a boolean value indicating which image is to be used: updateImage(imgId, isOver);. The boolean value of true is passed when the mouse is over the anchor element or it has focus. A false value is passed when the mouse moves off of the anchor element or it loses focus. The updateImage() function uses the image id to load the image and then changes the src attribute based on the boolean value. Note that since the image is for decorative purposes, it has a null alt attribute.

Note

It is best to use images that are similar in size and to specify the height and width attributes on the image element. This will prevent any changes to the layout of the page when the image is updated. This example uses images which are identical in size.

## Examples

### Example 1

```html
<!doctype html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Changing Image Source in a Device Independent Manner</title>
    <script>
       /* This function will change the image src of an image element.
        * param imgId - the id of the image object to change
        * param isOver - true when mouse is over or object has focus,
         false when mouse move out or focus is lost
       */
       function updateImage(imgId, isOver) {
       var theImage = document.getElementById(imgId);
       if (theImage != null) {
         if (isOver) {
           theImage.setAttribute("src","yellowplus.gif");
         }
         else {
           theImage.setAttribute("src","greyplus.gif");
         }
       }
     }
    </script>
  </head>
  <body>
    <p>Mouse over or tab to the links below and see the image change.</p>
    <a href="https://www.w3.org/WAI/"
       onmouseover="updateImage('wai', true);" onfocus="updateImage('wai', true);"
       onmouseout="updateImage('wai',false);" onblur="updateImage('wai',false);">
       <img alt="" id="wai" src="greyplus.gif">
       W3C Web Accessibility Initiative</a> &amp;
    <a href="https://www.w3.org/International/" onmouseover="updateImage('i18n', true);" 
       onfocus="updateImage('i18n',true);" onmouseout="updateImage('i18n',false);"
       onblur="updateImage('i18n',false);">
       <img alt="" id="i18n" src="greyplus.gif">
       W3C Internationalization</a>
  </body>
</html>
```

## Tests

### Procedure

Load the web page and test the events using a mouse and via the keyboard.

1. Check that the "standard" image is displayed as expected when the web page is loaded.
2. Using the mouse:
3. Using the keyboard:
4. Verify that the layout of other elements on the page is not affected when the image is changed.

### Expected Results

* All of the steps for the above checks are true.
