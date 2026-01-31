# Technique SVR5: Specifying the default language in the HTTP header

## About this Technique

This technique relates to [3.1.1: Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page) (Advisory).

This technique applies to server-side technologies, including server-side scripting languages and server configuration files for setting HTTP headers.

## Description

The objective of this technique is to provide information on the primary language or languages in a web page, in order to identify the audience of the content. The Content-Language HTTP header can contain a list of one or more language codes, which can be used for language negotiation between a user agent and a server. If the language preferences in a user agent are set correctly, language negotiation can help the user to find a language version of the content that suits their preferences.

Note that the Content-Language HTTP header does not serve to identify the language used for processing the content. The content processing language can be identified by means of other techniques, such as the attributes lang and xml:lang in markup languages.

This technique ensures that the primary language of the document, as specified for example in the lang or xml:lang attribute, is listed in the Content-Language HTTP header.

## Examples

### Example 1: Setting content language in Java Servlet and JSP

In Java Servlet or JavaServer Pages (JSP), developers can use response.setHeader("Content-Language", lang), in which "lang" stands for a language tag (for example, "en" for English):

```java
...
public void doGet(HttpServletRequest request, HttpServletResponse response)
  throws ServletException, IOException {
   ...
   response.setHeader("Content-Language", "en");
   PrintWriter out = response.getWriter();
   ...
}
```

### Example 2: Setting content language in PHP

In PHP, developers can send a raw HTTP header with the header method. The following example sets the language to French:

```php
<?php header('Content-language: fr'); ... ?>
```

## Related Resources

No endorsement implied.

* [W3C Internationalization FAQ: HTTP and meta for language information](https://www.w3.org/International/questions/qa-http-and-lang)
* [Declaring metadata about the language(s) of the intended audience](https://www.w3.org/TR/2014/NOTE-i18n-html-tech-lang-20140603/#metadata) in Authoring HTML: Language declarations - W3C Working Group Note 3 June 2014.
* [RFC 9110, 8.5. Content-Language](https://www.rfc-editor.org/rfc/rfc9110#field.content-language)
* [PHP header](https://php.net/manual/en/function.header.php).

## Related Techniques

* [H57: Using the language attribute on the HTML element](../html/H57)

## Tests

### Procedure

1. Use a Live HTTP Header viewer to find the value of the Content-Language header.
2. Check that this value matches the default language of the web page.

### Expected Results

* Step #2 is true.
