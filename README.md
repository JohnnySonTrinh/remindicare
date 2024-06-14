# [RemindiCare](https://remindicare-c84864436945.herokuapp.com/)

The RemindiCare project is a comprehensive solution designed to assist users in managing their medication schedules effectively. As an innovative application, RemindiCare addresses the crucial need for a reliable and user-friendly platform to ensure medication adherence, which is a significant concern in healthcare management. By providing a suite of functionalities, including registration, user authentication, medication schedule management, reminders, tracking, logging, and analytics, RemindiCare aims to enhance the overall user experience and support both patients and caregivers in maintaining optimal health outcomes.

<div align="center">
  <img src="landing-page.png" alt="Landing page">
</div>

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/JohnnySonTrinh/remindicare)](https://github.com/JohnnySonTrinh/remindicare/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/JohnnySonTrinh/remindicare)](https://github.com/JohnnySonTrinh/remindicare/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/JohnnySonTrinh/remindicare)](https://github.com/JohnnySonTrinh/remindicare)
---

## Table of content

- [User Experience](#user-experience)
	- [Initial Dicsussion](#initial-discussion)
	- [User Stories](#user-stories)
	- [Project Goals](#project-goals)
- [Design](#design)
	- [Wireframes](#wireframes)
	- [Database Design](#database-design)
	- [Color Scheme](#color-scheme)
	- [Typography](#typography)
- [Features](#features)
- [Future Features](#future-features) 
- [Tools & Technologies Used](#tools-&-technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
---

## User Experience

### Initial Discussion

- Medication adherence is critical for the successful treatment of various health conditions, yet it is often challenging for patients to remember to take their medications consistently.
- Non-adherence can lead to severe health complications, increased healthcare costs, and reduced quality of life.
- RemindiCare seeks to mitigate these issues by offering a robust and intuitive app that not only reminds users to take their medications but also allows them to log and track their intake, view adherence patterns, and share important data with their healthcare providers.

### User Stories

- All user stories are mapped to Issues in Github, with acceptance criteria and tasks.
- We tracked the issues with a Github Project [progress board](https://github.com/users/JohnnySonTrinh/projects/7) and grouped them into Epics so that we could follow Agile methodology.

### Project Goals

- The main goal of RemindiCare is to create an simple, intuitive and reliable medication management app to enhance user adherence and support healthcare needs.
- Designed with a user-centric approach, the app aims to meet the needs of patients, caregivers, and healthcare providers.
- By leveraging a well-designed database, RemindiCare ensures that all user data is managed effectively.
---

## Design

### Wireframes
- To follow best practice and ensure that our site will look good on all screensizes, wireframes were developed for mobile and desktop sizes. 
  - We used [Balsamiq](https://balsamiq.com/wireframes) and [Figma](https://www.figma.com/design/M7sAzpW0rdoQYFe8Wh78Re/RemindiCare?node-id=0-1&t=Cd9Tcfz4qpEbdWce-0) to design our app wireframes.

<!-- Add Screenshot of wireframes -->

<details>
  <summary>Click to view Wireframes</summary>
    ![Screenshots of wireframes]()
    ![Screenshots of wireframes]()
</details>

### Database Design
- This database uses a Postgres database form Code Institute.
<details>
  <summary>Click to view ER Diagram</summary>
    ![ER Diagram for this project]()
</details>

### Color Scheme

- For the RemindiCare project, we have thoughtfully incorporated the color scheme of the partnering company to ensure a cohesive and professional appearance.
- By aligning our app’s design with the company's established visual identity, we aim to create a seamless and recognizable user experience.

<details>
  <summary>Click to view color palett</summary>
    ![RemindiCare color palett]()
</details>
<br>

We used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.


```css
:root {
  --clr-green: #2a834e;
  --clr-orange: #d15b21;
  --clr-cream: #f7efe9;
  --clr-blue: #00c1f3;
  --clr-purple: #531295;
  --clr-grey-1: hsl(208, 14%, 56%);
  --clr-grey-2: hsl(208, 10%, 37%);
  /* White/black color shades */
  --clr-white: #ffffff;
  --clr-black: #111111;
  /* Primary and secondary font families */
  --ff-primary: "Averia Serif Libre", serif;
  --ff-secondary: "Poppins", sans-serif;
  /* Commonly used CSS properties for consistency */
  --transition: all 0.3s linear;
  --spacing: 0.25rem;
  --radius: 0.5rem;
  --light-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}
```

#### Typography

We used Google Fonts for this project. The titles are Averia serif libre.
<div align="left">
  <img src="static/images/readme/font-averia-serif-libre.png" alt="Title font" width="400">
</div>

The main font is Poppins, which is clear and easy to read, for accessibility:

<div align="left">
  <img src="static/images/readme/font-poppins.png" alt="Main font" width="400">
</div>

---

## Features
ToDo!



---

## Future Features

<!-- These are all the awesome things that the page will have in the future -->
---

## Tools & Technologies Used

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![Git](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating wireframes.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
---
## Credits

Todo!

Thanks to the whole team!
