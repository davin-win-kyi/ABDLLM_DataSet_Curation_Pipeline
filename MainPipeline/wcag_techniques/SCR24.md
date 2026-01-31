# Technique SCR24: Using progressive enhancement to open new windows on user request

## About this Technique

This technique relates to [3.2.5: Change on Request](https://www.w3.org/WAI/WCAG22/Understanding/change-on-request) (Sufficient when used for including pop-up windows).

This technique applies to HTML.

## Description

The objective of this technique is to avoid confusion that may be caused by the appearance of new windows that were not requested by the user. Suddenly opening new windows can disorient or be missed completely by some users. New windows / tabs can be opened with the HTML target attribute or JavaScript. The example below demonstrates how to open new windows with script: it adds an event handler to a link and warns the user that the content will open in a new window.

## Examples

### Example 1: Using JavaScript to open a new tab / window

#### Markup:

The script is included in the head of the document, and the link has an id that can be used as a hook by the script.

```html
<script src="popup.js"></script>
...
<a href="help.html" id="newwin">Show Help</a>
```

#### Script:

```javascript
window.onload = addHandlers;

function addHandlers(){
  var objAnchor = document.getElementById('newwin');
  
  if (objAnchor){
    objAnchor.firstChild.data = objAnchor.firstChild.data + ' (opens in a new window)';
    objAnchor.onclick = function(event){return launchWindow(this, event);}
    // UAAG requires that user agents handle events in a device-independent manner
    // but only some browsers do this, so add keyboard event to be sure
    objAnchor.onkeypress = function(event){return launchWindow(this, event);}
  }
}
   
   function launchWindow(objAnchor, objEvent)
   {
     var iKeyCode, bSuccess=false;
   
     // If the event is from a keyboard, we only want to open the
     // new window if the user requested the link (return or space)
     if (objEvent && objEvent.type == 'keypress')
     {
       if (objEvent.keyCode)
         iKeyCode = objEvent.keyCode;
       else if (objEvent.which)
         iKeyCode = objEvent.which;
   
       // If not carriage return or space, return true so that the user agent
       // continues to process the action
       if (iKeyCode != 13 && iKeyCode != 32)
         return true;
     }
   
     bSuccess = window.open(objAnchor.href);
   
     // If the window did not open, allow the browser to continue the default
     // action of opening in the same window
     if (!bSuccess)
       return true;
   
     // The window was opened, so stop the browser processing further
     return false;
   }
```

## Related Resources

No endorsement implied.

* [HTML - Navigable target names](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-target-names)
* [Wikipedia: Progressive Enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement)

## Related Techniques

* [H83: Using the target attribute to open a new window on user request and indicating this in link text](../html/H83)

## Tests

### Procedure

1. Activate each link in the document to check if it opens a new window.
2. For each link that opens a new window, check that it uses script to accomplish each of the following:

### Expected Results

* #2 is true.
