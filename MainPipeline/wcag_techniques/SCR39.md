# Technique SCR39: Making content on focus or hover hoverable, dismissible, and persistent

## About this Technique

This technique relates to [1.4.13: Content on Hover or Focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus) (Sufficient).

This technique applies to any technology that supports the display of additional content on pointer hover.

## Description

Additional content that is displayed when a user moves the pointer over a trigger or moves the keyboard focus to the trigger (for example, a pop-up) must remain visible to allow users time to read and interact with the content and must allow the user to move the pointer over the additional content.

Low vision users who magnify their screens often see only a small part of the screen at a time (their viewport). This means that the additional content may not be fully visible in the current viewport and users may need to move their mouse over the additional content to read it. web authors should therefore ensue that additional content stays visible when the pointer moves away from the trigger to the (mostly adjacent) additional content. additional content should also be dismissible without moving the focus, so that users can read content covered by the additional content.

## Examples

### Example 1: Content preview for links

When hovering over or focusing on a link, a content preview for the link appears just above or below that link. Users can move the pointer over the additional content (pop-up) so that they can fully read the additional content. Pressing the Esc key dismisses (closes) the additional content.

#### HTML of example 1

```html
<p>This is the 
   <a class="a-and-tooltip" id="parent" href="index.html">trigger
   <span id="popup" role="tooltip">And this additional text 
    gives additional context on the trigger term
   </span>
  </a>.
   Text and popup are <strong>in one link (a)</strong> element.
</p>
```

#### CSS of example 1

```css
[role="tooltip"] {
  display: none;
  padding: 0.5em;
  background:white;
  color: black;
  border:solid black 2px;
  width:10em;
}

.a-and-tooltip {
  position: relative;
}

[role="tooltip"] {
  position: absolute;
  left:0;
  top:1em;
}
```

#### JavaScript of example 1

```javascript
// trigger and popup inside the same link

var parent = document.getElementById("parent");

parent.onmouseover = function() {
  document.getElementById("popup").style.display = "block";
}

parent.onmouseout = function() {
  document.getElementById("popup").style.display = "none";
}

parent.onfocus = function() {
  document.getElementById("popup").style.display = "block";
}

parent.onblur = function() {
  document.getElementById("popup").style.display = "none";
}

// hide when ESC is pressed

document.addEventListener("keydown", (e) => {
  if ((e.keyCode || e.which) === 27)
    document.getElementById("popup").style.display = "none";
});
```

[Working example of content on hover or focus](../../working-examples/script-hoverable/)

## Tests

### Procedure

For additional content that appears on hover check that:

1. The pointer can be moved over the additional content without the additional content disappearing.
2. The additional content stays visible and does not automatically close after a time.
3. The content can be closed without moving the pointer way from the trigger. Either by pressing Esc, by pressing another documented keyboard shortcut, or by activating the trigger.

For additional content that appears on focus check that:

1. The additional content stays visible and does not automatically close after a time.
2. The content can be closed without moving the focus way from the trigger. Either by pressing Esc, by pressing another other documented keyboard shortcut, or by activating the trigger.

### Expected Results

For content that appears on hover:

* #1, #2 and #3 are true.

For content that appears on focus:

* #1 and #2 are true.
