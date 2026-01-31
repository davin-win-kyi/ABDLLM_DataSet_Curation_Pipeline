# Technique PDF21: Using List tags for lists in PDF documents

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable).

This technique applies to tagged PDF documents with lists.

## Description

The intent of this technique is to create lists of related items using list elements appropriate for their purposes. PDF files containing lists are normally created or repaired using a tool for authoring PDF.

When markup is used that visually formats items as a list but does not indicate the list relationship, users may have difficulty navigating the information. An example of such visual formatting is simply using line-breaks to separate list items.

Some assistive technologies allow users to navigate from list to list or item to item. If the lists are not correctly formatted with list tags, these users will have difficulty understanding the list content.

The easiest way to create lists in PDF content is to format them properly using list markup in the authoring tool, for example, Microsoft Word or OpenOffice Writer. However, if you do not have access to the source file and authoring tool, you can use Acrobat Pro's Reading Order tool and the Tags panel.

The structure types for lists in PDF documents are:

* L - the List tag, which contains one or more LI tags.
* LI - the List Item tag. List item tags can contain Lbl and LBody tags.
* Lbl - the list item label. Contains distinguishing information such as a item number or bullet character.
* LBody - the list item body. Contains list item content, or in the case of a nested list, it may contain additional List tag trees.

## Examples

### Example 1: Adding lists to Microsoft Word documents

This example is shown with Microsoft Word. There are other software tools that perform similar functions.

On the Home ribbon, use the lists tools to create or repair lists in Word documents. This is the easiest way to ensure that lists are formatted correctly when they are converted to PDF.

### Example 2: Adding lists to OpenOffice Writer documents

This example is shown with OpenOffice Writer. There are other software tools that perform similar functions.

Use the Bullets and Numbering tool to create or repair lists in OpenOffice Writer documents. This is the easiest way to ensure that lists are formatted correctly when they are converted to PDF.

### Example 3: Ensuring that lists are correctly formatted using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. View → Navigation Panels... → Accessibility Tags
2. Inspect the lists in the document to determine which, if any, are not formatted properly.

In the following image, the third list is formatted as text. The list items are separated only by line-breaks. Assistive technology may not be able to render the list intelligibly for users.

To repair the list, use the Tags panel to create list tags in the content.

The following image shows the resulting first list item correctly formatted.

This example, with two list items not nested inside the list element, is shown in the [working example of ensuring lists are properly formatted](../../working-examples/pdf-lists/lists.pdf).

## Related Resources

No endorsement implied.

* Section 14.8.4.3.3 (List Elements) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G115: Using semantic elements to mark up structure](../general/G115)

## Tests

### Procedure

1. For a list in a PDF document, verify in one of the following ways:

### Expected Results

* #1 is true
