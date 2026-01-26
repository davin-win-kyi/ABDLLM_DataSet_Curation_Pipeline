# Technique SCR14: Using scripts to make nonessential alerts optional

## About this Technique

This technique relates to:

* [2.2.4: Interruptions](https://www.w3.org/WAI/WCAG22/Understanding/interruptions) (Sufficient)
* [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Advisory)

This technique applies to scripting technologies which use scripting alerts for non-emergency communication.

## Description

The objective of this technique is to toggle announcements to screen readers of changes in a stock-price alert component. By default, when the stock price changes, the change is announced by screen readers. This could be annoying to some users, so there are buttons to allow users to toggle the announcements on or off.

This technique uses the aria-live property to turn the stock component into a live region and the aria-atomic property to tell screen readers to announce all of the component's content rather than just what was updated when the stock is updated. For the sake of this demo, the stock updates every 10 seconds. If announcements are turned on, the aria-live property is set to assertive; if announcements are turned off, the aria-live property is set to off. The two buttons used to control the announcements use the aria-pressed property, updated to either true or false, to inform screen reader users which button is pressed and therefore whether their screen reader will announce the stock updates or not. In a real-life situation, an author should consider setting a cookie (or equivalent) to store the user's preference so that it's set over multiple visits to the page.

## Examples

### Example 1: Updating screen reader settings for stock price update alerts

The script below will update a stock value in an aria-live component every 10 seconds. If the user presses the "Turn Announcements Off" button, their screen reader will stop making announcements when the stock value changes; if they press the "Turn Announcements On" button, the announcements will start again.

#### The JavaScript

```html
<script>
document.addEventListener("DOMContentLoaded", function (e) {
  const stockBox = document.querySelector("#stock-box");
  const stockMovement = document.querySelector("#stock-movement");
  const onBtn = document.querySelector("#live-on");
  const offBtn = document.querySelector("#live-off"); 
  const stocks = new Array("stock went down", "stock stayed the same", "stock went up");
  let loopCount = 0;	
		
  onBtn.addEventListener("click", modifyLive, false);
  offBtn.addEventListener("click", modifyLive, false);
		
  function modifyLive(e){
    let elm = e.currentTarget;
    let liveState = elm.getAttribute("id");
    if (liveState === "live-off"){
      stockBox.setAttribute("aria-live", "off");
      onBtn.setAttribute("aria-pressed", "false");
      offBtn.setAttribute("aria-pressed", "true");
    }
    else{
      stockBox.setAttribute("aria-live", "assertive");
      onBtn.setAttribute("aria-pressed", "true");
      offBtn.setAttribute("aria-pressed", "false");      
    }
  }
		
  setInterval(() => {
    if(loopCount >2){
      loopCount = 0;
    }
    stockMovement.innerHTML = stocks[loopCount];
      loopCount++;
    }, 10000)
  });
</script>
```

#### The HTML

```html
<body>
  <h1>Turbo Encabulator Stock Information</h1>	
  <div id="stock-box" aria-atomic="true" aria-live="assertive">
    <span>Turbo Encabulator Stock Price: </span>
    <span id="stock-movement">stock went up</span>
  </div>
  <p>Use the buttons to toggle screen reader announcements of stock changes:</p>
  <div>
    <button aria-pressed="true" id="live-on" type="button">
     Turn Announcements On</button>
    <button aria-pressed="false" id="live-off" type="button">
     Turn Announcements Off</button>
  </div>
</body>
```

Working example of this code: [Demonstration of toggling ARIA alerts](../../working-examples/script-toggle-aria-alerts/).

## Tests

### Procedure

For a web page that supports non-emergency interruptions:

1. Load the web page and verify that no non-emergency alerts are displayed.
2. Verify there is a mechanism to activate and deactivate the non-emergency interruptions.

### Expected Results

* For a web page that supports non-emergency interruptions, checks #1 and #2 are true.
