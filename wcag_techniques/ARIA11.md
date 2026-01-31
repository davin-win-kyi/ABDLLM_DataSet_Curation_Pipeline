# Technique ARIA11: Using ARIA landmarks to identify regions of a page

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient)
* [1.3.6: Identify Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-purpose) (Sufficient)
* [2.4.1: Bypass Blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks) (Sufficient when used for grouping blocks of repeated material in a way that can be skipped)

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to provide programmatic access to sections of a web page. Landmark roles (or "landmarks") programmatically identify sections of a page. Landmarks help assistive technology (AT) users orient themselves to a page and help them navigate easily to various sections of a page.

They also provide an easy way for users of assistive technology to skip over blocks of content that are repeated on multiple pages and notify them of programmatic structure of a page. For instance, if there is a common navigation menu found on every page, landmark roles (or "landmarks") can be used to skip over it and navigate from section to section. This will save assistive technology users and keyboard users the trouble and time of tabbing through a large amount of content to find what they are really after, much like a traditional "skip links" mechanism. (Refer to User Agent Notes above for specifics of AT support). A blind user who may be familiar with a news site's menu, and is only interested in getting to the top story could easily navigate to the "main" landmark, and bypass dozens of menu links. In another circumstance, a user who is blind may want to quickly find a navigation menu, and can do so by jumping to the navigation landmark.

Landmarks also can help sighted keyboard-only users navigate to sections of a page using a [browser plugin](https://www.tpgi.com/improving-access-to-landmark-navigation/).

Landmarks are inserted into the page using the role attribute on an element that marks the section. The value of the attribute designates the type of landmark. These role values are listed below. For HTML mappings of landmark roles, refer to the Rules of ARIA attribute usage by HTML element table in the [ARIA In HTML recommendation](https://www.w3.org/TR/html-aria/).

* banner: A region that contains mostly site-oriented content, such as the logo or a site-specific search tool.
* navigation: A region that contains navigation links to other pages or different parts of the same page.
* main: A region that contains a page's main content.
* region: A region that contains a perceivable section of the page containing content that is sufficiently important for users to be able to navigate to the section. A region landmark isn't exposed as a landmark region unless it has an accessible name, often provided using aria-label or aria-labelledby.
* form: A region of the document that represents a collection of form-associated elements, some of which can represent editable values that can be submitted to a server for processing. A form landmark isn't exposed as a landmark region unless it has an accessible name.
* search: A region of the page containing search functionality.
* complementary: Any section of the document that supports the main content, yet is separate and meaningful on its own.
* contentinfo: A region that contains information about the parent document such as copyrights and links to privacy statements.

There are cases when a particular landmark role could be used more than once on a page, such as on primary and secondary blocks of navigation. In these cases, identical roles should be named using a valid technique for labeling regions.

Landmarks should supplement native semantic markup such as HTML headings, lists and other structural markup. Landmarks are interpretable by WAI-ARIA-aware assistive technologies and are not exposed by browsers directly to users.

It is a best practice to include all content on the page in landmarks, so that screen reader users who rely on them to navigate from section to section do not lose track of content.

## Examples

### Example 1: Simple landmarks

The following example shows how landmarks might be added to an HTML document:

```html
<div role="banner">site logo and name, etc. here</div>
<div role="search">search functionality here</div>
<div role="navigation">a list of navigation links here</div>
<div role="form">a sign-up form here</div>
<div role="main">the page's main content here</div>
<div role="region">a sponsor's promotion here</div>
<div role="complementary">sidebar content here</div>
<div role="contentinfo"> site contact details, copyright information, etc. here </div>
```

### Example 2: Multiple landmarks of the same type and aria-labelledby

The following example shows a best practice of how landmarks might be added to an HTML document in situations where there are two or more of the same type of landmark on the same page. For instance, if a navigation role is used multiple times on a page, each instance may have a unique label specified using aria-labelledby:

```html
<div aria-labelledby="site-nav-heading" role="navigation">
  <h2 id="site-nav-heading">Site</h2>
    <ul>
      <li><a href="...">nav link 1</a></li>  
      <li><a href="...">nav link 2</a></li>
      <li><a href="...">nav link 3</a></li>
   </ul>
</div>
<div aria-labelledby="related-nav-heading" role="navigation">
  <h2 id="related-nav-heading">Related Topics</h2>
    <ul>
      <li><a href="...">topic link 1</a></li>
      <li><a href="...">topic link 2</a></li>
      <li><a href="...">topic link 3</a></li>
    </ul>
</div>
```

### Example 3: Multiple landmarks of the same type and aria-label

The following example shows a best practice of how landmarks might be added to an HTML document in situations where there are two or more of the same type of landmark on the same page, and there is no existing text on the page that can be referenced as the label:

```html
<div aria-label="Site" role="navigation">
   <ul>
      <li><a href="...">nav link 1</a></li>
      <li><a href="...">nav link 2</a></li>
      <li><a href="...">nav link 3</a></li>
   </ul>
</div>
<div aria-label="Tags" role="navigation">
   <ul>
      <li><a href="...">tag link 1</a></li>
      <li><a href="...">tag link 2</a></li>
      <li><a href="...">tag link 3</a></li>
   </ul>
</div>
```

### Example 4: Search form

The following example shows a search form with a "search" landmark. The search role typically goes on the form element or a div surrounding the form:

```html
<form role="search">
   <label for="product-search" id="search-label">Search</label>
   <input id="product-search" placeholder="title, author, or ISBN" type="text">
   <button type="submit">Find Books</button>
</form>
```

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices, Landmark Regions](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/)
* [W3C Web Accessibility Tutorials, Page Regions](https://www.w3.org/WAI/tutorials/page-structure/regions/)
* [Accessible Rich Internet Applications (WAI-ARIA), Landmark Roles](https://www.w3.org/TR/wai-aria/#landmark_roles)
* [Improving access to landmark navigation](https://www.tpgi.com/improving-access-to-landmark-navigation/)
* [Landmarks browser extension](https://matatk.agrip.org.uk/landmarks/)

## Related Techniques

* [G1: Adding a link at the top of each page that goes directly to the main content area](../general/G1)
* [G124: Adding links at the top of the page to each area of the content](../general/G124)
* [ARIA13: Using aria-labelledby to name regions and landmarks](../aria/ARIA13)
* [ARIA20: Using the region role to identify a region of the page](../aria/ARIA20)
* [H69: Providing heading elements at the beginning of each section of content](../html/H69)
* [H100: Providing properly marked up email and password inputs](../html/H100)
* [SCR28: Using an expandable and collapsible menu to bypass block of content](../client-side-script/SCR28)

## Tests

### Procedure

1. Examine each element with a [landmark role](https://www.w3.org/TR/wai-aria/#landmark_roles).
2. Examine whether the correct element has been used to mark up content. For example: a navigation role has been used to mark up a section with navigation links, or the main role is used to contain the page's main content.
3. If a landmark region needs to have an accessible name to be exposed as a landmark, check to see that there is an accessible name.
4. If the same type of landmark appears multiple times on the page, check that each one is given a unique and meaningful accessible name.

### Expected Results

* #1, #2, #3, and #4 are true.
