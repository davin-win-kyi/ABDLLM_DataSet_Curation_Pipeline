# Technique SCR33: Using script to scroll content, and providing a mechanism to pause it

## About this Technique

This technique relates to:

* [2.2.1: Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable) (Sufficient)
* [2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) (Sufficient)

This technique applies to technologies that support script-controlled scrolling of content.

## Description

The objective of this technique is to provide a way for users to stop scrolling content when the scrolling is created by a script. Scrolling content can be difficult or impossible to read by users with low vision or with cognitive disabilities. The movement can also be distracting for some people making it difficult for them to concentrate on other parts of the web page.

## Examples

### Example 1

In this example CSS and JavaScript are used to visually present some text in a scrolling format. A link is included to pause the scrolling movement.

This implementation will display the full text and omit the link when JavaScript or CSS are unsupported or inactive.

#### The HTML component

```html
...
<div id="scroller">
  <p id="tag">This text will scroll and a Pause/Scroll link will be present 
  when JavaScript and CSS are supported and active.</p>
</div>
...
```

#### The CSS component

```css
...
body {
  font:1em verdana,sans-serif;
  color:#000;
  margin:0
}

#scroller {
  position:relative;
  overflow:hidden;
  width:15em;
  border:1px solid #008080;
}
  
#tag {
  margin:2px 0;
}

#testP {
  visibility:hidden;
  position:absolute;
  white-space:nowrap;
} 

 #top {
  width:350px;
  margin:auto;
}
...
```

#### The JavaScript component

```javascript
var speed=50        // speed of scroller
var step=3          // smoothness of movement
var StartActionText= "Scroll"  // Text for start link
var StopActionText = "Pause"   // Text for stop link
 
var x, scroll, divW, sText=""
 
function onclickIE(idAttr,handler,call){
  if ((document.all)&&(document.getElementById)){idAttr[handler]="Javascript:"+call}
}
 
function addLink(id,call,txt){
  var e=document.createElement('a');
  e.setAttribute('href',call);
  var linktext=document.createTextNode(txt);
  e.appendChild(linktext);
  document.getElementById(id).appendChild(e);
}
 
function getElementStyle() {
  var elem = document.getElementById('scroller');
  if (elem.currentStyle) {
    return elem.currentStyle.overflow;
  }
  else if (window.getComputedStyle) {
    var compStyle = window.getComputedStyle(elem, '');
    return compStyle.getPropertyValue("overflow");
  }
  return "";
}

function addControls(){
  
  // test for CSS support first 
  // test for the overlow property value set in style element or external file
  if (getElementStyle()=="hidden") {
    var f=document.createElement('div');
    f.setAttribute('id','controls');
    document.getElementById('scroller').parentNode.appendChild(f);
    addLink('controls','Javascript:clickAction(0)',StopActionText);
    onclickIE(document.getElementById('controls').childNodes[0],"href",'clickAction(0)');
    document.getElementById('controls').style.display='block';
  }
}
 
function stopScroller(){clearTimeout(scroll)}
  
function setAction(callvalue,txt){
  var c=document.getElementById('controls')
  c.childNodes[0].setAttribute('href','Javascript:clickAction('+callvalue+')')
    onclickIE(document.getElementById('controls').childNodes[0],"href",'clickAction

  ('+callvalue+')')
  c.childNodes[0].firstChild.nodeValue=txt
}

function clickAction(no){
  switch(no) {
    case 0:
      stopScroller();
      setAction(1,StartActionText);
      break;
    case 1:
      startScroller();
      setAction(0,StopActionText);
  }
}

function startScroller(){
  document.getElementById('tag').style.whiteSpace='nowrap'
  var p=document.createElement('p')
  p.id='testP'
  p.style.fontSize='25%' //fix for mozilla. multiply by 4 before using
  x-=step
  if (document.getElementById('tag').className) p.className=document.getElementById

  ('tag').className
    p.appendChild(document.createTextNode(sText))
    document.body.appendChild(p)
    pw=p.offsetWidth
    document.body.removeChild(p)
    if (x<(pw*4)*-1){x=divW}
    document.getElementById('tag').style.left=x+'px'
    scroll=setTimeout('startScroller()',speed)
}
  
function initScroller(){
  if (document.getElementById && document.createElement && document.body.appendChild) {
    addControls();
    divW=document.getElementById('scroller').offsetWidth;
    x=divW;
    document.getElementById('tag').style.position='relative';
    document.getElementById('tag').style.left=divW+'px';
    var ss=document.getElementById('tag').childNodes;
    for (i=0;i<ss.length;i++) {sText+=ss[i].nodeValue+" "};
    scroll=setTimeout('startScroller()',speed);
  }
}
  
function addLoadEvent(func) {
  if (!document.getElementById | !document.getElementsByTagName) return
  var oldonload = window.onload
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload()
      func()
    }
  }
}
  
addLoadEvent(initScroller)
```

A working example of this code, [Example of using script to scroll content and providing a mechanism to pause it](../../working-examples/script-scroll-pause/), is available.

## Related Techniques

* [G4: Allowing the content to be paused and restarted from where it was paused](../general/G4)

## Tests

### Procedure

1. Check that a mechanism is provided to pause the scrolling content.
2. Use the pause mechanism to pause the scrolling content.
3. Check that the scrolling has stopped and does not restart by itself.
4. Check that a mechanism is provided to restart the paused content.
5. Use the restart mechanism provided to restart the scrolling content.
6. Check that the scrolling has resumed from the point where it was stopped.

### Expected Results

* Checks #3 and #6 are true.
