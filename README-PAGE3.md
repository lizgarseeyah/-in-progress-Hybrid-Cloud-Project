**Problem Statement:** This program aims at analyzing Covid-19 data and how it impacts our economy.

## Back-end

**Application Functionality:**
- Fetch data from data source (html)
- Import, clean, and preprocess the data
- Identify and apply best models (ensemble method)
- Feature Extraction and optimize data

**Requirements:**
- Secure data at rest and in transit
- Use functions 

## Front-end

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
Navigation Section
Query Section
Basic Daily and Total Metric
Charts Section
Login

**Application Requirements**
- Require sign-on
- Require 2MFA
- Frameworks: React?
