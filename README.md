# Tutorial #4: Styling the content of your website
After structuring the content of your website using HTML, you are ready to start styling it using CSS. Implementing CSS rules to make your webpage look like you want requires time, and you could easily spend an entire semester learning CSS techniques for controlling the presentation of a website.

Thus, we will use a CSS framework called [Bootstrap](https://getbootstrap.com/), one of the most popular frameworks for styling websites. 
We will use Bootstrap for two reasons:
1. Bootstrap makes it faster to style a webpage
2. Bootstrap allows you to build responsive websites and applications

In this tutorial, you will find several links to [Bootstrap official documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) in each task. This tutorial's main purpose is to familiarize yourself with the Bootstrap documentation and apply Bootstrap main CSS classes to style your website.

Before proceeding, download the version of the [website](https://github.com/josecarlosgt/Web-Design-and-Development/tree/tutorial-2-designing-and-structuring-content) created in the previous tutorial containing the structure and images. In this tutorial, we will apply Bootstrap styling rules to the index.html file.

## Task 1: Installing bootstrap
Reference: [Bootstrap Docs > Introduction](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

The easiest way to add Bootstrap to your website is using the content delivery network (CDN) servers recommended by Boostrap. More sophisticated ways of using Bootstrap require downloading the source files, which allows higher customization.

We will use the CDN resources:
- Include the CSS resource into the \<head\> element
- Include the JavaScript resource right before the closing </body> tag
- You also need to include a [responsive meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag) which ensures proper rendering of your webpage on mobile devices. This is necessary because Bootstrap automatically optimizes your code for mobile devices.

Put it all together and your webpage should look like this:
```html
<!doctype html>
<html lang="en">
    <head>
    ...
       
        <!-- Responsive metatag -->    
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    ...
    </head>
    <body>
        <!-- Bootstrap JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        
        ...
  </body>
</html>       
```
## Task 2: Styling text and images

### Reboot: [Bootstrap Docs > Content > Reboot](https://getbootstrap.com/docs/5.0/content/reboot/)

When you start using Bootstrap out of the box, it applies a reboot of the default browser styles. This means Bootstrap strips out all the default styles like margin, padding, font styles, and size, replacing them with a clean and basic set of default Bootstrap styles. The purpose of this reboot is to provide you with a simple baseline to build upon the style of your website that is consistent across browsers.  

### Typography: [Bootstrap Docs > Content > Typography](https://getbootstrap.com/docs/5.0/content/typography/)

Bootstrap also provides several features for styling text content that allow you to create customized headings, paragraphs, lists, and more.

The feature [display headings](https://getbootstrap.com/docs/5.0/content/typography/#display-headings) allows you to display your headings in a larger, slightly more prominent style.

Add "display-2" to h1, "display-5" to h2, and "display-6" to h3 elements:

```html
<h1 class="display-2">...</h1>
<h2 class="display-5">...</h2>
<h3 class="display-6">...</h3>
```
> Note the display headings classes use a numbering independent of the HTML heading elements. The display headings classes can be used with any HTML element.

The feature [lead](https://getbootstrap.com/docs/5.0/content/typography/#lead) allows you to make paragraphs stand out. We can use this feature for the first paragraph on our website to make it look slightly bigger and relevant than the rest of the paragraphs:

```html
<p class="lead">
    Laguna Brava Ecotourism is an organization run by <em>local community members</em> based in Laguna Brava. Laguna Brava is a <a href="https://en.wikipedia.org/wiki/Karst">karstic lake</a> of incomparable beauty located in western Guatemala. Laguna Brava is located in a remote and highly underdeveloped region, so reaching and exploring the lake takes a mix of extreme adventure and intimate contact with nature. The lake beauty lies in the colours variety of its waters, which depends on the sun's position. Laguna Brava is also known as Yolnabaj by the region's inhabitants, which translates as "rough lake". Despite its name, the waters of Laguna Brava Laguna are so calm that they instantly awaken a deep feeling of peace.
</p>
```

Use the [unstyled lists](https://getbootstrap.com/docs/5.0/content/typography/#lists) feature to remove the decoration and margin of list items:
```html
<ul class="list-unstyled">
    <li>Duration: 5 hours approx.</li>
    <li>Price: $50 USD</li>
    <li>Minimum: 2 pax</li>
</ul>
```

### Images: [Bootstrap Docs > Content > Images](https://getbootstrap.com/docs/5.0/content/images/)

Images in Bootstrap are made responsive with the *.img-fluid* class. Add this class to the three images in the website:

```html    
<img src="img/panoramic-laguna-brava-2.jpg" class="img-fluid" alt="Laguna Brava lake image">
...
```

Notes:
- Adding responsive behavior usually involves adjusting the [max-width](https://www.w3schools.com/cssref/pr_dim_max-width.asp) CSS property of HTML elements. This property defines the maximum width of an element's content and it prevents the element from becoming larger than the value specified by max-width.
- img-fluid maintains a 100% max-width regardless of the size of the screen, so images never become larger than their parent elements (containers). As a result, images are resized to fit the screen. 

## Task 3: Leveraging class utilities
Bootstrap provides several utility classes for styling content. Many of these classes follow conventions on how to refer to the sides of HTML elements.
For example,
- *start* refers to left
- *end* refers to right
- *top* and *bottom* remain the same
These terms act as suffixes in several classes that control style aspects such as borders, alignment, and spacing, as you will see below.

### Text: [Bootstrap Docs > Utilities > Text](https://getbootstrap.com/docs/5.0/utilities/text/)

Bootstrap provides common text utilities to control weight, alignment, and more.

Using [font weight](https://getbootstrap.com/docs/5.0/utilities/text/#font-weight-and-italics) classes, control the style of the labels on the guided visits options:

```html
<span class="fw-bold">Duration: </span>...</li>
<span class="fw-bold">Price: </span>...</li>
<span class="fw-bold">Minimum: </span>...</li>
```

Using [text decoration](https://getbootstrap.com/docs/5.0/utilities/text/#text-decoration) classes, adjust the style of the safety statement on the introductory text to the guided visits:

```html
<strong class="text-decoration-underline fw-normal">we provide life vests and local guides who know the lake very well to take care of your safety.</strong>
 ```

Using [text alignment](https://getbootstrap.com/docs/5.0/utilities/text/#text-alignment) classes, center the main heading and the headings in guided visits sections:

```html
<h1 class="display-2 text-center">...</h1>
<h3 class="display-6 text-center">...</h3>
```
Notes:
- Text alignment classes also include *text-start* for aligning text to the left and *text-end* for aligning text to the right. 

### Borders: [Bootstrap Docs > Utilities > Borders](https://getbootstrap.com/docs/5.0/utilities/borders/)

Border utilities allow you to style the border and border-radius of an element like images and buttons. For example:

```html
<span class="border"></span>
<span class="border-top"></span>
<span class="border-end"></span>
<span class="border-bottom"></span>
<span class="border-start"></span>
```

[Border-radius](https://getbootstrap.com/docs/5.0/utilities/borders/#border-radius) classes in Bootstrap allow you to modify the border-radius property. [border-radius](https://www.w3schools.com/cssref/css3_pr_border-radius.asp) is a CSS property that defines the radius of an element's corners. Round the corner of the guided visits images: 

```html
<img src="img/kayak.jpg" class="img-fluid rounded-pill" alt="Lake challenge kayak image">
```

This effect gives the images a more natural appearance by eliminating the abrupt pauses that result when lines change direction in sharp corners.

### Color: [Bootstrap Docs > Utilities > Colors](https://getbootstrap.com/docs/5.0/utilities/colors/)

Color utilities include predefined classes to colorize text. Adjust the color and font weight of the warning statement in the first guided visit option:

```html
<strong class="text-warning fw-bold">This guided visit is physically demanding, and we recommend it for only those in excellent physical condition.</strong>
```

Bootstrap enables more comprehensive customization for working with colors. For now, we will use the default [color system](https://getbootstrap.com/docs/5.0/customize/color/). You can also use this system for defining [background colors](https://getbootstrap.com/docs/5.0/utilities/background/) of any HTML element.

### Spacing: [Bootstrap Docs > Utilities > Spacing](https://getbootstrap.com/docs/5.0/utilities/spacing/)

Spacing utilities provide a wide range of shorthand classes to specify margin and padding. These shorthand classes follow the notation {property}{sides}-{size} to set specific values of margin and padding.

Add a gap between the sections following the lead paragraph by adding a vertical margin. Since we want to add a margin to the entire section (title and paragraph), we wrap all the elements in the section in a *div* element that acts as a container. Then, we apply the spacing shorthand class.

Add the *div* container to the "Who are we?" and "What do we offer?" sections:

```html
<div class="my-4">
    <h2 class="display-5">...</h2>
    <p>
        ...
    </p>
</div>
```

Note that *my-4* follows the notation {property}{sides}-{size} where
- {property} is *m* (margin)
- {sides} is *y* (vertical)
- {size} is *4*
- Look at the documentation for learn about the different configuations

## Task 4: Creating containers
Reference: [Bootstrap Docs > Layout > Containers](https://getbootstrap.com/docs/5.0/layout/containers/)

Features:
- Containers are the most basic layout element in Bootstrap and are required to use the grid system, which you will use in the next task to arrange your content in rows and columns.
- Containers allow you to wrap your page content and then apply padding around the content.
- They can also center your content on the page in a central column.

Use the default container which sets a fixed width for screen sizes.

```html
<main class="container">
```

### Breakpoints

Bootstrap containers allow you to tailor the content of your webpage to fit a specific screen size. To represent screen sizes, Bootstrap use the concept of breakpoints. [Breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/) are the building blocks of responsive design in Bootstrap. Bootstrap includes six default breakpoints:
-X-Small
-Small
-Medium
-Large
-Extra large
-Extra extra large  

Each breakpoint has a dimension associated that represents a particular viewport or device screen size. The breakpoints serve as a system to specify responsive behavior in HTML elements. For example, if you want to tailor your webpage to be displayed in *large* screens (i.e., 992 pixels width or wider), you can wrap the webpage's content into a *container-lg* class container:

```html
<div class="container-lg">100% wide until large breakpoint</div>
```

This means the *div* container will keep constant widths to fit your content in large screens, *preserving paddings and center alignment.* If your webpage is displayed on smaller screens, the content will automatically occupy 100% of the screen. More technically, the breakpoints system specifies values for the max-width property.

Experiment with different container classes to appreciate the difference. What happens if you use the container-xxl class instead of the default container? Use the inspector tool to appreciate the difference.

## Task 5: Adjusting the grid layout
Reference: [Bootstrap Docs > Layout > Containers](https://getbootstrap.com/docs/5.0/layout/containers/)

[Bootstrap's grid layout system](https://getbootstrap.com/docs/5.0/layout/grid/) allows you to arrange content in columns and rows following a fully responsive design. The grid layout uses a twelve-column system which means the width of a single column can vary from one to twelve.

This system allows you, for example, to arrange your content three columns of size four each:

```html
<div class="container">
  <div class="row">
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
  </div>
</div>
```

Furthermore, you can add breakpoints to create a grid system that starts out stacked and becomes horizontal at the small breakpoint (sm):

```html
<div class="container">
    <div class="row">
        <div class="col-sm">
            Column
        </div>
        <div class="col-sm">
            Column
        </div>
        <div class="col-sm">
            Column
        </div>
    </div>
</div>
```

You can also adjust the size of the columns when they become horizontal:
```html
<div class="container">
    <div class="row">
        <div class="col-sm-8">
            Column
        </div>
        <div class="col-sm-2">
            Column
        </div>
        <div class="col-sm-2">
            Column
        </div>
    </div>
</div>
```

> When arranging your content in columns using Bootstrap grid system, you need to use a combination of *col* classes wrapped inside a *row* class container.

Use the *col-lg* class to display the content of the website as two columns for large screens (*lg* breakpoint) and as one column for smaller screens:

```html
<div class="row">
    <article class="col-lg">
        ...
    </article>
    <article class="col-lg">
        ...
    </article>
</div>
```

Another approach to defining responsive behavior is explicitly specifying the number of columns to display in each breakpoint. Use the responsive *.row-cols-* classes to quickly set the number of columns that best render your content. 

Using *.row-cols-* and the *lg* breakpoint, we can achieve the same behaviour that displays the content of the website as two columns for large screens and as one column for smaller screens:

```html
<div class="row row-cols-1 row-cols-lg-2">
    <article class="col">
        ...
    </article>
    <article class="col">
        ...
    </article>
</div>
```

Adjust the spacing between each \<article\> to add gaps both horiontally and vertically using horizontal padding (*px*) and bottom margin (*mb*) classes:

```html
<article class="col px-5 mb-4">
```

Also, adjust the spacing between the image and the text within each guided visit by enclosing the text and features list inside a *div* container with top margin:
```html
<div class="mt-2">
    ...
    <ul class="list-unstyled">
        ...
    </ul>
</div>
```

Result:
```html
<div class="row">
    <article class="col-lg px-5 mb-4">
        <h3 ...>...</h3>
        <img ...>
        <div class="mt-2">
            ...
            <ul class="list-unstyled">
                ...
            </ul>
        </div>        
    </article>
    <article class="col-lg px-5 mb-4">
        ...
    </article>
</div>
```

## Task 6: Creating buttons
Reference: https://getbootstrap.com/docs/5.0/components/buttons/

Bootstrap includes several predefined button styles. Add a "Book here" button in each guided visit using the *btn* class:

```html
<a class="btn btn-primary btn-sm" href="javascript:void(0)">Book here</a> 
```
> This button also specifies color and size.

## Task 7: Adding icons
Reference: https://icons.getbootstrap.com/

Finally, try out Bootstrap Icons library for adding icons to your webpage. To use Bootstrap icons library, you need to add the corresponding CSS resource into the \<head\> tag:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
```

Remember we adjusted the color of the warning statement in the first guided visit option? Add an exclamation icon to increase the attion of the viewer:

```html
<i class="bi bi-exclamation-triangle"></i>
```
>Icons are also a great way to make your content more accessible for people with color blindness.

Final result:
```html
Cross the four kilometres in a kayak guided by a local guide. <strong class="text-warning fw-bold"><i class="bi bi-exclamation-triangle"></i> This guided visit is physically demanding, and we recommend it for only those in excellent physical condition.</strong>
```

## Task 8: Making the header image full-height (EXTRA)

We could attempt to increase the appealing of our website by making the header image to fill the full height of the screen. These images are called *hero* or banner images, and they are commonly used together with the main headline to communicate the primary message of the webpage quickly.

Adding a full-height image requires additional CSS rules that we can add internally to the webpage:

```html
<style>
    /*
        Full page image: https://www.w3schools.com/howto/howto_css_full_page.asp
        Text on Images: https://css-tricks.com/design-considerations-text-images/
        Text shadow property: https://www.w3schools.com/cssref/css3_pr_text-shadow.asp
        CSS min-height Property: https://www.w3schools.com/cssref/pr_dim_min-height.asp 
    */
    header {
        background: #FFFFFF url('img/panoramic-laguna-brava-2.jpg') no-repeat center;
        background-size: cover;		
        height: 100vh;	
        min-height: 300px;
    }
    header div {
        position: absolute;
        top: 70%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
</style>
```

Notes:
- The [index.html](./index.html) file contains the final HTML document. You can view this webpage in GitHub Pages [here](https://josecarlosgt.github.io/Web-Design-and-Development/).
- The [index-fh-header.html](./index-fh-header.html) file contains another version that uses additional CSS rules to implement a full-height image header. You can view this webpage in GitHub Pages [here](https://josecarlosgt.github.io/Web-Design-and-Development/index-fh-header.html).
- Note that the additional CSS rules added in the *index-fh-header.html* version were moved to an external CSS file. 
