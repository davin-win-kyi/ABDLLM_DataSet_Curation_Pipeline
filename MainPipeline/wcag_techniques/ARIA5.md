# Technique ARIA5: Using WAI-ARIA state and property attributes to expose the state of a user interface component

## About this Technique

This technique relates to [4.1.2: Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value) (Sufficient when used with [G10: Creating components using a technology that supports the accessibility … notification of changes](../general/G10)).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The objective of this technique is to use [WAI-ARIA state and property attributes](https://www.w3.org/TR/wai-aria/#states_and_properties) to expose the state, properties and values of a user interface component so that they can be read and set by assistive technology, and so that assistive technology is notified of changes to these values. The WAI-ARIA specification provides a normative description of each attribute, and the role of the user interface elements that they support. When rich internet applications define new user interface widgets, exposing the state and property attributes enables users to understand the widget and how to interact with it.

## Examples

### Example 1: A toggle button

A widget with role button acts as a toggle button when it implements the attribute aria-pressed. When aria-pressed is true, the button is in a "pressed" state. When aria-pressed is false, it is not pressed. If the attribute is not present, the button is a simple command button.

The following snippet from the [ARIA Authoring Practices Guide (APG) examples for button](https://www.w3.org/WAI/ARIA/apg/example-index/button/button.html) shows WAI-ARIA mark-up for a toggle button to mute/unmute audio:

```html
<a tabindex="0"
  role="button"
  id="toggle"
  aria-pressed="false">
  Mute
  ...
</a>
```

The a element has a role="button" and an aria-pressed attribute. The following excerpt from the Javascript for this example updates the value of the aria-pressed attribute:

```javascript
/**
* Toggles the toggle button's state between *pressed* and *not pressed*.
*
* @param {HTMLElement} button
*/

function toggleButtonState(button) {
  var isAriaPressed = button.getAttribute('aria-pressed') === 'true';
  button.setAttribute('aria-pressed', isAriaPressed ? 'false' : 'true');
  ...
}
```

### Example 2: A slider

A widget with role slider lets a user select a value from within a given range. The slider represents the current value and the range of possible values via the size of the slider and the position of the handle. These properties of the slider are represented by the attributes aria-valuemin, aria-valuemax, and aria-valuenow.

The following snippet from the [ARIA Authoring Practices Guide (APG) color viewer slider example](https://www.w3.org/WAI/ARIA/apg/example-index/slider/slider-color-viewer.html) shows WAI-ARIA mark-up for one of the sliders:

```html
<div id="id-red" class="color-slider-label">Red</div>
<div class="color-slider red"
  role="slider"
  tabindex="0"
  aria-valuemin="0"
  aria-valuenow="128"
  aria-valuemax="255"
  aria-labelledby="id-red">
   ...
</div>
```

The following excerpt from the Javascript for this example updates the value of the aria-valuenow attribute when the value of the slider handle is changed:

```javascript
moveSliderTo(slider, value) {
  ...
  slider.sliderNode.setAttribute('aria-valuenow', value);
  ...
}
```

## Related Resources

No endorsement implied.

* [Accessible Rich Internet Applications (WAI-ARIA), Roles](https://www.w3.org/TR/wai-aria/#usage_intro)
* [Accessible Rich Internet Applications (WAI-ARIA), The Roles Model](https://www.w3.org/TR/wai-aria/#roles)
* [Accessible Rich Internet Applications (WAI-ARIA), Supported States and Properties](https://www.w3.org/TR/wai-aria/#states_and_properties)
* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [Using WAI-ARIA in HTML](https://www.w3.org/TR/aria-in-html/)

## Related Techniques

* [ARIA4: Using a WAI-ARIA role to expose the role of a user interface component](../aria/ARIA4)
* [H91: Using HTML form controls and links](../html/H91)

## Tests

### Procedure

[The WAI-ARIA specification, Section 5.3, Categorization of Roles](https://www.w3.org/TR/wai-aria/#roles_categorization) defines the required and inherited states and properties for each role.

For a user interface component using the WAI-ARIA role attribute:

1. Check that the required states and properties for the role are present.
2. Check that no WAI-ARIA states or properties that are neither required, supported, nor inherited are present.
3. Check that the state and property values are updated to reflect the current state when the user interface component changes state.

### Expected Results

* #1, #2, and #3 are true.

## Test Rules

The following are Test Rules related to this Technique. It is not necessary to use these particular Test Rules to check for conformance with WCAG, but they are defined and approved test methods. For information on using Test Rules, see [Understanding Test Rules for WCAG Success Criteria](https://www.w3.org/WAI/WCAG22/Understanding/understanding-act-rules.html).

* [Element with role attribute has required states and properties](/WAI/standards-guidelines/act/rules/4e8ab6/)
* [ARIA state or property is permitted](/WAI/standards-guidelines/act/rules/5c01ea/proposed/)
