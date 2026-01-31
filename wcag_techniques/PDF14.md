# Technique PDF14: Providing running headers and footers in PDF documents

## About this Technique

This technique relates to:

* [2.4.8: Location](https://www.w3.org/WAI/WCAG22/Understanding/location) (Advisory)
* [3.2.3: Consistent Navigation](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation) (Advisory)

This technique applies to tagged PDF documents.

## Description

The objective of this technique is to help users locate themselves in a document by providing running headers and footers via pagination artifacts. This is normally accomplished using a tool for authoring PDF.

Running headers and footers help make content easier to use and understandable by providing repeated information in a consistent and predictable way. The content of headers and footers will vary widely depending on the document scope and content, the audience, and design decisions. Some examples of location information that may be used in headers and footers are listed below. Whether the information appears in a header or a footer is often a design decision; page numbers often appear in footers but they may alternatively appear in headers.

* Document title
* Current chapter and/or section in the document
* Page numbers with location information such as, "Page 3-4" or "Page 9 of 15."
* Author and/or date information.

Consistency helps users with cognitive limitations, screen-reader users and low-vision magnifier users, and users with intellectual disabilities understand content more readily.

The easiest way to provide page headers and footers is in the authoring tool for the document. Authoring tools typically provide features for creating header and footer text and information (such as page numbers). However, if after converting your document to PDF, you need to add or modify page headers and footers, authoring or repair tools like Adobe Acrobat Pro's Header & Footer tools can be used. In all cases, the tools generate page headers and footers in consistent and predictable layout, format, and text.

## Examples

### Example 1: Adding running headers and footers using Microsoft Word

This example is shown with Microsoft Word. There are other software tools that perform similar functions.

In Microsoft Word, use the Header and Footer tools in the Insert ribbon. When the Word document is converted into a PDF, the headers and footers will be tagged as pagination artifacts.

This example is shown in operation in the [working example of adding running headers using Word (Word file)](../../working-examples/pdf-headers-footers/headers-footers-word.docx) and [working example of adding running headers using Word (PDF file)](../../working-examples/pdf-headers-footers/headers-footers-word.pdf).

### Example 2: Adding running headers and footers using OpenOffice Writer

This example is shown with OpenOffice Writer. There are other software tools that perform similar functions.

In OpenOffice Writer, use the Insert → Header and Insert → Footer tools, which allow you to specify header and footer information and layout, as shown in the following images.

When converted to PDF, the page headers and footers appear in the document as they do in the converted Word document in Example 1.

This example is shown in operation in the [working example of adding running headers using OpenOffice Writer (OpenOffice file)](../../working-examples/pdf-headers-footers/headers-footers.odt) and [working example of adding running headers using OpenOffice Writer (PDF file)](../../working-examples/pdf-headers-footers/headers-footers-oo.pdf).

### Example 3: Adding running headers and footers to PDF documents using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

In Adobe Acrobat Pro, you can add or modify headers and footers:

1. Select the Edit PDF tool.
2. In the newly-opened Edit PDF toolbar, select Header & Footer → Add.
3. In the Add Header and Footer tool, specify text and formats for headers and footers in your document.
4. Use the Previews to make sure the text, fonts, and layout are as you want them for your document.

The image below shows Acrobat Pro's Add Header and Footer tool.

## Related Resources

No endorsement implied.

* Section 14.8.2.2 (Real Content and Artifacts) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G61: Presenting repeated components in the same relative order each time they appear](../general/G61)
* [PDF9: Providing headings by marking content with heading tags in PDF documents](../pdf/PDF9)
* [PDF2: Creating bookmarks in PDF documents](../pdf/PDF2)

## Tests

### Procedure

1. Check that running headers and/or footers are provided and contain information to help users locate themselves within the document (such as page numbers or chapter numbers).
2. If section headers are used in the running header or footer, check that the section header and the running header or footer are consistent.

### Expected Results

* #1 and #2 are true.
