# Radical Rides
The Radical Rides e-commerce platoform aims to address the pain point of .....  

Link to live site [here](https://radical-rides-7dc93d43c139.herokuapp.com/).

<p align="center">
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1700912560/Project%204/Screenshot_2023-11-25_at_11.41.37_AM_tswplp.png" width="auto" height="auto" alt="image of the Radical Rides website home page on all devices"></p>

## E-commerce business model & Product Model Canvas
A....

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1699533539/Project%204/Screenshot_2023-11-09_at_12.38.25_PM_me714m.png" width="auto" height="auto" alt="image of the Radical Rides product model canvas">

## Business Requirements
Prior to initiating the project's development, user stories were created to give a high level understanding of what the platform's functional requirements will be and they were assigned labels based on their importance using the MoSCoW prioritization method.   

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1700907160/Project%204/Screenshot_2023-11-25_at_10.10.48_AM_q4lvfq.png" width="auto" height="auto" alt="image of the Radical Rides website userstories">

The user stories were then placed into a kanban board in order to track the progress of the platform's development.  The Agile development kanban board can be found [here](https://github.com/users/Xalil404/projects/5/views/1).

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1700907194/Project%204/Screenshot_2023-11-25_at_10.12.21_AM_yeq1db.png" width="auto" height="auto" alt="image of the Radical Rides project agile kanban board">

## Wireframes
Once the user stories were completed, the next phase of the project was to complete the UX of all the expected pages and functionalites in the platform. All wireframes can be found in the designMD file [here](https://github.com/Xalil404/Radical_Rides/blob/main/DESIGN.md).  

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1700905215/Project%204/Screenshot_2023-11-25_at_9.36.39_AM_nwxc2j.png" width="auto" height="auto" alt="Radical Rides project wireframes"> 

## Database Schema
After the wire-frames completion, a database schema was created to understand what information should be stored on the back-end database.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1699528747/Project%204/Screenshot_2023-11-09_at_11.18.22_AM_ho9t8k.png" width="auto" height="auto" alt="Radical Rides Project DB schema"> 

## Features 
The Radical Rides e-commerce site consists of the following pages and features:

* Landing Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1699528747/Project%204/Screenshot_2023-11-09_at_11.18.22_AM_ho9t8k.png" width="auto" height="auto" alt="Radical Rides landing page"> 

## Testing
All fucntional testing, user story testing, device compatibility testing and browswer compatibility testing can be found in the [TestingMD](https://github.com/Xalil404/Radical_Rides/blob/main/TESTING.md) file.

## Deployment

Deployment of the Radical Rides application required deployment of the web app on 3 platforms: Heroku, ElephantSQL and AWS S3 through the following steps:

* In [ElephantSQL](https://www.elephantsql.com/) I created a new instance and copied the new database URL.

* The on [Heroku](heroku.com) I created a new application and in the app's config vars section added the ElephantSQL database URL.

* In my project's settings.py file I installed psycopg2, imported the dj_database_url, commented out the DATABASES section and replaced it with another temporary DATABASES section, migrated the database models to the new database, loaddata-ed the categories, products and created a new superuser. After completing the migration I removed the newly created temporary DATABASES section and uncommented the original DATABASES section, git commited and git pushed my code in order to initiate the deployment.

* Then on AWS I created a new bucket to store static files and configured the bucket's settings. In the bucket's settings, I updated the CORS configuration, enabled ACLs, updated object ownership permissions, generated a bucket policy, created a new group in the Identify and Access Management (IAM) section, attached the newly generated bucket policy to it, and finally retrieved and downloaded the access keys in a CSV file.

* Back in the IDE I added 'storages' to my apps in settings.py and an additional setting to use AWS storage.

* In [Heroku](heroku.com), in the config vars section, I added the AWS retrieved keys and to use AWS and removed the disable collect static variable so that static files would be pushed to S3.  

* Back in the IDE again, I added a custom_storages.py file, imported S3Boto storage and added a media and static storage classes. After committing and pushing the latest changes, I deployed the app again.

* Back in AW S3 I created a media folder, uploaded all the proudct images, granted them public read access and completed the media upload process. 

* Then from the [Stripe](https://stripe.com/en-ie) admin interface I retrieved the Stripe public and private keys and added them as config variables in the Heroku app settings.  Also in the Stripe admin dashboard I added the web app's checkout URL in the webhook endpoint URL section and marked it to receive all events. 

* I then copied the Stripe webhook signing secret and added to the config vars in the Heroku settings.

## Credits

* [Shopify](https://www.shopify.com/tools/business-name-generator) to generate the website business name.

* [Colors](https://coolors.co/) to generate the website branding and color palette. 

* [Unsplash](https://unsplash.com/) & [Pixels](https://www.pexels.com/) for marketing images.

* [Favicon.io](https://favicon.io/) for web app Favicon. 

* [Online Converter](https://www.online-convert.com/) was used to convert jpeg or png images into webp files.

* [Github](https://github.com/) for version control.

* [GoogleFonts](https://fonts.google.com/) for fonts selection.

* [FontAwesome](https://fontawesome.com/) for icons selection.

* [Django Framework](https://www.djangoproject.com/) for adminpanel, account authentication and other apps.

* [Heroku](https://www.heroku.com/) for front-end deployment.

* [FlexDex](https://www.flexdexskateboards.com/) and [Decathalon.ie](https://www.decathlon.ie/) for product stock data.

* [Amazon S3](https://aws.amazon.com/s3/) for hosting static files.

* [ElephantSQL](https://www.elephantsql.com/) for database hosting. 

* [Bootstrap](https://getbootstrap.com/) for HTML and CSS code snippets.

* The Code Academy [Boutique Ado](https://boutique-ado123321-0cc6174e0aff.herokuapp.com/), [Task Manager](https://zadachamanager-d3722b3cb1b7.herokuapp.com/), [To Do App](https://todoprilozheniya-b8e10f9f2dc1.herokuapp.com/), and [Code Star Blog](https://helloblog-eb1bdbb756c3.herokuapp.com/) walk-through projects for guidance during development. 

* [DrawSQL](https://drawsql.app/) to create database schema.

* [Miro](https://miro.com/) to create design wireframes.