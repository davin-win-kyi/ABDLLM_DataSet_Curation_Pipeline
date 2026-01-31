# Technique PDF2: Creating bookmarks in PDF documents

## About this Technique

This technique relates to [2.4.5: Multiple Ways](https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways) (Advisory).

This technique applies to tagged PDF documents.

## Description

The intent of this technique is to make it possible for users to locate content using bookmarks (outline entries in an Outline dictionary) in long documents.

A person with cognitive disabilities may prefer a hierarchical outline that provides an overview of the document rather than reading and traversing through many pages. This is also a conventional means of navigating a document that benefits all users.

## Examples

### Example 1: Converting a table of contents created with Microsoft Word to bookmarks in a PDF

This example is shown with Microsoft Word and Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Create a table of contents at the beginning of the Word document.
2. Use Save as... → PDF to convert the Word document to PDF.

The table-of-contents entries in the converted document will be linked to the headings in the document. In addition, the headings will appear as PDF Bookmarks in the Acrobat navigation pane.

If the document provides a glossary and/or index, these sections should have headings that appear in the table of contents (and thus as bookmarks in the Navigation pane). The table of contents also should be marked up with a heading so it is bookmarked as well.

If this markup has not been done in the authoring tool, Adobe Acrobat Pro can be used to provide the tags. See [PDF9](../pdf/PDF9) if you need to modify converted headings or add new ones.

This example is shown in operation in the [working example of creating bookmarks with Word](../../working-examples/pdf-bookmarks/bookmarks.docx).

### Example 2: Converting a table of contents created with OpenOffice and Writer to bookmarks in a PDF

This example is shown with OpenOffice Writer and Adobe Acrobat Pro and Reader. There are other software tools that perform similar functions.

1. Using the Styles and Formatting dialog found in the Format option, or by press F11, select the text to appear in the table of contents and then select a Heading.

The table-of-contents entries in the converted document will be linked to the headings in the document, and will appear as PDF Bookmarks in the left-hand Navigation pane. The OpenOffice.org Table of Contents and Bookmarks look the same as they appeared in Example 1.

This example is shown in operation in the [working example of creating bookmarks with OpenOffice Writer](../../working-examples/pdf-bookmarks/bookmarks.odt).

### Example 3: Adding bookmarks using Adobe Acrobat Pro after conversion

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

After conversion to tagged PDF, you may decide to add bookmarks that were not automatically generated. Like the converted bookmarks, tagged bookmarks use the underlying structural information in the document.

1. In the Bookmarks panel, choose the options menu, then choose New Bookmarks From Structure...
2. From the Structure Elements dialog, select the elements you want specified as tagged bookmarks.
3. The tagged bookmarks are nested under a new, untitled bookmark. Access the context menu for the new bookmark and select the Rename option to rename the new bookmark.

This example is shown in operation in the [working example of creating bookmarks with Acrobat Pro](../../working-examples/pdf-bookmarks/bookmarks.pdf).

### Example 4: Creating bookmarks with the outline hierarchy

The following code fragment illustrates part of an outline hierarchy used to create bookmarks This is typically accomplished by an authoring tool.

```
121 0 obj
  << /Type /Outlines
    /First 22 0 R
    /Last 29 0 R
    /Count 6
  >>
endobj
22 0 obj
  << /Title (Applying Guerrilla Tactics to Usability Testing by People with Disabilities)
    /Parent 21 0 R
    /Next 29 0 R
    /First 25 0 R
    /Last 28 0 R
    /Count 4
    /Dest [3 0 R /XYZ 0 792 0]
  >>
endobj
25 0 obj
  << /Title (Getting started)
    /Parent 22 0 R
    /Next 26 0 R
    /Dest [3 0 R /XYZ null 701 null]
  >>
endobj
```

## Related Resources

No endorsement implied.

* Section 12.3.3 (Document Outline) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Acrobat and Accessibility](https://webaim.org/techniques/acrobat/acrobat)

## Related Techniques

* [G64: Providing a Table of Contents](../general/G64)

## Tests

### Procedure

1. Check that the Bookmarks panel displays bookmarks.
2. Check that the bookmarks link to the correct sections in the document.

### Expected Results

* Check #1 and Check #2 are true.
