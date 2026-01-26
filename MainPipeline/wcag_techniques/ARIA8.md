# Technique ARIA8: Using aria-label for link purpose

## About this Technique

This technique relates to:

* [2.4.4: Link Purpose (In Context)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context) (Sufficient when used for identifying the purpose of a link using link text combined with programmatically determined link context)
* [2.4.9: Link Purpose (Link Only)](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-link-only) (Sufficient)

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The objective of this technique is to describe the purpose of a link using the aria-label attribute. The aria-label attribute provides a way to place a descriptive text label on an object, such as a link, when there are no elements visible on the page that describe the object. If descriptive elements are visible on the page, the aria-labelledby attribute should be used instead of aria-label. Providing a descriptive text label lets a user distinguish the link from links in the web page that lead to other destinations and helps the user determine whether to follow the link. In some assistive technologies the aria-label value will show in the list of links instead of the actual link text.

Per the [Accessible Name and Description Computation](https://www.w3.org/TR/accname/) and the [Accessible Name and Description Computation](https://www.w3.org/TR/html-aam-1.0/#accessible-name-and-description-computation) in the HTML Accessibility API Mappings 1.0, the aria-label text will override the text supplied within the link. As such the text supplied will be used instead of the link text by assistive technology. Due to this it is recommended to start the text used in aria-label with the text used within the link. This will allow consistent communication between users.

## Examples

### Example 1: Describing the purpose of a link in HTML using aria-label.

In some situations, designers may choose to lessen the visual appearance of links on a page by using shorter, repeated link text such as "read more". These situations provide a good use case for aria-label in that the simpler, non-descriptive "read more" text on the page can be replaced with a more descriptive label of the link. The words "read more" are repeated in the aria-label (which replaces the original anchor text of "Read more") to allow consistent communication between users.

Note

The Success Criterion [2.5.3 Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name) requires that the visible label is included as part of the 'accessible name', which is generally set by the aria-label. The examples below meet this requirement.

```html
<h4>Neighborhood News</h4>
<p>Seminole tax hike: Seminole city managers are proposing a 75% increase in 
  property taxes for the coming fiscal year.
  <a href="taxhike.html" aria-label="Read more about Seminole tax hike">
   Read more</a>
</p> 
  
<p>Baby Mayor: Seminole voters elect the city's youngest mayor ever by voting
   in 3 year old Willy "Dusty" Williams in yesterday's mayoral election.
   <a href="babymayor.html" aria-label="Read more about Seminole's new baby mayor">
    Read more</a>
</p>
```

## Related Resources

No endorsement implied.

* [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/)
* [Accessible Name and Description Computation](https://www.w3.org/TR/accname/)

## Related Techniques

* [ARIA6: Using aria-label to provide labels for objects](../aria/ARIA6)
* [ARIA14: Using aria-label to provide an accessible name where a visible label cannot be used](../aria/ARIA14)
* [ARIA7: Using aria-labelledby for link purpose](../aria/ARIA7)
* [G91: Providing link text that describes the purpose of a link](../general/G91)
* [H30: Providing link text that describes the purpose of a link for anchor elements](../html/H30)

## Tests

### Procedure

For link elements that use aria-label:

1. Check that the value of the aria-label attribute properly describes the purpose of the link element.

### Expected Results

* #1 is true.
