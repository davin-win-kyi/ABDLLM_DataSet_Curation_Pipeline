# Technique PDF20: Using Adobe Acrobat Pro's Table Editor to repair mistagged tables

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient when used for making information and relationships conveyed through presentation programmatically determinable).

This technique applies to tagged PDF documents with tables.

## Description

The purpose of this technique is to show how table cells in PDF documents can be marked up so that the logical relationships among rows and columns are preserved and recognized by assistive technology. This is typically accomplished by using a tool for authoring PDF.

However, tables converted to PDF may have incorrectly merged or split table cells, even if they were marked up correctly in the authoring tool. Authors can ensure that table cells are structured properly by using the Table Editor in Adobe Acrobat Pro's Reading Order tool.

## Examples

### Example 1: Repairing table cells using the table editor in the Reading Order tool in Adobe Acrobat Pro

This example is shown with Adobe Acrobat Pro. There are other software tools that perform similar functions.

This example uses a table that was marked up correctly when it was created in Microsoft Word. Some table headers span two rows in the header row; one table header spans two columns.

To check the table in the PDF document:

1. Advanced → Accessibility → Reading Order...
2. Select the table by clicking the number in the top left hand corner of the table (3 in the reading order in the image below).
3. Select the Table Editor button on the Reading Order panel. The table cells will be outlined in red and labeled with their tags. The red outlines may not exactly match up to the table cells but you should be able to determine if the cells are tagged correctly.

The following image shows the example table in the Reading Order tool.

The following images shows the example table in the Table Editor. The cells are outlined in red, and the tab for each cell is displayed. Upon conversion, the Results headers were correctly split, but most of the table headers were incorrectly tagged as table data cells.

To repair the header cells:

1. Select the cell in the table (it will be outlined in blue when selected)
2. Right click the cell and select Table Cell Properties...
3. In the Table Cell Properties dialog, change Data Cell to Header Cell.

Similarly, to repair the incorrectly split header cells to the left of Results header:

1. Select the top cell in the column (it will be outlined in blue when selected)
2. Right click the cell and select Table Cell Properties...
3. In the Table Cell Properties dialog, change the Row Span from 1 to 2

The following image shows the repaired example table.

This example is shown in operation in the [working example of repairing table structure (Word file)](../../working-examples/pdf-complex-table/complex-table.docx) and [working example of repairing table structure (PDF file)](../../working-examples/pdf-complex-table/complex-table.pdf).

### Example 2: Marking up a table using table structure elements

The following code fragment illustrates code that is typical for a simple table (header row and data row) such as shown in Examples 1-3:

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
 <</A[23 0 R 120 0 R]
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
* [PDF6: Using table elements for table markup in PDF Documents](../pdf/PDF6)

## Tests

### Procedure

1. For a table that has been repaired with the Table Editor, confirm one of the following:

### Expected Results

* #1 is true.
