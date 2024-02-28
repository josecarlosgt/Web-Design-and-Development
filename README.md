# Tutorial: Structuring the content of your website

This document describes the steps for structuring information in an HTML document. The content is based on the narrative for the [Laguna Brava Ecotourism Website](https://docs.google.com/document/d/1km0BxhWLX4hsJDRVkEDGWBFxr76Hyf_FNUubJtaPo5c/edit?usp=sharing) created following [the web design process](https://docs.google.com/presentation/d/17QH5RDWIGE9UkEPn0g89vhl6Iw7_nao2lsCcfX6HS2o/edit?usp=sharing) discussed in class.

## Skills
- Structure content using HTML tags

Each task below provides links that explain the purpose of each HTML tag. These links point to two popular learning resources on web development:

- [Mozilla MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). This website contains detailed and up-to-date documentation on HTML.
- [W3Schools](https://www.w3schools.com/) This website contains examples and brief explanations of HTML.

We will use the following text. 

> *Page's Title:* Welcome to Laguna Brava Ecotourism
>
> *Welcome blurb:* Learn everything about the activities that Laguna Brava offers to its visitors.
>
> *Description of activities*  
> The Mayan communities of the Chuj ethnicity settled around the lake offer several activities that allow visitors to enjoy **Laguna Brava's** natural beauty. In these activities, members of the Laguna Brava community provide life vests and local guides who know the lake very well to ensure your safety.
>
> *Guided visits options*
>
> *Acitivy 1*  
> The Lake Challenge  
> Put your strengths to work by crossing the four kilometers in a kayak guided by a local guide. This **adventure** is physically demanding and recommended for only those in excellent physical condition.
> - Duration: 5 hours approx.
> - Price: USD 50
> - Minimum: 2 pax

## Preview

![Web page Preview](page-preview.jpg)

## Task 1: Creating the basic structure

Fill in the \<title\> element with a descriptive title and specify UTF-8 as the character encoding set (charset) using the meta tag.
Recall this title will appear on the browser's window or tab.

```html
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Laguna Brava Ecotourism</title>
    </head>
    <body>
    </body>
</html>
```

## Task 2: Adding the main headline

Inside the body element, create the main heading. Use the [level 1 heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) (\<h1\>) element.

```html
<h1>Welcome to Laguna Brava Ecotourism</h1>
```

## Task 3: Adding Paragraphs and sub-headings
Structure the page's welcome blurb, general description of activities, and description of the local communities using [paragraph elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) and heading elements.

You can follow the structure below:

```html
<h1>...</h1>
<p>[Welcome blurb]</p>

<!-- activities description -->
<h2>Activities</h2>
<p>
    [General description of activities ]
</p>
```

```html
<!-- Activity 1 -->
<h3>The Lake Challenge</h3>
<p>
    ...
</p>
```

## Task 4: Adding lists
Each guided visit option contains details organized as a list (e.g., price and minimum number of people). Use the [unordered list element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul) to structure this information right below the sub-heading in each activity.

```html
<h3>The Lake Challenge</h3>
<p>
...
</p>
<ul>
    <li>Duration: 5 hours approx.</li>
    <li>Price: $50 USD</li>
    <li>Minimum: 2 pax</li>
</ul>
            
```

## Task 5: Adding links
Choose at least one word or phrase and make it a hyperlink (link) using the [anchor element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a).

Specify the URL of another website using the hyperlink reference (href) attribute of the anchor element. HTML attributes are commonly used in HTML to provide additional information and control the content within an HTML tag.

```html
The Mayan communities of the <a href="https://en.wikipedia.org/wiki/Chuj_people">Chuj ethnicity</a> settled around the lake offer several activities that allow visitors to enjoy Laguna Brava's natural beauty.
```

Notes:
- The link allows the viewer of the page to click on it and jump into the referring or target page. When this happens, you may realize that the target page opens in the same browser window.
- You may also look at how to make the hyperlink to open the target page in a browser tab or window.

## Task 6: Adding images
Add a few images using the [image element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img). Specify the URL of the image in the source (src) property of the \<img\> tag. 

We will use local images, which means the server will host these images. Create an *img/* in the same folder containing your *index.html* document and add the images to be included in each image tag below.

Place the image before the level 1 heading created in task 2.

```html
<img src="img/panoramic-laguna-brava-2.jpg" alt="Laguna Brava lake" title="Laguna Brava">
<h1>...</h1>
```

> [Download the header image](https://github.com/josecarlosgt/Web-Design-and-Development/raw/tutorial-2-designing-and-structuring-content/img/panoramic-laguna-brava-2.jpg)

Notes:
- The image element does not require a closing tag because this element does not enclose any content. All the information required to display an image is specified as attributes of the image element.
- To make the \<img\> tag work, you need to add an image file and make it accessible from the folder where your index.html is located. Developers usually create an image folder named "img" or "images" that contains all the images displayed on a website. The image URL can be a relative path, e.g., "images/myimage.jpg", which means the image is served locally or an absolute path, e.g., https://josecarlosgt.github.io/Web-Design-and-Development/img/kayak.jpg, which means the image is served externally by another web server.
- You can also use the title attribute to provide additional information about the image. Most browsers will display the content of this attribute in a tooltip when the user hovers over the image.

## Task 7: Adding a web form
HTML borrows the concept of a form to refer to different elements that allow you to collect information from visitors to your site. Refer to Chapter 7: Forms (uploaded to Canvas) for a more detailed explanation of how web forms operate.

A web form consists of a form ([\<form\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)) element and a combination of controls, such as input and other elements that allow the user to enter different types of data. These sites provide more information on creating web forms.

- [Form element](https://www.w3schools.com/html/html_forms.asp)
- [HTML input types](https://www.w3schools.com/html/html_form_input_types.asp)
- [Label element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)

Form controls serve as points on the web page that direct or control the user's interaction with the web page. The simplest form control on a web form is a text input that directs the user to key in text content, such as their name or email address.

### Preview

![Preview 2](form-preview.jpg)

After the last paragraph, create a web form that requests comments from your page's viewers based on their experiences in Laguna Brava:

```html
<form>
</form>
```

Inside the form element, create a text input field to capture the user's name:
```html
<label for="name">Name: </label>
<input type="text" name="name" id="name" placeholder="Write your name">
```

Use the [break line element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br) to produces a line break in text (carriage-return) as necessary to separate each group of elements.

```html
<br>
```

Create an email input field to capture the user's email:
```html
<label for="email">Email: </label>
<input type="email" name="email" id="email" placeholder="Write your email">
```

Use the [line break element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br) to display each label/input pair in your form in a single line:
```html
<label for="name">Name: </label>
<input type="text" name="name" id="name" placeholder="Write your name"><br><br>
...
```

Create a [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea) field to capture the users' comment:
```html
<label for="experience">Experience: </label>
<textarea name="experience" id="experience" placeholder="Please share with us your experience." rows="5" cols="50"></textarea>
```

Create a submit input field to display a submit button:
```html
<input type="submit" value="Submit">
```    

Notes:
- Notice the difference between the text and email fields
- The name attribute in the input and textarea elements is useful for managing the data entered by the user in server-side programs. We will ignore this attribute for now, since we are focusing only on developing the front-end of a webpage, i.e., the code that runs in the client (web browser).
- Notice how adding [label elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label) and the [placeholder attribute](https://www.w3schools.com/tags/att_input_placeholder.asp) to your input text and textarea fields improve the usability of your form.
- Notice how the id attribute of the input fields relates to the for attribute of the label element.
 
Use the [horizontal rule element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr) to separate the form from the rest of the content in the webpage.

```html
<hr>
```

Note that the line break and horizontal rule elements (as well as the \<input\> and \<img\>) elements do not require a closing tag because these elements do not enclose any content. 

Finally, add a comment on top of the form element to state the purpose of your form using the syntax <!--  -->. Comments in HTML are not displayed to the user of the page. The purpose of comments is to explain your code, which can help you or help others to edit the source code at a later date.

```html
<!-- A form asking for page viewer's experiences -->
```

[**Persist** the data captured in the web form](https://docs.google.com/document/d/1RAIx-JZjfczV0gJI_8PNTx6jgpuOi0jKEOdl4tw8HOo/edit?usp=sharing) to store the comments from Laguna Brava Ecotourism's visitors.
