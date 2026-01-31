# Technique PDF23: Providing interactive form controls in PDF documents

## About this Technique

This technique relates to [2.1.1: Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard) (Sufficient when used for ensuring keyboard control).

This technique applies to tagged PDF documents with forms.

## Description

The objective of this technique is to ensure that interactive form controls in PDF documents allow keyboard operation. Interactive PDF forms are generally created using a tool for authoring PDF.

The types of PDF form controls are: text input field, check box, radio button, combo box, list box, and button.

Form controls allow users to interact with a PDF document by filling in information or indicating choices, which can then be submitted for processing. Users who rely on keyboard access must be able to recognize and understand the form fields, make selections, and provide input to complete the forms, and submit the form, just as sighted users can.

Interactive form controls can be provided for forms created by converting a scanned paper form to tagged PDF or by creating a form in an authoring application such as Microsoft Word or Open Office and converting it to tagged PDF.

However, documents created by authoring applications that provide form design features might not fully retain their fillable form fields on conversion to PDF. Complex forms in particular may not have properly converted form fields and labels when tagged in conversion.

Using Adobe Acrobat Pro with forms in converted documents, you can ensure that form fields are keyboard accessible and usable by:

* Opening tagged PDF documents with form fields and creating interactive PDF form elements with the Identify Form Fields tool.
* Modifying fillable form fields, or adding form fields, using Adobe Acrobat Pro

## Examples

### Example 1: Adding interactive controls to existing forms in PDF documents using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

If you have a form in a tagged PDF document (created by scanning a paper form or using an authoring tool to generate tagged PDF), you can use Adobe Acrobat Pro to make the form elements keyboard accessible in the same page locations as the static form.

1. Use the Accessibility tool and then Identify Form Fields option to automatically detect form fields and make them fillable.

This example is shown in operation in the [working example of Interactive Controls in Acrobat](../../working-examples/pdf-interactive-form-fields/form-fields-keybd.pdf) (PDF).

### Example 2: Adding form controls in PDF documents using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

You can add keyboard accessible form controls to your form as follows:

1. Select the Prepare Form tool
2. From the newly-opened Prepare Form toolbar, select the type of form control you want to add.

### Example 3: Adding a text field in a PDF document using the /Tx field type

The following code fragment illustrates code that is typical for a simple text field such as shown in Examples 1 and 2. This is typically accomplished by an authoring tool.

```
<< /AP -dict-                                                   
   /DA /Helv  0 Tf 0 g
   /DR -dict-
   /F 0x4
   /FT Tx              % FT key set to Tx for Text Field
   /P -dict-
   /Rect -array-
   /StructParent 0x1
   /Subtype Widget
   /T Date you are available   % Partial field name Date
   /TU Date you are available: use mm/dd/yyyy format % TU tool tip value serves as short description
   /Type Annot
   /V Pat Jones
>>
...
<Start Stream>
 BT
  /P <</MCID 0 >>BDC
  /CS0 cs 0  scn 
  /TT0 1 Tf
    -0.001 Tc 0.003 Tw 11.04 0 0 11.04 72 709.56 Tm
    [(P)-6(le)-3(as)10(e)-3( )11(P)-6(rin)2(t)-3( Y)8(o)-7(u)2(r N)4(a)11(m)-6(e)]TJ
  0 Tc 0 Tw 9.533 0 Td
  ( )Tj
  -0.004 Tc 0.004 Tw 0.217 0 Td
  [(\()-5(R)-4(e)5(q)-1(u)-1(i)-3(r)-3(e)-6(d)-1(\))]TJ
 EMC
  /P <</MCID 1 >>BDC
  0 Tc 0 Tw 4.283 0 Td
  [( )-2( )]TJ
   EMC
   /ArtifactSpan <</MCID 2 >>BDC
   0.002 Tc -0.002 Tw 0.456 0 Td
  [(__)11(___)11(___)11(___)11(___)11(_)11(____)11(___)11(___)11(__)]TJ
  0 Tc 0 Tw 13.391 0 Td
  ( )Tj
  EMC
 ET
<End Stream>
```

## Related Resources

No endorsement implied.

* Section 12.7 (Interactive Forms) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)

## Related Techniques

* [G202: Ensuring keyboard control for all functionality](../general/G202)
* [PDF3: Ensuring correct tab and reading order in PDF documents](../pdf/PDF3)
* [PDF12: Providing name, role, value information for form fields in PDF documents](../pdf/PDF12)
* [PDF15: Providing submit buttons with the submit-form action in PDF forms](../pdf/PDF15)

## Tests

### Procedure

1. For each form control, verify that it is properly implemented by tabbing to each form control and checking that it can be activated or that its value can be changed from the keyboard.

### Expected Results

* #1 is true.
