# Technique PDF8: Providing definitions for abbreviations via an E entry for a structure element

## About this Technique

This technique relates to [3.1.4: Abbreviations](https://www.w3.org/WAI/WCAG22/Understanding/abbreviations) (Sufficient when used with [G102: Providing the expansion or explanation of an abbreviation](../general/G102)).

This technique applies to tagged PDF documents containing abbreviations or acronyms.

## Description

The objective of this technique is to provide an expansion or definition of an abbreviation for the first occurrence of the abbreviation. For example, a reference to an abbreviation, such as "WCAG", should be available as "Web Content Accessibility Guidelines (WCAG)" on its first occurrence in a document.

This is done by setting expansion text using an /E entry for a structure element, and is normally accomplished using a tool for authoring PDF. A Span structure element is typically used to tag the abbreviation, but the /E entry is valid with any structure element.

This technique is applicable for any abbreviation, including acronyms and initialisms. Note that on the first occurrence of the abbreviation, both the abbreviation and the expansion text must be provided. This will aid recognition of later use of the abbreviation.

PDF documents may be enhanced by providing expansions for abbreviations. In fact, such expansions are required for accessibility to ensure understanding by people who have difficulty decoding words; rely on screen magnification (which may obscure context); have limited memory; or who have difficulty using context to aid understanding.

## Examples

### Example 1: Adding an /E entry to an abbreviation using Adobe Acrobat Pro's Tags panel

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

In a tagged PDF document:

1. Select View → Show/Hide → Navigation Panes → Accessibility Tags.
2. Select the first instance of the abbreviated text that needs to be expanded. If the selected text is part of a larger tag, use the Accessibility Tags panel's "Create Tag from Selection", and create a new Span tag. In this example, the text "WCAG2.2" (within the LBody tag) has been enclosed in a Span tag.
3. In the Tags panel, access the context menu for the spanned text and select Properties...
4. In the Content tab of the Properties dialog, enter the expansion text, followed by the originally selected text.

The following image illustrates this technique:

This example is shown in operation in:

* [Working example of Providing definitions for Abbreviations (Word document)](../../working-examples/pdf-abbreviation-definitions/pdf-abbreviation-definitions.docx);
* [Working example of Providing definitions for Abbreviations (OpenOffice document)](../../working-examples/pdf-abbreviation-definitions/pdf-abbreviation-definitions.odt);
* [Working example of Providing definitions for Abbreviations (PDF document)](../../working-examples/pdf-abbreviation-definitions/pdf-abbreviation-definitions.pdf).

### Example 2: Using a /Span structure element with an /E entry to define an abbreviation

The following code fragment illustrates code that is typical for using the /Span structure element to define an abbreviation.

This example uses the sentence "Sugar is commonly sold in 5 lb bags." The abbreviation "lb" is tagged as a /Span structure element with an /E entry (typically accomplished by an authoring tool).

```
1 0 obj                                  % structure element
  << /Type /StructElemen
           /S /Span                      % element type
           /P ...                        % Parent in structure hierarchy
           /K << /Type /MCR
                      /Page 2 0 R        % Page containing marked-content sequence
                     /MCID 0             % Marked content identifier for "lb"
              >>
           /E  (pound, lb)
  >>
endobj
```

### Example 3: Using a /TH structure element with an /E entry to define an abbreviation

As noted in the Description, the /E entry is valid with any structure element.

The following code fragment illustrates code that is typical for using an /E entry to define an abbreviation.

A table that contains columns for each month uses abbreviations as the values of column headers. The expansion for each abbreviation is provided as the /E entry of the /TH structure element (typically accomplished by an authoring tool).

```
1 0 obj                                  % structure element
  << /Type /StructElemen
          /S /TH                        % element type
          /P ...                        % Parent in structure hierarchy
          /K << /Type /MCR
                      /Page 2 0 R       % Page containing marked-content sequence
                      /MCID 0           % Marked content identifier for "Dec"
             >>
          /E  (December, Dec)
  >>
endobj
```

## Related Resources

No endorsement implied.

* Section 14.9.5 (Expansion of Abbreviations and Acronyms) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G102: Providing the expansion or explanation of an abbreviation](../general/G102)
* [G55: Linking to definitions](../general/G55)
* [G62: Providing a glossary](../general/G62)
* [G70: Providing a function to search an online dictionary](../general/G70)
* [G97: Providing the first use of an abbreviation immediately before or after the expanded form](../general/G97)

## Tests

### Procedure

1. Verify that the first occurrence of abbreviations that require expansion text have /E entries on an enclosing tag by one of the following and that both the abbreviation and the expansion text are provided:

### Expected Results

* Check #1 is true.
