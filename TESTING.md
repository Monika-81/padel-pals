# **Testing**

1. [Manual testing](#manual-testing)
    - Browser compadability
2. [Code validation](#code-validation)
    - Python PEP8
    - W3School (HTML & CSS)
    - Lighthouse
    - WAVE
3. [Bugs and fixes](#bugs-and-fixes)

---

### **Manual testing**

During the entire developing stage I repeatedly tested the elements added and altered regarding appearance as well as responsiveness via the simulated live server GitPod provides. After the site was live deployed I also checked the site regularly trough my smartphone for first hand updates on a live mobile viewport.

In combination with the direct visual view of the page provided by the live server I frequently used Google Chrome developer tools, both for direct changes of the code as well as the tools for responsive testing of different platforms and screen sizes. As a compliment to DevTools I also checked how the website responded on diffrent screen sizes and screen orientaion using Responsive Design Checker. The final version of website passed all the visual and functional apperences changes on both large and small screens as well as the change between landscape and portrait orientaion changes on the same device. For example of how the same mobile screen funtions in both orientations, see below.
 
 My best friend during the debugging and testing was to commit in and out code as well ass to the <em>{{ }}</em>-function in the HTML to see if I targeted the right element or if my view was reachable from where I wanted to reach certain database items from a model.

<br>

### **Browser compadability**
<br>

- [BrowserStack](https://www.browserstack.com/)

The websites compatibility to various browsers (Chrome, Safari, Opera, Firefox, Internet Explorer, Edge) including different versions of said browsers, was tested using the BrowserStack application on both desktop and mobile. Different mobile versions was tested also for different browsers. Over all the functionality were consistent throughout for most of the devices and browsers. No notable difference was found. Exampel pictures below:

- Iphone SE
- Pixel 3 XL
- Windows 11 chrome
- Windows 8 firefox
- Mac lion firefox
- All the devices that was included in the check

<details>
<br>

![Iphone SE](/static/images/screenshots/iPhone-SE.png)
![Pixel 3 XL](/static/images/screenshots/Pixel-3-XL.png)
![win 11 chrome](/static/images/screenshots/win11_chrome_71.0.jpg)
![win 8 firefox](/static/images/screenshots/win8.1_firefox_30.0.jpg)
![mac lion firefox](/static/images/screenshots/maclion_firefox_38.0.jpg)
![Responsive many](/static/images/screenshots/responsive-many.png)

<br>
</details>


[Back to top](#testing)

---

### **Code validation**
<br>

- [Python PEP8 Validator](http://pep8online.com/) 

When the basic structure of the project was done I ran code validation through the PEP8 Validator. This procedure was repeated multiple times to validate that the code was working during the developing process. Mostly the PEP8 reported bugs with whitespace, both too much whitespace as missing whitespace in the code, as well as with my lines being too long. The settings.py still have seven errors in the end due to too long lines och codenames or continuing line over indented. None of those have I changed since that ended up rendering other errors.
Below are the final test of the python files in PEP8:

- settings.py (with errors)
- admin.py
- forms.py
- models.py
- views.py

<details>
<br>

![settings](/static/images/screenshots/settings.py_validation_third.png)
![admin](/static/images/screenshots/PEP8-admin.png)
![forms](/static/images/screenshots/PEP8-forms.png)
![models](/static/images/screenshots/PEP8-models.png)
![views](/static/images/screenshots/PEP8-views.png)


<br>
</details>

<br>

- [HTML Validation](https://www.w3schools.com/) 

When the basic structure of the project was done I ran code validation through W3Schools Validator for all the HTML files as well as the CSS file. The biggest problem with the HTML are the many other templates that share the <em>{% block content %}</em> and throws errors with missing tags or to many line breaks. 

The problems with linebreaks are left since the code works and it looks fine when you compare the same section live in Dev tools. The raw source code from Dev Tools that I use to validate the code consists of white spaces where the pyhon code is suppose to be. The same code is tested ok for the homepage and topic views but throws an error when the playlist view is loaded.

There is also an issue with Summernote rendering extra tags around the text in the posts and comments that transfer over to the raw html code, there are an image exampel with the errors below.
Some semantic and code logic errors where made on my behalf and corrected after the last validation.

<details>
<br>
 
**Errors**

![Summernote](/static/images/screenshots/Error-in-code-playdisplay.png)
![Indention error](/static/images/screenshots/html-indention-blocks-error.png)
![Indention error](/static/images/screenshots/html-indention-blocks-error2.png)
![Play list error](/static/images/screenshots/html-playdisplay-error.png)
![Play list error](/static/images/screenshots/html-error.png)
![Error not changed](/static/images/screenshots/html-error-code-not-changed.png)


**Finished check result**

![Base](/static/images/screenshots/html-validation-base.homepage.png)
![Topic page](/static/images/screenshots/html-validation-topic.page.png)
![Remaining problem](/static/images/screenshots/play-end.png)
![Remaining problem](/static/images/screenshots/play-end2.png)
![Remaining problem](/static/images/screenshots/plan-end3.png)


Last picture mentions a <span> that are delibratly there since the nav code changes if the user is logged in or logged ut.  

<br>
</details>

<br>

- [CSS Validation](https://www.w3schools.com/) 

The CSS had one error before deployment, had to many paramenters regarding the jumbotron image.
Below are the error, the code that was wrong and the finished result.

<details>
<br>

![Error](/static/images/screenshots/css_validation_error.png)
![Code](/static/images/screenshots/css_validation_error_problem.png)
![No error](/static/images/screenshots/css_validation_ok.png)

<br>
</details>

<br>

- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

I also ran the page through Lighthouse for both desktop and mobile to test out the performance and accessibility of the page. The input gave me further information how to proceed with the project, and was repeated after all major changes and bug fixes. The biggest problem was that the performance on mobile viewport until I added a smaller picture for smaller screen sizes. Below are the results from the hompage on bot desktop and mobile. But the result was the same at the other urls as well.

<details>
<br>

![Lighthouse desktop](/static/images/screenshots/lighthouse-desktop-home.png)
![Lighthouse mobile](/static/images/screenshots/lighthouse-mobile-home.pngg) 

<br>
</details>

<br>


- [WAVE](https://wave.webaim.org/)

To validate the accessibility further I also tested the site at Wave - Web Accessibility Evaluation Tool. No errors where found and the four warnings are give to the paragraphs with justified text, but I decided to keep the justified text out of design choice.

<details>
<br>

![WAVE](/static/images/screenshots/wave-home.png) 

<br>
</details>

<br>

[Back to top](#testing)


---


### **Bugs and fixes**
There where a number of bugs and mishaps committed through the development as I tried to learn the best way to code the app. I freaquently created logical errors due to not understanding the flow of the code correctly but as the project came along, and the bugs with it, I started too see and understand more naturally what I had done too cause the bug to happen. As seen in the commits made, I change code - then later changes it back again (or partly) as I figured it out along the development process.

**The major bugs where**: <br>
1. 
<br>

**Bug not fixed**:
- None that I know of at the moment of admission.
<br>

[Back to top](#testing)

---