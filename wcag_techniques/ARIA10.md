# Technique ARIA10: Using aria-labelledby to provide a text alternative for non-text content

## About this Technique

This technique relates to [1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) (Sufficient).

This technique applies to HTML with [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to provide a short description for an element that can be read by assistive technologies by using the aria-labelledby attribute. The aria-labelledby attribute associates an element with text that is visible elsewhere on the page by using an id reference value that matches the id attribute of the labeling element. Assistive technology such as screen readers use the text of the element identified by the value of the aria-labelledby attribute as the text alternative for the element with the attribute.

## Examples

### Example 1: Providing a short description for a complex graphic

This example shows how to use the aria-labelledby attribute to provide a short text description for a read-only complex graphic of an star rating pattern; the graphic is composed of several image elements. The text alternative for the graphic is the label, visible on the page beneath the star pattern.

```html
<div role="img" aria-labelledby="star-id">
  <img src="fullstar.png" alt="">
  <img src="fullstar.png" alt="">
  <img src="fullstar.png" alt="">
  <img src="fullstar.png" alt="">
  <img src="emptystar.png" alt="">
</div>
<div id="star-id">4 of 5</div>
```

Working example: [Providing a short description for a complex graphic](../../working-examples/aria-labelledby-description-complex-graphic/).

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/)
* [Accessible Name and Description Computation](https://www.w3.org/TR/accname/)

## Related Techniques

* [H37: Using alt attributes on img elements](../html/H37)
* [F65: Failure of Success Criterion 1.1.1 due to omitting the alt attribute or text alternative on img elements, area elements, and input elements of type "image"](../failures/F65)

## Tests

### Procedure

1. Examine each element where the aria-labelledby attribute is present and the element does not support the alt attribute.
2. Check whether the value of the aria-labelledby attribute is the id of an element on the web page.
3. Determine that the text of the element identified by the aria-labelledby attribute accurately labels the element, provides a description of its purpose, or provides equivalent information.

### Expected Results

* #2 and #3 are true.
