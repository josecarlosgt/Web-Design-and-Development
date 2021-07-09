# Tutorial #1 - Exercise: Creating a HTML document

When creating a webpage from scratch, the first step is to create some basic tags that every page must have. These are:

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

To start creating your webpage, write down the code above in a text file using a source-code editor (e.g., VS Code). Save the text file with the name "index.html".  As a convention, the home page or main page of any website is located in a file called index.html. By default, web servers will render the content in this file when a user visits a website.

Now, try to open it using a web browser by clicking on the index.html file. When opening the text file in the browser, you should get a blank page.

You will notice that the URL in the browser starts with "file:". This prefix in the URL indicates that the browser is using the File protocol because the HTML file lives locally on your computer. If you were accessing the index.html file through the Web, then your browser would have to use the HTTP protocol.

## \<meta\>: The metadata element

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta

## UTF-8 encoding

```html
<meta charset="utf-8">
```
