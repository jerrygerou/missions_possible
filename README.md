# Project missions_possible
Django app for creating survey questions and providing answers.


## Tech Stack
- Python/Django language/framework
- PostgreSQL database
- Bulma CSS framework

## Notes on the Project (User)
- A user can create an account or login to an existing account.
- A user can view the existing list of Missions.
- A user can create a new Mission.
- A user can view details of a Mission, consisting of its Questions and Answers, if available.

## Notes on the Project (development)
- A parent class was created for Questions, implementing an OpenEndedQuestion and RatingQuestion class.
- Answers track both a response and the user who responded.


## What's next? (What I'd do with more time)
- Would like to explore how to create parent class for Answers to dry up code.
- Explore multiple choice questions (create an array from provided string), radio or checkbox (depending)
- More visually pleasing.
- Deploy to Heroku.


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

- [ ] The visual design and the UI semantics aren't important for this challenge; style and interactivity are entirely optional    
- [ ] Allow questions to be re-ordered in a stable way, i.e. no question should have the same position    
- [ ] Allow responses to be searched    
- [ ] Deploy the application to Heroku
