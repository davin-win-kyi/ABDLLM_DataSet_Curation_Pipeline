# Technique SCR31: Using script to change the background color or border of the element with focus

## About this Technique

This technique relates to [2.4.7: Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible) (Sufficient).

This technique applies to HTML CSS, script.

## Description

This purpose of this technique is to allow the author to use JavaScript to apply CSS, in order to make the focus indicator more visible than it would ordinarily be. When an element receives focus, the background color or border is changed to make it visually distinct. When the element loses focus, it returns to its normal styling. This technique can be used on any HTML user agent that supports Script and CSS, regardless of whether it supports the :focus pseudo class.

## Examples

### Example 1

In this example, when the link receives focus, its background turns yellow. When it loses focus, the yellow is removed. Note that if the link had a background color to begin with, you would use that color rather than "" in the script.

```html
<script>function toggleFocus(el) {
  el.style.backgroundColor =  el.style.backgroundColor=="yellow" ? "inherit" : "yellow";
}
</script>
...
<a href="example.html" 
 onfocus="toggleFocus(this)" onblur="toggleFocus(this)">focus me</a>
...
```

## Related Techniques

* [C15: Using CSS to change the presentation of a user interface component when it receives focus](../css/C15)

## Tests

### Procedure

1. Tab to each element in the page
2. Check that the focus indicator is visible

### Expected Results

* Step #2 is true
