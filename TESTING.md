# **Testing**

1. [Manual testing](#manual-testing)
    - Browser compatability
2. [Code validation](#code-validation)
    - Python PEP8
    - W3School (HTML & CSS)
    - Lighthouse
    - WAVE
3. [Bugs and fixes](#bugs-and-fixes)

---

### **Manual testing**

During the entire developing stage I repeatedly tested the elements added and altered regarding appearance as well as responsiveness via the simulated live server GitPod provides. After the site was live deployed I also checked the site regularly trough my smartphone for first hand updates on a live mobile viewport.

In combination with the direct visual view of the page provided by the live server I frequently used Google Chrome developer tools, both for direct changes of the code as well as the tools for responsive testing of different platforms and screen sizes. As a compliment to DevTools I also checked how the website responded on different screen sizes and screen orientaion using Responsive Design Checker. The final version of the website passed all the visual and functional appereances changes on both large and small screens as well as the change between landscape and portrait orientaion changes on the same device. For example of how the same mobile screen funtions in both orientations, see below.
 
 My best friend during the debugging and testing was to commit in and out code as well as to the <em>{{ }}</em>-function in the HTML to see if I targeted the right element or if my view was reachable from where I wanted to reach certain database items from a model.


 Before the User Stories where marked as closed, I tested the stories to see if the result was satisfying and the app lived up to the project plan, see project board for more information [Kanban](https://github.com/Monika-81/padel-pals/projects/1).

<br>

### **Browser compadability**
<br>

- [BrowserStack](https://www.browserstack.com/)

The websites compatibility to various browsers (Chrome, Safari, Opera, Firefox, Internet Explorer, Edge) including different versions of said browsers, was tested using the BrowserStack application on both desktop and mobile. Different mobile versions was tested also for different browsers. Over all the functionality were consistent throughout for most of the devices and browsers. No notable difference was found. Example pictures below:

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

When the basic structure of the project was done I ran code validation through the PEP8 Validator. This procedure was repeated multiple times to validate that the code was working during the developing process. Mostly the PEP8 reported bugs with whitespace, both too much whitespace as missing whitespace in the code, as well as with my lines being too long. The settings.py still have seven errors in the end due to too long lines and codenames or continuing line over indented. None of those have I changed since that ended up rendering other errors.
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

When the basic structure of the project was done I ran code validation through W3Schools Validator for all the HTML files as well as the CSS file. The biggest problem with the HTML is the many other templates that share the <em>{% block content %}</em> and throws errors with missing tags or too many line breaks. 

The problems with linebreaks are left since the code works and it looks fine when you compare the same section live in Dev tools. The raw source code from Dev Tools that I use to validate the code consists of white spaces where the pyhon code is supposed to be. The same code is tested ok for the homepage and topic views but throws an error when the playlist view is loaded.

There is also an issue with Summernote rendering extra tags around the text in the posts and comments that transfer over to the raw html code, there are an image example with the errors below.
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


Last picture mentions a <span> that are deliberatly there since the nav code changes if the user is logged in or logged ut.  

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

To validate the accessibility further I also tested the site at Wave - Web Accessibility Evaluation Tool. No errors were found and the four warnings are given to the paragraphs with justified text, but I decided to keep the justified text out of design choice.

<details>
<br>

![WAVE](/static/images/screenshots/wave-home.png) 

<br>
</details>

<br>

[Back to top](#testing)


---


### **Bugs and fixes**
There were a number of bugs and mishaps committed through the development as I tried to learn the best way to code the app. I frequently created logical errors due to not understanding the flow of the code correctly but as the project came along, and the bugs with it, I started to see and understand more naturally what I had done too cause the bug to happen. As seen in the commits made, I changed code - then later changed it back again (or partly) as I figured it out along the development process.

**The major bugs where**: <br>
1. The first custom CSS was not loading to Heroku
- Turned to the slack community for help, and noticed I had missplaced a 's' in the settings.py file: Had STATIC_DIR not STATIC_DIRS.
2. Comment view not updateing after comment post, error message 500: 'TypeError at /go/ 'Comments' object is not iterable'.
- Unclear what the error was, rewrote the post code from scratch, changed comments_form to comment_form and then it worked.
3. URL and view of topics detail not working, had problems wireing up the topics URL mostly because I wanted to show the topics menu in many windows. 
- Solved by trial and error and in the end understood thanks to tutoring from Alex and the use of 'topics = Topic.objects.all()' in more views.
4. Correlating to that bug I couldn't get the recent post to render in the same view as the topics list. 
- The solution was to change the code to post i posts (not post_list) and to fix the code above.
5. The delete post suddenly stopped workig.
- Had the same code in urls.py for the app after adding delete comment.: path('', views.delete, name=''=), edited to separate paths.
6. Had problems with the play form at the beginning, wouldn't save to the backend admin terminal and would display an error if the fields were not filled out correctly. 
- The solution was to validate the input and display an error message if the form was incorrect. I also hade to implement the HttpsResponse reserve.
7. In connection with the problems above, I had problems displaying the time and date from the form. 
- In the end there were type-o's again: in the forms.py I said widget not widgets.
8. Late in the project I noticed a major bug with CSS and picturs not loading to heroku.
- Found the tips to install the whitnoise package from a thread on Slack. But also noticed that the image folder had accidentally duplicated in the static folder. Adjusted and pust, and everything was working again.
9. The add post page was reachable if you typed in the adress as a none logged in user.
- Added authentication to load the add post form.
10. The email validation template stopped showing the button to confirm the adress after I styled the template. 
- Had multiple tries to fix it but nothing really worked. In the end I went back to almost the original file but left out a {% user.display %} argument that kept throwing errors.



<br>

**Bug not fixed**:
- None that I know of at the moment of admission.
<br>

[Back to top](#testing)

---