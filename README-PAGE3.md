**Summary Statement:** This program aims at analyzing Covid-19 data from the link below.

https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/

The python program calculates the number of U.S. confirmed cases, U.S. deaths, and U.S. recovered to date. The python program uses a framework called Flask and Jinja2 to send this data via APIs and render these calculations to be displayed on the html dashboard. 

![Front-Page](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/web_app_update.png)

**Requirements:**
- Secure data at rest and in transit
- Use functions 

## Web Application

The web application is designed to display the COVID data that was processed and analyzed in the previous step. Javascript, HTML, CSS, and React was used in the creation of this app.

Packages Used:
Bootstrap 4.2
FusionCharts
FusionMaps
FusionCharts React

Step 1: Environment setup

The first step I did was install Facebook’s React boilerplate which sets up React and additional utilities that were used. This was accomplished in terminal by typing to create an environment w/ dependencies in my created folder:

npx create-react-app covid-dashboard
Bootstrap was also installed to create layout and user-interface:

$ npm install --save bootstrap
One of the tools I used to render charts in the dashboard was a package called FusionCharts.
$ npm install react-fusioncharts --save
$ npm install fusioncharts --save

https://www.fusioncharts.com/download/fusioncharts-suite-xt?framework=react

FusionMaps will also be used to render maps:
$ npm install --save fusionmaps
FusionCharts also provides a lightweight and simple-to-use component for React that can be used to add JS charts in react app without any hassle. We will be using it in our app. Let’s install it using the command below:
$ npm install --save react-fusioncharts
Step 2: Fetching data from [data science project]

Step 3: Building the dashboard layout

Import Boostrap into index.js so that it can be used to build the layout:
import "bootstrap/dist/css/bootstrap.css";

The application is divided into 5 parts:

- Navigation Section
- Charts
- COVID-19 Metrics
- Charts Section
- Login (next version)
- Search Button

After building each section, the dynamic web application now displays daily covid data analyzed by python.  
**Next version updates:**
- Enable single sign-on
- Require 2MFA
