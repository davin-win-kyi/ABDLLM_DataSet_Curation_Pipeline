# Technique PDF15: Providing submit buttons with the submit-form action in PDF forms

## About this Technique

This technique relates to [3.2.2: On Input](https://www.w3.org/WAI/WCAG22/Understanding/on-input) (Sufficient when used with [G80: Providing a submit button to initiate a change of context](../general/G80)).

This technique applies to tagged PDF documents with forms.

## Description

The objective of this technique is to provide a mechanism that allows users to explicitly request a change of context using the submit-form action in a PDF form. The intended use of a submit button is to generate an HTTP request that submits data entered in a form, so it is an appropriate control to use for causing a change of context. In PDF documents, submit buttons are normally implemented using a tool for authoring PDF.

## Examples

### Example 1: Adding a submit button using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Select the Prepare Form tool.
2. Using the Prepare Form toolbar, add a button to the form.
3. Select the button and access the context menu and select the Properties... menu item.
4. In the General tab, provide a Name. This will be used by any JavaScript scripting, so should be a value that can be assigned to a variable.
5. In the General tab, provide a tooltip for the button.
6. In the Options tab, choose an option in the Layout menu for the button label, icon image, or both. Then, type text in the Label box to identify the button as a submit button and/or click Choose Icon and locate the image file you want to use.
7. In the Actions tab: For Select Trigger, choose Mouse Up. (The Mouse Up event is keyboard accessible and, in addition, ensures that the button will not change context unexpectedly, as it might with with a Mouse Enter event.) For Select Action, choose Submit A Form. Click Add.
8. In the Add dialog, enter a URL to collect data on a server or collect form data as e-mail attachments.

### Example 2: Adding a script action to a submit button in a PDF document using JavaScript

The following JavaScript code illustrates the use of a script to specify the submit-form action. To add this script to the form field:

1. Open the Button Properties dialog, as shown in Example 1, and select the Actions tab
2. Select Run a JavaScript from the drop-down list, and select the Add button
3. Enter JavaScript code in the JavaScript Editor dialog.

This example is shown in operation in the [working example of adding a script action to a submit button](../../working-examples/pdf-submit-button/submit-button-js.pdf).

## Related Resources

No endorsement implied.

* Section 12.7.5.2 (Submit-Form Action) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G80: Providing a submit button to initiate a change of context](../general/G80)
* [PDF23: Providing interactive form controls in PDF documents](../pdf/PDF23)
* [PDF12: Providing name, role, value information for form fields in PDF documents](../pdf/PDF12)

## Tests

### Procedure

1. For each page that submits a form, visually verify that the form contains a submit button and check one of the following:

### Expected Results

* #1 is true for each page that contains a form.
