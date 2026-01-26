# Technique SCR18: Providing client-side validation and alert

## About this Technique

This technique relates to:

* [3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) (Sufficient)
* [3.3.3: Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion) (Advisory)
* [3.3.4: Error Prevention (Legal, Financial, Data)](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data) (Advisory)

This technique applies to content that validates user input.

## Description

The objective of this technique is to validate user input as values are entered for each field, by means of client-side scripting. If errors are found, an alert dialog describes the nature of the error in text. Once the user dismisses the alert dialog, it is helpful if the script positions the keyboard focus on the field where the error occurred.

## Examples

### Example 1: Checking a single control with an event handler

The following script will check that a valid date has been entered in the form control.

```html
<label for="date">Date:</label>
<input type="text" name="date" id="date" 
  onchange="if(isNaN(Date.parse(this.value))) 
  alert('This control is not a valid date. 
  Please re-enter the value.');">
```

### Example 2: Checking multiple controls when the user submits the form

The following sample shows multiple controls in a form. The form element uses the onsubmit attribute which creates an event handler to execute the validation script when the user attempts to submit the form. If the validation is successful, the event returns true and the form submission proceeds; if the validation finds errors, it displays an error message and returns false to cancel the submit attempt so the user can fix the problems.

Note

This example demonstrates an alert for simplicity. A more helpful notification to the user would be to highlight the controls with problems and add information to the page about the nature of the errors and how to navigate to the controls that require data fixes.

Although this example uses an onsubmit attribute on the form element for brevity, normal practice is to create a submit event listener when the page is loaded.

Script code:

```javascript
function validate() {
  // initialize error message
  var msg = "";
	
  //validate name
  var pattern = /^[a-zA-Z\s]+$/;
  var el = document.getElementById("name");
  
  if (!pattern.test(el.value)) {
    msg += "Name can only have letters and spaces. ";
  }
	
  // validate number
  var pattern = /^[\d\-+\.\s]+$/;
  var el = document.getElementById("tel");

  if (!pattern.test(el.value)) {
    msg += "Telephone number can only have digits and separators. ";
  }
	
  if (msg != "") {
    alert(msg);
    return false;
  }
  else {
  return true;
  }
```

Form code:

```html
<form action="multiple-controls.html" onsubmit="return validate()">
  <div>
    <label for="name">Name:</label>
    <input autocomplete="name" id="name" name="name" type="text">
  </div>
  <div>
    <label for="tel">Telephone number:</label>
    <input autocomplete="tel" id="tel" name="tel" type="tel">
  </div>
  <div>
    <input type="submit">
  </div>
</form>
```

This is demonstrated in the [working example of checking multiple controls when the user submits the form](../../working-examples/script-check-multiple-controls/).

## Related Techniques

* [G89: Providing expected data format and example](../general/G89)

## Tests

### Procedure

For form fields that require specific input:

1. enter invalid data
2. determine if an alert describing the error is provided.

### Expected Results

* #2 is true
