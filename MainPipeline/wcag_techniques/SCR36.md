# Technique SCR36: Providing a mechanism to allow users to display moving, scrolling, or auto-updating text in a static window or area

## About this Technique

This technique relates to [2.2.1: Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable) (Sufficient).

This technique applies to any technology that moves, blinks, or updates text and can create a static block of text.

## Description

Some web pages display scrolling text because there is limited space available. Scrolling the text in a small text window makes the content available for users who can read quickly enough, but causes problems for users who read more slowly or use assistive technology. This technique provides a mechanism to stop the movement and make the entire block of text available statically. The text may be made available in a separate window or in a (larger) section of the page. Users can then read the text at their own speed.

This technique does not apply when the text that is moving can not be displayed all at once on the screen (e.g., a long chat conversation).

Note

This technique can be used in combination with a style switching technique to present a page that is a [conforming alternate version](https://www.w3.org/TR/WCAG22/#dfn-conforming-alternate-versions) for non-conforming content. Refer to [C29: Using a style switcher to provide a conforming alternate version](../css/C29) and [Understanding Conforming Alternate Versions](https://www.w3.org/WAI/WCAG22/Understanding/conformance#conforming-alt-versions) for more information.

## Examples

### Example 1: Expanding Scrolling Text in Place

A large block of text is scrolled through a small marquee area of the page. A button lets the user stop the scrolling and display the entire block of text.

Note

This code example requires that both CSS and JavaScript be turned on and available.

#### The CSS component

```css
#scrollContainer {
  background-color: darkblue;
  left: 10px;
  overflow: hidden;
  top: 50px;
  visibility: visible;
}

.scrolling {
  height: 50px;
  position: absolute;
  width: 200px;
}

.notscrolling {
  margin:10px;
  width: 500px;
}

#scrollingText {
  color: white;
  top: 0px;
}

.scrolling #scrollingText {
  position: absolute;
}
```

#### The script and HTML content:

```html
<script>
var tid;
function init() {
  var st = document.getElementById('scrollingText');
  st.style.top = '0px';
  initScrolling();
}

function initScrolling () {
  tid = setInterval('scrollText()', 300);
}
	
function scrollText () {
  var st = document.getElementById('scrollingText');
  if (parseInt(st.style.top) > (st.offsetHeight*(-1) + 8)) {
    st.style.top = (parseInt(st.style.top) - 5) + 'px';
  }
  else {
    var sc = document.getElementById('scrollContainer');
    st.style.top = parseInt(sc.offsetHeight) + 8 + 'px';
  }
}

function toggle() {
  var scr = document.getElementById('scrollContainer');
  if (scr.className == 'scrolling') {
    scr.className = 'notscrolling';
    clearInterval(tid);
    document.getElementById('scrollButton').value="Shrink";
  }
  else {
    scr.className = 'scrolling';
    initScrolling();
    document.getElementById('scrollButton').value="Expand";
  }
}

<input type="button" id="scrollButton" value="Expand" onclick="toggle()">
<div id="scrollContainer" class="scrolling">
  <div id="scrollingText" class="on">
    ... Text to be scrolled ...
  </div>
</div>
...
```

Working example of this code: [Expanding Scrolling Text in Place](../../working-examples/script-scroll-text-expand/).

## Related Techniques

* [G4: Allowing the content to be paused and restarted from where it was paused](../general/G4)
* [SCR33: Using script to scroll content, and providing a mechanism to pause it](../client-side-script/SCR33)
* [SCR22: Using scripts to control blinking and stop it in five seconds or less](../client-side-script/SCR22)
