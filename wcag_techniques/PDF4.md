# Technique PDF4: Hiding decorative images with the Artifact tag in PDF documents

## About this Technique

This technique relates to [1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) (Sufficient).

This technique applies to tagged PDF documents.

## Description

The purpose of this technique is to show how purely decorative images in PDF documents can be marked so that they can be ignored by Assistive Technology by using the /Artifact tag. This is typically accomplished by using a tool for authoring PDF.

In PDF, artifacts are generally graphics objects or other markings that are not part of the authored content. Examples of artifacts include page header or footer information, lines or other graphics separating sections of the page, or decorative images.

## Examples

### Example 1: Marking an image as an artifact using Acrobat Pro's TouchUp Reading Order Tool

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

The TouchUp Reading Order Tool can be used to mark an image as "Background / Artifact", which removes it from the document tag structure.

1. Open the TouchUp Reading Order Tool in Acrobat Pro: Accessibility → TouchUp Reading Order
2. Select the decorative image in the document
3. In the TouchUp Reading Order Tool, click the Background/Artifact button to remove the selected image from the tag structure

This example is shown in operation in the [working example of creating a decorative image (Word file)](../../working-examples/pdf-decorative-image/decorative-image.docx) and [working example of marking a background image as an artifact (PDF file)](../../working-examples/pdf-decorative-image/decorative-image.pdf).

### Example 2: Marking an image as an artifact in a PDF document using an /Artifact tag or property list

The PDF specification allows images to be marked as "artifacts". An artifact is explicitly distinguished from real content by enclosing it in a marked-content sequence with the /Artifact tag.

#### /Artifact

```
BMC  ...  EMC
```

or

#### /Artifact propertyList

```
BDC  ...  EMC
```

The first is used to identify a generic artifact; the second is used for artifacts that have an associated property list. Note, to aid in text reflow, artifacts should be defined with property lists whenever possible. Artifacts lacking a specified bounding box are likely to be discarded during reflow.

Property list entries for artifacts include Type, BBox, Attached, and Subtype.

## Related Resources

No endorsement implied.

* Section 14.8.2.2 (Real Content and Artifacts) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Tests

### Procedure

1. For an image that is purely decorative, use one of the following to verify that it is marked as an artifact:

### Expected Results

* #1 is true.
