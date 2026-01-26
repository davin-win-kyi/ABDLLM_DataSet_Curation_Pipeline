# Technique ARIA15: Using aria-describedby to provide descriptions of images

## About this Technique

This technique relates to [1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The objective of this technique is to provide descriptions of images when a short text alternative does not adequately convey the function or information provided in the object.

A feature of WAI-ARIA is the ability to associate descriptive text with a section, drawing, form element, picture, and so on using the aria-describedby property. Descriptive text provided using aria-describedby is separate from the short name provided using the alt attribute in HTML. An advantage of providing long descriptions using content from the same page as the image is that the alternative is available to all, including sighted people who do not have assistive technology.

Like aria-labelledby, aria-describedby can accept multiple ids to point to other regions of the page using a space separated list. It is also limited to ids for defining these sets.

## Examples

### Example 1: Describing an image

The following example shows how aria-describedby can be applied to an image to provide a long description, where that text description is on the same page as the image.

```html
<img src="ladymacbeth.jpg" alt="Lady MacBeth" aria-describedby="p1">
<p id="p1">This painting dates back to 1889 and is oil on canvas. It was created by 
 John Singer Sargent, and represents ...</p>
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML to Platform Accessibility APIs Implementation Guide: Accessible Name and Description Calculation](https://www.w3.org/TR/html-aapi/#accessible-name-and-description-calculation)

## Related Techniques

* [ARIA6: Using aria-label to provide labels for objects](../aria/ARIA6)
* [ARIA16: Using aria-labelledby to provide a name for user interface controls](../aria/ARIA16)
* [G92: Providing long description for non-text content that serves the same purpose and presents the same information](../general/G92)

## Tests

### Procedure

1. Examine each image element where a aria-describedby attribute is present.
2. Examine whether the aria-describedby attribute programmatically associates an element with its text description, via the id attribute on the element where the text to be used as the description is found.
3. Examine whether the combined text equivalent and associated text description accurately describe or provide the equivalent purpose to the object.

### Expected Results

* #1, #2, and #3 are true.
