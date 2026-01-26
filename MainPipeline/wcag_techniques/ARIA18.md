# Technique ARIA18: Using aria-alertdialog to Identify Errors

## About this Technique

This technique relates to:

* [3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) (Sufficient)
* [3.3.3: Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion) (Sufficient)
* [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Advisory)

This technique applies to technologies that support [Accessible Rich Internet Applications (WAI-ARIA)](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to alert people that an input error has occurred. Using role="alertdialog" creates a notification. This notification should be modal with the following characteristics:

* aria-label or aria-labelledby attribute gives the alertdialog an accessible name.
* The alertdialog contains at least one focusable element, and the focus should move to that element when the alertdialog opens.
* The tab order is constrained within the alertdialog whilst it is open.
* When the alertdialog is dismissed, the focus moves back to the position it had before the alertdialog opened, if possible.

Note that the alertdialog should not be present in a way that it will be accessed by assistive technology until it is needed. One way to do this is not to include it in the static HTML and instead to insert it into the DOM via script when the error condition is triggered. The insertion would correspond to the following HTML sample.

## Examples

### Example 1: Alert dialog

This example shows how a notification using role="alertdialog" can be used to notify someone they have entered invalid information.

```html
<div role="alertdialog" aria-labelledby="alertHeading">
  <h1 id="alertHeading">Error</h1>
  <p>Employee's Birth Date is after their hire date.
   Please verify the birth date and hire date.</p>
  <button>Save and Continue</button>
  <button>Return to page and correct error</button>
</div>
```

Working example: [Alert dialog](../../working-examples/aria-alertdialog-identify-errors/).

## Related Resources

No endorsement implied.

* [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)

## Tests

### Procedure

1. Trigger the error that causes the alertdialog to appear.
2. Determine that the alertdialog contains at least one focusable element, and the focus moves to that element when the alertdialog opens.
3. Determine that the tab order is constrained within the alertdialog while it is open, and when the alertdialog is dismissed, the focus moves back to the position it had before the alertdialog opened, if possible.
4. Examine the element with alertdialog applied.
5. Determine that either the aria-label or aria-labelledby attribute has been correctly used to give the alertdialog an accessible name.
6. Determine that the contents of the alertdialog identifies the input error.
7. Determine whether contents of the alertdialog suggests how to fix the error.

### Expected Results

* Checks #2, #3, #5 and #6 are true. For Success Criterion 3.3.3, check #7 is also true.
