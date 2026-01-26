# Technique ARIA13: Using aria-labelledby to name regions and landmarks

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to provide names for regions of a page that can be read by assistive technology. The aria-labelledby attribute provides a way to associate a section of the page marked up as a region or landmarks with text that is on the page that labels it.

Landmark roles (or "landmarks") programmatically identify sections of a page. Landmarks help assistive technology (AT) users orient themselves to a page and help them navigate easily to various sections of a page.

Like aria-describedby, aria-labelledby can accept multiple ids to point to other regions of the page using a space separated list. It is also limited to ids for defining these sets.

## Examples

### Example 1: Identify a landmark with on-page text

Below is an example of aria-labelledby used on a complementary Landmark. The region of the document to which the heading pertains could be marked with the aria-labelledby property containing the value of the id for the header.

```html
<div role="complementary" aria-labelledby="hdr1">
  <h1 id="hdr1">Top News Stories</h1>
  ...
</div>
```

### Example 2: Identification for Application landmarks

The following code snippet for application landmarks with static prose. If you have a regional landmark of type application and static descriptive text is available, then on the application landmark, include an aria-describedby reference to associate the application and the static text as shown here:

```html
<div role="application" aria-labelledby="p123" aria-describedby="info">
   <h1 id="p123">Calendar<h1>
   <p id="info">This calendar shows the game schedule for the Boston Red Sox.</p>
   <div role="grid">
    ...
   </div>
</div>
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/)

## Related Techniques

* [ARIA10: Using aria-labelledby to provide a text alternative for non-text content](../aria/ARIA10)
* [ARIA6: Using aria-label to provide labels for objects](../aria/ARIA6)
* [ARIA9: Using aria-labelledby to concatenate a label from several text nodes](../aria/ARIA9)
* [ARIA16: Using aria-labelledby to provide a name for user interface controls](../aria/ARIA16)
* [ARIA7: Using aria-labelledby for link purpose](../aria/ARIA7)
* [G92: Providing long description for non-text content that serves the same purpose and presents the same information](../general/G92)

## Tests

### Procedure

1. Examine each element with attribute role=region or with a [landmark role](https://www.w3.org/TR/wai-aria/#landmark_roles), where an aria-labelledby attribute is also present.
2. Check that the value of the aria-labelledby attribute is the id of an element on the page.
3. Check that the text of the element with that id accurately labels the section of the page.

### Expected Results

* #2 and #3 are true.
