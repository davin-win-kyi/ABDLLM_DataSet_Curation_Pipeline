# Technique ARIA7: Using aria-labelledby for link purpose

## About this Technique

This technique relates to [2.4.4: Link Purpose (In Context)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context) (Sufficient when used for identifying the purpose of a link using link text combined with programmatically determined link context).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

With the aria-labelledby attribute, authors can use a visible text element on the page as a label for a focusable element (a form control or a link). For example, a "read more..." link could be associated with the text of the heading of the preceding section to make the purpose of the link unambiguous (see example 1).

When associating text to a focusable element with the help of aria-labelledby, the target text element is given an id which is referenced in the value of the aria-labelledby attribute of the focusable element.

It is also possible to use several text elements on the page as a label for a focusable element. Each of the text elements used must be given a unique ID which is referenced as a string of ids (IDREF) in the value of the aria-labelledby attribute. The label text should then be concatenated following the order of ids in the value of the aria-labelledby attribute.

When applied on links, aria-labelledby can be used to identify the purpose of a link that may be readily apparent for sighted users, but less obvious for screen reader users.

The specified behavior of aria-labelledby is that the associated label text is announced instead of the link text (not in addition to the link text). When the link text itself should be included in the label text, the ID of the link should be referenced as well in the string of IDs forming the value of the aria-labelledby attribute.

For more information on the naming hierarchy please consult the [Accessible Name and Description Computation](https://www.w3.org/TR/accname/).

## Examples

### Example 1: Providing additional information for links

This example will mean that the link text as shown on screen is then used as the start of the accessible name for the link. Screen readers will announce this as: "Read more ...Storms hit east coast" and will display that same text in the links list which is very useful for screen reader users who may browse by links.

```html
<h2 id="headline">Storms hit east coast</h2>
<p>Torrential rain and gale force winds have struck the east coast, 
   causing flooding in many coastal towns.
  <a id="p123" href="news.html" aria-labelledby="p123 headline">Read more...</a>
</p>
```

### Example 2: Concatenating link text from multiple sources

There may be cases where an author will place a tag around a section of code that will be referenced.

```html
<p>Download <span id="report-title">2012 Sales Report</span>:
   <a aria-labelledby="report-title pdf" href="#" id="pdf">PDF</a> |
   <a aria-labelledby="report-title doc" href="#" id="doc">Word</a> |
   <a aria-labelledby="report-title ppt" href="#" id="ppt">PowerPoint</a>
</p>
```

## Related Resources

No endorsement implied.

* [Accessible Name and Description Computation](https://www.w3.org/TR/accname/)

## Tests

### Procedure

For each link that has an aria-labelledby attribute:

1. Check that each id in the value of the aria-labelledby attribute matches an id of a text element used as part of the link purpose.
2. Check that the combined value of the text referenced by the one or more ids in the aria-labelledby attribute properly describes the purpose of the link element.

### Expected Results

* Checks #1 and #2 are true.
