# Technique PDF18: Specifying the document title using the Title entry in the document information dictionary of a PDF document

## About this Technique

This technique relates to [2.4.2: Page Titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled) (Sufficient when used with [G88: Providing descriptive titles for web pages](../general/G88)).

This technique applies to tagged PDF documents.

## Description

The intent of this technique is to show how a descriptive title for a PDF document can be specified for assistive technology by using the /Title entry in the document information dictionary and by setting the DisplayDocTitle flag to True in a viewer preferences dictionary. This is typically accomplished by using a tool for authoring PDF.

Document titles identify the current location without requiring users to read or interpret page content. User agents make the title of the page easily available to the user for identifying the page. For instance, a user agent may display the page title in the window title bar or as the name of the tab containing the page.

## Examples

### Example 1: Setting the document title in the metadata and specifying that the title be displayed in the title bar using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

Open the PDF document in Adobe Acrobat Pro:

1. Select File → Properties
2. Select the Description tab to view the metadata in the document, including the document information dictionary
3. Modify the Title field to add or change the document's Title entry

Note that, with Adobe Acrobat installed, you can also enter and read the data properties information from the desktop. Access the file's context menu, choose Properties, and select the PDF tab. Any information you type or edit in this dialog box also appears in the Document Properties Description when you open the file.

To display the document title in the title bar of a user agent:

1. Select File → Properties
2. Select the Initial View tab
3. In the Window Options section, select Document Title in the Show pull-down list.

The title is now displayed in the title bar.

### Example 2: A /Title entry in the document information dictionary of a PDF document

The following code fragment illustrates code that is typical for providing a /Title entry in a document information dictionary that contains a document title.

```
1 0 obj   
  << /Title (Applying Guerrilla Tactics to Usability Testing by People with Disabilities)    
    /Author (Mary Smith) 
    /CreationDate (D:19970915110347-08'00')    
  >>   
endobj
```

## Related Resources

No endorsement implied.

* Section 14.3.3 (Document Information Dictionary) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G88: Providing descriptive titles for web pages](../general/G88)

## Tests

### Procedure

1. Verify that the title for the document is correctly specified and displayed in the user agent title bar by applying one of the following:

### Expected Results

* #1 is true.
