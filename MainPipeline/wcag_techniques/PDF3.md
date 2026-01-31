# Technique PDF3: Ensuring correct tab and reading order in PDF documents

## About this Technique

This technique relates to:

* [1.3.2: Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence) (Sufficient)
* [2.1.1: Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard) (Sufficient when used for ensuring keyboard control)
* [2.4.3: Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order) (Sufficient when used for giving focus to elements in an order that follows sequences and relationships within the content)

This technique applies to tagged PDF documents.

## Description

The intent of this technique is to ensure that users can navigate through content in a logical order that is consistent with the meaning of the content. Correct tab and reading order is typically accomplished using a tool for authoring PDF.

For sighted users, the logical order of PDF content is also the visual order on the screen. For keyboard and assistive technology users, the tab order through content, including interactive elements (form fields and links), determines the order in which these users can navigate the content. The tab order must reflect the logical order of the document.

Logical structure is created when a document is saved as tagged PDF. The reading order of a PDF document is determined primarily by the tag order of document elements, including interactive elements, but the order of content within individual tags is determined by the PDF document's content tree structure.

If the reading order is not correct, keyboard and assistive technology users may not be able to understand the content. For example, some documents use multiple columns, and the reading order is clear visually to sighted users as flowing from the top to the bottom of the first column, then to the top of the next column. But if the document is not properly tagged, a screen reader may read the document from top to bottom, across both columns, interpreting them as one column.

The simplest way to ensure correct reading order is to structure the document correctly in the authoring tool used to create the document, before conversion to tagged PDF. Note, however, that pages with complex layouts with graphics, tables, footnotes, side-bars, form fields, and other elements may not convert to tagged PDF in the correct reading order. These inconsistencies must then be corrected with repair tools such as Acrobat Pro.

When a PDF document containing form fields has a correct reading order, all form fields are contained in the tab order in the appropriate order, and in the correct order relative to other content in the PDF. Common tab-order errors include:

* Form fields missing from the tagged content.
* Form fields in the wrong location in the PDF content; e.g., at the end of non-interactive content.

## Examples

### Example 1: Creating a 2-column document using Microsoft Word

This example is shown with Microsoft Word. There are other software tools that perform similar functions.

Multi-column documents created using Word's Layout → Columns tool typically are in the correct reading order when converted to tagged PDF. The following image shows Word's Columns tool.

This example is shown in operation in the [working example of 2-column document (Word file)](../../working-examples/pdf-reading-order/reading-order-2cols-word.docx) and [working example of 2-column document using Word (PDF file)](../../working-examples/pdf-reading-order/reading-order-2cols-word.pdf).

### Example 2: Creating a 2-column document using OpenOffice Writer

This example is shown with OpenOffice Writer. There are other software tools that perform similar functions.

Multi-column documents created using OpenOffice Writer's Columns tool typically are in the correct reading order when converted to tagged PDF. The image below shows Writer's Columns tool. The Columns tool can be found under Format.

This example is shown in operation in the [working example of 2-column document using OpenOffice Writer (OpenOffice file)](../../working-examples/pdf-reading-order/reading-order-2cols-oo.odt) and [working example of 2-column document using OpenOffice Writer (PDF file)](../../working-examples/pdf-reading-order/reading-order-2cols-oo.pdf).

### Example 3: Setting the tab order for one or more pages using Adobe Acrobat Pro

In a tagged PDF document:

1. Open Organize Pages tool.
2. Select one or more page thumbnails.
3. Right-click to access the context menu for the selected thumbnail(s) and select Page Properties.
4. Select the Tab Order tab in the Page Properties dialog.
5. If needed, select a tab order option:

This example is shown in operation in the [working example of setting the tab order (Word file)](../../working-examples/pdf-reading-order/reading-order.docx) and [working example of setting the tab order (PDF file)](../../working-examples/pdf-reading-order/reading-order.pdf).

### Example 4: Repairing the reading order using the Tags panel in Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

Use the Tags panel to correct the reading order. Either:

* Drag and drop a tag to its required position, or
* Cut a tag and paste it to its required position.

## Related Resources

No endorsement implied.

* Section 14.8 (Tagged PDF) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Acrobat and Accessibility](https://webaim.org/techniques/acrobat/acrobat)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G57: Ordering the content in a meaningful sequence](../general/G57)
* [G59: Placing the interactive elements in an order that follows sequences and relationships within the content](../general/G59)
* [G202: Ensuring keyboard control for all functionality](../general/G202)

## Tests

### Procedure

1. Verify that the content is in the correct reading order by one of the following:
2. Verify that the tab order is correct for focusable content by one of the following:

### Expected Results

* #1 and Check #2 are true.
