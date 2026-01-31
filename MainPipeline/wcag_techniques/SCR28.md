# Technique SCR28: Using an expandable and collapsible menu to bypass block of content

## About this Technique

This technique relates to [2.4.1: Bypass Blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks) (Sufficient when used for grouping blocks of repeated material in a way that can be skipped).

This technique applies to technologies that provide client side scripting.

## Description

This technique allows users to skip repeated material by placing that material in a menu that can be expanded or collapsed under user control. The user can skip the repeated material by collapsing the menu. The user invokes a user interface control to hide or remove the elements of the menu. The resources section lists several techniques for menus, toolbars and trees, any of which can be used to provide a mechanism for skipping navigation.

Note

Similar approaches can be implemented using server-side scripting and reloading a modified version of the web page.

## Examples

### Example 1: Toggling a table of contents

The table of contents for a set of web pages is repeated near the beginning of each web page. A button at the beginning of the table of contents lets the user remove or restore it on the page.

```html
...
<script>
let tocToggle = document.querySelector(".toc-toggle");
let toc = document.querySelector("#toc");
tocToggle.addEventListener("click", toggle, false);

function toggle(e){
  let elm = e.currentTarget;
  if(elm.getAttribute("aria-expanded") === "false"){
    elm.setAttribute("aria-expanded", "true");
  }
  else{
    elm.setAttribute("aria-expanded", "false");
  }
}
</script>

...

<button aria-controls="toc" aria-expanded="true" class="toc-toggle" type="button">
  Toggle Table Of Contents
</button>
<nav aria-labelledby="toc-header" id="toc">
  <h2 id="toc-header">Table of Contents</h2>
  <ul>
    <li><a href="#sec1">Section 1</a></li>
    <li><a href="#sec2">Section 2</a></li>
    <li><a href="#sec3">Section 3</a></li>
    <li><a href="#sec4">Section 4</a></li>
  </ul>
</nav>
...
```

Working example of this code: [Toggle table of contents with a button](../../working-examples/script-toggle-toc-button/).

## Related Resources

No endorsement implied.

* [ARIA - Disclosure (Show/Hide) pattern.](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)

## Related Techniques

* [H69: Providing heading elements at the beginning of each section of content](../html/H69)

## Tests

### Procedure

1. Check that some user interface control allows the repeated content to be expanded or collapsed.
2. Check that when the content is expanded, it is included in the programmatically determined content at a logical place in the reading order.
3. Check that when the content is collapsed, it is not part of the programmatically determined content.

### Expected Results

* All checks above are true.

## Test Rules

The following are Test Rules related to this Technique. It is not necessary to use these particular Test Rules to check for conformance with WCAG, but they are defined and approved test methods. For information on using Test Rules, see [Understanding Test Rules for WCAG Success Criteria](https://www.w3.org/WAI/WCAG22/Understanding/understanding-act-rules.html).

* [Block of repeated content is collapsible](/WAI/standards-guidelines/act/rules/3e12e1/proposed/)
* [Bypass Blocks of Repeated Content](/WAI/standards-guidelines/act/rules/cf77f2/proposed/)
