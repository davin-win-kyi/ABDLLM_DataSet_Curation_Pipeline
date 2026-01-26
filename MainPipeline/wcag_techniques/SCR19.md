# Technique SCR19: Using an onchange event on a select element without causing a change of
                    context

## About this Technique

This technique relates to:

* [3.2.2: On Input](https://www.w3.org/WAI/WCAG22/Understanding/on-input) (Sufficient)
* [3.2.5: Change on Request](https://www.w3.org/WAI/WCAG22/Understanding/change-on-request) (Sufficient)

This technique applies to HTML with support for scripting.

## Description

The objective of this technique is to demonstrate how to correctly use an onchange event with a select element to update other elements on the web page. This technique will not cause a change of context. When there are one or more select elements on the web page, an onchange event on one, can update the options in another select element on the web page. All of the data required by the select elements is included within the web page.

It is important to note that the select item which is modified is after the trigger select element in the reading order of the web page. This ensures that assistive technologies will pick up the change and users will encounter the new data when the modified element receives focus. This technique relies on JavaScript support in the user agent.

## Examples

### Example 1

This example contains two select elements. When an item is selected in the first select, the choices in the other select are updated appropriately. The first select element contains a list of continents. The second select element will contain a partial list of countries located in the selected continent. There is an onchange event associated with the continent select. When the continent selection changes, the items in the country select are modified using JavaScript via the Document Object Model (DOM). All of the data required, the list of countries and continents, is included within the web page.

Overview of the code below

* countryLists array variable which contains the list of countries for each continent in the trigger select element.
* countryChange() function which is called by the onchange event of the continent select element.
* The HTML code to create the select elements in the body of the web page.

```html
<!doctype html> 
<html lang="en"> 
  <head> 
    <meta charset=utf-8"> 
    <title>Dynamic Select Statements</title> 
    <script>
    // array of possible countries in the same order as they appear
    // in the country selection list 
    var countryLists = new Array(4) 
    countryLists["empty"] = ["Select a Country"]; 
    countryLists["North America"] = ["Canada", "United States", "Mexico"]; 
    countryLists["South America"] = ["Brazil", "Argentina", "Chile", "Ecuador"]; 
    countryLists["Asia"] = ["Russia", "China", "Japan"]; 
    countryLists["Europe"]= ["Britain", "France", "Spain", "Germany"]; 
  
    /* CountryChange() is called from the onchange event of a select element. 
     * param selectObj - the select object which fired the on change event. 
    */ 
  
    function countryChange(selectObj) { 
    // get the index of the selected option 
    var idx = selectObj.selectedIndex; 
  
    // get the value of the selected option 
    var which = selectObj.options[idx].value; 
  
    // use the selected option value to retrieve the list of items 
    // from the countryLists array 
    cList = countryLists[which]; 
  
    // get the country select element via its known id 
    var cSelect = document.getElementById("country"); 
  
    // remove the current options from the country select 
    var len=cSelect.options.length; 
  
    while (cSelect.options.length > 0) { 
      cSelect.remove(0); 
    } 
  
    var newOption; 
    // create new options 
    for (var i=0; i<cList.length; i++) { 
      newOption = document.createElement("option"); 
      newOption.value = cList[i];  // assumes option string and value are the same 
      newOption.text=cList[i]; 
  
   // add the new option 
    try { 
      cSelect.add(newOption);  // this will fail in DOM browsers but is needed for IE 
    } 
    catch (e) { 
      cSelect.appendChild(newOption); 
    } 
  } 
} 
  </script>
</head>
<body>
  <h1>Dynamic Select Statements</h1>
  <label for="continent">Select Continent</label>
  <select id="continent" onchange="countryChange(this);">
    <option value="empty">Select a Continent</option>
    <option value="North America">North America</option>
    <option value="South America">South America</option>
    <option value="Asia">Asia</option>
    <option value="Europe">Europe</option>
  </select>
  <div>
    <label for="country">Select a country</label>
    <select id="country">
      <option value="0">Select a country</option>
    </select>
  </div>
</body>
</html>
```

Here is a working example: [Dynamic Select](../../working-examples/script-dynamic-select/)

## Related Resources

No endorsement implied.

* [Accessible Forms using WCAG 2.0](http://usability.com.au/2008/09/accessible-forms-using-wcag-2-0/)
* [Change of context](https://www.w3.org/TR/WCAG22/#dfn-change-of-context) definition

## Tests

### Procedure

1. Navigate to the trigger select element (in this example, the one to select continents) and change the value of the select.
2. Navigate to the select element that is updated by the trigger (in this example, the one to select countries).
3. Check that the matching option values are displayed in the other select element.
4. Navigate to the trigger select element, navigate through the options but do not change the value.
5. Check that the matching option values are still displayed in the associated element.

It is recommended that the select elements are tested with an assistive technology to verify that the changes to the associated element are recognized.

### Expected Results

* Step #3 and #5 are true.
