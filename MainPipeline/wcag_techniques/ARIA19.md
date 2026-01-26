# Technique ARIA19: Using ARIA role=alert or Live Regions to Identify Errors

## About this Technique

This technique relates to:

* [3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) (Sufficient)
* [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Sufficient using a more specific technique)

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to notify Assistive Technologies (AT) when an input error occurs. The aria-live attribute makes it possible for an AT (such as a screen reader) to be notified when error messages are injected into a Live Region container. The content within the aria-live region is automatically read by the AT, without the AT having to focus on the place where the text is displayed.

There are also a number of [special case live region roles](https://www.w3.org/TR/wai-aria/#live_region_roles) which can be used instead of applying live region properties directly.

## Examples

### Example 1: Injecting error messages into a container with role=alert already present in the DOM

The following example uses role=alert which is equivalent to using aria-live=assertive.

In the example there is an empty error message container element with aria-atomic=true and an aria-live property or alert role present in the DOM on page load. The error container must be present in the DOM on page load for the error message to be spoken by most screen readers. aria-atomic=true is necessary to make Voiceover on iOS read the error messages after more than one invalid submission.

jQuery is used to test if the inputs are empty on submit and inject error messages into the live region containers if so. Each time a new submit is attempted the previous error messages are removed from the container and new error messages injected.

```javascript
$(document).ready(function(e) {
  $('#signup').submit(function() {
    $('#errors').html('');
    if ($('#first').val() === '') {
      $('#errors').append('<p>Please enter your first name.</p>');
    }
    if ($('#last').val() === '') {
      $('#errors').append('<p>Please enter your last name.</p>');
    } 
    if ($('#email').val() === '') {
      $('#errors').append('<p>Please enter your email address.</p>');
    }
    return false;
  });
});
<form name="signup" id="signup">
  <p id="errors" role="alert" aria-atomic="true"></p>
  <div>
    <label for="first">First Name (required)</label><br>
    <input type="text" name="first" id="first">
  </div>
  <div>
    <label for="last">Last Name (required)</label><br>
    <input type="text" name="last" id="last">
  </div>
  <div>
    <label for="email">Email (required)</label><br>
    <input type="text" name="email" id="email">
  </div>
  <div>
    <input type="submit" name="button" id="button" value="Submit">
  </div>
 </form>
```

Working example: [Using role=alert to identify errors](../../working-examples/aria-alert-identify-errors/).

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
* [HTML5 Accessibility Chops: ARIA role=alert browser support](https://www.paciellogroup.com/blog/2012/06/html5-accessibility-chops-aria-rolealert-browser-support/)
* [WAI-ARIA, Supported States and Properties, aria-describedby](https://www.w3.org/TR/wai-aria/#aria-describedby)
* [WAI-ARIA, The Roles model, alert](https://www.w3.org/TR/wai-aria/#alert)

## Tests

### Procedure

1. Determine that an empty error container with role=alert or aria-live=assertive attribute is present in the DOM at page load.
2. Trigger the error that causes the content in the live region to appear or update.
3. Determine that the error message was injected into the already present error container.

### Expected Results

* #1 and #3 are true.
