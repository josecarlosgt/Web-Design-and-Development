# Tutorial: Styling the content of your website

CSS (Cascading Style Sheets) is a language for describing how a web page is styled for visual presentation.

## Instructions

This document explains the steps for styling content in a HTML document using CSS. Each task below provides links that explain the purpose CSS properties and techniques.

Before starting with Task 1, download and unzip the [base zipped folder](https://github.com/josecarlosgt/Web-Design-and-Development/raw/tutorial-4-styling-css/base.zip). Create a css folder with an external CSS stylesheet with the name: *mystyel.css*. Include the external stylesheet in the index.html file:

```html
<head>
    ...
    <link rel="stylesheet" href="css/mystyle.css">
</head>
```

## Task 1: Styling text

### Font properties

Many CSS properties control the font properties for displaying text. CSS font properties include:

- [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family): specifies the font family, such as "Times New Roman" or serif.
- [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size): changes the font size, such as 120%, small, or 12px.
- [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight): specifies the font weight, such as normal or bold.
- [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style): changes the text style, such as normal, italic, or oblique.
- [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant): specifies the variant of the text, such as normal or small-caps.
- [font](https://developer.mozilla.org/en-US/docs/Web/CSS/font): is shorthand for setting several font properties at the same time. E.g., font: italic 12pt Georgia, serif;

**font-family**

The [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property contains a list of fonts specified as family names separated by commas.
A family name is the name of a specific font, like "Times New Roman", "Arial", or "Georgia". Family names containing spaces must be wrapped in quotations marks, while family names without spaces do not.

A generic family is a more general group of fonts, like serif, sans-serif, cursive, fantasy, or monospace. The web browser will use the first font listed that is available.

> A good practice is to start the list with the intended font and end with a generic family. E.g., font-family: Arial, Helvetica, sans-serif;

This [link](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#some_common_font_families) contains a list of common font famliies:

Use a type selector targeting the *body* element to add the following CSS rule that gives the text of your website a sharp look:

```css
body {
    font-family: Arial, sans-serif;
}
```

> Serif fonts convey a classic, elegant, or traditional feel. In contrast, the clean lines and sharp edges of sans-serif fonts are more appropriate for more direct communication. For this reason, sans-serif fonts are more common in Web development as they render out content on a screen more clearly, which increases legibility for users across different devices.

**font-size**

The [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) can be specified using a predefined size name, a relative size name, or a number with an absolute or relative size unit.

The predefined size names are xx-small, x-small, small, medium, large, x-large, and xx-large, where medium is the default size. The relative size names are smaller and larger which change the font size for an element to be smaller or larger than the font size of the parent element.

An absolute size is a size that is fixed and independent of other CSS sizes. Absolute size units include:

- px: pixels (1px = 1/96in)
- cm: centimeters
- mm: millimeters
- in: inches
- pt: points (1pt = 1/72in)
- pc: pica (1pc = 12pt)

A relative size is a size that is relative to another size. Some common relative size units include:

- em - Relative to the parent element's font size. E.g., 2em = 2 × parent element's font size.
- rem - Relative to the root element's font size. E.g., 1.5rem = 1.5 × <html> element's font size.
- vw - 1% of the viewport's width. E.g., 10vw = 10% of browser's width.
- vh - 1% of the viewport's height. E.g., 5vh = 5% of browser's height.
- % - Percentage of the element's font size. E.g., 120% = 20% larger than the current font size.

>Sizes specified with rem have no relationship with the parent element; thus, rem sizes are suitable for achieving a consistent style in elements located on multiple locations of the website. In this practice, since we are working on a single page and creating CSS rules for elements at specific locations, we will use *em* for defining font sizes.

Use type selectors to specify the sizes of the headers on the webpage:

```css
h1 {
    font-size: 6em;
    font-variant: small-caps;
}

h2 {
    font-size: 3em;
    font-variant: small-caps;
}
```

> The rules above also includes other font properties, such as [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant).
    
Try to declare all properties for the h1 element using the shorthand property [font](https://developer.mozilla.org/en-US/docs/Web/CSS/font).

Create a rule with a class named *bold* to display in bold the text used as labels in the features list for each activity. Use the [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property:

```css
.bold {
    font-weight: bold;
}
```

Use an id selector to display in bold the label elements in the contact form :

```css
#experience_form label {
    font-weight: bold;
}
```

### Text properties

In addition to font properties, CSS also provides text properties to control how text is displayed. Some common CSS text properties include:

- [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align): changes the horizontal alignment of text for an element. Possible values are: left, right, center, and justify.
- [text-decoration](): add or remove text decorations like underlining or a line-through. Possible values are: overline, line-through, underline, and none.
- [text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration): converts letters to UPPERCASE, lowercase, or Capitalizes Initial Letters. Possible values are: uppercase, lowercase, and capitalize.
- [text-indent](https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent): specifies the first line's indentation amount.

Use the [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) property to text in the main header and footer:

```css
h1 {
    font-size: 6em;
    font-variant: small-caps;

    text-align: center;
}

footer {
    text-align: center;
}
```

> The main heading is a block element, thus it occupies an entire line on the webpage. The text-align property is useful for aligning text that lives inside a block element. We will use another technique later for centering other types of content. 

## Task 2: Sizing

A block element's content spans the width of the enclosing parent element by default. However, the content size can be changed with the width and height CSS properties:

- The [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) property specifies the content's width. E.g.,: width: 20px; makes the content 20px wide.
- The [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) property specifies the content's height. E.g.,: height: 30px; makes the content 30px high.

The values for the [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) and [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) dimension properties can be:

- length: defines the dimension as an absolute value.
- percentage: defines the dimension as a percentage of the containing block's height.
- auto: the browser will calculate and select a height for the specified element. This value is helpful with other properties when centering block elements.

> Since sizes of elements like inputs and spacing between elements are rather independent, we will use pixels (an absolute size unit) for images and spacing.

Use a descendant selector to style the header image as full-width. Descendant selectors are a form of [CSS combinators](https://www.w3schools.com/css/css_combinators.asp) that multiple selectors.  

```css
header img {
    width: 100%;
}
```

> A common error is using width or height on inline elements. An inline element like <span> has a width and height equal to the size of the element's content. The width and height cannot be changed unless the inline element's display property is changed to inline-block. However, images are special because although they have a display value of inline by default, their dimensions are defined by the image's intrinsic values, like inline-block. 

Increase the width of the input elements to a fixed size of 300px using [attribute selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#attribute_selectors). These selectors give you different ways to select elements based on a certain attribute:

```css
#experience_form input[type="text"], input[type="email"] {
    width: 300px;
} 

#experience_form textarea {
    width: 100%;
    height: 100px;
}
```

> Note that size is unrelated to an HTML document's structure; thus, CSS rules should control any size adjustment.
    
## Task 3: Layout and spacing properties

The following CSS properties control spacing:

- [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding): specifies the padding thickness. E.g., padding: 5px; creates a 5 pixel padding around the content.
- [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin): specifies the margin thickness. E.g., margin: 10px; creates a 10 pixel margin.

![The box model](img/box-model.png)

### Layout: Centering the webpage

An essential aspect of styling a website is the layout. The layout is the arrangement of all visual elements on a webpage. In this part, we will adjust the layout of the webpage by aligning block elements to the center and creating grids of two columns.

The rule below centers block elements by setting the top and bottom margins to 0 and the left and right margins to auto, i.e., they are determined by the browser. The *centering* effect is achieved by also setting the width (otherwise, a block element will take up the entire width of the page). Once you have specified the width, setting the left and right margins to auto will make the browser put an equal gap on each side of these elements. As a result, we can use this rule to center any block element on the page.

Create a container class that centers relative to the width of the page the content of the elements inside: 

```css
.container {
    margin-top: 0;
    margin-right: auto;
    margin-bottom: 50px;
    margin-left: auto;

    max-width: 960px;
}
```

> When applying the previous rule to center the web page,  [max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) corresponds to the screen size in which we tailor our page to be rendered. 960px is a value commonly used for web pages designed to be rendered on large screens. We can also use *max-width* in combination with the *width* property to implement a responsive design, but we will discuss this topic later.

The padding and margin properties may take 1 to 4 values as a shorthand to write spacing rules more concisely:

- One value - Specifies uniform thickness around the box. E.g., margin: 20px; specifies 20px margin thickness around the box.
- Two values - Specifies top and bottom, right and left thickness. E.g., margin: 10px 20px; specifies 10px top and bottom margins and 20px right and left margins.
- Three values - Specifies top, right and left, and bottom thickness. E.g., margin: 10px 30px 20px; specifies 10px top margin, 30px right and left margins, and 20px bottom margin.
- Four values - Specifies top, right, bottom, and left thickness. E.g., margin: 10px 30px 20px 40px; specifies 10px top margin, 30px right margin, 20px bottom margin, and 40px left margin.

Thus, we can rewrite the rule above using the following shorthand:

```css
.container {
    max-width: 960px;
    margin: 0 auto 50px auto;
}
```

### Layout: Multicolumn grids

The traditional way in CSS to handle multicolumn grids consisted of using floats and positioning properties, which often involved writing intricate HTML and CSS rules. The Flexible Box Layout, commonly known as [Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox), and Grid are two popular alternatives to cope with the limitations of floats and position properties. In this tutorial, we will use flex.

To use flex, we first have to create a container using an element with a display type of flex so that every descendent element within it becomes a flex item. The default behavior of flex items is to stack side to side.
Then, we can control the presentation of those flex items using several flexbox CSS properties applied to the items themselves or the container.

The content of each activity would look better if positioned to the right of each activity's photo. The CSS rules below use flex to position the content left, causing the description and features list of each activity to appear next to the activity's photo. Create a grid of two columns by using a flex container and adjusting the padding of the elements in the flex container:

Use the [display](https://developer.mozilla.org/en-US/docs/Web/CSS/display) to create a flex container for each activity:

```css
.activity-row {
    display: flex;
    margin-bottom: 20px;
}

.activity-col {
    padding: 10px;
}
```

Apply the same technique to the communities section:

```css
#communities {
    display: flex;
}
```

We can also use the [display](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property to transform *inline* elements into *block* elements. The *inline-block* value generates a block element box surrounding the element's content, as if it were a single inline box, with adjustable margin, padding, width, and height. 

```css
#experience_form input, #experience_form textarea, #experience_form label {
    display: block;

    margin-bottom: 10px;
}
```

Add the following rules to adjust the margin and padding between elements of the contact form:

```css
#experience_form input, #experience_form textarea {
    margin-bottom: 10px;
    padding: 10px;
}
```

## Task 4: Borders

[Border](https://developer.mozilla.org/en-US/docs/Web/CSS/border) properties specifies the border's thickness, style, color, among other aspects. E.g., border: 2px solid blue; creates a solid blue border that is 2 pixels thick.

Draw a separator dividing each section on the web page by drawing a border at the bottom of each section:

```css
.container {
    max-width: 960px;
    margin: 0 auto 50px auto;

    border-bottom: 1px solid grey;
}
```

The [border-radius](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius) property rounds the corners of an element's outer border edge. Change the rectangular shape of the images in the image of each activity to circular:

```css
.activity-col img {
    border-radius: 50%;
}
```

> The padding, border, and margin CSS properties can apply only to one side by adding a -top, -left, -bottom, or -right suffix to the CSS property. E.g., padding-top:5px; specifies 5 pixels of padding above the content.

## Task 5: Styling the navigation menu

Create add a navigation menu using the [nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav) element. Note the links in the navigation menu are local to the page, and they require each section to contain an id property with the same value.

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
}
```

The following rule removes the decoration or bullet points included by default in list items:

```css
nav li {
    list-style-type: none;
}
```

Add the following rule to adjust the space between each item in the navigation menu:

```css

nav ul {
    background-color: black;
    margin: 0;
    padding: 0;
    text-align: right;
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
