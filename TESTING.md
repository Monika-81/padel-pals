# **Testing**

1. [Manual testing](#manual-testing)
    - Browser compadability
2. [Code validation](#code-validation)
    - Python PEP8
    - W3School
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