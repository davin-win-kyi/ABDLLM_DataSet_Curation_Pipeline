# Technique SCR16: Providing a script that warns the user a time limit is about to expire

## About this Technique

This technique relates to [2.2.1: Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable) (Sufficient, together with [SCR1: Allowing the user to extend the default time limit](../client-side-script/SCR1)).

This technique applies to time limits exist that are controlled by script.

## Description

The objective of this technique is to notify users that they are almost out of time to complete an interaction. When scripts provide functionality that has time limits, the script can include functionality to warn the user of imminent time limits and provide a mechanism to request more time. 20 seconds or more before the time limit occurs, the script provides a confirm dialog that states that a time limit is imminent and asks if the user needs more time. If the user answers "yes" then the time limit is reset. If the user answers "no" or does not respond, the time limit is allowed to expire.

This technique involves time limits set with the window.setTimeout() method. If, for example, the time limit is set to expire in 60 seconds, you can set the time limit for 40 seconds and provide the confirm dialog. When the confirm dialog appears, a new time limit is set for the remaining 20 seconds. Upon expiry of the "grace period time limit" the action that would have been taken at the expiry of the 60 second time limit in the original design is taken.

## Examples

### Example 1

A page of stock market quotes uses script to refresh the page every five minutes in order to ensure the latest statistics remain available. 20 seconds before the five minute period expires, a confirm dialog appears asking if the user needs more time before the page refreshes. This allows the user to be aware of the impending refresh and to avoid it if desired.

```html
<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8">
   <title>Stock Market Quotes</title>
   <script>
     function timeControl() {
     // set timer for 4 min 40 sec, then ask user to confirm.
     setTimeout('userCheck()', 280000);
     }

     function userCheck() {
     // set page refresh for 20 sec
     var id=setTimeout('pageReload()', 20000);
     // If user selects "OK" the timer is reset 
     // else the page will refresh from the server.
     if (confirm("This page is set to refresh in 20 seconds. 
       Would you like more time?"))
       {
          clearTimeout(id);
          timeControl();
       }
     }

     function pageReload() {
       window.location.reload(true);
     }

    timeControl();
  </script>
</head>
<body>
   <h1>Stock Market Quotes</h1>
   ...
</body>
</html>
```

## Related Techniques

* [SCR1: Allowing the user to extend the default time limit](../client-side-script/SCR1)

## Tests

### Procedure

On a web page that has a time limit controlled by a script:

1. Load the page and start a timer that is 20 seconds less than the time limit.
2. When the timer expires, check that a confirmation dialog is displayed warning of the impending time limit.

### Expected Results

* #2 is true.
