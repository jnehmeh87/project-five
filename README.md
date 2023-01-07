# Portfolio Project 5 - Ader Films
## Purpose

Ader Films is a Django application for stock footage user e-commerce.

The users can can check the companie's work, have a profile, watch stock videos, add to bag and make purchases.

This application was created for the purpose of completing the Portfolio 5 for the Code Institute's Full Stack Developer & E-commerce course and is entirely fictional.
The project covers Full Stack framework with a user centric approach in mind.  A full list of technologies used can be found in the technologies section of this document.

Here is the live version of my project. [here](https://ader-films.herokuapp.com/)

![program Mock Up](assets/images/mockup.png)

## User Experience (UX)
The user can chech the website for new video stock footage or pictures and buy their needs of them. The user can also register and login to be able to create a profile and keep track of their purchases and receive emails. The Super user will be able to add, update and remove new items to the stock.

### User stories
* As a user, I want to be able to view items in bag
* As a user, I want to be able to register, login and logout
* As a user, I want to be able to sort items and categories 
* As a user, I want to be able to search 
* As a user, I want to be able to view details about items
* As a user, I want to be able to be able to view items in bag
* As a user, I want to be able to make purchases
* As a user, I want to be able to receive confirmation emails

#### First Time Visitor Goals
* Get to know more about Ader Films
* Check Ader films list of various work
* View video and picture stock footage
* Subscribe to Ader films newsletter, as well as register and have a profile

#### Returning Visitor Goals
* A returning user is to make a purchase for old or new stock footage

#### Frequent Visitor Goals
* Frequent visitors are likely looking for new stock footage that suits their need for their film production

### Languages used
* HTML, CSS, JavaScript, Python+Django
* Relational database (recommending MySQL or Postgres)

## Features
* On the home page have a nav bar as well as a footer. The user can read more about Ader films, as well as check previous production work. Also it includes a shop button that takes us to the store

![Home](assets/images/home.png)
![Shop now button](assets/images/shop-now.png)

* The footer remains on all pages, as well as the nav bar
![Footer](assets/images/footer.png)

* The user can register, login or logout

![Login drop menu](assets/images/login-drop.png)
![Login](assets/images/login.png)
![Logout](assets/images/logout.png)
![Register](assets/images/register.png)

* As well as they get notifications messages when they do or when they make a purchase or if any error

![Notifications](assets/images/notification.png)

* The user can see a list of items Video with their name, category and rating. They can directly add to back or see detailed view

![Item list View](assets/images/items-list.png)


* The user can also see how many items we have on page and sort by category, pricem location and name. As well as search for specific things

![Items quantity](assets/images/items-qt.png)
![Navbar drop down](assets/images/drop-down.png)
![Navbar drop down 2](assets/images/drop-down2.png)
![Sorting](assets/images/sorting.png)
![Search](assets/images/search.png)

* The user can see details of the item Video as well description about each item and and autoplay video. The user can see the video on full screen

![Item detail View](assets/images/item-detail.png)

* The authenticated user can personalize their profile and keep track of their purchases

![Personalized profile](assets/images/personalized-profile.png)

* Add to bag can be made directly from items list, as well in the item detail and a bag toast appears with items inside 

![Item Card](assets/images/items-card.png)
![Bag toast](assets/images/bag-toast.png)

* Inside the bag, a user can read info about items as wel as see prices and remove item from back. They can shop more and checkout

![Bag](assets/images/bag.png)

* On checkout a user can fill details and card details as well as see what is inside the bage befor purchase. After purchase the user receives a confirmation with billing details

![Checkout](assets/images/checkout.png)
![Purchase confirmation](assets/images/purchase-confirmation.png)
![Purchase notification confirmation](assets/images/purchase-notification.png)

* A super user can add, update and delete recipes. Edit and remove buttons are added both in the main page and the detailed view to have faster access. When adding or updating a recipe, we redirect to the detailed view of the recipe and when deleting we redirect to the home page, also there is a cancel button to take us back to the home page in case we do not want to delete.
![Add Item](assets/images/Add.png)
![Update Item](assets/images/update.png)
![Update message](assets/images/update-message.png)
![Delete Item](assets/images/delete-button.png)

* The footer has external links to [facebook](https://www.facebook.com/profile.php?id=100089241821179) page and [privacy policy generator](www.privacypolicagenerator.info)

![Social Media Links](assets/images/footer-social.png)
![Facebook Page](assets/images/fb-page.png)
![Privacy Policy](assets/images/privacy-policy.png)

* The footer also includes a subscribe to Newsletter by [Mail Chimp](www.mailchimp.com) with an account created for this project

![Mailchimp footer](assets/images/footer-mailchimp.png)
![Mailchimp login](assets/images/mailchimp-login.png)
![Mailchimp audience](assets/images/mailchimp-audience.png)

* I created a business email account for this project aderfilmsproduction@gmail.com with [Google](www.google.com) to test receiving and sending emails when subscribing or doing any purchase.

![Email sent](assets/images/email-sent.png)
![Email registration confirmation](assets/images/email-register.png)
![Email pruchase confirmation](assets/images/email-purchase.png)

## Future features:
- After purchase, a client will be redirected to a page to download High quality videos. 
- Calendar to book a meeting for film production purpose for other businesses.
- Adding a personalized page for people who works with ader films, featuring their work as well.


## Testing

I have manually tested this project by doing the following:
- Tested in my local terminal and the Heroku terminal.


## Bugs
### Solved Bugs
- Stripe wasn't functioning well as in the videos and that was affecting the email process. Tutors helped me surpass this and it appears that by using an older version of stripe, I wasn't actually needing the new code provided by Code institute. So when I set it back to the code use in the project, everything worked perfectly.


## Validator Testing
- The validator shows an error caused by crispy forms, The crispy form is causing an error on the recipe_details pages that I can't fix:
* Here is an example [https://validator.w3.org/nu/?doc=https://foodupmood.herokuapp.com/easy-candy-apples/]

- Those pages are validate and have no more issues
* Index.html [https://validator.w3.org/nu/?doc=https://ader-films.herokuapp.com/]
* signup.html [https://validator.w3.org/nu/?doc=https://ader-films.herokuapp.com/accounts/signup/]
* login.html [https://validator.w3.org/nu/?doc=https://ader-films.herokuapp.com/accounts/login/]

- PEP8
    - No errors were returned from PEP8online.com

## Deployment

To deploy the project, allow other people to run the app and see it working, there are 3 methods to allow you to complete these actions:

### Forking and Cloning

Accessing GitHub and navigating to my repositories will allow users to copy my code directly from the source, either by forking or cloning: Accessing the base repository and clicking on the code button next to Gitpod link will bring up a drop-down to create a repository of your own in your own GitHub repo. You can also download a zip file and copy the information into a new file of your own making to continue working on it.

### Local Deployment

For my local deployment, I use Gitpod to edit and run my terminal;
- From GitHub, once the repository has been created (either as a new project or by forking/cloning) I will then click on the Gitpod button to implement the creation of a workspace to edit the promotional sales review system.

***The workspace should not be closed due to the env.py file - as it is never added to GitHub, if you create a new workspace you will need to re-add the env.py file and reinstall all libraries used each time. Pinning a workspace and accessing it from Gitpod workspaces rather than GitHub button would prevent this loss of information each time***

### Remote Deployment

For this project, remote deployment is a complex procedure and I will list out the complete steps to make your site work on a separate hosting service; For my project, I will be using Heroku.

- This first step, once we are in Gitpod, is to install our required packages and libraries:
    - Using Command Line Interface (CLI) in the terminal, type:

            pip3 install Django==3.2 gunicorn
            pip3 install dj_database_url psycopg2
            pip3 install dj3-cloudinary_storage

    - we need to add these to our requirements.txt file using the CLI:

            pip3 freeze --local > requirements.txt

- We now need to build our Project structure using the CLI:

        django-admin startproject PROJ_NAME .

***The trailing full stop is very important so please don't forget to include it in your command***

    - For my project, I named it projectFour, but you can choose anything.

- Once we have the project, we need to create an actual app to handle our individual functions:
    
        python3 manage.py startapp APP_NAME

    - My app is called collection as it is designed to handle my collection of characters, comments, series, and suggestions.

- Now we have an app, we need to add it t our approved INSTALLED_APPS in the Project settings.py file

- Once they are linked, we have to migrate changes to our database - by creating the app we have created a models.py file that handles our database designs and these have to be migrated over to the database to function. To do this, in the CLI terminal, type:

        python3 manage.py migrate

- To test if this is correctly built, in CLI, type:

        python3 manage.py runserver

This has built the foundation for our project, now we need to get the Heroku App built to receive the information from Github.

- In Heroku.com create/sign in to account and then navigate to the dashboard and create a new app with an appropriate APP_NAME and set the region to whichever is most appropriate - for myself it was Europe.
- We need to add a database to the app to store our uploaded record entries: For this, we need to go to the Resources tab and run a search for the Add-on called 'Heroku Postgres'
- in the Settings tab, we can now click Reveal Config Vars and we have a new KEY/VALUE pair for our DATABASE_URL with a Postgres:// address. Copy the Value in its entirety.

We will now be swapping between our Dev Environment as well as Heroku to complete deployment.

- In our Dev Environment, we need to create a new env.py file to handle all the values that we need to keep secret. This must be at the top level of our file structure. We need to import a library and define some details into this file:

        import os

        os.environ["DATABASE_URL"] = "paste postgres:// here"

        os.environ["SERCRET_KEY"] = "input a secret key"

***There are secret key generators online to help you generate one, or you can simply put a random string of letters together***

- Take the secret key value and head to the Heroku dashboard to reveal config vars again.
    - This time add a new key called SECRET_KEY
    - Paste in the value you copied from the env.py file

- In our settings.py file, we now need to make sure our project references the new variables from the env.py file, so we need to add below the current imports Path line:

        import os
        import dj_database_url

        if os.path.isfile("env.py"):
           import env

- There is already a secret_key variable, but we need to replace the existing value with os.environ.get("SECRET_KEY")
- We have a databases variable already assigned as well, but we are going to comment out this existing section and replace it with our own:

        DATABASES_URL = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }

- Now we have linked up a new Database, we need to migrate our files again to make sure they are linked - In CLI type:

        python3 manage.py migrate

Along with our DevEnv and Heroku, we also need one additional facility to handle our static and media files: AWS

- In a browser, navigate to https://aws.amazon.com/ and sign in/up for an account as ROOT USER.
- To create your account, you need to provide a credit card, you will get 1 free year per user and card. So your card won't be charged and you need to be dicreet about your secret keys you provide.
- Once in, you need to create your S3 bucket, where all your media and static files will be secured.
- Then you need to make to make the bucket public with IAM and assign your created S3 bucket to these privacy policy.
- You need to add this code in the settings.py and later in the config var in Heroku config vars, you need to enter the secret access key, Use AWS to true:

            if 'USE_AWS' in os.environ:
        # Cache control
                AWS_S3_OBJECT_PARAMETERS = {
                        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                        'CacheControl': 'max-age=94608000',
                }

        # Bucket config
                AWS_STORAGE_BUCKET_NAME = 'project-name'
                AWS_S3_REGION_NAME = 'eu-north-1'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

        # Override static and media URLs in production
                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


- The last thing we need to add to our Heroku, for now, is the DISABLE_COLLECTSTATIC Key with the value set to 1. To be removed on production.

- In order for AWS work properly, we need to install storages in the terminal then freeze requirements, by writing the following codes in the terminal:
        pip3 install storages
        pip3 freeze > requirements.txt

***The order of these lines is very important so make sure they are in the correct order!!!***


- We now need to link the file to the templates directory in Heroku. Under the BASE_DIR line, add:

        TEMPLATES = [
                {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                

- We need to tell the templates directory where we will find the templates we will be using, so in TEMPLATES, in the 'DIRS' variable list, we need to add 

        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'templates', 'allauth'),
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  #required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'bag.contexts.bag_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },

- The last thing in our settings.py file we need to include, is the host locations for running our app. We need one for Heroku and one for our local DevEnv, so we just need to adjust the following:

        ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]

- So now we have storage for our files, we need to add our folders to the correct locations - in our top level of the directory, we now need to add media, static, and templates.

- For stripe, we need to create an account at https://www.stripe.com and connect with their documentation to our javascript and webhook handler in the checkout app. We also need to add these lines in settings.py to allow our app access for payments:

        STRIPE_CURRENCY = 'usd'
        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
        STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

- To be able to work properly, we need to install stripe and countries in the terminal then freeze requirements by writing the following codes in the terminal:
        pip3 install stripe
        pip3 install countries
        pip3 freeze > requirements.txt

- Also to config vars in Heroku, we need to add Public, WH and Secret Key.

- For email handling, we need to add the following lines to settings.py:

        if 'DEVELOPMENT' in os.environ:
                EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
                DEFAULT_FROM_EMAIL = 'example@example.com'
        else:
                EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
                EMAIL_USE_TLS = True
                EMAIL_PORT = 587
                EMAIL_HOST = 'smtp.gmail.com'
                EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
                EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
                DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

- For heroku to be able to access and send emails, we also need to include in the conf var Email host user and email host password.

- We need to create a file that tells Heroku exactly how we expect the app to be run, so we need to create the Procfile (The initial cap is intentional) in the top level of the directory.
- In Procfile, we need to add:

        web: gunicorn PROJ_NAME.wsgi

- We now need to save the files and structure we have created in gitpod to our GitHub repository using the CLI:

        git add .
        git commit -m "deployment commit"
        git push

- Once this has been pushed to our main branch, we need to get our main branch deployed to Heroku.

- In Heroku, Deploy tab, we can add our Github repository to the deployment method. Once this is linked, we can scroll down and deploy the main branch.

At this point, the same screen from our 'runserver' test should now be displayed on the deployed webpage. This is the basic deployment of the app completed.

For final deployment:

- Change DEBUG to False in our settings.py file

- Add X_FRAME_OPTIONS = 'SAMEORIGIN'

This completes the settings part of Luke's Animé Base, but we still need to upload the final settings with:

        git add .
        git commit -m "deployment commit"
        git push

This should now have the final design of your site all working perfectly. You have successfully deployed the site!

***JUST TO REITERATE - For final deployment of site, remember to switch debug to False as this will allow anyone to gain access to secret information***

### Frameworks, Libraries & Programs used
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website and [Git Pages](https://pages.github.com/) is used for the deployment of the live site.
* [GitPod](https://gitpod.io/)
	* GitPod is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Am I Responsive?](http://ami.responsivedesign.is/)
	* Used to generate the screenshots for responsive design.

### Credits
- All videos and pictures used in the project are my own and I added the logo covering the media to keep the usage of media only to my Website.
- Youtube.com where I used my already uploaded previous work to the channel and included that in the home page
- To my Mentor [Chris Quinn](https://github.com/10xOXR) who has been an exceptional help throughout the course, so far.