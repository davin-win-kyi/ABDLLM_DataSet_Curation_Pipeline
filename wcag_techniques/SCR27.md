# Technique SCR27: Reordering page sections using the Document Object Model

## About this Technique

This technique relates to [2.4.3: Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order) (Sufficient when used for changing a web page dynamically).

This technique applies to HTML, script.

## Description

The objective of this technique is to provide a mechanism for re-ordering component which is both highly usable and accessible. The two most common mechanisms for reordering are to send users to a set-up page where they can number components, or to allow them to drag and drop components to the desired location. The drag and drop method is much more usable, as it allows the user to arrange the items in place, one at a time, and get a feeling for the results. Unfortunately, drag and drop relies on the use of a mouse. This technique allows users to interact with a menu on the components to reorder them in place in a device independent way. It can be used in place of, or in conjunction with drag and drop reordering functionality.

The menu is a list of links using the device-independent onclick event to trigger scripts which re-order the content. The content is re-ordered in the Document Object Model (DOM), not just visually, so that it is in the correct order for all devices.

## Examples

### Example 1

This example does up and down reordering. This approach can also be used for two-dimensional reordering by adding left and right options.

The components in this example are list items in an unordered list. Unordered lists are a very good semantic model for sets of similar items, like these components. The menu approach can also be used for other types of groupings.

The modules are list items, and each module, in addition to content in div elements, contains a menu represented as a nested list.

```html
<ul id="swapper">
    <li id="black">
      <div class="module">
        <div class="module_header">
          <!-- menu link -->
          <a href="#" onclick="ToggleMenu(event);">menu</a>
          <!-- menu -->
          <ul class="menu">
            <li><a href="#" onclick="OnMenuClick(event)" 
              onkeypress="OnMenuKeypress(event);">up</a></li>
            <li><a href="#" onclick="OnMenuClick(event)" 
              onkeypress="OnMenuKeypress(event);">down</a></li>
          </ul>
        </div>
      <div class="module_body">
        Text in the black module
      </div>
    </div>
  </li>
  ...
</ul>
```

Since we've covered the showing and hiding of menus in the simple tree samples, we'll focus here just on the code that swaps the modules. Once we harmonize the events and cancel the default link action, we go to work. First, we set a bunch of local variables for the elements with which we'll be working: the menu, the module to be reordered, the menuLink. Then, after checking the reorder direction, we try to grab the node to swap. If we find one, we then call swapNode() to swap our two modules, and PositionElement() to move the absolutely-positioned menu along with the module, and then set focus back on the menu item which launched the whole thing.

```javascript
function MoveNode(evt,dir){
  
  HarmonizeEvent(evt);
  evt.preventDefault();
    
  var src = evt.target;
  var menu = src.parentNode.parentNode;
  var module = menu.parentNode.parentNode.parentNode;
  var menuLink = module.getElementsByTagName("a")[0];
  var swap = null;
  
  switch(dir){
    case 'up': {
      swap = module.previousSibling;
      while (swap && swap.nodeType != 1){
        swap = swap.previousSibling;
      }
        break;
    }
    case 'down': {
      swap = module.nextSibling;
      while (swap && swap.nodeType != 1){
        swap = swap.nextSibling;
      }
        break;
    }
  }
  if (swap && swap.tagName == node.tagName){
    module.swapNode(swap);
    PositionElement(menu,menuLink,false,true);
  }
  src.focus();
}
```

The CSS for the node swap is not much different than that of our previous tree samples, with some size and color adjustment for the modules and the small menu.

```css
ul#swapper {
  list-item-style:none;
  margin:0px;
  padding:0px;
}

ul#swapper li {
  border:1px solid black;
  height:5em;
  list-style:none;
  margin:1em;
  padding:0;
  width:15em;
}

ul#swapper li a {
  color:white;
  font-size:90%;
  text-decoration:none;
}
    
ul#swapper li div.module_header {
  padding:0 0.2em;
  text-align:right;
}

ul#swapper li div.module_body {
  padding:0.2em;
}
    
ul#swapper ul.menu {
  background-color:#eeeeee; 
  border:1px solid gray;
  display:none;
  height:auto;
  list-style:none;
  margin:0;
  padding:0;
  position:absolute;
  text-align:left;
}

ul#swapper ul.menu li {
  border:none;
  font-weight:normal;
  height:auto;
  margin:0;
  text-align:left;
  width:5em;
}

ul#swapper ul.menu li a {
  color:black;
  display:block;
  padding:0 0.1em;
  text-decoration:none;
  width:100%;
}
```

## Tests

### Procedure

1. Find all components which can be reordered via drag and drop.
2. Check that there is also a mechanism to reorder them using menus build of lists of links.
3. Check that the menus are contained within the re-orderable items in the DOM.
4. Check that scripts for reordering are triggered only from the onclick event of links.
5. Check that items are reordered in the DOM, not only visually.

### Expected Results

* #2 through #5 are true.
