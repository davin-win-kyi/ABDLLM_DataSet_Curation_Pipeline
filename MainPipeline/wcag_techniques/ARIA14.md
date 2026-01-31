# Technique ARIA14: Using aria-label to provide an accessible name where a visible label cannot be used

## About this Technique

This technique relates to [4.1.2: Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

For sighted users, the context and visual appearance of an element can provide sufficient cues to determine the purpose. An example is the “×” often used in the top-right corner of dialogs to indicate the control for closing the dialog. While it might be visually clear that the button with the “×” symbol closes the dialog, users with assistive technologies rely on accessible names that clearly communicate the purpose of components, in this case “Close”.

When no clear visible text label is available due to design decisions, the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) can be set by using the aria-label attribute instead, provided that the element has an implicit or explicit [role that supports naming](https://www.w3.org/TR/wai-aria-1.2/#namefromauthor).

The aria-label attribute can also be used to provide an accessible name for custom controls that are not [labelable elements](https://html.spec.whatwg.org/multipage/forms.html#category-label), and cannot therefore use a <label> element with the for attribute.

For instance, aria-label or aria-labelledby are the most suitable way to provide an accessible name when a <div> element is made editable using the contentEditable attribute, instead of native form elements such as <input type="text"> or <textarea> in order to provide a richer text editing experience.

## Examples

### Example 1: A close button in a dialog

On a page, a button displays a dialog (a <div> element) with additional information. The “close” element is implemented as a <button> containing merely the symbol “×”. The property aria-label="close" is used to provide an accessible name to the button.

```html
<dialog id="dialog">
  This is the content of the dialog.
  <button aria-label="Close">×</button>
</dialog>
```

Working example: [Close button example](../../working-examples/aria-label-accessible-name-dialog/).

### Example 2: A phone number with multiple fields

```html
<div role="group" aria-labelledby="groupLabel">
  <span id="groupLabel">Work Phone</span>
  +<input autocomplete="tel-country-code" type="number" aria-label="country code">
  <input autocomplete="tel-area-code" type="number" aria-label="area code">
  <input autocomplete="tel-local" type="number" aria-label="subscriber number">
</div>
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/)

## Related Techniques

* [ARIA6: Using aria-label to provide labels for objects](../aria/ARIA6)
* [ARIA16: Using aria-labelledby to provide a name for user interface controls](../aria/ARIA16)

## Tests

### Procedure

For elements that use the aria-label attribute:

1. Check that the value of the aria-label attribute properly describes the purpose of an element where user input is required

### Expected Results

* #1 is true.
