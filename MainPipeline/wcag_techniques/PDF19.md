# Technique PDF19: Specifying the language for a passage or phrase with the Lang entry in PDF documents

## About this Technique

This technique relates to:

* [3.1.1: Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page) (Sufficient)
* [3.1.2: Language of Parts](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts) (Sufficient)

This technique applies to tagged PDF documents.

## Description

The objective of this technique is to specify the language of a passage, phrase, or word using the /Lang entry to provide information in the PDF document that user agents need to present text and other linguistic content correctly. This is normally accomplished using a tool for authoring PDF.

Both assistive technologies and conventional user agents can render text more accurately when the language is identified. Screen readers can load the correct pronunciation rules. As a result, users with disabilities are better able to understand the content.

Note

This technique can be used to set the default language for the entire document if the entire document is contained in the container or tag. In this case, this technique would apply to Success Criterion 3.1.1.

## Examples

### Example 1: Adding a /Lang entry to specify the language for a paragraph using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. In the Navigation Panes, select the Accessibility Tags option.
2. Find the tag that contains the content that is in a different language.
3. Right-click the tag and select Properties in the context menu.
4. In the Tags tab in the Object Properties dialog, select the correct language from the drop-down list.

Note

Acrobat includes numerous preset language selections. If you need to specify a language that is not on the list, such as Russian, you must type the ISO 639-2 code for the language, rather than its name.

### Example 2: Adding a /Lang entry to specify the language for a specific word or phrase using Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Select the word or phrase that is in a different language.
2. Open the Accessibility Tags panel and select the Create Tag From Selection option.
3. Find the newly-created tag and right-click on it.
4. In the Tag tab in the Properties dialog, select the language from the drop-down list.

When you tag a word or phrase, Acrobat splits the original content into three document content tags: one for the text that precedes your selection, one for the selection, and one for the text that follows the selection. As needed, drag the document content tag for the selected text into position between the other two tags, so that the text reads in the proper order. All three tags must also be at the same level beneath their parent tag. Drag them into place if they are not.

This example is shown in operation in the [working example of marking a specific word or phrase in Acrobat Pro (PDF)](../../working-examples/pdf-lang-phrase/lang-of-phrase.pdf).

### Example 3: Specifying the language for a word or phrase in a PDF document using a /Lang entry

Below the level of the default document language, the language for a passage may be specified for the following items:

* Marked-content sequences that are not in the structure hierarchy, through a /Lang entry in a property list attached to the marked-content sequence with a Span tag.
* Structure elements of any type, through a /Lang entry in the structure element dictionary.

The following code fragment illustrates code that is typical for using the /Lang entry to override the default document language by specifying a marked-content sequence within a page's content stream:

```
/P % Start of marked-content sequence
   BDC
      (See you later, or in Spanish you would say, ) Tj
      /Span << /Lang (es-MX) >>% Start of nested marked-content sequence
     BDC
      (Hasta la vista.) Tj
     EMC% End of nested marked-content sequence
   EMC% End of marked-content sequence
```

The following code fragment illustrates code that is typical for using the /Lang entry in the structure element dictionary. In this case, the /Lang entry applies to the marked-content sequence having an MCID (marked-content identifier) value of 0 within the indicated page's content stream.

```
1 0 obj% Structure element
  << /Type /StructElem
    /S /Span% Structure type
    /P /P% Parent in structure hierarchy
    /K<< /Type /MCR
      /Pg 2 0 R% Page containing marked-content sequence
      /MCID 0% Marked-content identifier
     >>
   /Lang (es-MX)% Language specification for this element
   >>
endobj
2 0 obj% Page object
  << /Type /Page
     /Contents 3 0 R% Content stream
   …
   >>
   endobj
3 0 obj% Page's content stream
  << /Length … >>
    stream
     BT
      /P % Start of marked-content sequence
      BDC
     (See you later, or in Spanish you would say, ) Tj
     /Span << /MCID 0 >>% Start of nested marked-content sequence
    BDC
     (Hasta la vista.) Tj
    EMC% End of nested marked-content sequence
  EMC% End of marked-content sequence
 ET
 endstream
 endobj
```

## Related Resources

No endorsement implied.

* Section 14.9.2 (Natural Language Specification) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [ISO 639-2 Codes](https://www.loc.gov/standards/iso639-2/php/code_list.php)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [PDF16: Setting the default language using the /Lang entry in the document catalog of a PDF document](../pdf/PDF16)

## Tests

### Procedure

1. Verify that the language of a passage, phrase, or word that differs from the language of the surrounding text is correctly specified by a /Lang entry on an enclosing tag or container:
2. Verify that if the container or tag contains the entire document, the language setting is the language intended as the default for the document.

### Expected Results

* #1 and #2 are true.
