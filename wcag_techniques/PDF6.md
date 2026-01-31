# Technique PDF6: Using table elements for table markup in PDF Documents

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable).

This technique applies to tagged PDF documents with tables.

## Description

The purpose of this technique is to show how tables in PDF documents can be marked up so that they are recognized by assistive technology. This is typically accomplished by using a tool for authoring PDF.

Tabular information must be presented in a way that preserves relationships within the information even when users cannot see the table or the presentation format is changed. Information is considered tabular when logical relationships among text, numbers, images, or other data exist in two dimensions (vertical and horizontal). These relationships are represented in columns and rows, and the columns and rows must be recognizable in order for the logical relationships to be perceived.

Tagged tables can be created using the Add Tags to Document feature in Adobe Acrobat, using the Object Library in Adobe LiveCycle, or converting tables to PDF from a third-party application, such as Microsoft Word. However, the resulting tables may not be tagged correctly and you should ensure that table tagging issues are resolved.

Within PDF documents, a table uses the following structure types for table elements:

* A table element (Table).
* One or more table row elements (TR) which define each row of table cells as immediate children of the Table element.
* One or more table header elements (TH) or table data elements (TD) as the immediate children of each table row element.
* Cells that span two or more rows or columns should use the RowSpan or ColSpan attribute.
* For tables that contain blank cells, you may need to add empty TD cells so that each row or column has the same number of cells.

## Examples

### Example 1: Creating tables in Microsoft Word that have correctly tagged headings when converted to PDF

This example is shown with Word. There are other software tools that perform similar functions.

1. Select the table
2. In the Ribbon, select Table Design.
3. Check the Header Row checkbox

This example is shown in operation in the [working example of tagged table headings in Word](../../working-examples/pdf-table-headers/table-example-header-row.docx).

Note

When the table has a more complex heading structure, this mark-up must be added in a PDF editor such as Acrobat Pro.

### Example 2: Creating tables in OpenOffice.org Writer 2.2 that have correctly tagged headings when converted to PDF

This example is shown with OpenOffice.org Writer. There are other software tools that perform similar functions.

1. Access the table's context menu and select Table...
2. Select the Table Format tab.
3. Check Repeat Heading and select "1" in the First Rows listbox as shown in the following image.

This example is shown in operation in the [working example of tagged table headings in OpenOffice Writer](../../working-examples/pdf-table-headers/table-example-header-row.odt).

Note

OpenOffice.org Writer can only mark up cells as column headings, not as row headings. Only the first row can be marked as heading for all table columns. When the table has row headings or a more complex heading structure, this mark-up must be added in a PDF editor such as Acrobat Pro.

### Example 3: Modifying table tags using the Tags tab in Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

To check that a converted document with tables has correct table tagging:

1. Open the View menu → Show/Hide → Navigation Panes → Accessibility Tags.
2. Manually inspect each table's tags to make sure that header and data cells have been converted correctly.

Note that in this case, the table headers were incorrectly formatted, and are marked as data cells (TD). To change these to TH tags:

1. On the Accessibility Tags tab, expand the table row that contains the header cells, as shown on the image above.
2. Select all of the incorrectly-formatted cells, open the context menu, and select Properties...
3. On the Tags tab in the Properties dialog, use the Type dropdown to change Table Data Cell to Table Header Cell.

This example is shown in operation in the [working example of tagged table headings in Acrobat](../../working-examples/pdf-table-headers/table-example-repaired.pdf).

### Example 4: Marking up a table using table structure elements

The following code fragment illustrates code that is typical for a simple table (header row and data row):

```
95 0 obj                %Structure element for a table
  << 
    /A 39 0 R
    /K[96 0 R 101 0 R 106 0 R 111 0 R]
    /P 93 0 R
    /S/Table              %standard structure type is table
  >> 
  endobj
96 0 obj                %Structure element for a table row
  << 
    /K[97 0 R 98 0 R 99 0 R 100 0 R]
    /P 95 0 R
    /S/TR                 %standard structure type is table row
  >> 
  endobj
  97 0 obj                %Structure element for a table header
  <<
    /A[23 0 R 120 0 R]
    /K 1
    /P 96 0 R
    /S/TH                 %standard structure type is table head
    /Pg 8 0 R
  >> 
  endobj
  104 0 obj                %Structure element for table data (cell contents)
  << 
    /A 29 0 R
    /K 7
    /P 101 0 R
    /S/TD                  %standard structure type is table data
    /Pg 8 0 R
  >> 
endobj
```

## Related Resources

No endorsement implied.

* Section 14.8.4.3.4 (Table Elements) in [PDF 1.7 (ISO 32000-1) (PDF)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)
* [Create and verify PDF accessibility (Acrobat Pro)](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)

## Related Techniques

* [H51: Using table markup to present tabular information](../html/H51)
* [PDF20: Using Adobe Acrobat Pro's Table Editor to repair mistagged tables](../pdf/PDF20)

## Tests

### Procedure

1. For each table, confirm one of the following:

### Expected Results

* #1 is true.
