# Technique PDF1: Applying text alternatives to images with the Alt entry in PDF documents

## About this Technique

This technique relates to [1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) (Sufficient).

This technique applies to tagged PDF documents with images.

## Description

The objective of this technique is to provide text alternatives for images via an /Alt entry in the property list for a Tag. This is normally accomplished using a tool for authoring PDF.

PDF documents may be enhanced by providing alternative descriptions for images, formulas, and other items that do not translate naturally into text. In fact, such text alternatives are required for accessibility: alternate descriptions are human-readable text that can be vocalized by text-to-speech technology for the benefit of users with vision disabilities.

When an image contains words that are important to understanding the content, the text alternative should include those words. This will allow the alternative to accurately represent the image. Note that it does not necessarily describe the visual characteristics of the image itself but must convey the same meaning as the image.

## Examples

### Example 1: Adding alt text to an image in Adobe Acrobat DC Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Open the Accessibility panel via the Tools → Accessibility options.
2. Select the image in the document and select the "Set Alternative Text" option in the Accessibility tools panel.
3. In the Set Alternative Text dialog that appears, type in your alternative text, then press the Save & Close button.

This example is shown in operation in the [working example of Adding an /Alt entry to an image](../../working-examples/pdf-alt-entry-to-an-image/alt-entry-to-an-image.pdf).

### Example 2: Adding alt text to an image in Microsoft Word

1. Right-click on the image and choose View Alt Text
2. Type the alternative text into the text box provided.

### Example 3: Adding alt text to an image in OpenOffice with the Writer add-on

This example is shown with Open Office Writer. There are other software tools that perform similar functions.

1. Select "Insert" then "picture", select the image to be inserted
2. Right click on the mouse
3. Select "Description"
4. Enter a text title and a good text description
5. Click OK.

### Example 4: Adding a text alternative to an image in a PDF document using an /Alt entry

The /Alt property used on an image of mountains with a moon and trees typically would be used like this (typically accomplished by an authoring tool):

```
/Figure <</Alt (Sketch of Mountains with moon rising over trees)>>
```

The image might also be represented by a tag with a different name. A different name might be used because the tag name is written in a language other than English or because a specific tool uses a different name for some other reason. In this situation, it is also necessary that the RoleMap contained within the StructTreeRoot for the PDF document contain an entry which explicitly maps the name of the tag used for the image with the standard structure type used in PDF documents (in this case, Figure). If the RoleMap contains only an entry mapping Shape tags to Figure tags, the rolemap information would appear as follows:

```
/RoleMap << /Shape /Figure >>
```

In this case, the usage of the /Alt entry as follows would also be correct:

```
/Shape <</Alt (Crater Lake in the summer, with the blue sky, clouds and
 crater walls perfectly reflected in the lake) >>
```

Note that the /Alt entry in property lists can be combined with other entries.

## Related Resources

No endorsement implied.

* Section 14.9.4 (Replacement Text) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Acrobat and Accessibility](https://webaim.org/techniques/acrobat/acrobat)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G94: Providing short text alternative for non-text content that serves the same purpose and presents the same information as the non-text content](../general/G94)

## Tests

### Procedure

For all images which need equivalents:

1. Verify the images have /Alt entries on an enclosing tag by one of the following:

### Expected Results

* Check #1 is true.
