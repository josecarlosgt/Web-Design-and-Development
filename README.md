# Tutorial: Styling the content of your website

CSS (Cascading Style Sheets) is a language for describing how a web page is styled for visual presentation.

## The box model

HTML elements take up space on the web page. The box model is essential for understanding how to adjust the space between elements. The box model describes the size of each element as a series of nested boxes, where each box determines a different property:

- Content: The innermost box contains the content of the element, such as text and images. To change the size of the *content box*, use the *height* and *width* properties (see Task 2 below).
- Padding: The padding box contains the content box and adds a transparent area around the content.
- Border: The border box contains the padded content and adds an optionally colored area around the padding.
- Margin: The margin box contains all three boxes and adds a transparent area around the border.

![box-model](img/box-model.png)

### Block and inline boxes

The box model also broadly defines two general types of boxes: block boxes and inline boxes. Their characteristics refer to how the box behaves in terms of page flow and in relation to other boxes on the page.

If a box has an outer display type of block, it will behave in the following ways:

- The box will break onto a new line.
- The box will extend in the inline direction to fill the space available in its container. In most cases this means that the box will become as wide as its container, filling up 100% of the space available.
- The width and height properties are respected.
- Padding, margin and border will cause other elements to be pushed away from the box.
- Examples: \<h1\>, \<p\>, \<div\>

If a box has an outer display type of inline, then:

- The box will not break onto a new line.
- The width and height properties will not apply.
- Vertical padding, margins, and borders will not cause other inline boxes to move away from the box.
- Horizontal padding, margins, and borders will apply and will cause other inline boxes to move away from the box.

> In short, properties like padding, margin, height, and width only work with block elements. Block elements, like paragraphs and headings, occupy the entire line of the webpage, while inline elements, like links and spans, occupy only the space corresponding to the content they contain.

## Instructions

This document explains the steps for styling content in a HTML document using CSS. Each task below provides links that explain the purpose CSS properties and techniques.

Before starting with Task 1, rename the file *structure.html* to *index.html* and create an external CSS stylesheet with the name: *mystyel.css*. Include the external stylesheet in the index.html file:

```html
<head>
    ...
    <link rel="stylesheet" href="mystyle.css">
</head>
```

You will need to website created in the previous tutorial. You can download the website from [here](https://github.com/josecarlosgt/Web-Design-and-Development/archive/refs/heads/tutorial-2-designing-and-structuring-content.zip).

## Task 1: Styling text

### Font properties

Many CSS properties control the font properties for displaying text. CSS font properties include:

- font-family: specifies the font family, such as "Times New Roman" or serif.
- font-size: changes the font size, such as 120%, small, or 12px.
- font-weight: specifies the font weight, such as normal or bold.
- [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style): changes the text style, such as normal, italic, or oblique.
- [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant): specifies the variant of the text, such as normal or small-caps.
- [font](https://developer.mozilla.org/en-US/docs/Web/CSS/font): is shorthand for setting several font properties at the same time. Ex: font: italic 12pt Georgia, serif;

**[font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)**

The font-family property contains a list of fonts specified as family names separated by commas.
A family name is the name of a specific font, like "Times New Roman", "Arial", or "Georgia". Family names containing spaces must be wrapped in quotations marks, while family names without spaces do not.

A generic family is a more general group of fonts, like serif, sans-serif, cursive, fantasy, or monospace. The web browser will use the first font listed that is available.

> A good practice is to start the list with the intended font and end with a generic family. Ex: font-family: Arial, Helvetica, sans-serif;

This [link](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#some_common_font_families) contains a list of common font famliies:

Add the following CSS rule to give the text of your website a sharp look:

```css
body {
    font-family: Arial, sans-serif;
}
```

> Serif fonts convey a classic, elegant, or traditional feel. In contrast, the clean lines and sharp edges of sans-serif fonts are more appropriate for more direct communication. For this reason, sans-serif fonts are more common in Web development as they render out content on a screen more clearly, which increases legibility for users across different devices.

**[font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)**

The font size can be specified using a predefined size name, a relative size name, or a number with an absolute or relative size unit.

The predefined size names are xx-small, x-small, small, medium, large, x-large, and xx-large, where medium is the default size. The relative size names are smaller and larger which change the font size for an element to be smaller or larger than the font size of the parent element.

An absolute size is a size that is fixed and independent of other CSS sizes. Absolute size units include:

- px: pixels (1px = 1/96in)
- cm: centimeters
- mm: millimeters
- in: inches
- pt: points (1pt = 1/72in)
- pc: pica (1pc = 12pt)

A relative size is a size that is relative to another size. Some common relative size units include:

- em - Relative to the parent element's font size. Ex: 2em = 2 × parent element's font size.
- rem - Relative to the root element's font size. Ex: 1.5rem = 1.5 × <html> element's font size.
- vw - 1% of the viewport's width. Ex: 10vw = 10% of browser's width.
- vh - 1% of the viewport's height. Ex: 5vh = 5% of browser's height.
- % - Percentage of the element's font size. Ex: 120% = 20% larger than the current font size.

**Sizes specified with rem have no relationship with the parent element; thus, rem sizes are suitable for achieving a consistent style in elements located on multiple locations of the website. In this practice, since we are working on a single page and creating CSS rules for elements at specific locations, we will use *em* for defining font sizes.**

Add the following CSS rules to increase the font size of the headers in your website:

```css
h1 {
    font-size: 5em;
    font-style: italic;
    font-variant: small-caps;
}

h2 {
    font-size: 2em;
    font-variant: small-caps;
}

h3 {
    font-size: 1.5em;
}
```

> The rules above also includes other font properties, such as [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant) and [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style).
    
Try to declare all properties for the h1 element using the shorthand property [font](https://developer.mozilla.org/en-US/docs/Web/CSS/font).

### Text properties

In addition to font properties, CSS also provides text properties to control how text is displayed. Some common CSS text properties include:

- text-align: changes the horizontal alignment of text for an element. Possible values are: left, right, center, and justify.
- text-decoration: add or remove text decorations like underlining or a line-through. Possible values are: overline, line-through, underline, and none.
- text-transform: converts letters to UPPERCASE, lowercase, or Capitalizes Initial Letters. Possible values are: uppercase, lowercase, and capitalize.
- text-indent: specifies the first line's indentation amount.

Use the [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) property to text in the main header:

```css
h1 {
    font-size: 5em;
    font-style: italic;
    font-variant: small-caps;

    text-align: center;
}
```

> The main heading is a block element, thus it occupies an entire line on the webpage. The text-align property is useful for aligning text that lives inside a block element. We will use another technique later for centering other types of content. 

## Task 2: Sizing

A block element's content spans the width of the enclosing parent element by default. However, the content size can be changed with the width and height CSS properties:

- The width property specifies the content's width. Ex: width: 20px; makes the content 20px wide.
- The height property specifies the content's height. Ex: height: 30px; makes the content 30px high.

> A common error is to use width or height on inline elements. An inline element like <span> has a width and height equal to the size of the element's content. The width and height cannot be changed unless the inline element's display property is changed to inline-block (more on this later).

However, images are special because although they have a display value of inline by default, their dimensions are defined by the image's intrinsic values, like inline-block. 

Currently, the *width* and *height* attributes of the *img* tag control the size of the images displayed on our website. However, image size is unrelated to our HTML document's structure or content, and CSS rules should control any size adjustment.

Remove all the *width* and *height* attributes (if any) of the image elements and add the following CSS rules:

```css
header img {
    width: 960px;
}

article img {
    width: 400px;
}
```

> The rules above specify the size of the images using a length (absolute) value. When specifying only the width attribute of an image, the browser automatically calculates the image's height.
    
The values for the [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) and [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) dimension properties can be:

- length: defines the dimension as an absolute value.
- percentage: defines the dimension as a percentage of the containing block's height.
- auto: the browser will calculate and select a height for the specified element. This value is useful with other properties when centering block elements.

**Since image sizes and spacing between elements are rather independent, we will use pixels (an absolute size unit) for images and spacing.**
    
## Task 3: Borders & Spacing

The CSS properties that control borders and spacing:

- padding: specifies the padding thickness. Ex: padding: 5px; creates a 5 pixel padding around the content.
- border: specifies the border's thickness, style, and color. Ex: border: 2px solid blue; creates a solid blue border that is 2 pixels thick.
- margin: specifies the margin thickness. Ex: margin: 10px; creates a 10 pixel margin.

The padding and margin properties may have from 1 to 4 values:

- One value - Specifies uniform thickness around the box. Ex: margin: 20px; specifies 20px margin thickness around the box.
- Two values - Specifies top and bottom, right and left thickness. Ex: margin: 10px 20px; specifies 10px top and bottom margins and 20px right and left margins.
- Three values - Specifies top, right and left, and bottom thickness. Ex: margin: 10px 30px 20px; specifies 10px top margin, 30px right and left margins, and 20px bottom margin.
- Four values - Specifies top, right, bottom, and left thickness. Ex: margin: 10px 30px 20px 40px; specifies 10px top margin, 30px right margin, 20px bottom margin, and 40px left margin.

The padding, border, and margin CSS properties can apply only to one side by adding a -top, -left, -bottom, or -right suffix to the CSS property. Ex: padding-top:5px; specifies 5 pixels of padding above the content.

Adjust the spacing of the form elements:

```css
#experience_form {
    border: 1px solid black;
    padding: 10px;
    margin-bottom: 30px;
}

#experience_form input, #experience_form textarea {
    width: 300px;
    padding: 10px;
}

#experience_form textarea {
    height: 100px;
}
```

## Task 4: Centering the webpage

The rule below centers block elements by setting the top and bottom margins to 0 and the left and right margins to auto, i.e., they are determined by the browser. The *centering* effect is achieved by also setting the width (otherwise, a block element will take up the entire width of the page). Once you have specified the width, setting the left and right margins to auto will make the browser put an equal gap on each side of these elements. As a result, we can use this rule to center any block element on the page.

```css
.center {
    max-width: 960px;
    margin: 0 auto;
}
```

> When applying the previous rule to center the web page,  [max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) corresponds to the screen size in which we tailor our page to be rendered. 960px is a value commonly used for web pages designed to be rendered on large screens. We can also use *max-width* in combination with the *width* property to implement a responsive design, but we will discuss this topic later.

Create a new div to wrap all the content of the webpage and apply the rule above:

```html
<body>
    <div class="center"> 
        ...
    </div>
</body>
```

## Task 5: Putting everything together: Create a navigation menu

Let's add a navigation menu using the [nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav) element. Note the links in the navigation menu are local to the page, and they require each section to contain an id property with the same value.

```html
<nav>
    <ul>
        <li>
            <a href="#communities">Communities</a>
        </li>
        <li>
            <a href="#activities">Activities</a>
        </li>
        <li>
            <a href="#contact">Contact</a>
        </li>
    </ul>
</nav>
```

Browsers come with several default CSS rules for elements like links and list items. Apply the following CSS rules to style the links in the navigation menu:

```css
nav a {
    text-decoration: none;
    font-weight: bold;
    font-size: larger;
}
```

The following rule removes the decoration or bullet points included by default in list items:

```css
nav li {
    list-style-type: none;
}
```

We can use the [display](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property to transform *inline* elements into *block* elements. The *inline-block* value generates a block element box surrounding the element's content, as if it were a single inline box, with adjustable margin, padding, width, and height. 

Add the following rule to adjust the space between each item in the navigation menu:

```css

nav ul {
    padding: 0;
    text-align:center;
}

nav li {
    list-style-type: none;

    display: inline-block;
    padding: 10px;
}
```

### Pseudo-classes
    
We will [pseudo-classes](https://www.w3schools.com/css/css_pseudo_classes.asp) to style the link items in the navigation bar to achieve the following visual presentation:
- Show links as gray by default using the hexadecimal value of DCDCDC.
- Show unvisited and visited links with the same default gray color.
- The links should turn white when the user hovers the pointer over the links.
- The links should turn white when the user clicks on them.

Use a hexadecimal code to specify the white color.

```css
/* unvisited link */
nav a:link {
  color: #DCDCDC;
}

/* visited link */
nav a:visited {
  color: #DCDCDC;
}

/* mouse over link */
nav a:hover {
  color: white;
}

/* selected link */
nav a:active {
  color: white;
}    
```

> Pseudo-classes in CSS allow you to change the default styles associated with the different states of link elements that result from interactions between the user and the elements. For example, the user hovering the mouse or pointer on a link causes the link to be in the state of hover.

## Task 6: Layout (Advanced)
    
An essential aspect of styling a website is the layout. The layout is the arrangement of all visual elements on a webpage. The traditional way in CSS to handle layout consisted of using floats and positioning properties, which often involved writing intricate HTML and CSS rules. The Flexible Box Layout, commonly known as Flexbox, and Grid are two popular alternatives to cope with the limitations of floats and position properties. In this tutorial, we will use flex.

To use flex, we first have to create a container using an element with a display type of flex so that every descendent element within it becomes a flex item. The default behavior of flex items is to stack side to side.
Then, we can control the presentation of those flex items using several flexbox CSS properties applied to the items themselves or the container.

The content of each activity would look better if positioned to the right of each activity's photo. The CSS rules below use flex to position the content left, causing the description and features list of each activity to appear next to the activity's photo:

```css
.flex-container {
 display: flex;   
}
```

Use the following HTML as a guide to style the content of each actvity using the CSS rule above: 

```html
<article class="activity">
    <!-- Self-contained content intended to be independently distributable -->
    <h3>The Lake Challenge</h3>
    <figure class="flex-container">
        ...
    </figure>
</article>
```

Adjust the spacing of the elements reloated to each activity:

```css
.activity img {
    margin-right: 10px;
}
    
.activity figure {
    margin-top: 0;
}
    
.activity ul {
    padding: 0;
}
```

Place the bullet points of each activity's features inside the element's content box:

```css
.activity li {
    list-style-position: inside;
}
```
