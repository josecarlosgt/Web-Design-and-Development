# Tutorial #1 - Exercise: Creating an HTML document

In this exercise, you will create an HTML document from scratch with the basic structure.

> [Link to slides with additional explanations](./slides.pdf)

## Task 1: Creating the basic structure

When creating a webpage from scratch, the first step is to create the basic tags that every page must have. These are:

- [\<html\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html): represents the root of an HTML document and indicates that anything in between is HTML code.
- [\<head\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head): contains information about the webpage (rather than information that is shown within the browser's window).
- [\<title\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title): the contents of the \<title\> element are shown on top of the browser window or page's tab.
- [\<body\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body): contains the document itself. It indicates that anything between it and the closing \</body\> tag should be shown inside the browser's window.

```html
<html>
    <head>
        <title></title>
    </head>
    <body>
    </body>
</html>
```

To start creating your webpage, write down the code above in a text file using a source-code editor (e.g., VS Code). Save the text file with the name "index.html". As a convention, any website's home page or main page is located in a file called index.html.

Now, try to open it using a web browser by clicking on the index.html file. When opening the text file in the browser, you should get a blank page. Alternatively, you can use the local development server provided by the Live Server extension of VS Code.

You will notice that the URL in the browser starts with "file:". This prefix in the URL indicates that the browser is using the File protocol because the HTML file lives locally on your computer. If you were accessing the index.html file through the Web, your browser would have to use the HTTP protocol.

## Task 2: Specifying the title

Fill in the \<title\> element with the title that you want to give to your webpage. Athough this text will not be part of the web page inside's content, I will will appear on the browser's window.

```html
<title>My home page</title>
```

## Task 3: Specifying the character encoding set (charset)

Declare the character encoding set or charset. You should always set the charset metatag as the first item in the <head> section. Not doing so can lead to a long pause before the browser starts to present information to your visitors. The following line shows the syntax for setting the character set to UTF-8, which is the standard charset used in the current version of HTML (HTML5).

```html
<meta charset="utf-8">
```
## Task 4: Creating some content

Add the following text inside the body tag:

```
Hello, this is my home page. <what a simple page!>
```

Notice that literally writing the \< \> characters is not possible as these characters have a meaning in HTML. Therefore, you need to write these characters using HTML entities; doing so is also known as escaping.

```
Hello, this is my home page. &lt;what a simple page&gt;
```

You can also use the HTML code. However, using the HTML entity names is considered a better practice since they are more legible to the human eye.

```
Hello, this is my home page. &#60;what a simple page&#62;
```

The [index.html](./index.html) file contains the final HTML document.
