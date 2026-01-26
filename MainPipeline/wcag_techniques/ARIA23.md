# Technique ARIA23: Using role=log to identify sequential information updates

## About this Technique

This technique relates to [4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages) (Sufficient).

This technique applies to content using [WAI- ARIA](https://www.w3.org/TR/wai-aria/).

## Description

The purpose of this technique is to notify Assistive Technologies (AT) when content has been appended to sequential information concerning the application's history or logs. The aria live region role of log has an implicit aria-live value of polite and aria-atomic value of false, which allows a user to be notified via AT (such as a screen reader) when log messages are added. The new content within the aria-live region is automatically read by the AT, without the AT having to focus on the place where the text is displayed. See [WAI-ARIA 1.1 log (role)](https://www.w3.org/TR/wai-aria-1.1/#log) for more details.

## Examples

### Example 1: Updating the contents of a chat conversation

Comments that users type into a chat input field are appended to the end of the chat history region. The region is marked with role of log so that new additions are announced by ATs. When each new chat message appears, a screen reader should announce its content (depending on AT/browser compatibility).

```html
<div id="chatRegion" role="log" aria-labelledby="chatHeading">
  <h4 id="chatHeading">Chat History</h4>
  <ul id="conversation">
    <li>The latest chat message</li>
  </ul>
</div>
```

[Working example: using role="log" with chat conversation](../../working-examples/aria-role-log/chatlog.html)

### Example 2: Updating the log of a server

An application log records time-stamped activities. The log is exposed in the app as a view, with the region marked with the role of log so that the new additions are announced by the ATs. (The default value for the aria-relevant attribute is "additions", so the removal of the old top entries due to log size limitations will not be announced.) When each new log entry is added, a screen reader announces it.

```html
<div id="activityLog" role="log">
  <h4 id="logHeading">Recent activity</h4>
  <ul id="logentries"">
    <li>08:03 UserX logged off</li>
  </ul>
</div>
```

[Working example: using role="log" with server log](../../working-examples/aria-role-log/serverlog.html)

## Tests

### Procedure

On a page that contains sequentially updating information:

1. Check that the container for the information is given a role of log.

### Expected Results

* #1 is true.
