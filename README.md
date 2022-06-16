# **Padel Pals**

**Padel Pals** is the discussion forum for Padel Tennis enthusiasts. The forum aims to be a platform for discussions about padel, socializing with other padel interested people as well as to search for teams that are missing a player for a booked session, or to announce that the user is avalible if someone wants to team up. This site targets various kinds of people whom are interested in knowing more about the padel tennis sport, discuss rules, gear, techniques, etc and to just socialize with likeminded padel players.

Let me introduce you further to [**Padel Pals**](https://padelpals.herokuapp.com/)!
<br>
<br>

![Home](/static/images/screenshots/home.png)
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
    - [Jumbotron](#jumbotron)
    - [Topic navigation](#topic-navigation)
    - [Topic list](#topic-list)
    - [Topic posts](#topic-view)
    - [Play event list](#play-event-list)
    - [Play event posts](#play-event-post)
    - [Add post](#add-post)
    - [Add play event](#add-play-event)
    - [Edit post](#edit-post)
    - [Delete post](#delete-post)
    - [Like post](#like-post)
    - [Comments](#comments)
    - [Profile page](#profile-page)
    - [Contact form](#contect-form)
    - [Search function](#search-function)
    - [Admin](#admin)

   
4. [**Skeleton**](#skeleton)
    - [Technologies](#technologies)

5. [**Surface**](#surface)
    - [Design](#design) 

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
- people that are curious about the sport
- people who like to discuss and learn more about padel
- people that like to find new friends to play padel with

What the user will be looking for:

- An interactive forum website, where a verified user can leave posts and comments 
- A website with information that can be read, even if you are not logged in
- The ability to make a personal user account to access all the content of the site
- The ability to post, comment and like posts
- The ability to find other users that like to play padel at a certain time

[Back to top](#padel-pals)

<br>

## Scope 

---


### **User Stories**

<br>

**Epic: Admin**
- As a Site Admin I can reach the admin functionalities from the main navigation so that I can get quick accesss
- As a Site Admin I can manage the site so that community rules are upheld
- As a Site Admin I can add or delete posts and comments so that the community rules are upheld 

**Epic: Account Management**
- As a Site User I can sign up for an account so that I can use all the features reserved for members
- As a Site User I can log in to the site so that I can use all the features of the site
- As a Site User I can easily log out from the site so that my account and its content remains secure
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
- As a logged in Site User I can create new post and comments in a topic so that I can discuss and socialize with other members of the community
- As a logged in Site User I can edit or delete my posts and comment so that I display the right content that interests me
- As a logged in Site User I can like posts so that others can see if a topic is popular and/or relevant
- As a Site User I get confirmation or error messages so that I know everything is working correctly

**Epic: Find Player**
- As a Site User I want to find missing player/players or a team that are missing a player so that I can play when it suits me

<br>

To follow an agile approch, a project board (kanban-board) was set up using GitHub Projects: [Kanban](https://github.com/Monika-81/padel-pals/projects/1)

<br>

### Entity Relationship Diagram

<br>

![ERD](/static/images/screenshots/ERD.png)

<br>
<br>

### Wireframes

The wireframes for the project is very basic to get the feeling where I wanted the project to go, but over all the choices of the design grew with the development.

![Mobile](/static/images/screenshots/wireframe-mobile-home.png)
![Desktop](/static/images/screenshots/wireframe-desktop-home.png)

<br>

<br>

[Back to top](#padel-pals)

<br>

### **Features**

<br>

#### **Home page**
<details>
The homepage gives the user a short introduction to the forum, who they are and what the purpose of the forum is. It also explains to the site user that to access all the functions of the forum, the user needs to create an account and links to the sign up page. Underneath the welcome message is a second menu of the topics of the forum as well as a list of the most recent posts in the forum. The main vision of the site was to make it sporty yet easy to navigate, read and sleak in the design.

<br>
<br>

![Home page desktop](/static/images/screenshots/homepage.png)
![Home page mobile](/static/images/screenshots/homepage_mobile.png)

<br>
</details>

#### **Navigation**
<details>
At the top of the website there is an internal navigation bar. The logo as well as the 'home' choice directs the user back to itself. If the user is not logged in, he or she finds the options to register or login. When the user is logged in, the login link changes to log out and a dropdown menu emerges. In the dropdown menu the user can add a new forum post or search for a team or players to play padel with. There is also a menu option to display the profile page of the user. If the user is an admin user they can find the link to the backend administration in the same dropdown menu. To the far right in the navigation bar there is a search function. The top navigation bar transforms to an expandable navigation bar on smaller screens.

<br>
<br>

![Navbar desktop](/static/images/screenshots/navbar-desktop-small.png)
![Navbar desktop dropdown](/static/images/screenshots/navbar-desktop-expanded.png)

<br>
<br> 

![Navbar mobile expanded dropdown](/static/images/screenshots/navbar-mobile-large-expanded.png)
![Navbar mobile expanded](/static/images/screenshots/navbar-mobile-large.png)
![Navbar mobile collapsed](/static/images/screenshots/navbar-mobile-small.png)

<br>
</details>

#### **Jumbotron**
<details>
Directly under the top navigation bar the user is greeted with a "hero image" in a jumbotron display. On the homepage the jumbotron relays a message quickly describing the content and essence of the forum site, it also informs the user that to access the full content of the site - the user needs the create an account. A link to the sign up page helps the user to quickly navigate to the sigt straight from the jumbotron's welcome message. As the user moves around on the site the text in the jumbotron changes to a "logo text" that also functions as a link to the home page. The hero image behind the text sets the mode for the site and acts as a visual information for the user to what the site is about. The image also contains the color team for the site. For better contrast of the text on smaller screens, the jumbotron displays an overlay on screens-sizes smaller than 800px.

<br>
<br>

![Jumbotron home desktop](/static/images/screenshots/jumbotron-home-desktop.png)
![Jumbotron forum desktop](/static/images/screenshots/jumbotron-desktop.png)

<br>
<br> 

![Jumbotron home mobile](/static/images/screenshots/jumbotron-home-mobile.png)
![Jumbotron forum mobile](/static/images/screenshots/jumbotron-mobile.png)

<br>
</details>

#### **Topic navigation**
<details>
There is a second navigation bar under the jumbotron image that displays the topic of the discussion forum. There are three discussion topics: "Gear : a topic about anything gear related", "Technique : where the players can ask for technique tips as well as give each other technique tips" and "Anything : And eveything else that the community like to discuss with each other, a social platform.". The last item in the menu is the "Play" topic, that displays requests from other user to find a team or a player to play with. The navigation topics are highlighted when hovered or clicked. 

<br>
<br>

![Topicnav desktop](/static/images/screenshots/topicnav-desktop.png)
![Topicnav desktop highlighted](/static/images/screenshots/topicnav-highlighted-desktop.png)

<br>
<br> 

![Topicnav mobile](/static/images/screenshots/topicnav-mobile.png)
![Topicnav mobile highlighted](/static/images/screenshots/topicnav-highlighted-mobile.png)

<br>
</details>


#### **Topic list**
<details>
After a user have chosen one of the three discussion topics they are greeted with a view of the posts under that topic. The posts are ordered by creation date, with the newest post first. If there are more than six posts under each topic, the site is paginated and the user can move forward or backward by clicking the navigation furthest down underneath all the posts. Each post displays the title, topic, content of the post as well as the author of the post and when the post was last edited. There is also two counters showing the amount of comments and likes the post have gotten. If the user wants to read that post and see the comments, the whole card works as a link to the post display. If the user wants to add a post, there is also a navigation button at the start of the list that takes the user to the add post form. Only logged in users get to see the button since that feature is for members of the forum only.

<br>
<br>

![Topic desktop](/static/images/screenshots/Topic-desktop.png)
![Topic tablet](/static/images/screenshots/Topic-tablet.png)

<br>
<br> 

![Topic mobile](/static/images/screenshots/Topic-mobile.png)
![Topic scrolled mobile](/static/images/screenshots/Topic-scrolled-mobile.png)

<br>
</details>


#### **Topic posts**
<details>

The view of the topic post contains the post, a comments list section and an input box to leave a new comment. At the top of the post the user can once again read the title, the topic as well as the content of the post. It also shows who created the post, when and if it last was updated. Underneath is also to social interaction counters, displaying how many comments the post has as well as how many likes. The amount of interaction the site user have access to depends on if the user is just browsing the page, is logged in and created the post as well as if the user have created any comments. A none registered user can see and read the comments but no more, neither comment or like a post. A user that is reading the post can like or unlike the post, leave a comment and edit or delete their comment. THe post creator can, except from all of the above, also edit and delete their post.

<br>
<br>

![Topicpost desktop](/static/images/screenshots/topicpost-desktop.png)
![Topicpost desktop none user](/static/images/screenshots/topicpost-desktop2.png)
![Topicpost tablet](/static/images/screenshots/topicpost-tablet.png)


<br>
<br> 

![Topicpost mobile](/static/images/screenshots/topicpost-mobile1.png)
![Topicpost scrolled mobile](/static/images/screenshots//topicpost-mobile2.png)
![Topicpost fully scrolled moile](/static/images/screenshots/topicpost-mobile3.png)

<br>
</details>

#### **Play event list**
<details>
As with the topics listed under the first three discussion topics of the forum, the 'Play' choice in the topic navigation renders a list of play event inquires from other community members. The posts can be two kinds of inquires; to search for a team or to find a player for your team. The post displays the time and date the post creator wishes to play, the location as well as how many have commented on the post.
 
<br>
<br>

![Play list desktop](/static/images/screenshots/play-desktop.png)
![Play list tablet](/static/images/screenshots/play-tablet.png)
![Play list mobile](/static/images/screenshots/play-mobile.png)

<br>
</details>

#### **Play event posts**
<details>
The view of the play event post contains the same features as the topic post described above, except that the play event posts also highlight the time, date and location of the planned game. Underneath the post is a comments section and comments box (if the user is logged in). It also shows who created the post, when and if and when it last was updated. One difference with the play event posts is that the social interaction counters only show the amount of comments on the post. There are no way to like or unlike a play event inquiry. The feature has been activly decided against to encurage straight communication via comments with the inquiree if the user wants to join in for a game. As with the topic posts, the amount of interaction the site user have access to depends on if the user is just browsing the page, is logged in and created the post as well as if the user have created any comments. A none registered user can see and read the comments but no more, neither comment or like a post. A user that is readning the post can leave a comment and edit or delete their comment. The post creator can, except from all of the above, also edit and delete their post. If a user leaves a comment anywhere in the forum, they get a confirmation message.


<br>
<br>

![Play display tablet](/static/images/screenshots/play-display-tablet.png)
![Play display tablet message](/static/images/screenshots/play-display-tablet-message.png)

<br>
<br> 

![Play display mobile](/static/images/screenshots/play-display-mobile1.png)
![Play display mobile](/static/images/screenshots/play-display-mobile2.png)
![Play display mobile](/static/images/screenshots/play-display-mobile3.png)

<br>
</details>

#### **Add Post**
<details>
To add a post in the forum the user has to be logged in. There are two way to add a post, through the add button under the topic navigation that are displayed on all topic list views and the homepage. Or by choosing to add a post or play event from the dropdown menu in the top navigation bar. The post form to add a new topic to the forum gives the user a list of choices of the topics to choose from. Then the user has to pick a title and write their content. All three fields are required before the user can create a post. If the user submits a form with incorrect input, they get an error message that displays what went wrong. If the post was created successfully, the user is redirected to the homepage where they get confirmation that the post has been submitted both by a message and by seeing their post at the top of the recently added posts. 

<br>
<br>

![Add post button](/static/images/screenshots/add-post1.png)
![Add post dropdown](/static/images/screenshots/add-post2.png)

<br>
<br> 

![Add form](/static/images/screenshots/add-form.png)
![Add choices](/static/images/screenshots/postchoice1.png)
![Add error](/static/images/screenshots/add-error.png)
![Add success](/static/images/screenshots/add-success.png)

<br>
</details>

#### **Add play event**
<details>
To add a play event the user has the same choices as with adding a post, by choosing to add at the play event list or by chosing to add an event from the dropdown menu. There are two topics to chose from, 'Team' or 'Player. The form requires that the user specifies a location, a description of the event as well as to fill out the date via a calander and the time via a seperate field. All five fields are required before the user can create a post. If the user submits a form with incorrect input, they get an error message that displays what went wrong. If the post was created successfully, the user is redirected to the homepage where they get confirmation that the post has been submitted both by a message and by seeing their post at the top of the recently added posts. 
(The choices how to add a play event post and the messages are the same as when the player adds a regular forum post, see reference images above).

<br>
<br> 

![Play form](/static/images/screenshots/play-form.png)
![Play choices](/static/images/screenshots/playchoice1.png)
![Play choices](/static/images/screenshots/playchoice2.png)
![Play choices](/static/images/screenshots/playchoice3.png)

<br>
</details>

#### **Edit Post**
<details>
To edit the forum post or play event, the user can either find their post through the forum posts or find a list of the user's own posts on their profile page and navigate to the post from their (more information on the profile page, see below). The fields are prepopulated with the content of the post the user wishes to edit.

<br>
<br> 

![Edit button](/static/images/screenshots/edit.png)
![Edit post](/static/images/screenshots//edit-post.png)
![Edit play](/static/images/screenshots/edit-play.png)

<br>
</details>

#### **Delete Post**
<details>
To delete a post the user can use the same tactic to find their posts as when they want to edit a post, either from the forum list views or from the personal page. The delete button has an outline color of yellow that turns the whole button yellow if the user hovers or clicks the button. On doing so a modal i displayed over the site, asking the user if they are sure they want to delete their post. The user can choose to cancel the request and go back to the post, or to confirm the deletion of the post. If the post is deleted all the comments will be as well.

<br>
<br> 

![Delete button](/static/images/screenshots/delete.png)
![Delete modal](/static/images/screenshots/delete2.png)

<br>
</details>

#### **Comments**
<details>
As a site user you can read all the comments even if you are not logged in. The comments section are located below the post and if the mobile screen is narrow the comments box to leave a comment is located last. A non logged in user can not see the box to add a comment. The user that has left a comment on a post has the choice to edit or delete their comment. The function to edit and the delete are almost identical to editing and deleting a post.

<br>
<br> 

![Comment not logged in](/static/images/screenshots/none-comments.png)
![Comment](/static/images/screenshots/comment.png)
![Edit comment](/static/images/screenshots/edit-comment.png)
![Delete comment](/static/images/screenshots/delete-comment.png)

<br>
</details>

#### **Like Post**
<details>
To add more interactivity and a more social aspect to the forum, the user has the oppertunity to like or unlike post that the user finds interesting, good, agrees with and so on. A user that is not logged in can see the amount of likes but can not interact with the function. It's only forum posts that a user can like and the amount of likes are displayed at recent posts, list view and at the posts view itself. If the comment is liked by the user the hollow heart icon becomes solid, and vice versa if the user decides to unlike the post.

<br>
<br> 

![Likes list](/static/images/screenshots/likes.png)
![Likes post](/static/images/screenshots/likes-post.png)
![Toggled like](/static/images/screenshots/liked.png)

<br>
</details>

#### **Profile Page**
<details>

In the dropdown menu on the left hand side of the navigation bar at the top, the user can reach their personal page. The personal page displays the username (read only) and if the user has an email adress attached to the account. An email adress is not required to start an account but if the user wants to connect an email account to their profile they need to verify their email as well. They can also leave it unverified. The email adress have no larger function conneted to the forum as of the features the forum displays today. 

Except for seeing their username and email adress field, the user can access all of their posts (not comments) from the profile page as well. There is a list display underneath the profile information. If the user clicks on a list link they will be transported to the site of the post. 

<br>
<br> 

![Profile page](/static/images/screenshots/profilepage.png)
![Update email](/static/images/screenshots/update-email.png)

<br>
</details>

#### **Contact Form**
<details>
Both logged in users and none logged in users can contact the admin of the page through the contact form linked to in the navigation bar at the top. The contact form goes directly to the back end administration site. As the user do not need to verify an email to start an account, the email field is required as mandatory for all so that the admin users can properly contact the user back. The contact form is a way for site users to leave feedbak, report ill behavior, to ask questions about the site and so on.

<br>
<br> 

![Contact form](/static/images/screenshots/contact-form.png)
![Confirmation](/static/images/screenshots/message.png)

<br>
</details>

#### **Search Function**
<details>

At the top right corner is a search function for the site. The site user does not need to be verified to search the topics. The search renders posts with the searched value in the forum post title or content or in the play events description. Each post is renderd in a separate list depending on where the search result was found. If the input dosent render a finding, the user gets feedback directly.

<br>
<br> 

![Search bar](/static/images/screenshots/search-bar.png)
![Search fail](/static/images/screenshots/seach-team.png)
![Search success](/static/images/screenshots/search-success.png)

<br>
</details>

#### **Admin**
<details>
An admin user can access the Django administration backend features directly from the dropdown bar after the user logged in. In the admin section the admin can create and delete posts, read contacts form sent to admin as well as remove users. The admin can also serch and filter through the various posts in the forum. 

![Search bar](/static/images/screenshots/admin%20.png)

<br>
</details>

#### **Future Feature**

Working with the kanban board and prioritizing the content in must/should/could naturally left ideas for the forum unfinished due to lack of time. What I would like to implement to the site in the future is:
- Email notifications when someone replies to a user's post
- Notifications when the user logs in, that someone has liked a post
- Possibility to directly repost another user to admin if they misbehave
- A more complete profile page with password reset, user image and description.
- The possibility to post videos and articles.

[Back to top](#padel-pals)

<br>

## **Surface**

### The Design

Due to failure in time management, this section is not reday before submitting the project.

[Back to top](#padel-pals)


## Skeleton

### Technologies
---

#### **Languages**

- **Django**
<br> For this full stack project the Python based framework Django is the development language for the application. I used PostgreSQL database, psycopg2 as the adapter and a gunicorn server. I installed a battery of extra libraries to help run everything smoothly:

    * Cloudinary (to host static files)
    * AllAuth (for authentication)
    * Summernote (for the django admin)
    * Crispy forms (to render good locking forms)
    * Bootstrap 4 (to style the content and make it resposive)
    * Whitnoise (to serve the static files)

- **HTML5**
<br> I used HTML to create the base structure of the project. I started with a basic boilerplate set up and created the first crude structure of the page out of the original design. 

- **CSS3**
<br> The CSS was used to apply the custom styles to the HTML skeleton. In a separate document the creation of the design came forth. 

- **Javascript**
<br> A small amount of javascript was used in this application, no separate script was needed and the code is located in the base template.

<br>

#### **Tools**

- [Heroku](https://www.heroku.com/)
    -  I used Heroku to deploy the application. 

- [Balsamiq](https://balsamiq.com/)
    - I used Balsamiq to make the basic wireframes for this project.

- [Cloudinary](https://cloudinary.com/)
    - I used to create the API's that connects the application to the spreadsheet at Google Sheet. 

- [Lucid Chart](https://www.lucidchart.com/pages/)
    - I used Lucid Chart to design the data model and list mock up for the project.

- [GitPod](https://www.gitpod.io/)
    - I used GitPod as the code editor as well as to display to test out changes in my code.

- [GitHub](https://github.com/)
    - I used GitHub to create a repository for my project.

- [Gmail](https://gmail.com)
    - I used a email account on gmail to work as the backend email ater deplayment.

- [Cloudinary](https://cloudinary.com/)
    - I used to create the API's that connects the application to the spreadsheet at Google Sheet.


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

    - Then add config vars by clicking 'Reveal Config Vars'. I used _Config Var_ called `PORT`, set to `8000`.
    - If you have credentials for your project, you need to add these as well. Create another _Config Var_ called `CREDS` and paste the copy of the requeriments code inside your credentials file into the value field.

- Now it's time to deploy the app. Go back to the top of the page and click "Deploy".
- Choose a deployment method, I used GitHub since my repository is located on GitHub.
- Scroll down to 'Connect to GitHub' and search for your project. Make sure you are connected to the right GitHub account. Click 'Connect'.
- Keep scrolling downwards, now you can choose between Automatic Deployment or Manual Deployment. I choose Manual first, until the app was properly deployed and a link to the app was visual. Then I choose to enable automatic deployment for smoother testing. 

The live app can be found here: https://padelpals.herokuapp.com/
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
- Press enter and then install the dependencies you like to use for the project.
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

For most of the development and bug fixes I went back to the Code Institute LMS (over and over again) and the learning material for this section of the course. I also turned again and again to [DjangoProject](https://www.djangoproject.com/) and [Get Bootstrap](https://getbootstrap.com) as well as to the Slack community and the search function, where I found many tips when I got stuck. When I didn't find the answers to understand what I needed to change there, I consulted external sources while searching for the answer using Google. In some cases I used bits of code from external sources in my project, if so they are credited in the code and / or below. Usually I took inspiration from an outside sourse, to learn how it was done, but in the end had to modify it to suit my project.

Some of the other sites media I frequently **consulted** was :
<br>

* [Codemy.com](https://www.youtube.com/c/Codemycom) - the turorials 'Create a simple django blog' & 'Django Wednesdays'
* [CodingWithMitch](https://www.youtube.com/channel/UCoNZZLhPuuRteu02rh7bzsw)
* [Fullstack Python](https://www.fullstackpython.com) 
* [Stack Overflow](https://stackoverflow.com/) 

- To get the Django framework installed and set up, I followed the Code institutes Django Blog video and cheatsheet.
- I built the navbar with codeinspiration from [Get Bootstrap](https://getbootstrap.com/docs/4.3/components/navbar/)
- To understand better how to show extra content when I rendered my views, I consulted [Django Project](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/) and [StackOverflow](https://stackoverflow.com/questions/63308865/get-threads-from-specific-forum-category-in-django-view), I also watched Corey Schafers [Python Django Tutorial](https://www.youtube.com/watch?v=-s7e_Fy6NRU) and found help from [Tutorialguruji](https://www.tutorialguruji.com/python/django-pass-multiple-models-to-my-listview/)
- I learnt more about slugifying from [Full stack Python](https://www.fullstackpython.com/django-utils-text-slugify-examples.html):
```
base_slug = slugify(self.title, allow_unicode=allow_unicode)
```
- and [Stack OverFlow](https://stackoverflow.com/questions/42429463/django-generating-random-unique-slug-field-for-each-model-object):
```
 self.slug = ''.join(str(random.randint(0, 9)) for _ in range(8))
 ```
 - Inspiration for how to build the profile page came from [app-generator](https://github.com/app-generator/sample-django-extended-user-profile) and [Django Project](https://docs.djangoproject.com/en/4.0/topics/auth/default) 
 - On  I learnt more about pagination on [Codemy.com](https://www.youtube.com/watch?v=N-PB-HMFmdo) and [Django Project](https://docs.djangoproject.com/en/4.0/topics/pagination); code credit for the code in the pagination.html template!
 - I learnt more about form widgets from [Stack Overflow](https://stackoverflow.com/questions/54748183/django-modelform-widgets-and-labels) & [Stack Overflow](https://stackoverflow.com/questions/9878475/django-modelform-override-widget) as well as from [CodingEntrepreneurs](https://www.youtube.com/watch?v=quJzUzCs6Q0) on youtube.com.
- Code credit for displaying a modal when deleteing a post or comment, section markted in the thread.html & play_display.html template: [Solutions Cloud](https://www.youtube.com/watch?v=uC9cgOQ0bXI)
- Inspiration for how to create a search bar comes from [Codemy.com](https://www.youtube.com/watch?v=AGtae4L5BbI)


<br>

### **Media**
- The jumbotron image comes from the artist Vincenzo Morelli at [Unsplash](https://unsplash.com/photos/Cj35lHL4atY).
- The image at the top of this page, that shows how the website is presented on different media screens are a screenshot from [Am I responsive?](http://ami.responsivedesign.is/)
- The [AudioWide](https://fonts.google.com/specimen/Audiowide) font come from [Google Fonts](https://fonts.google.com/).
- The template used in the project was provided by Code Institute.

<br>
<br>

### **Acknowledgement**

- My mentor **Precious Ijege** at Code Institute for valuable input and encouragement.
- A big thanks to the tutor Alex at Tutor support, who understands my blacked out brain and explanations and pointed me towards a simple solution when I ran into a problem displaying the topic navigation on all sites.
- The Slack community for being such an open, warm and sharing place. 
- **Viet Hoang** for letting me run the app by him and for getting user experience input before, during and at the final stage of the project.


[Back to top](#buy-me)

---
