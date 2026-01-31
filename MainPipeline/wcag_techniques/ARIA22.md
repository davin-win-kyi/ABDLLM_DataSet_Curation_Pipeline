# Technique ARIA22: Using role=status to present status messages

## About this Technique

This technique relates to:

* [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Sufficient using a more specific technique)
* [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Sufficient, together with [G193: Providing help by an assistant in the web page](../general/G193))

This technique applies to content using [WAI- ARIA](https://www.w3.org/TR/wai-aria/).

## Description

This technique uses the status role from the ARIA specification to notify Assistive Technologies (AT) when content has been updated with information about the user's or application's status. This is done by adding role="status" to the element that contains the [status message](https://www.w3.org/TR/WCAG22/#dfn-status-messages). The aria live region role of status has an implicit aria-live value of polite, which allows a user to be notified via AT (such as a screen reader) when status messages are added. The role of status also has a default aria-atomic value of true, so that updates to the container marked with a role of status will result in the AT presenting the entire contents of the container to the user, including any author-defined labels (or additional nested elements). Such additional context can be critical where the status message text alone will not provide an equivalent to the visual experience. The content of the aria-live container is automatically read by the AT, without the AT having to focus on the place where the text is displayed. See [WAI-ARIA status (role)](https://www.w3.org/TR/wai-aria/#status) for more details.

Note that since role="status" is currently not treated as atomic by default in some environments, it is advisable to add an explicit aria-atomic="true" if the entire contents of the container should be announced.

## Examples

### Example 1: Including a search results message

After a user presses a Search button, the page content is updated to include the results of the search, which are displayed in a section below the Search button. The change to content also includes the message "5 results returned" near the top of this new content. This text is given an appropriate role for a status message. A screen reader will announce "5 results returned".

```html
<div role="status" aria-atomic="true">5 results returned.</div>
```

[Working example: role=status on search results](../../working-examples/aria-role-status-searchresults/)

### Example 2: Updating the shopping cart status

After a user presses an Add to Shopping Cart button, content near the Shopping Cart icon updates to read "1 items". The container for this text (in this case a <p>) is marked with the role of status. Because it adds visual context, the shopping cart image — with succinct and accurate alt text — is also placed in the container. Due to the aria-atomic value, a screen reader will announce "Shopping cart, six items".

```html
<p role="status" aria-atomic="true">
  <img src="shopping-cart.png" alt="Shopping Cart">
  <span id="cart">0</span> items
</p>
```

[Working example: role=status on a shopping cart](../../working-examples/aria-role-status-shoppingcart/)

## Tests

### Procedure

For each [status message](https://www.w3.org/TR/WCAG22/#dfn-status-messages):

1. Check that the container destined to hold the status message has a role attribute with a value of status before the status message occurs.
2. Check that when the status message is triggered, it is inside the container.
3. Check that elements or attributes that provide information equivalent to the visual experience for the status message (such as a shopping cart image with proper alt text) also reside in the container.

### Expected Results

* #1, #2 and #3 are true.
