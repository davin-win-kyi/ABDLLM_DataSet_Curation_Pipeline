# Technique ARIA6: Using aria-label to provide labels for objects

## About this Technique

This technique relates to [1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to provide a label for objects that can be read by assistive technology. The aria-label attribute provides the text label for an object, such as a button. When a screen reader encounters the object, the aria-label text is read so that the user will know what it is.

Authors should be aware that aria-label may be disregarded by assistive technologies in situations where aria-labelledby is used for the same object. For more information on the naming hierarchy please consult the [accessible name and description computation](https://www.w3.org/TR/accname/#mapping_additional_nd_te) section of the Accessible Name And Description Computation recommendation. Authors should be aware that use of aria-label will override any native naming such as alt on images or label associated with a form field using the for attribute.

## Examples

### Example 1: Distinguishing navigation landmarks

The following example shows how aria-label could be used to distinguish two navigation landmarks in an HTML document, where there are more than two of the same type of landmark on the same page, and there is no existing text on the page that can be referenced as the label.

```html
<div role="navigation" aria-label="Primary">
  <ul>
    <li>...a list of links here ...</li>
  </ul>
</div>
<div role="navigation" aria-label="Secondary">
  <ul>
    <li>...a list of links here ...</li>
  </ul>
</div>
```

### Example 2: Identifying region landmarks

The following example shows how a generic "region" landmark might be added to a weather portlet. There is no existing text on the page that can be referenced as the label, so it is labelled with aria-label.

```html
<div role="region" aria-label="weather portlet"> 
  ...
</div>
```

### Example 3: Providing a label for Math

Below is an example of a MathML function, using the math role, appropriate label, and MathML rendering:

```html
<div role="math" aria-label="6 divided by 4 equals 1.5">
  <math xmlns="https://www.w3.org/1998/Math/MathML">
    <mfrac>
      <mn>6</mn>
      <mn>4</mn>
    </mfrac>
      <mo>=</mo>
      <mn>1.5</mn>
  </math>
</div>
```

## Related Resources

No endorsement implied.

* [HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam-1.0/)
* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)

## Related Techniques

* [ARIA16: Using aria-labelledby to provide a name for user interface controls](../aria/ARIA16)
* [H44: Using label elements to associate text labels with form controls](../html/H44)

## Tests

### Procedure

For each element where a aria-label attribute is present.

1. Examine whether the text description accurately labels the object or provides a description of its purpose or provides equivalent information.

### Expected Results

* #1 is true.
