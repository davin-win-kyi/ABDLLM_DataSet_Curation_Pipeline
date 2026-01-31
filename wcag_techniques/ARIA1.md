# Technique ARIA1: Using the aria-describedby property to provide a descriptive label for user interface controls

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Advisory)
* [3.3.2: Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions) (Sufficient when used with [G131: Providing descriptive labels](../general/G131))

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to demonstrate how to use the WAI-ARIA [aria-describedby](https://www.w3.org/TR/wai-aria-1.2/#aria-describedby) property to provide programmatically determined, descriptive information about a user interface element. The aria-describedby property may be used to attach descriptive information to one or more elements through the use of an id reference list. The id reference list contains one or more unique element ids.

Refer to [ARIA in HTML](https://www.w3.org/TR/html-aria/) for information on how to provide WAI-ARIA States and Properties with HTML. WAI-ARIA States and Properties are compatible with other languages as well; refer to documentation in those languages.

Note

The aria-describedby property is not designed to reference descriptions on an external resource - since it is an id, it must reference an element in the same DOM document.

## Examples

### Example 1: Using aria-describedby to associate instructions with form fields

Sample form field using aria-describedby to associate instructions with form fields while there is a form label.

```html
<form>
  <label for="fname">First name</label>
  <input aria-describedby="int2" autocomplete="given-name" id="fname" type="text">
  <p id="int2">Your first name is sometimes called your "given name".</p>
</form>
```

### Example 2: Using aria-describedby property to provide more detailed information about the button

```html
<div>
  <span id="fontDesc">Select the font faces and sizes to be used on this page</span>
  <button aria-describedby="fontDesc" id="fontB" type="button">Fonts</button>
</div>
<div>
  <span id="colorDesc">Select the colors to be used on this page</span>
  <button aria-describedby="colorDesc" id="colorB" type="button">Colors</button>
</div>
<div>
  <span id="customDesc">Customize the layout and styles used on this page</span>
  <button aria-describedby="customDesc" id="customB" type="button">Customize</button>
</div>
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Overview](https://www.w3.org/WAI/standards-guidelines/aria/).
* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/).
* [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/)
* [Accessible Name and Description Computation](https://www.w3.org/TR/accname/).
* [aria-describedby attribute ( MDN )](https://developer.mozilla.org/en-US/docs/web/accessibility/aria/attributes/aria-describedby).
* [Using WAI-ARIA in HTML](https://www.w3.org/TR/aria-in-html/).

## Related Techniques

* [ARIA2: Identifying a required field with the aria-required property](../aria/ARIA2)
* [ARIA7: Using aria-labelledby for link purpose](../aria/ARIA7)

## Tests

### Procedure

1. Check that there is a user interface control having an aria-describedby attribute that references one or more elements via unique id.
2. Check that the referenced element or elements provide additional information about the user interface control.

### Expected Results

* Checks #1 and #2 are true.
