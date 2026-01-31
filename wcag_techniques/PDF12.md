# Technique PDF12: Providing name, role, value information for form fields in PDF documents

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable)
* [4.1.2: Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value) (Sufficient when used with [G135: Using the accessibility API features of a technology to expose names and … notification of changes](../general/G135))

This technique applies to tagged PDF documents with interactive form fields.

## Description

The objective of this technique is to ensure that assistive technologies can gather information about and interact with form controls in PDF content.

The types of PDF form controls are: text input field, check box, radio button, combo box, list box, and button.

Providing name, role, state, and value information for all form components enables compatibility with assistive technology, such as screen readers, screen magnifiers, and speech recognition software used by people with disabilities.

The following table describes how the role, name, value, and state are defined for PDF form controls created using Adobe Acrobat Pro. Adobe LiveCycle Designer provides the same controls as well as several additional ones: see Example 2 below.

## Examples

### Example 1: Specifying name, role, value and/or state for a form field using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

This example uses a check box for illustration; the procedure is the same for other form controls.

1. Open the Prepare Form tool.
2. Select the form field you are creating or modifying and access the context menu for it.
3. Select the Properties... option.
4. Specify the name by adding a value to the Tooltip field. This will used by the accessibility API as the Name for the control. To conform to the Label In Name Criterion, the Tooltip value must contain the text that presented visually.
5. If you need to specify the default value and state, select the Options tab for these options.

The image below shows the Check Box Properties dialog, open in the General tab. (The Name field in the dialog is not needed for accessibility.)

This example is shown in operation in the [working example of specifying name, role, value using Acrobat Pro](../../working-examples/pdf-name-role-value-form-fields/form.pdf).

### Example 2: Adding a checkbox in a PDF document using the /Btn field type

The following code fragment illustrates code that is typical for a simple check box field such as shown in Examples 1 and 2. This is typically accomplished by an authoring tool.

```
1 0 obj
  << /FT /Btn     % Role
     /TU Retiree  % Name
     /V /Yes      % Value
     /AS /Yes
     /AP << /N << /Yes 2 0 R /Off 3 0 R>>
  >>
endobj
```

## Related Resources

No endorsement implied.

* Section 12.7.4 (Field Types) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [PDF23: Providing interactive form controls in PDF documents](../pdf/PDF23)
* [PDF5: Indicating required form controls in PDF forms](../pdf/PDF5)
* [PDF22: Indicating when user input falls outside the required format or values in PDF forms](../pdf/PDF22)

## Tests

### Procedure

1. For the form control, verify that name, role, and value/state are specified by one of the following:

### Expected Results

* #1 is true.
