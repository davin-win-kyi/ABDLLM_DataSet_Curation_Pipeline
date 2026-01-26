# Technique SCR32: Providing client-side validation and adding error text via the DOM

## About this Technique

This technique relates to:

* [3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) (Sufficient)
* [3.3.3: Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion) (Advisory)

This technique applies to script used with HTML.

## Description

The objective of this technique is to demonstrate the display of an error message when client side validation of a form field has failed. Anchor elements are used to display the error messages in a list and are inserted above the fields to be validated. Anchor elements are used in the error messages so that focus can be placed on the error message(s), drawing the user's attention to it. The href of the anchor elements contain an in-page link which references the fields where error(s) have been found.

In a deployed application, if Javascript is turned off, client side validation will not occur. Therefore, this technique would only be sufficient in situations where scripting is relied upon for conformance or when server side validation techniques are also used to catch any errors and return the page with information about the fields with errors.

## Examples

### Example 1: Listing errors in a block at the top of a form

This example validates required fields as well as fields where a specific format is required. When an error is identified, the script inserts a list of error messages into the DOM and moves focus to them.

#### HTML for the form

```html
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <title>Form Validation</title>
    <meta charset="utf-8">
    <link href="css/validate.css" rel="stylesheet">
    <script src="scripts/validate.js">
  </head>
  <body>
    <h1>Form Validation</h1>
    <p>The following form is validated before being submitted if scripting
      is available, otherwise the form is validated on the server. All fields are
      required, except those marked optional. If errors are found in the submission,
      the form is cancelled and a list of errors is displayed
      at the top of the form.</p>

    <p>Please enter your details below.</p>
	
    <h2>Validating Form</h2>
    <form id="personalform">
      <div class="validationerrors"></div>
      <fieldset>
        <legend>Personal Details</legend>
          <div>
            <label for="forename">Please enter your forename</label>
            <input autocomplete="given-name" class="string"
             id="forename" name="forename" type="text" value="">
         </div>
         <div>
            <label for="age">Please enter your age</label>
            <input class="number" id="age" name="age" type="text" value="">
         </div>
         <div>
           <label for="email">Please enter your email address</label>
           <input autocomplete="email" class="email" id="email"
            name="email" type="text" value="">
         </div>
      </fieldset>
      <div>
        <input type="submit" name="signup" value="Sign up">
      </div>
    </form>
    
    <h2>Second Form</h2>
    <form id="secondform">
      <div class="validationerrors"></div>
      <fieldset>
        <legend>Second Form Details</legend>
          <div>
            <label for="suggestion">Enter a suggestion</label>
            <input class="string" id="suggestion" name="suggestion" type="text" value="">
          </div>
          <div>
            <label for="optemail">Please enter your email address (optional)</label>
            <input autocomplete="email" class="optional email" id="optemail"
             name="optemail" type="text" value="">
          </div>
          <div>
            <label for="rating">Please rate this suggestion</label>
            <input class="number" id="rating" name="rating" type="text" value="">
          </div>
          <div>
            <label for="jibberish">Enter some jibberish (optional)</label>
            <input id="jibberish" name="jibberish" type="text" value="">
          </div>
      </fieldset>
      <div>
        <input type="submit" name="submit" value="Add Suggestion">
      </div>
    </form>
  </body>
</html>
```

#### The Javascript which performs the validation and inserts the error messages

```javascript
window.onload = initialise;
function initialise() {
  var objForms = document.getElementsByTagName('form');
  var iCounter;
	
  // Attach an event handler for each form
  for (iCounter=0; iCounter<objForms.length; iCounter++) {
    objForms[iCounter].onsubmit = function(){return validateForm(this);};
  }
}
		
// Event handler for the form
function validateForm(objForm) {
  var arClass = [];
  var iErrors = 0;
  var objField = objForm.getElementsByTagName('input');
  var objLabel = objForm.getElementsByTagName('label');
  var objList = document.createElement('ol');
  var objError, objExisting, objNew, objTitle, objParagraph, objAnchor, objPosition;
  var strLinkID, iFieldCounter, iClassCounter, iCounter;
	
  // Get the id or name of the form, to make a unique
  // fragment identifier
  if (objForm.id) {
    strLinkID = objForm.id + 'ErrorID';
  }
  else {
    strLinkID = objForm.name + 'ErrorID';
  }
	
  // Iterate through input form controls, looking for validation classes
  for (iFieldCounter=0; iFieldCounter<objField.length; iFieldCounter++) {
    
  // Get the class for the field, and look for the appropriate class
  arClass = objField[iFieldCounter].className.split(' ');
  for (iClassCounter=0; iClassCounter<arClass.length; iClassCounter++) {
    switch (arClass[iClassCounter]) {
      case 'string':
        if (!isString(objField[iFieldCounter].value, arClass)) {
          if (iErrors === 0) {
            logError(objField[iFieldCounter], objLabel, objList, strLinkID);
          }
          else {
            logError(objField[iFieldCounter], objLabel, objList, '');
          }
          iErrors++;
        }
      break;
      case 'number':
        if (!isNumber(objField[iFieldCounter].value, arClass)) {
          if (iErrors === 0) {
            logError(objField[iFieldCounter], objLabel, objList, strLinkID);
          }
          else {
            logError(objField[iFieldCounter], objLabel, objList, '');
          }
          iErrors++;
        }
      break;
      case 'email' :
        if (!isEmail(objField[iFieldCounter].value, arClass)) {
          if (iErrors === 0) {
            logError(objField[iFieldCounter], objLabel, objList, strLinkID);
          }
          else {
            logError(objField[iFieldCounter], objLabel, objList, '');
          }
          iErrors++;
        }
        break;
      }
    }
  }
	
  if (iErrors > 0) {

    // If not valid, display error messages
    objError = objForm.getElementsByTagName('div');
				
    // Look for existing errors
    for (iCounter=0; iCounter<objError.length; iCounter++) {
      if (objError[iCounter].className == 'validationerrors') {
        objExisting = objError[iCounter];
      }
    }
	
    objNew = document.createElement('div');
    objTitle = document.createElement('h2');
    objParagraph = document.createElement('p');
    objAnchor = document.createElement('a');
	
    if (iErrors == 1) {
      objAnchor.appendChild(document.createTextNode('1 Error in Submission'));
    }
    else {
      objAnchor.appendChild(document.createTextNode(iErrors + ' Errors in Submission'));
    }

    objAnchor.href = '#' + strLinkID;
    objAnchor.className = 'submissionerror';

    objTitle.appendChild(objAnchor);
    objParagraph.appendChild(document.createTextNode('Please review the following'));
    objNew.className = 'validationerrors';

    objNew.appendChild(objTitle);
    objNew.appendChild(objParagraph);
    objNew.appendChild(objList);
				
    // If there were existing error, replace them with the new lot,
    // otherwise add the new errors to the start of the form
    if (objExisting) {
      objExisting.parentNode.replaceChild(objNew, objExisting);
    }
    else {
      objPosition = objForm.firstChild;
      objForm.insertBefore(objNew, objPosition);
    }
	
    // Allow for latency
    setTimeout(function() { objAnchor.focus(); }, 50);
				
    // Don't submit the form
    objForm.submitAllowed = false;
    return false;
  }
	
  // Submit the form
  return true;
	}
	
  // Function to add a link in a list item that points to problematic field control
  function addError(objList, strError, strID, strErrorID) {
    
		var objListItem = document.createElement('li');
    var objAnchor = document.createElement('a');
		 
    // Fragment identifier to the form control
    objAnchor.href='#' + strID;

    // Make this the target for the error heading
    if (strErrorID.length > 0) {
      objAnchor.id = strErrorID;
    }
	
    // Use the label prompt for the error message
    objAnchor.appendChild(document.createTextNode(strError));

    // Add keyboard and mouse events to set focus to the form control
    objAnchor.onclick = function(event){return focusFormField(this, event);};
    objAnchor.onkeypress = function(event){return focusFormField(this, event);};
    objListItem.appendChild(objAnchor);
    objList.appendChild(objListItem);
  }

  function focusFormField(objAnchor, objEvent) {
    var strFormField, objForm;

    // Allow keyboard navigation over links
    if (objEvent && objEvent.type == 'keypress') {
      if (objEvent.keyCode != 13 && objEvent.keyCode != 32) {
        return true;
      }
    }
	
    // set focus to the form control
    strFormField = objAnchor.href.match(/[^#]\w*$/);
    objForm = getForm(strFormField);
    objForm[strFormField].focus();
    return false;
  }

    // Function to return the form element from a given form field name
    function getForm(strField) {
      var objElement = document.getElementById(strField);

    // Find the appropriate form
    do {
      objElement = objElement.parentNode;
    } while (!objElement.tagName.match(/form/i) && objElement.parentNode);

    return objElement;
  }
	
  // Function to log the error in a list
  function logError(objField, objLabel, objList, strErrorID) {
    var iCounter, strError;

    // Search the label for the error prompt
    for (iCounter=0; iCounter<objLabel.length; iCounter++) {
      if (objLabel[iCounter].htmlFor == objField.id) {
        strError = objLabel[iCounter].firstChild.nodeValue;
      }
    }

    addError(objList, strError, objField.id, strErrorID);
  }
	
  // Validation routines - add as required

  function isString(strValue, arClass) {
    var bValid = (typeof strValue == 'string' && strValue.replace(/^\s*|\s*$/g, '') 
    !== '' && isNaN(strValue));

    return checkOptional(bValid, strValue, arClass);
  }

  function isEmail(strValue, arClass) {
    var objRE = /^[\w-\.\']{1,}\@([\da-zA-Z\-]{1,}\.){1,}[\da-zA-Z\-]{2,}$/;
    var bValid = objRE.test(strValue);

    return checkOptional(bValid, strValue, arClass);
  }
	
  function isNumber(strValue, arClass) {
    var bValid = (!isNaN(strValue) && strValue.replace(/^\s*|\s*$/g, '') !== '');

    return checkOptional(bValid, strValue, arClass);
  }

  function checkOptional(bValid, strValue, arClass) {
    var bOptional = false;
    var iCounter;

    // Check if optional
    for (iCounter=0; iCounter<arClass.length; iCounter++) {
      if (arClass[iCounter] == 'optional') {
        bOptional = true;
      }
    }

    if (bOptional && strValue.replace(/^\s*|\s*$/g, '') === '') {
      return true;
    }

    return bValid;
  }
```

Working example of this technique implemented using PHP, Javascript, CSS and HTML: [Form Validation Example](../../working-examples/script-form-validation-2/index.php).

## Related Techniques

* [G83: Providing text descriptions to identify required fields that were not completed](../general/G83)
* [G85: Providing a text description when user input falls outside the required format or values](../general/G85)
* [SCR18: Providing client-side validation and alert](../client-side-script/SCR18)

## Tests

### Procedure

Create error messages using anchor tags and appropriate scripting via the technique above.

1. Load the page.
2. Enter a valid value in the field(s) associated with an error message and verify that no error messages are displayed.
3. Enter an invalid value in the field(s) associated with an error message and verify that the correct error message for the field is displayed.
4. Verify that the error messages receive focus.
5. Enter a valid value in the field(s) associated with the displayed error message and verify that the error message is removed.
6. Repeat for all fields with associated error messages created via anchor tags.

Note

It is recommended that you also run the above procedure using an assistive technology.

### Expected Results

* Checks #2, #3, #4, and #5 are all true.
