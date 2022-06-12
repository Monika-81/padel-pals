# **Padel Pals**

**Padel Pals** is the discussion forum for Padel Tennis enthusiasts. The forum aim to be a platform for discussion about padel, socializing with other padel interested people as well as a to search for a team that are missing a player for a booked session, or to annunce that the user is avalible if someone whant to team up. This site targets various kinds of people whom are interested in knowing more about the padel tennis sport, discuss rules, gear, technique etc and to just soocialze with likeminded padel players.

Let me introduce you further to [**Padel Pals**](https://padelpals.herokuapp.com/)!
<br>
<br>

![alt text](image.jpg)
<br>


## **Content**
1. [**Strategy**](#strategy)
    - [UX](#ux)

2. [**Scope**](#scope)
    - [User Stories](#user-stories)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Wireframes](#wireframes)    

3. [**Structure**](#structure)
    - [Home page](#home-page)
    - [Navigation](#navigation)
    - [Topic List](#topic-list)
    - [Topic view](#topic-view)
    - [Play event list](#play-event-list)
    - [Forum post](#forum-post)
    - [Add post](#add-post)
    - [Edit post](#edit-post)
    - [Delete post](#delete-post)
    - [Like post](#like-post)
    - [Comments](#comments)
    - [Profile page](#profile-page)
    - [Contact form](#contect-form)
    - [Search function](#search-function)
   
4. [**Skeleton**](#skeleton)
    - [Technologies](#technologies)

5. [**Surface**](#surface)
    - [Design](#design)
    - [Color scheme](#color-scheme)   

6. [**Testing**](#testing)
    
7. [**Deployment**](#deployment)
    - [Deployment](#deployment)
    - [Clone](#clone)
    - [Forking](#forking)

8. [**Credits**](#credits)
    - [Content](#content)
    - [Acknowledgement](#acknowledgement)

[Back to top](#padel-pals)

<br>

## Strategy

---


### **UX** 

<br>

With the UX principles in mind I started with Strategy phace, thinking about the target audience and what features would benefit them. 

The target audience are:

- people of all age groups but mostly adults
- people that enjoy playing padel
- people that are qurious about the sport
- people who like to discuss and learn more about padel
- people that like to fin new friends to play padel with

What the user will be looking for:

- An interactive forum website, where a verified user can leave post and comment 
- A website with information that can be read, even if you are not logged in
- The ability to make a personal user account to access all the content of the site
- The ability to post, comment and like post
- The ability to find other users that like to play padel a certain time

[Back to top](#padel-pals)

<br>

## Scope 

---


### **User Stories**

<br>

**Epic: Admin**
- As a Site Admin I can reach the admin functionalities from the main navigation so that I can get quick      accesss
- As a Site Admin I can manage the site so that community rules are uphold
- As a Site Admin I can add or delete posts and comments so that the community rules are upheld 

**Epic: Account Management**
- As a Site User I can sign up for an account so that I can use all the features reserved for members
- As a Site User I can log in to the site so that I can use all the features of the site
- As a Site User I can easily log out from the site so that my account and it's content remains secure
- As a Site User I can contact admin so that I can leave feedback and ask questions
- As a Site User I can create a personal profile so that I can control my content

**Epic: Forum View**
- As a Site User I can read posts and comments in detail so that I can get an understanding for the community
- As a Site User I can see a list of what topics I can discuss for easy navigation and posting
- As a Site User I can see the latest post at the home page so that I get the newest input directly
- As a Site User I can use a search function so that I can find the right post that interests me
- As a Site User I can easily and intuitively navigate the site so that I can find what I am looking for
- As a Site User I can see the date a post was created and updated so that I know how accurate it is

**Epic: Forum Interactions**
- As a logged in Site User I can create new post and comments in a topic so that I can discuss and socialize with the other members of the community
- As a logged in Site User I can edit or delete my posts and comment so that I display the right content that intrests me
- As a logged in Site User I can like a posts so that others can see If a topic is popular and/or good information
- As a Site User I get confirmation or error messages so that I know everything is working correctly

**Epic: Find Player**
- As a Site User I want to find missing player/players or a team that are missing a player so that I can play when it suits me

[Back to top](#padel-pals)

<br>

### **Features**

<br>

#### **Home page**
<details>
The home page gives the user a short introduction to the forum, who they are and what the purpose of the forum is. It also explains to the site user that to access all the functions of the forum, the user needs to create an account and links to the sign up page. Underneath the welcome messge is a list of the most recent posts in the forum. The main design theme of the page was to make it spory yet easy to read and sleek in the design.

<br>
<br>
![alt text](image.jpg)
<br>
</details>

#### **Navigation**
<details>
At the top of the website there is an internal navigation bar. The logo as well as the 'home' choice directs the user back to itself. If the user is not logged in, he or she finds the options to register or login in the manu section that will help the user choose between the "about page" (home page), "activities page" and the "sign up page" - also know as "join". The current page the user is visiting is marked for easier navigation on the site. On desktop and landscape oriented screens the navigation bar is located to the top right side of the page, and on portrait oriented devices the navigation bar is fixed at the top of the screen.

<br>
<br>
<strong>The list sorted on location, by default.</strong>
<br>
<img src="" width=1200> 
<br>
<br>
<strong>The list sorted by the need to buy or not.</strong>
<br>
<img src="" width=1200>
<br>
</details>


#### **Topic list**
<details>

<br>
<br>
<strong>The list sorted on index number.</strong>
<br>
<img src="" width=1200> 
<br>
</details>


#### **Topic View**
<details>

<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Play event list**
<details>
 
<br>
<br>
<strong>Their is 6 actions for the user to pick from.</strong>
<br>
<img src="g" width=1200> 
<br>
<br>
</details>

#### **Forum post**
<details>

<br>
<br>
<strong>Check all items.</strong>
<br>
<img src="" width=1200> 
<br>
<br>
<strong></strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>Check one item.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>After the first item is checked, the user gets the choice to check another item straight away or go back to the main menu.</strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Add Post**
<details>

<br>
<br>
<strong>First the user choose an item.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>Then the uses gets to input the new quantity before confirming the choice.</strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Edit Post**
<details>

<br>
<br>
<strong>First the user choose an item.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>Then the uses gets to input the new location before confirming the choice. The user is displayed examples of different locations in the store. </strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>


#### **Delete Post**
<details>

<br>
<br>
<strong>The user gets three input fields to fill out.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>After the user confirms the choice to add the input's given, the new updated list is displayed. </strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Comments**
<details>

<br>
<br>
<strong>The user gets three input fields to fill out.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>After the user confirms the choice to add the input's given, the new updated list is displayed. </strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Like Post**
<details>

<br>
<br>
<strong>First the user choose an item.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>Then the uses gets to input the new location before confirming the choice. The user is displayed examples of different locations in the store. </strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Profile Page**
<details>

<br>
<br>
<strong>The user needs to confirm the displayed row as the correct one they want to delete.</strong>
<br>
<br>
<img src="" width=1200>
<br>
<br>
<strong>After the user confirms the choice to add the input's given, the new updated list is displayed. </strong>
<br>
<br>
<img src="" width=1200>
<br>
</details>

#### **Contact Form**
<details>

<br>
<br>
<strong>The user get's the choice to go back.</strong>
<img src="" width=1200>
<br>
</details>

#### **Search Function**
<details>

<br>
<br>
<strong>The user get's the choice to go back.</strong>
<img src="" width=1200>
<br>
</details>

#### **Future features**


[Back to top](#padel-pals)

<br>


## Technologies
---

### **Languages**

- **Python**
<br>

- **HTML5**
<br> I used HTML to create the base structure of the project. I started with a basic boilerplate set up and created the first crude structure of the page out of the original design. 

- **CSS3**
<br> The CSS was used to apply the custom styles to the HTML skeleton. In a separate document the creation of the design came forth. 

- **Javascript**
<br> Javascript is the life of the game and makes the game interactive to the user. It's the language used to create the functions that drives the game forward.

<br>

### **Tools**

- [Heroku](https://www.heroku.com/)
    -  I used Heroku to deploy the application.  

- [Lucid Chart](https://www.lucidchart.com/pages/)
    - I used Lucid Chart to design the data model and list mock up for the project.

- [GitPod](https://www.gitpod.io/)
    - I used GitPod as the code editor as well as to display to test out changes in my code.

- [GitHub](https://github.com/)
    - I used GitHub to create a repository for my project.

- [Google-auth](https://google-auth.readthedocs.io/en/master/)
    - I used Google-auth to authenticate the Google API's so the project could be accessed in the cloud.

- [Cloudinary](https://cloudinary.com/)
    - I used to create the API's that connects the application to the spreadsheet at Google Sheet.


- [PEP8](http://pep8online.com/)
    - I used PEP8 online check to test and validate my python code.  





[Back to top](#padel-pals)

---

## **Testing**

For more information about the testing performed during the development, go to the separate [testing](/TESTING.md) page.
<br>
<br>

[Back to top](#padel-pals)

---

## **Deployment**

### **Deployment**

The project was deployed to **Heroku** from **GitPod**:
- After creating an account or logging in to an existing one on Heroku, click the "New" button on the right hand side of the 'Personal' menu.
- Choose the option 'Create new app' and then choose a unique name for your application and the right region. Then click 'Create New App'.
- Next you need to add buildpacks and create config vars, this is utterly **important** to have done before you deploy your app!

    .......
    - Then add config vars by clicking 'Reveal Config Vars'. I used _Config Var_ called `PORT`, set to `8000`.
    - If you have credentials for your project, you need to add these as well. Create another _Config Var_ called `CREDS` and paste the copy of the requeriments code inside your credentials file into the value field.

- Now it's time to deploy the app. Go back to the top of the page and click "Deploy".
- Choose a deployment method, I used GitHub since my repository is located on GitHub.
- Scroll down to 'Connect to GitHub' and search for your project. Make sure you are connected to the right GitHub account. Click 'Connect'.
- Keep scrolling downwards, now you can choose between Automatic Deployment or Manual Deployment. I choose Manual first, until the app was properly deployed and a link to the app was visual. Then I choose to enable automatic deployment for smoother testing. 

The live app can be found here: https://padelpals.herokuapp.com/ (Yes! I made a type-o choosing the name of the application on Heroku and noticed too late to change it.)
<br>

<br>
<br>


A copy of this GitHub Repository can be made by either making a copy on your local machine or by forking the GitHub content. By using a copy of the repository changes can be made to the copy without affecting the original code. To make a copy of the repository, follow these steps:

### **Clone**
- Locate the repository at **GitHub**.
- At the top of the file's menu, click the green *code* button to the right.
- The first option in the drop-down menu is clone, where you get three choices of how to clone the repository.
- To clone a copy of the python project, click the 'copy' icon on the right-hand side of **Clone with HTTPS**.
- Choose your code editor, open GitBash and change the working directory to where you want the cloned directory to be made saved.
- In the terminal you write git clone and then paste the copied URL. Like this: '$ git clone https://github.com/Monika-81/padel-pals.git' 
- Press enter and then install the dependencies you like to use for the project. To run this project I recommend to atleast install **gspread**.
<br>

### **Forking**
- Locate the repository at **GitHub**.
- At the top right-hand side is a button called *fork*, click on the button to create a copy of the original repository in your GitHub Account.
<br>
<br>


[Back to top](#buy-me)

---

## **Credits**

### **Content**

For most of the development and bug fixes I went back to the Code Institute LMS and the learning material for the ..... I also turned to the Slack community and the search function, where I found many tips when I got stuck. When I didn't find the answers to understand what I needed to change there, I consulted external sources while searching for the answer using Google. No piece of code was copied to use in the project, by reading on many different sites I learned more about python and used what I learned to try out was doing wrong.

Some of the sites I frequently **consulted** was :
<br>

* [CodeGrepper](https://www.codegrepper.com/)
* [DelftStack](https://www.delftstack.com/)
* [Programiz](https://www.programiz.com/)
* [PyPi](https://pypi.org/project/prettytable/)
* [Python](https://www.python.org/)  
* [PythonGuides](https://pythonguides.com/)
* [RealPython](https://realpython.com/)
* [Stack Overflow](https://stackoverflow.com/) 
* [W3School](https://www.w3schools.com/)

<br>
The template used in the project was provided by Code Institute. The terminal design of the app on Heroku is due to the code supplied in the template.
<br>
<br>

### **Acknowledgement**

- My mentor **Precious Ijege** at Code Institute for valuable input and encouragement.
- The Slack community for be such an open, warm and sharing place. 
- **Viet Hoang** for letting me run the app by him and for getting user experience input before, during and at the final stage of the project.


[Back to top](#buy-me)

---
