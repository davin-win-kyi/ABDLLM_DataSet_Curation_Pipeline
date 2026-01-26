# Technique ARIA20: Using the region role to identify a region of the page

## About this Technique

This technique relates to [1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships) (Sufficient).

This technique applies to technologies that support [Accessible Rich Internet Applications](https://www.w3.org/TR/wai-aria/).

## Description

This technique demonstrates how to assign a generic region role to a section of a page so that user agents and assistive technologies may be able to programmatically identify it. The region role demarcates a segment of the page that contains content of significance so that it is more readily discoverable and navigable. The generic region should be used when the section cannot be marked up using a standard document landmark role (see [ARIA11](ARIA11)).

It is important to name regions, because they are generic grouping elements and users will need some way to tell which region they are in. Regions can be named using aria-labelledby, aria-label, or another technique. Doing so helps to better expose content and information relationships on the page. The role of region should be used prudently, because if overused they can make the page overly verbose for screen reader users.

## Examples

### Example 1: Region on a news website

A section on the home page of a news website that contains a poll that changes every week is marked up with role="region". The h3 above the form is referenced as the region's name using aria-labelledby.

```html
<div role="region" aria-labelledby="pollhead">
  <h3 id="pollhead">This week's Poll</h3>
  <form>
    <fieldset>
      <legend>Do you believe the tax code needs to be overhauled?</legend>
      <input type="radio" id="r1" name="poll">
      <label for="r1">No, it's fine the way it is</label>
      <input type="radio" id="r2" name="poll">
      <label for="r2">Yes, the wealthy need to pay more</label>
      <input type="radio" id="r3" name="poll">
      <label for="r3">Yes, we need to close corporate loopholes</label>
      <input type="radio" id="r4" name="poll">
      <label for="r4">Changes should be made across the board</label>
    </fieldset>
  </form>
  <a href="results.php">See Poll Results</a>
</div>
```

### Example 2: Identifying a region on a banking site

A user can expand links on a bank website after logging in to see details of term deposit accounts. The details are within a span marked up with region role. The heading for the region has role=heading and is included in the aria-labelledby that names the region.

```html
<ol>
  <li>
    <button aria-controls="block1" aria-expanded="false" id="l1" title="show details"
      type="button">John Henry's Account <img alt="" src="images/panel_expand.gif">
    </button>
    <div id="block1" class="nowHidden" tabindex="-1" aria-labelledby="l1 cd1"
      role="region">
      <span id="cd1" role="heading" aria-level="3">Certificate Of Deposit</span>
      <table>
        <tr>
          <th scope="row">Account:</th>
          <td>25163522</td>
         </tr>
         <tr>
          <th scope="row">Start date:</th>
          <td>February 1, 2014</td>
         </tr>
         <tr>
          <th scope="row">Maturity date:</th>
          <td>February 1, 2016</td>
         </tr>
         <tr>
          <th scope="row">Deposit Amount:</th>
          <td>$ 3,000.00</td>
         </tr>
         <tr>
          <th scope="row">Maturity Amount:</th>
          <td>$ 3,072.43</td>
        </tr>
      </table>
    </div>
  </li>
</ol>
```

### Example 3: Identifying a portlet with a generic region

This example shows how a generic region landmark might be added to a weather portlet. There is no existing text on the page that can be referenced as the label, so it is labelled with aria-label.

```html
<div role="region" aria-label="weather portlet"> 
  ...
</div>
```

## Related Resources

No endorsement implied.

* [The Roles Model (role=region)](https://www.w3.org/TR/wai-aria/#region)

## Related Techniques

* [ARIA11: Using ARIA landmarks to identify regions of a page](../aria/ARIA11)
* [ARIA12: Using role=heading to identify headings](../aria/ARIA12)
* [ARIA13: Using aria-labelledby to name regions and landmarks](../aria/ARIA13)

## Tests

### Procedure

For each section marked up with role="region":

1. Examine the content and ensure that it is important enough to have an independent landmark
2. Ensure that a standard landmark role is not appropriate for this content
3. Check that the region has a programmatically determined name

### Expected Results

* Checks #1-3 are true.
