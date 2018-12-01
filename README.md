# Project Two App

## Overview
### What is ths app for?
This is my project two application. It is a website created for a Governor elect for US state Nevada which uses a backend database and displays data using filters. This is used to promote the candidate for election. The main idea involves
- The education page, the user will filter two Nevada versions that will highlight the need for funding. They can also compare the results with two other states and see results on screen. 
### What does it do?
This app will show images and information for the campaign and focus on education funding using a database (school donations data), this will allow users to fill in a contact form and filter a database and display the information.
### How does it work?
The app has been created using flask and uses a noSQL database from a third party. This is hosted on Heroku and styled using Bootstrap, the mongo database uses various javascript frameworks to filter and display the data.
## Features

### Existing Features
- Database used has been altered to reflect information i want to show users by adding new data, removing old data, amending data to fit my requirements.
- When pressing on the education header line, more information will slide toggle and it to the user.
- The contact form has validation requirements and JS alert once the user has completed the form correctly.
- Images will change styling when hovered over
- Buttons on About page will show more information when pressed.

### Features Left to Implement
- Extra graph formats to be added to showcase campaign

## Tech Used
### This Includes:
- [Flask](http://flask.pocoo.org/)
    - **Flask** used to display our website pages and retrieve data from the database and return it to the browser.
- [MongoDB](https://www.mongodb.com/)
    - **MongoDB** used to facilitate the backend database.
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** used to give our project a simple, responsive layout.
- [PyCharm](https://www.jetbrains.com/)
    - **PyCharm** used to create app.
- [D3](https://d3js.org/)
    - **D3.js** used to manipulate data driven charts with filtration using DC and cross filter..
- [DC](https://dc-js.github.io/dc.js/)
    - **DC.js** used for filtering data.
- [CrossFilter](http://square.github.io/crossfilter/)
    - **Crossfilter** used to view large datasets.
- [Heroku](https://www.heroku.com/)
    - **Heroku** used to showcase the application

## Testing
### Responsiveness
With bootstrap formatting i have configured the website to work on various screens using breakpoints.

### Browsers
Tested using the below browsers available
- Safari
- Chrome 
- Firefox 
- Internet Explorer
- IE Edge

## Deployment
### Local - How to run this site locally.
- Open CLI and `pip3 install flask`
- Download files from repository with requirements.txt which will have libraries used on project.

### Hosting - web application has been hosted on **Heroku**
- Created app using Heroku on web and add Herokupostgres database
- Changes to config vars on Heroku.
- Install on CLI `gunicorn` update requirements.txt
- Create Procfile to allow `Heroku` know this is a Flask application

## Contribution
- Images were sourced from google
- Social button styling was sourced from a third party but has been amended to suit my app.

## Author
William Russell