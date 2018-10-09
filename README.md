# Project missions_possible
Django app for creating survey questions and providing answers.


## Tech Stack
- Python/Django language/framework
- PostgreSQL database
- Bulma CSS framework

## Notes on the Project (User)
- A user can create an account or login to an existing account.
- ![login](https://user-images.githubusercontent.com/21090906/46682503-5591c080-cbb3-11e8-9846-4a13e09af652.png)
- A user can logout of said account.
- ![logged_out](https://user-images.githubusercontent.com/21090906/46682504-5591c080-cbb3-11e8-8968-e44e54b62cd6.png)
- A user can view the existing list of Missions.
- ![home](https://user-images.githubusercontent.com/21090906/46682502-5591c080-cbb3-11e8-8a5f-51a5e6a1af98.png)
- A user can create a new Mission, with a name and a description.
- ![mission_create](https://user-images.githubusercontent.com/21090906/46682626-aa353b80-cbb3-11e8-87ff-82569b3ec1ef.png)
- A user can view details of a Mission, consisting of its Questions and Answers, if available.
- ![mission_detail](https://user-images.githubusercontent.com/21090906/46682500-5591c080-cbb3-11e8-9c91-72e47579acc8.png)
- A user can create an OpenEndedQuestion for a Mission.
- A user can create a RatingQuestion for a Mission.
- ![question_create](https://user-images.githubusercontent.com/21090906/46682498-5591c080-cbb3-11e8-8e82-0f6e6287bddb.png)
- A user can submit an Answer for both OpenEnded and Rating Questions.
- ![open_ended_answer](https://user-images.githubusercontent.com/21090906/46682499-5591c080-cbb3-11e8-9f50-daa64aa18b1d.png)
- ![rate_answer](https://user-images.githubusercontent.com/21090906/46682497-5591c080-cbb3-11e8-9442-e5ee19528fc2.png)

## Notes on the Project (development)
- A parent/super class was created for Questions, implementing an OpenEndedQuestion and RatingQuestion class.
- Answers track both a response and the user who responded.
- A few unit tests are in place.
- Implemented a Makefile (faster commands)


## What's next? (What I'd do with more time)
- Would like to explore how to create parent class for Answers to dry up code.
- As the questions have differing Answer models, displaying on HTML is janky - OpenAnswer and Rating are displayed separately. I _could_ do `mission.question_set.all`, but that adds complication with Answer models displaying.
- Explore multiple choice questions (create an array from provided string), radio or checkbox (depending)
- More visually pleasing.
- Deploy to Heroku.


## Getting Started
- Clone repo
- Create database in psql (`create database missions_posible;`)
- `make server`
- http://localhost:8000/
- Run tests with `make test`


# Code Challenge Expectations
A central feature of the platform is allowing researchers to build questions for mobile users to answer. We have a variety of question types ranging from open ended to video prompts. Regardless of the question type we accept a consistently formatted response which is suitable for viewing, analysis, and export. In our system, questions belong to a parent object, called a "mission", and are strictly ordered.

Your challenge is to create a small web application that replicates this core functionality. The application only needs to facilitate creating new questions, submitting responses, and viewing submissions.    

### Requirements

- [x] Users must be able to define two or more of these question types:    
    - [x] Open Ended - Prompts users to write in a sentence or paragraph    
    - [ ] Single Choice - Provides several choices and a user may select one    
    - [ ] Multiple Choice - Provides several choices and a user may select one or more    
    - [x] Rating - Allows a user to select a value between a minimum and maximum integer value    
- [x] Users must be able to submit responses for each question in a mission    
- [x] Users must be able to view all submitted responses in a mission    
- [x] No authentication is necessary, but responses should belong to a single user    

### Technical Requirements

- [x] You may implement the application in any language or framework you like
- [x] You must use Postgres for the database layer (Make good use of the database)
- [x] You must use git to commit your progress (History matters)

### Bonus

- [x] The visual design and the UI semantics aren't important for this challenge; style and interactivity are entirely optional    
- [ ] Allow questions to be re-ordered in a stable way, i.e. no question should have the same position    
- [ ] Allow responses to be searched    
- [ ] Deploy the application to Heroku
