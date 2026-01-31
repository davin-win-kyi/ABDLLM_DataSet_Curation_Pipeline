# Technique ARIA2: Identifying a required field with the aria-required property

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Advisory)
* [3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) (Sufficient)

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The objective of this technique is to provide programmatic indication that a form field (which shown through presentation to be required) is mandatory for successful submission of a form.

The fact that the element is required is often visually presented (via a text or non-text symbol, or text indicating input is required or color / styling) but this is not programmatically determinable as part of the field's name.

The WAI-ARIA aria-required property indicates that user input is required before submission. The aria-required property can have values of true or false. For example, if a user must fill in an address field, then aria-required is set to true.

Note

Use of aria-required="true" might be beneficial even when an asterisk or other text symbol is programmatically associated with the field as it may reinforce its required property for some assistive technology users.

The fact that the element is required is often visually presented (such as a sign or symbol after the control). Using the aria-required property in addition to the visual presentation makes it much easier for user agents to pass on this important information to the user in a user agent-specific manner. Refer to [ARIA in HTML](https://www.w3.org/TR/html-aria/) for information on how to provide WAI-ARIA States and Properties with HTML. WAI-ARIA States and Properties are compatible with other languages as well; refer to documentation in those languages.

## Examples

### Example 1: The required property is indicated by an asterisk placed in the label element

```html
<form>
  <p>Note: * denotes a required field</p>
  <div>
    <label for="usrname">Login name *:</label>
    <input aria-required="true" autocomplete="username" id="usrname" type="text">
  </div>
  <div>
    <label for="pwd">Password *:</label>
    <input aria-required="true" autocomplete="current-password" 
     id="pwd" type="password">
  </div>
  <div>
    <input type="submit" value="Login">
  </div>
</form>
```

### Example 2: The required property is indicated by the word "required" placed next to the label element

```html
<form>
  <div>
    <label for="fname">First name:</label> <span>(required)</span>
    <input aria-required="true" autocomplete="given-name" id="fname" type="text">
  </div>
  <div>
    <label for="mname">Middle name:</label> <span>(required)</span>
    <input autocomplete="additional-name" id="mname" type="text">
  </div>
  <div>
    <label for="lname">Last name:</label> <span>(required)</span>
    <input aria-required="true" autocomplete="family-name" id="lname" type="text">
  </div>
  <div>
    <label for="email">Email address:</label> <span>(required)</span>
    <input aria-required="true" autocomplete="email" id="email" type="text">
  </div>
  <div>
    <label for="zip_post">Zip / Postal code:</label> <span>(required)</span>
    <input aria-required="true" autocomplete="postal-code" id="zip_post" type="text">
  </div>
  <div>
    <input type="submit" value="Next Step">
  </div>
</form>
```

### Example 3: Required fields are indicated by a red border around the fields and a star icon rendered via CSS using ::after

This example uses custom radio buttons with role=radio. The CSS properties are available below the form.

```html
<form>
  <label data-required="true" for="acctnum">Account Number</label>
  <input aria-required="true" id="acctnum" type="text">

  <p data-required="true" id="radio_label">
    Please send an alert when balance exceeds $3,000.
  </p>

  <ul aria-required="true" aria-labelledby="radio_label" role="radiogroup">
    <li aria-checked="false" id="rb1" role="radio" tabindex="0">Yes</li>
    <li aria-checked="false" id="rb2" role="radio" tabindex="-1">No</li>
  </ul>
</form>
```

Related CSS style definition for this example:

```css
[aria-required=true] {
  border: red thin solid;
}
[data-required=true]::after {
  content: url('/iconStar.gif');
}
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Overview](https://www.w3.org/WAI/standards-guidelines/aria/).
* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/).
* [aria-required=true: WCAG 2 Compliance versus Best Practice](http://www.deque.com/blog/aria-requiredtrue-wcag-2-compliance-practice/).

## Tests

### Procedure

For each control which is shown via presentation to be required.

1. Check whether the aria-required attribute is present:
2. Check whether the value of the aria-required attribute is the correct required state of the user interface component.

### Expected Results

* Checks #1 and #2 are true
