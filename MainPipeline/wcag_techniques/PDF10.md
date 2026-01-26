# Technique PDF10: Providing labels for interactive form controls in PDF documents

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable)
* [3.3.2: Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions) (Sufficient)
* [4.1.2: Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value) (Sufficient when used with [G135: Using the accessibility API features of a technology to expose names and … notification of changes](../general/G135))

This technique applies to content implemented in Adobe Tagged PDF.

## Description

The objective of this technique is to ensure that users of assistive technology are able to perceive form control labels and understand how form controls are used.

Form controls allow users to interact with a PDF document by filling in information or indicating choices which can then be submitted for processing. Assistive technology users must be able to recognize and understand the form fields, make selections, and provide input to complete the forms, and submit the form, just as sighted users can. Understandable labels that convey the purpose of each form control are essential to form accessibility.

Form inputs generally have labels and instructions to help users understand what information is required and how to fill in the form. Unless these labels are programmatically associated with the relevant fields, assistive technology might not be able to associate them correctly, and thus users might not understand how to complete the form.

Using Adobe Acrobat Pro with documents with interactive forms, you can make sure that the forms are accessible and usable by making sure that programmatically associated labels that convey the purpose of the fields are provided.

The heuristics used by assistive technology will sometimes use the text label if a programmatically associated label cannot be found. The TU entry (which is the tooltip) of the field dictionary is the programmatically associated label. Therefore, add a tooltip to each field to provide a label that assistive technology can interpret.

## Examples

### Example 1: Providing labels using the Forms tool in Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

As noted in the Description, text labels added in an authoring tool and then converted to PDF might be visually associated with the fields but are not programmatically associated, and you should provide a tooltip.

1. Select the Prepare Form tool.
2. For the field you want to edit, access the context menu and select the Properties dialog.
3. In the General tab of the Properties dialog, type a description for the form field in the Tooltip field.
4. Repeat for all form fields.

This example is shown in operation in the [working example of providing labels using the forms tool (PDF)](../../working-examples/pdf-form-labels/form.pdf).

### Example 2: Adding a tooltip to interactive form controls

The following code fragment illustrates the use of the TU entry to provide a tooltip (or programmatically associated text label) for a form field. This is typically accomplished by an authoring tool.

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
   /TU Date you are available: use MM/DD/YYYY format % TU tool tip serves as description
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

* [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G131: Providing descriptive labels](../general/G131)
* [G162: Positioning labels to maximize predictability of relationships](../general/G162)
* [PDF23: Providing interactive form controls in PDF documents](../pdf/PDF23)
* [PDF5: Indicating required form controls in PDF forms](../pdf/PDF5)
* [PDF22: Indicating when user input falls outside the required format or values in PDF forms](../pdf/PDF22)

## Tests

### Procedure

1. For each form control, verify visually that the label is positioned correctly in relation to the control.
2. For each form control, verify that the name is programmatically associated with the control by one of the following: Open the PDF document with a tool that is capable of showing the name associated with the control and verify that the name is associated correctly with the control. Use a tool that exposes the document through the accessibility API , and verify that the name is associated correctly with the control.

### Expected Results

* #1 and #2 are true.
