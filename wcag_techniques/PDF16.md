# Technique PDF16: Setting the default language using the /Lang entry in the document catalog of a PDF document

## About this Technique

This technique relates to [3.1.1: Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page) (Sufficient).

This technique applies to tagged PDF documents.

## Description

The objective of this technique is to specify a document's default language by setting the /Lang entry in the document catalog. This is normally accomplished using a tool for authoring PDF.

Both assistive technologies and conventional user agents can render text more accurately when the language of the document is identified. Screen readers can load the correct pronunciation rules. Visual browsers can display characters and scripts correctly. Media players can show captions correctly. As a result, users with disabilities are better able to understand the content.

## Examples

### Example 1: Adding a /Lang entry to specify the default document language using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Open the document in Adobe Acrobat Pro
2. From the File menu, select "Properties..."
3. In the "Properties" dialog, select the "Advanced" tab
4. In the "Reading Options" field, select the default language from the "Language" combo box

Note

Acrobat includes numerous preset language selections. If you need to specify a language that is not on the list, such as Russian, you must type the ISO 639-2 code for the language, not its name.

### Example 2: Specifying the default document language in a PDF document using a /Lang entry

The natural language used for text in a document is determined in a hierarchical fashion, based on whether an optional /Lang entry is present in any of several possible locations. At the highest level, the document's default language may be specified by a /Lang entry in the document catalog.

The following code fragment illustrates code that is typical for using the /Lang entry in the document catalog for a document's default language (in this case English). (This is typically accomplished by an authoring tool.)

```
1 0 obj
   << /Type /Catalog
      ...
      /Lang (en)
      ...
   >> 
 endobj
```

## Related Resources

No endorsement implied.

* Section 14.9.2 (Natural Language Specification) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [ISO 639-2 Codes](https://www.loc.gov/standards/iso639-2/php/code_list.php)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [PDF19: Specifying the language for a passage or phrase with the Lang entry in PDF documents](../pdf/PDF19)

## Tests

### Procedure

1. Verify that the default language for the document is correctly specified by applying one of the following:

### Expected Results

* #1 is true.
