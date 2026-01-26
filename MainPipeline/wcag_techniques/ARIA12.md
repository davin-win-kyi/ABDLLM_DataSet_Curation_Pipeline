# Technique ARIA12: Using role=heading to identify headings

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to provide a way for Assistive Technologies (AT) to identify a piece of content as a heading. Applying role="heading" to an element causes an AT (like a screen reader) to treat it as though it were a heading. The role="heading" property must be paired with the aria-level property to define the heading level.

When possible, [use native heading markup](https://www.w3.org/TR/using-aria/#rule1). For example, it is preferable to use an h1 element, rather than using <div role="heading" aria-level="1">. Native HTML elements have implicit styling and features that won't necessarily be replicated with ARIA equivalents. For instance, heading elements will have specific styling adjustments made when viewing a page in a browser's Reader Mode. Whereas a <div role="heading" aria-level="1"> will not be styled as a heading, because the underlying element is a div. ARIA only modifies the way an element is exposed to assistive technology, it does nothing to change the implicit style or functionality of the element it is applied to.

## Examples

### Example 1: Simple headings

This example demonstrates how to implement headings using role="heading" and aria-level.

```html
<div role="heading" aria-level="2">Global News Items</div>
... a list of global news with editorial comment....
   
<div role="heading" aria-level="3">Politics</div>
... a list of global political news stories ...
```

### Example 2: Additional heading levels

This example demonstrates how to implement a level 7 heading using role="heading" and the aria-level attribute. Since HTML only supports headings up to level 6, there is no native element to provide these semantics.

```html
<h5>Fruit Trees</h5>
<h6>Apples</h6>
<p>Apples grow on trees in areas known as orchards...</p>
   ...
<div role="heading" aria-level="7">Jonagold</div>
<p>Jonagold is a cross between the Golden Delicious and Jonathan varieties...</p>
```

Headings with an aria-level of 10 or higher can create difficulties for users. At the time of writing (2024), most combinations of user agents and assistive technologies report such levels as being level 2.

## Related Resources

No endorsement implied.

* [Accessible Rich Internet Applications (WAI-ARIA), heading role.](https://www.w3.org/TR/wai-aria/#heading)
* [Accessible Rich Internet Applications (WAI-ARIA), aria-level property.](https://www.w3.org/TR/wai-aria/#aria-level)
* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML, the h1 , h2 , h3 , h4 , h5 , and h6 elements](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements).

## Related Techniques

* [H42: Using h1-h6 to identify headings](../html/H42)
* [H69: Providing heading elements at the beginning of each section of content](../html/H69)
* [G141: Organizing a page using headings](../general/G141)
* [F2: Failure of Success Criterion 1.3.1 due to using changes in text presentation to convey information without using the appropriate markup or text](../failures/F2)

## Tests

### Procedure

1. Examine each element with the attribute role="heading".
2. Determine whether the content of the element is appropriate as a heading.
3. Determine whether the aria-level value is the appropriate hierarchical level.

### Expected Results

* #2 and #3 are true.
