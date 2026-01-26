# Technique PDF9: Providing headings by marking content with heading tags in PDF documents

## About this Technique

This technique relates to:

* [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable)
* [2.4.1: Bypass Blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks) (Sufficient when used for grouping blocks of repeated material in a way that can be skipped)

This technique applies to tagged PDF documents with headings.

## Description

The purpose of this technique is to show how headings in PDF documents can be marked so that they are recognized by assistive technologies. Headings are marked up using the heading elements (H, H1, H2, ... H6) in the structure tree. This is typically accomplished by using a tool for authoring PDF.

Heading markup can be used:

* to indicate start of main content;
* to mark up section headings within the main content area;
* to demarcate different navigational sections, such as top or main navigation, left or secondary navigation, and footer navigation;
* to mark up images (containing text) which have the appearance of headings visually.

Because headings indicate the start of important sections of content, it is possible for assistive technology users to access the list of headings and to jump directly to the appropriate heading and begin reading the content. This ability to "skim" the content through the headings and go directly to content of interest significantly speeds interaction for users who would otherwise access the content slowly.

## Examples

### Example 1: Adding or modifying tagged headings in PDF documents with Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

1. Open the PDF document in Adobe Acrobat Pro.
2. Select Accessibility → Reading Order...
3. Open the Tags panel to view the Accessibility Tags

To correct the H3:

1. Click on H3's text.
2. Click on the Heading 2 tag in the TouchUp Reading Order panel.

### Example 2: Creating documents in Microsoft Word that have correctly tagged headings when converted to PDF

This example is shown with Microsoft Word. There are other software tools that perform similar functions.

Use Styles to create heading formats: Heading 1, Heading 2, Heading 3, etc. Make styles progress in a logical manner; e.g., a Heading 2 should come after a Heading 1.

## Creating documents in OpenOffice Writer that have correctly tagged headings when converted to PDF

This example is shown with OpenOffice Writer. There are other software tools that perform similar functions.

Select the text to become a heading, then use Format → Styles to create heading formats: Heading 1, Heading 2, Heading 3, etc.

Be sure to make header styles progress in a logical manner; e.g., Heading 2 should come after a Heading 1.

Export to PDF as follows:

1. From the File menu, select Export as PDF...
2. The first time you export as PDF, an Options Dialog appears.
3. Select Tagged PDF, then select Export.

## Marking up headings using /Hn elements

Headings within PDF documents can be marked up using /Hn elements in the structure tree, where n is numeral 1 through 6 (for example /H1, /H2, etc.).

The following code fragment illustrates code that is typical for using the /Hn elements to mark content. Note that /H1 has been role-mapped to /Head1 in this example. This is typically accomplished by an authoring tool.

```
0 obj% Document catalog
  << /Type /Catalog
     /Pages 100 0 R                  % Page tree
     /StructTreeRoot 300 0 R         % Structure tree root
  >>
endobj
 ...
300 0 obj% Structure tree root
  << /Type /StructTreeRoot
     /K [ 301 0 R                    % Two children: a chapter
        304 0 R                      % and a paragraph
        ]
     /RoleMap << /Chap /Sect         % Mapping to standard structure types
                 /Head1 /H
                 /Para /P
              >>
    /ClassMap << /Normal 305 0 R >>  % Class map containing one attribute class
    /ParentTree 400 0 R              % Number tree for parent elements
    /ParentTreeNextKey 2             % Next key to use in parent tree
    /IDTree 403 0 R                  % Name tree for element identifiers
  >>
endobj
301 0 obj                            % Structure element for a chapter
  << /Type /StructElem
     /S /Chap
     /ID (Chap1)                     % Element identifier
     /T (Chapter 1)                  % Human-readable title
     /P 300 0 R                      % Parent is the structure tree root
     /K [ 302 0 R                    % Two children: a section head
          303 0 R                    % and a paragraph
        ]
  >>
endobj
302 0 obj                            % Structure element for a section head
  << /Type /StructElem
     /S /Head1
     /ID (Sec1.1)                    % Element identifier
     /T (Section 1.1)                % Human-readable title
     /P 301 0 R                      % Parent is the chapter
     /Pg 101 1 R                     % Page containing content items
     /A << /O /Layout                % Attribute owned by Layout
           /SpaceAfter 25
           /SpaceBefore 0
           /TextIndent 12.5
        >>
    /K 0                             % Marked-content sequence 0
  >>
endobj
...
```

Within marked content containers, headings can be marked up using /Headn elements as follows for a first-level heading in a PDF document:

```
BT		 		% Start of text object
  /Head1 <</MCID 0 >>   	% Start of marked-content sequence
     BDC
        ...
        (This is a first level heading. Hello world: ) Tj
        ...
     EMC			% End of marked-content sequence
     ...
ET				% End of text object
```

## Related Resources

No endorsement implied.

* Section 14.8.4.3.2 (Paragraphlike Elements) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [PDF Accessibility Documentation:headings](https://accessdp.wordpress.com/fixing-pdfs-for-accessibility/headings/)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [G141: Organizing a page using headings](../general/G141)

## Tests

### Procedure

1. For all PDF content that is divided into separate sections, use one of the following to verify that headings are tagged correctly: Read the PDF document with a screen reader, listening to hear that the list of headings is announced correctly. Using a PDF editor, make sure the headings are tagged correctly. Use a tool that is capable of showing the /Head n entries to open the PDF document and verify that headings are tagged correctly. Use a tool that exposes the document through the accessibility API and verify that the headings are tagged correctly.

### Expected Results

* #1 is true.
