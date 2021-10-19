# Tutorial: Content Panels with Bootstrap 

In this tutorial, you will see several examples that give you practical insight into using Bootstrap components to include information in your website using content panels.

Bootstrap components covered in this lab:
- Slider
- Cards
- Collapsible content
- Accordion
- Modal window

In this tutorial, we will use [New Age](https://startbootstrap.com/previews/new-age) template from the [Start Bootstrap](https://startbootstrap.com/) website. Download the template from [here](https://github.com/josecarlosgt/Web-Design-and-Development/raw/tutorial-9-content-panels/new-age-template.zip).

## Part I: Creative Content Creation

Before starting with the task below, think of your favorite film. Then, think of two more movies related to your favorite choice. These movies will serve as the content of your webpage. 

The topic of your website is something that all of your films share, such as star an actor you like, belong to the same genre, or portray a social issue that you care about. Although each film is different, all of them should relate to your webpage's topic, making your webpage distinct while maintaining the focus of your webpage on a single idea. Selecting and elaborating on a topic makes it easier to concretize a message in our web pages and create content, such as images and text, to communicate the message. 

Then, for each movie, create the following content:
- The title of the movie
- An image
- A synopsis that you can get from an external source. The synopsis should consist of 5 or more sentences.
- A one or two sentences expressing your views about the movie. Your views should echoe the topic you chose.

Then, proceed by completing the tasks in the following part.

## Part II: Webpage Creation with Content Panels

Before creating the content panels, let's create the page title and headings.

Give a title to your webpage. The title should be representative of the topic you chose.

```html
<title>[PAGE TITLE]</title>
```

Give your webpage a main heading and short introduction. This content should also represent the topic you chose.

```html
<h1 ...>[MAIN HEADER]</h1>
<p class="lead ...">
    [SHORT INTRODUCTION]
</p>
```

## Task 1: [Slider](https://getbootstrap.com/docs/5.0/components/carousel/)

A slider positions a series of images next to each other but only shows one at a time. The images then slide from one to the next. In bootstrap, the slider is called carousel.

This slider loads several panels but only shows one at a time:

```html
<!-- Slider -->
<div id="carousel-films" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
    </div>
</div>
<!-- End of Slider -->
```

Notes:
- The *.active* class needs to be added to one of the slides; otherwise, the carousel will not be visible. 
- Also, use a unique id on the *.carousel* to allow controls (below)
- The *data-bs-ride* attribute controls the autoplay
- The carousel uses the *[d-block](https://getbootstrap.com/docs/4.0/utilities/display/)* and *[w-100](https://getbootstrap.com/docs/4.0/utilities/sizing/)* to ensure on carousel images to prevent browser default image alignment.

### Slider with controls

The following slider provides buttons that allow users to navigate between each of the slides:

```html
<!-- Slider -->
<div id="carousel-films" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="assets/img/placeholder.png" class="d-block w-100" alt="...">
        </div>
    </div>
    <!-- Slider controls -->
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel-films"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel-films"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button </div>
</div>
<!-- End of Slider -->
```

> Create a slider using the Bootstrap carousel component. Replace the *placeholder.png* and *alt* with your content.

## Task 2: [Cards](https://getbootstrap.com/docs/5.0/components/card/)

Now, we will organize the synopsis content using the Bootstrap cards component. A card acts as a content container that includes options for headers and footers. 

We will use the *article* element to create each card:

```html
<article class="col-lg card border-0">
    <div class="card-body">
        <h4 class="card-title text-center">[MOVE TITLE]</h4>
        <p class="card-text">
            <p class="mb-2">
                [SYNOPSIS]
            </p>
        </p>
    </div>
</article>
```

> Create three cards with the titles and synopsis of your movies.

## Task 3: [Collapse](https://getbootstrap.com/docs/5.0/components/collapse/)

The synopsis content may be made your webpage look saturated with too much text. We can display only a fragment of the content by default and allow the user to expand the rest.

We can use the collapse component to achieve this effect. Bootstrap uses a JavaScript plugin to show and hide content. Buttons or anchors are used as triggers that are mapped to specific elements you toggle. Collapsing an element will animate the height from its current value to 0.

Edit your cards content to show only one or two sentences of the synopsis and use the collapse component to hide the rest:

```html
<article class="col-lg card border-0">
    <div class="card-body">
        <h4 class="card-title text-center">[MOVE TITLE]</h4>
        <p class="card-text">
            <p class="mb-2">
                [SYNOPSIS (START)]
            </p>
            <div class="mb-2">
                <button class="btn btn-primary btn-sm py-0" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapse-synopsis-1" aria-expanded="false"
                    aria-controls="collapse-synopsis-1">
                    Read more
                </button>
            </div>
            <p class="collapse" id="collapse-synopsis-1">
                [SYNOPSIS (REST)]
            </p>
        </p>
    </div>
</article>
```

> Note the collapse behavior relies on assigning an identifier to the content to be expanded (e.g., *collapse-synopsis-1*). This identifier also appears on some of the properties (e.g., *data-bs-target* and *aria-controls*) in the button element that triggers the collapsible behavior. This identifier should be unique. Thus, adding more than one card involves assigning different ids.

The collapse component uses different types of HTML attributes that are common across content panels components in Bootstrap:
- *data-bs-toggle*: data property that specifies collapsible behavior
- *data-bs-target*: data property that specifies the id of the element to be collapsed/shown
- *aria-expanded*: attribute that indicates whether the element is collapsed or expanded 
- *aria-controls*: attribute that creates a cause and effect relationship. It identifies the element(s) controlled by the current element when that relationship isn't represented elsewhere on the page. The more widely the two elements are separated on the page, the more useful the aria-controls attribute becomes.

The Bootstrap JavaScript plugin uses the data properties (*data-bs-target* and *data-bs-toggle*) to implement the collapsible behavior.

Both *aria-expanded* and *aria-controls* correspond to the [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques) standard. These attributes only expose extra information to a browser's accessibility features and do not affect a page's internal structure.

## Task 4: [Accordion](https://getbootstrap.com/docs/5.0/components/accordion/)

The accordion comprises a collection of content organized as pairs of titles and panels. When you click on a title of an accordion, its corresponding panel expands to reveal the content.

```html
<!-- accordion -->
<div class="accordion" id="reviews-content">
    <article class="accordion-item">
        <h2 class="accordion-header" id="heading-1">
            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                data-bs-target="#review-1" aria-expanded="true" aria-controls="review-1">
                [TITLE OF YOUR REVIEW]
            </button>
        </h2>
        <div id="review-1" class="accordion-collapse collapse show" aria-labelledby="heading-1"
            data-bs-parent="#reviews-content">
            <div class="accordion-body">
                <p>
                    [CONTENT OF YOUR REVIEW]  
                </p>
            </div>
        </div>
    </article>
    <article class="accordion-item">
        <h2 class="accordion-header" id="heading-2">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                data-bs-target="#review-2" aria-expanded="false" aria-controls="review-2">
                [TITLE OF YOUR REVIEW]
            </button>
        </h2>
        <div id="review-2" class="accordion-collapse collapse" aria-labelledby="heading-2"
            data-bs-parent="#reviews-content">
            <div class="accordion-body">
                <p>
                    [CONTENT OF YOUR REVIEW] 
                </p>
            </div>
        </div>
    </article>
</div>
<!-- End of accordion -->
```

> Create one more accordion item. When creating your accordion, take the same considerations you took when using the collapse component, especially when assigning the identifiers for each item in your accordion.
>
> Also, note the first accordion item contains the *.show* class and *aria-expanded="true"*. The hidden items have *aria-expanded="false"* and their buttons have the class *.collapsed*.

## Task 5: [Modal Window](https://getbootstrap.com/docs/5.0/components/modal/)

Also known as pop-up, the modal window is content that appears "in front of" the rest of the page's content.

We will create a "Send feedback" [form](https://getbootstrap.com/docs/5.0/forms/overview/
) as a modal using Bootstrap modal component.

The template provided to you already contains, as part of the navigation bar, the button to trigger the modal window:

```html
<button class="btn btn-primary rounded-pill px-3 mb-2 mb-lg-0" data-bs-toggle="modal"
    data-bs-target="#feedbackModal">
    <span class="d-flex align-items-center">
        <i class="bi-chat-text-fill me-2"></i>
        <span class="small">Send Feedback</span>
    </span>
</button>
```

The content for the modal window will typically sit within the page, but it is hidden when the page loads using CSS. Add the modal content at the bottom of the page:

```html
<!-- Feedback Modal-->
<div class="modal fade" id="feedbackModal" tabindex="-1" aria-labelledby="feedbackModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-gradient-primary-to-secondary p-4">
                <h5 class="modal-title font-alt text-white" id="feedbackModalLabel">Send feedback</h5>
                <button class="btn-close btn-close-white" type="button" data-bs-dismiss="modal"
                    aria-label="Close"></button>
            </div>
            <div class="modal-body border-0 p-4">
                <form>
                    <div class="form-group mb-4">
                        <label for="email" class="form-label">Email address:</label>
                        <input type="email" class="form-control" id="email" placeholder="Enter your email">
                    </div>
                    <div class="form-group mb-4">
                        <label for="name" class="form-label">Name:</label>
                        <input type="text" class="form-control" id="name" placeholder="Enter your name">
                    </div>
                    <div class="form-group mb-4">
                        <label for="comment" class="form-label">Comment:</label>
                        <textarea class="form-control" id="comment" rows="3"></textarea>
                    </div>
                    <div class="text-center">
                        <button class="btn btn-secondary rounded-pill btn-lg disabled w-100" id="submitButton" type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<!-- End of Feedback Modal-->
```

## Other Content Panels

Bootstrap also has available several other components to implement content panels:
- [Offcanvas](https://getbootstrap.com/docs/5.0/components/offcanvas/)
- [Dropdowns](https://getbootstrap.com/docs/5.0/components/dropdowns/)
- [Tabs](https://getbootstrap.com/docs/5.0/components/navs-tabs/)

## Part III: Publish your Webpage

Create a repository for your webpage on GitHub. Then, publish your webpage to the Web using GitHub Pages.

Include a `README.md` file to your project with the URL of your webpage on the Web using the following syntax:

```
# [TITLE OF YOUR WEBPAGE] 

[Link to my webpage on the Web]([INCLUDE THE LINK HERE])
```
