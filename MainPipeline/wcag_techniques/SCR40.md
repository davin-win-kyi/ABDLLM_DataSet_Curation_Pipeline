# Technique SCR40: Using the CSS prefers-reduced-motion query in JavaScript to prevent motion

## About this Technique

This technique relates to [2.3.3: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions) (Sufficient).

This technique applies to javaScript animation which causes motion that is triggered by user interactions.

## Description

The objective of this technique is to allow users to prevent animations (including motion animations) from being displayed on web pages, by using JavaScript to evaluate the prefers-reduced-motion CSS Media Query.

Some users experience distraction or nausea from animated content. For example, if scrolling a page causes elements to move (other than the essential movement associated with scrolling the content, which is under the user's control) it can trigger vestibular disorders.

Media queries that selectively enable/disable JavaScript-driven animations based on operating system or user agent preferences allow users to avoid those triggers.

The understanding document for [Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html#resources) includes links for changing the 'reduced motion' setting.

## Examples

### Example 1: Evaluating the prefers-reduced-motion CSS Media Query in JavaScript

Users can indicate their motion preference for interfaces in their system. This choice can be detected in JavaScript by evaluating the prefers-reduced-motion CSS Media Query. The script can then decide to enable or disable animation effects based on the result of the media query test.

```js
const mediaQueryList = window.matchMedia("(prefers-reduced-motion: no-preference)");

if (mediaQueryList.matches) {
  /* The user has not expressed a preference for reduced motion – run JavaScript-based animation */
}
```

## Tests

### Procedure

For each interactive element that triggers a motion animation as a result of a user interaction:

1. Enable the reduced motion setting in your system;
2. Check that the motion animation is essential;
3. Check that the motion animation is suppressed.

### Expected Results

* #2 or #3 is true.
