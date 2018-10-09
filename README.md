# missions_possible
Django app for creating survey questions and providing answers.


# Code Challenge    

A central feature of the platform is allowing researchers to build questions for mobile users to answer. We have a variety of question types ranging from open ended to video prompts. Regardless of the question type we accept a consistently formatted response which is suitable for viewing, analysis, and export. In our system, questions belong to a parent object, called a "mission", and are strictly ordered.

Your challenge is to create a small web application that replicates this core functionality. The application only needs to facilitate creating new questions, submitting responses, and viewing submissions.    

### Requirements    

- [ ] Users must be able to define two or more of these question types:    
    - [ ] Open Ended - Prompts users to write in a sentence or paragraph    
    - [ ] Single Choice - Provides several choices and a user may select one    
    - [ ] Multiple Choice - Provides several choices and a user may select one or more    
    - [ ] Rating - Allows a user to select a value between a minimum and maximum integer value    
- [ ] Users must be able to submit responses for each question in a mission    
- [ ] Users must be able to view all submitted responses in a mission    
- [ ] No authentication is necessary, but responses should belong to a single user    

### Technical Requirements    

- [ ] You may implement the application in any language or framework you like    
- [ ] You must use Postgres for the database layer (Make good use of the database)    
- [ ] You must use git to commit your progress (History matters)    

### Bonus    

- [ ] The visual design and the UI semantics aren't important for this challenge; style and interactivity are entirely optional    
- [ ] Allow questions to be re-ordered in a stable way, i.e. no question should have the same position    
- [ ] Allow responses to be searched    
- [ ] Deploy the application to Heroku
