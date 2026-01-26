# Technique SVR1: Implementing automatic redirects on the server side instead of on the
	client side

## About this Technique

This technique relates to [3.2.5: Change on Request](https://www.w3.org/WAI/WCAG22/Understanding/change-on-request) (Sufficient).

This technique applies to server-side technologies, including server-side scripting languages and server configuration files with URLs or URL patterns for redirects.

## Description

The objective of this technique is to avoid confusion that may be caused when two new pages are loaded in quick succession because one page (the one requested by the user) redirects to another. Some user agents support the use of the HTML meta element to redirect the user to another page after a specified number of seconds. This makes a page inaccessible to some users, especially users with screen readers. Server-side technologies provide methods to implement redirects in a way that does not confuse users. A server-side script or configuration file can cause the server to send an appropriate HTTP response with a status code in the 3xx range and a Location header with another URL. When the browser receives this response, the location bar changes and the browser makes a request with the new URL.

## Examples

### Example 1: JSP/Servlets

In Java Servlets or JavaServer Pages (JSP), developers can use HttpServletResponse.sendRedirect(String url).

```java
...
public void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
  ...
  response.sendRedirect("/newUserLogin.do");
}
```

This sends a response with a 302 status code ("Found") and a Location header with the new URL to the user agent. It is also possible to set another status code with response.sendError(int code, String message) with one of the constants defined in the interface javax.servlet.http.HttpServletResponse as status code.

```java
...
public void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
  ...
  response.sendError(response.SC_MOVED_PERMANENTLY, "/newUserLogin.do");
}
```

If an application uses HttpServletResponse.encodeURL(String url) for URL rewriting because the application depends on sessions, the method HttpServletResponse.encodeRedirectURL(String url) should be used instead of HttpServletResponse.sendRedirect(String url). It is also possible to rewrite a URL with HttpServletResponse.encodeURL(String url) and then pass this URL to HttpServletResponse.sendRedirect(String url).

### Example 2: ASP

In Active Server Page (ASP) with VBScript, developers can use Response.Redirect.

```vbnet
Response.Redirect "newUserLogin.asp"
```

or

```vbnet
Response.Redirect("newUserLogin.asp")
```

The code below is a more complete example with a specific HTTP status code.

```vbnet
Response.Clear
Response.Status = 301
Response.AddHeader "Location", "newUserLogin.asp"
Response.Flush
Response.End
```

### Example 3: PHP

In PHP, developers can send a raw HTTP header with the header method. The code below sends a 301 status code and a new location. If the status is not explicitly set, the redirect response sends an HTTP status code 302.

```php
<?php
header("HTTP/1.1 301 Moved Permanently");
header("Location: https://www.example.com/newUserLogin.php");
?>
```

### Example 4: Apache

Developers can configure the Apache web server to handle redirects, as in the following example.

```apache
redirect 301 /oldUserLogin.jsp https://www.example.com/newUserLogin.do
```

## Related Resources

No endorsement implied.

* [Use standard redirects: do not break the back button!](https://www.w3.org/QA/Tips/reback) (W3C QA Tip).
* [RFC 9110: HTTP Semantics 15.4. Redirection 3xx](https://www.rfc-editor.org/rfc/rfc9110#name-redirection-3xx).
* [Interface javax.servlet.http.HttpServletResponse](https://docs.oracle.com/javaee/6/api/javax/servlet/http/HttpServletResponse.html) in the Java Servlets 6 API documentation.
* [PHP header](https://www.php.net/manual/en/function.header.php).
* [Apache Module mod_alias](https://httpd.apache.org/docs/current/mod/mod_alias.html) in the [Apache HTTP Server Version 2.4 Documentation](https://httpd.apache.org/docs/current/) describes how redirects can be specified in Apache 2.4.

## Tests

### Procedure

1. Find each link or programmatic reference to another page or web page.
2. For each link or programmatic reference to a URI in the set of web pages being evaluated, check if the referenced web page contains code (e.g., meta element or script) that causes a client-side redirect.
3. For each link or programmatic reference to a URI in the set of web pages being evaluated, check if the referenced URI does not cause a redirect OR causes a server-side redirect without a time-out.

### Expected Results

* Check #2 is false and check #3 is true.
