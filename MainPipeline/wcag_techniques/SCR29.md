# Technique SCR29: Adding keyboard-accessible actions to static HTML elements

## About this Technique

This technique relates to [2.1.1: Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard) (Advisory).

This technique applies to HTML, script.

## Description

The objective of this technique is to demonstrate how to provide keyboard access to a user interface control that is implemented by actions to static HTML elements such as div or span. This technique ensures that the element is focusable by setting the tabindex attribute, and it ensures that the action can be triggered from the keyboard by providing an onkeyup or onkeypress handler in addition to an onclick handler.

When the tabindex attribute has the value 0, the element can be focused via the keyboard and is included in the tab order of the document. When the tabindex attribute has the value -1, the element cannot be tabbed to, but focus can be set programmatically, using element.focus().

Because static HTML elements do not have actions associated with them, it is not possible to provide a backup implementation or explanation in environments in which scripting is not available. This technique should only be used in environments in which client-side scripting can be relied upon.

Note

Such user interface controls must still satisfy Success Criterion 4.1.2. Applying this technique without also providing role, name, and state information about the user interface control will results in [Failure F59](../failures/F59), Failure of Success Criterion 4.1.2 due to using script to make div or span a user interface control in HTML.

## Examples

### Example 1: Adding a JavaScript action to a div element

The div element on the page is given a unique id attribute and a tabindex attribute with value 0. A script uses the Document Object Model (DOM) to find the div element by its id and add the onclick handler and the onkeyup handler. The onkeyup handler will invoke the action when the Enter key is pressed. Note that the div element must be loaded into the DOM before it can be found and modified. This is usually accomplished by calling the script from the onload event of the body element. The script to add the event handlers will only execute if the user agent supports and has JavaScript enabled.

```html
<script>
// this is the function to perform the action. This simple example toggles a message.
function doSomething(event) {
  var msg=document.getElementById("message");
  msg.style.display = msg.style.display=="none" ? "" : "none";

  //return false from the function to make certain
  // that the href of the link does not get invoked
  return false;
  }
	
  // this is the function to perform the action when the Enter key has been pressed.  
  function doSomethingOnEnter(event) {
    var key = 0;

     // Determine the key pressed, depending on whether window.event
    // or the event object is in use
    if (window.event) {
      key = window.event.keyCode;
    }
    else if (event) {
      key = event.keyCode;
    }
		
    // Was the Enter or Space key pressed?
    if (key == 13 || key == 32) {
      return doSomething(event);
    } 

    // The event has not been handled, so return true
    return true;
  }
	
  // This setUpActions() function must be called to set the onclick and onkeyup
  // event handlers onto the existing div element.
  // This function must be called after the div element with id="active" 
  // has been loaded into the DOM.
  // In this example the setUpActions() function is called from the onload event
  // for the body element.
  function setUpActions() {
   
    // get the div object
    var active=document.getElementById("active");

    // assign the onclick handler to the object.
    active.onclick=doSomething;

    // assign the onkeyup handler to the object.
    active.onkeyup=doSomethingOnEnter;
}
</script>
 
<body onload="setUpActions();">
  <p>Here is the link to modify with a javascript action:</p>
  <div>
    <span id="active" role="button" tabindex="0">Do Something</span>
  </div>
  <div aria-live="polite">
    <div id="message">Hello, world!</div>
  </div>
</body>
```

Working example of this code: [Creating Divs with Actions using JavaScript](../../working-examples/script-action-on-div/).

## Related Resources

No endorsement implied.

* [HTML - Scripting](https://html.spec.whatwg.org/multipage/scripting.html#scripting-3)
* [HTML - Focus](https://html.spec.whatwg.org/multipage/interaction.html#focus)
* [ARIA Global States And Properties](https://www.w3.org/TR/wai-aria/#global_states)

## Related Techniques

* [SCR20: Using both keyboard and other device-specific functions](../client-side-script/SCR20)
* [SCR24: Using progressive enhancement to open new windows on user request](../client-side-script/SCR24)
* [SCR35: Making actions keyboard accessible by using the onclick event of anchors and buttons](../client-side-script/SCR35)
* [F59: Failure of Success Criterion 4.1.2 due to using script to make div or span a user interface control in HTML without providing a role for the control](../failures/F59)

## Tests

### Procedure

In a user agent that supports Scripting:

1. Click on the control with the mouse
2. Check that the scripting action executes properly
3. Check that it is possible to navigate to and give focus to the control via the keyboard
4. Set keyboard focus to the control
5. Check that pressing Enter or Space invokes the scripting action.

### Expected Results

* All of the checks are true
