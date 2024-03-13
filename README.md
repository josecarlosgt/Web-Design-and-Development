# Tutorial: Styling the content of your website

CSS (Cascading Style Sheets) is a language that describes how a web page is styled for visual presentation. We will style the content of our page by leveraging four concepts of graphic design to transmit a message to an audience effectively: typography, color, image composition, and layout.  

## Instructions

This document explains the steps for styling content in an HTML document using CSS. Each task below provides links that describe the purpose of common CSS properties.

[The styling work explained in the tasks implement the design contained in this mockup](https://drive.google.com/file/d/17DU9uiLM94beeoNBodDh5CYSwKlthBav/view?usp=sharing).

Before starting, download and unzip the [base zipped folder](https://github.com/josecarlosgt/Web-Design-and-Development/raw/tutorial-4-styling-css/base.zip) and define a location for the CSS rules to be created in each task. You can either use an external or internal stylesheet.

Using an external stylesheet requires *linking* the external stylesheet in your index.html file:

```html
<head>
    ...
    <link rel="stylesheet" href="css/mystyle.css">
</head>
```

Alternatively, you can use an internal stylesheet:

```html
<head>
    ...
    <style>
        /* CSS rules go here */
    </style>
</head>
```

## Task 1: Typography

### Font properties

Many CSS properties allow us to display text in a way that is visually appealing to the reader. CSS font properties include:

- [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family): specifies the font family, such as "Times New Roman" or serif.
- [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size): changes the font size, such as 120%, small, or 12px.
- [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight): specifies the font weight, such as normal or bold.
- [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style): changes the text style, such as normal, italic, or oblique.
- [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant): specifies the variant of the text, such as normal or small-caps.
- [font](https://developer.mozilla.org/en-US/docs/Web/CSS/font): is shorthand for setting several font properties at the same time. For example, *font: italic 12pt Georgia, serif;*

### font-family

The [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property contains a list of fonts specified as family names separated by commas. A family name is the name of a specific font, like "Times New Roman", "Arial", or "Georgia". Family names containing spaces must be wrapped in quotation marks, while family names without spaces do not.

A generic family is a more general group of fonts, like serif, sans-serif, cursive, fantasy, or monospace. The web browser will use the first available font listed. [This link contains a list of typical font families on the Web](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#some_common_font_families).

A good practice is to start the list with the intended font and end with a generic family. For example, *font-family: Arial, Helvetica, sans-serif*. Use a type selector targeting the *body* element to add the following CSS rule that gives the text of your website a sharp look:

```css
body {
    font-family: Arial, sans-serif;
}
```

> Serif fonts convey a classic, elegant, or traditional feel. In contrast, the clean lines and sharp edges of sans-serif fonts are more appropriate for direct communication. For this reason, sans-serif fonts are more common in web development as they render content on a screen more clearly, increasing users' legibility across different devices.

## Task 2: Image composition & sizing

Images are inline elements but also support properties characteristic of block elements like width and height. A block element's content spans the width of the enclosing parent element by default. However, the content size can be changed with the width and height CSS properties:

- The [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) property specifies the content's width. For example,: *width: 20px;* makes the content 20px wide.
- The [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) property specifies the content's height. For example,: *height: 30px;* makes the content 30px high.

The units for the [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) and [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) dimension properties can be:

- length: defines the dimension as an absolute value, such as pixels.
- percentage: defines the dimension as a percentage of the containing block's height.
- auto: the browser will calculate and select a height for the specified element. This value is helpful with other properties when centering block elements.

Since sizes of elements like inputs and spacing between elements are relatively independent of other elements, we usually use pixels (an absolute size unit) when specifying the size of elements and adjusting the space between elements.

When including images, it is a good practice to specify the height and width of the image directly on the *img* tag to keep the page rendering stable while the image loads. Specify the following sizes for the images on the page:

```html
...
<img src="img/panoramic-laguna-brava-2000.jpeg" width="960" height="236" alt="Panoramic view of Laguna Brava lake" title="Laguna Brava">
...
<img src="img/kayaking.jpeg" width="400" height="400" alt="View of the lake with kayak on the horizon">
...
<img src="img/boat-ride.jpeg" width="400" height="400" alt="View of rustic boat on the lake's shore">
...
```

Now, we will style the elements in the contact form. Specifying a unique ID for the form will help us to create CSS rules specific to the elements in the form.

```html
<form id="experience_form">
    ...
</form>
```
...

Increase the width of the input elements to a fixed size of 300px using [attribute selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#attribute_selectors). These selectors give you different ways to select elements based on a particular attribute. Then, style the textarea element so that it occupies all the width of the page. 

```css
#experience_form input[type="text"], input[type="email"] {
    width: 300px;
} 

#experience_form textarea {
    width: 100%;
    height: 100px;
}
```

> Note that the rules above use a descendant selector to style the form elements. Descendant selectors are a form of [CSS combinators](https://www.w3schools.com/css/css_combinators.asp) that combine multiple selectors based on the page's hierarchical structure.

## Layout

Layout is the the visual arrangement of all elements on a webpage. In invovles the principles of *contrast*, *alignment*,  *balance*, *proximity*, *space*, *balance*, and *repetition*. 

## Task #3: Contrast

*Contrast* is about adding visual prominence through various properties like size, color, and typography.

### font-size

The [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) can be specified using a predefined size name, a relative size name, or a number with an absolute or relative size unit.

The predefined size names are xx-small, x-small, small, medium, large, x-large, and xx-large, where medium is the default size. The relative size names are smaller and larger, which changes the font size for an element to be smaller or larger than the font size of the parent element.

An absolute size is a size that is fixed and independent of other CSS sizes. Absolute size units include:

- px: pixels (1px = 1/96in)
- cm: centimeters
- mm: millimeters
- in: inches
- pt: points (1pt = 1/72in)
- pc: pica (1pc = 12pt)

A relative size is a size that is relative to another size. These include:

- em - Relative to the parent element's font size. For example, 2em = 2 × parent element's font size.
- rem - Relative to the root element's font size. For example, 1.5rem = 1.5 × <html> element's font size.
- vw - 1% of the viewport's width. For example, 10vw = 10% of browser's width.
- vh - 1% of the viewport's height. For example, 5vh = 5% of browser's height.
- % - Percentage of the element's font size. For example, 120% = 20% larger than the current font size.

>Sizes specified with rem have no relationship with the parent element; thus, rem sizes are suitable for achieving a consistent style, as all elements sized with the "rem" unit will be updated automatically to maintain their relative size.

Use the following type selectors to specify the sizes of the headers on the webpage:

```css
h1 {
    font-size: 6rem;
}

h2 {
    font-size: 3rem;
}
```

### font-weight

Create a rule with a class named *bold* to display the text used as labels for each activity's features list in bold. Use the [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property:

```css
.bold {
    font-weight: bold;
}
```

Add the *bold* class to all elements to be displayed in bold, including the activity's features and the label elements in the contact form. Create *span* elements when necessary.

## Task #4: Alignment

*Alignment* involves arranging elements relative to the page or other elements to create order.

### Text properties

CSS provides several text properties to control how text is displayed. Some common CSS text properties include:

- [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align): changes the horizontal alignment of text for an element. Possible values are left, right, center, and justify.
- [text-decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration): add or remove text decorations like underlining or a line-through. Possible values are overline, line-through, underline, and none.
- [text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform): converts letters to UPPERCASE, lowercase, or Capitalizes Initial Letters. Possible values are uppercase, lowercase, and capitalize.
- [text-indent](https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent): specifies the first line's indentation amount.

Use the [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) property to center text in the main header and footer:

```css
h1 {
    font-size: 6em;
    text-align: center;
}

footer {
    text-align: center;
}
```

> The main heading is a block element, which occupies the whole width of the webpage. The text-align property helps align text that lives inside a block element. We will use other techniques to center block elements on the page.

## Task #5: Space

*Space* refers to the background against which page content is seen. We can control space through the following CSS properties:

- [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding): specifies the padding thickness. For example, padding: 5px creates a 5-pixel padding around the content.
- [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin): specifies the margin thickness. For example, if the margin is 10px, it creates a 10-pixel margin.

![The box model](img/box-model.png)

### Adjusting the space between elements in the form

Use the padding and margin properties and the [display](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property to transform *inline* elements into *block* elements. The *inline-block* value generates a block element box surrounding the element's content like a single inline box with adjustable margin, padding, width, and height.

```css
#experience_form input, #experience_form textarea, #experience_form label {
    display: block;
    margin-bottom: 10px;
}
```

```css
#experience_form input, #experience_form textarea {
    padding: 10px;
}
```

### Centering the webpage's content

An essential aspect of styling a website is the layout. The layout is the arrangement of all visual elements on a webpage.

In this task, we will adjust the layout of the webpage by aligning block elements to the center. The rule below centers block elements by setting the top and bottom margins to 0, and the left and right margins to auto, i.e., the browser automatically determine them. The *centering* effect is achieved by setting the width (otherwise, a block element will take up the entire width of the page). Once you have specified the width, setting the left and right margins to auto will make the browser put an equal gap on each side of these elements. As a result, we can use this rule to center any block element on the page.

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

Add the *container* class to the header and main elements of the page.

When applying the previous rule to center the web page, [max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) corresponds to the screen size in which we tailor our page to be rendered. 960px is a value commonly used for web pages designed to be rendered on large screens. We can also use *max-width* in combination with the *width* property to implement a responsive design, but we will discuss this topic later.

The padding and margin properties may take 1 to 4 values as a shorthand to write spacing rules more concisely:

- One value - Specifies uniform thickness around the box. For example, *margin: 20px;* specifies 20px margin thickness around the box.
- Two values - Specify the top, bottom, right, and left thickness. For example, *margin: 10px 20px;* specifies 10px top and bottom margins and 20px right and left margins.
- Three values - Specify top, right, left, and bottom thickness. For example, margin: *10px 30px 20px;* specifies 10px top margin, 30px right and left margins, and 20px bottom margin.
- Four values - Specifies top, right, bottom, and left thickness. For example, *margin: 10px 30px 20px 40px;* specifies 10px top margin, 30px right margin, 20px bottom margin, and 40px left margin.

Thus, we can rewrite the rule above using the following shorthand:

```css
.container {
    max-width: 960px;
    margin: 0 auto 50px auto;
}
```

### Task 6: Balance, Proximity, and Repetition

*Balance* relates to how elements are weighted against each other on different sides of the page to deliver a sense of completion. *Proximity* consists of placing related items close to each other so the viewer can perceive them as related while placing unrelated items apart. *Repetition* creates consistency within a hierarchical system.

We will balance the page's main content and the excess of the page's space by creating a grid of two columns. We will display the activity image in one column and the description in another.

The traditional way in CSS to handle multicolumn grids consisted of using floats and positioning properties, often involving writing intricate HTML and CSS rules. The Flexible Box Layout, commonly known as [Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox), and Grid are two popular alternatives to cope with the limitations of floats and position properties. In this tutorial, we will use flex.

To use flex, we first have to create a container using an element with a display type of flex so that every descendent element becomes a flex item. The default behavior of flex items is to stack side to side.
Then, we can control the presentation of those flex items using several flexbox CSS properties applied to the items themselves or the container.

The content of each activity would look better if positioned to the right of each activity's photo. The CSS rules below use flex to position the content left, causing each activity's description and features list to appear next to the activity's photo. Create a grid of two columns by using a flex container and adjusting the padding of the elements in the flex container:

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

### Borders

We will use a border to isolate the page's main content and display it further from the remaining elements. [Border](https://developer.mozilla.org/en-US/docs/Web/CSS/border) properties specify the border's thickness, style, and color, among other aspects. For example, *border: 2px solid blue;* creates a solid blue border 2 pixels thick.

Draw a separator dividing the main section on the web page by drawing borders on the main element:

```css
main {
    border-width: 1px;
    border-style: solid;
    border-width: grey; 
}
```

The rule above can be simplified using the *border* shorthand property:

```css
main {
    border: 1px solid grey;
}
```

The border shorthand property can also be applied to element sides:

```css
main {
    border-top: 1px solid grey; 
    border-bottom: 1px solid grey; 
}
```

> The padding, border, and margin CSS properties can apply only to one side by adding a -top, -left, -bottom, or -right suffix to the CSS property. For example, *padding-top:5px;* specifies 5 pixels of padding above the content.

The [border-radius](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius) property rounds the corners of an element's outer border edge. Change the rectangular shape of the images in the image of each activity to circular:

```css
.activity-col img {
    border-radius: 50%;
}
```

## Task 7: Color and creating an in-page navigation menu

Add a navigation menu using the [nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav) element. Note that the links in the navigation menu are local to the page, and each section must contain an ID property with the same value.

```html
<nav>
    <ul>
        <li>
            <a href="#activities">Things to Do</a>
        </li>
        <li>
            <a href="#contact">Contact</a>
        </li>
    </ul>
</nav>
```

Browsers have several default CSS rules for elements like links and list items. Apply the following CSS rules to style the links in the navigation menu:

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

> Pseudo-classes in CSS allow you to change the default styles associated with the different states of link elements that result from interactions between the user and the elements. For example, the user hovering the mouse or pointer on a link causes the link to be in the hover state.