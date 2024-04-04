# Wordle

Wordle is a Python command line interface (CLI) application which allows the user to play the well-known game of <a href="https://mashable.com/article/wordle-word-game-what-is-it-explained" target="_blank" rel="noopener">Wordle</a>.

The game was invented by Josh Wardle (Wordle is a pun on his surname) during the Coronavirus lockdown to amuse himself and his wife. It was launched in October 2021 and it is now played by millions worldwide. The rights of the game were sold in January 2022 to the New York Times. <a href="https://www.thesun.ie/tech/8147348/wordle-who-invented/" target="_blank" rel="noopener">(Source)</a>. 

The game can be enjoyed both by adults and children. To improve their vocabulary and grasp of the English language.

You can play the game here:
[Wordle](https://wordle-challenge-8b5fbd02f69c.herokuapp.com/)


[Back to top](#contents)

# Contents

- [Wordle](#Wordle)
- [Contents](#contents)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [Primary Goal](#primary-goal)
    - [Visitor Goals](#visitor-goals)
      - [First Time Visitor](#first-time-visitor)
      - [Returning and Frequent Visitor](#returning-and-frequent-visitor)
  - [Creation Process](#creation-process)
    - [Planning](#planning)
    - [Dependency diagram](#dependency-diagram)
    - [App Structure](#app-structure)
    - [Python Logic](#python-logic)
  - [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color Scheme](#color-scheme)
- [Features](#features)
    - [Mechanism of the Game](#mechanism-of-the-game)
    - [Winning message](#winning-message)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Python Packages](#python-packages)
- [Testing](#testing)
    - [Validation](#validation)
   - [Lighthouse Testing](#lighthouse-testing)
- [Bugs](#bugs)
- [Deployment to Heroku](#deployment-to-heroku)
  - [Project Deployment](#project-deployment)
  - [To fork the repository on GitHub](#to-fork-the-repository-on-github)
  - [To create a local clone of a project](#to-create-a-local-clone-of-a-project)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

[Back to top](#contents)
# User Experience (UX)

## User Stories

### Primary Goal

The primary goal of this CLI application is to provide a simple game for children and adults to help them develop their mastery and logical skills and to improve their grasp of the English language.

### Visitor Goals
The goal of the game is to guess the randomly selected 5 letter word within 6 attempts.

To aid the user they will be given feedback for each of their guesses.

#### First Time Visitor

  - A user can read the welcome message.
  - A user can find the game rules on the opening screen.
  - A user can expect a visual feedback for warnings, but also for winning the game.
  - A user can expect the number of attempts to be displayed in the winning message.
  - A user can choose to Play again after they have won, or choose to leave the game.

#### Returning and Frequent Visitor

  - A user who is familiar with the rules and has played before can begin straight away by typing their five-letter word. With <b>5,757</b> random words the game can be played as often as they want to.

[Back to top](#contents)
## Creation Process
### Planning

Before developing the application, I created a flow chart using LucidCharts (see below) which helped me organize dependencies and provided me with a blueprint to follow when developing the application.

For this project, I did not create any wireframes, as the application is rather simple in layout and is mainly intended to be played on the desktop. 

Example of requirements taken into account:

  - The game will use simple and clear representation
  - The user will have a choice to play again or stop playing the game.

[Back to top](#contents)
### Dependency diagram

  This is the original flow chart where I broke the program into managable clear steps. 

  ![Dependency Diagram](assets/images/wordle-lucid-chart.png)

[Back to top](#contents)
### App Structure
The application structure is very simple and uniformed as it is a CLI application and its dimensions are restricted by the display window of 80 characters per line on max 24 lines.

My main goal was for the content to fit within the restricted size of the window and to have all the features down to the user input prompt to be visible when launching in the Heroku application environment.

 ![Start screen](assets/images/start-screen.png)

[Back to top](#contents)

### Python Logic

  The logic of the game itself is not very difficult: The goal is to correctly guess the application's randomly selected five letter word.

  To aid the user they are given feedback as to which words closely match the randomly selected word.

  Anytime, the user does not provide the correct amount of letters for the word (5 letters), they are informed about their mistake and asked to correct their choice. All warning messages are displayed in red, so the user is alerted about the mistake. 

[Back to top](#contents)

## Design Choices

I tried to keep the game design very simple and legible. To make the letters for the user's guesses and how to play instructions to stand out I used [Colorama](https://pypi.org/project/colorama/).

I used a rectangular box to show all 6 guesses using [Box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character).

![Rectangular Game Box](assets/images/game-border.png)


[Back to top](#contents)
### Typography

I have not altered the type of font, as the original one I thought was legible and worked well with the application. 

[Back to top](#contents)

### Color Scheme

As regards the color scheme, as I explained in the Design Choices section I chose to install Coloroma. It is a key component to the game and in the next section I will explain more.

[Back to top](#contents)

# Features

[Back to top](#contents)

### Mechanism of the Game

The idea of the game is simple. To try and guess the five letter word randomly selected by the application at the start of the game. The text file <i>wordle_five.txt</i> is used to validate and to ensure only five-letter words are used.

#### ad 1) ATTEMPTS

The game is limited to 6 attempts each time the user makes a guess they are informed how many attempts they have remaining.

![Wordle Attempts](assets/images/wordle-attempts.png)


#### ad 2) GREEN LETTER

After each guess the user receives feedback to tell them if any of the letters contained in their guess are in the randomly selected word. 
To assist them, if any of the letters that are in the same spot as the randomly selected word. This letter (and any other letter) will highlight in <span style="color:green">Green</span> and display within the rectangular game box.

![Wordle Green](assets/images/wordle-green.png)

#### ad 3) BLUE LETTER

If any of the letters are in the randomly selected word but not in their current position they are highlighted in <span style="color:blue">Blue</span>.

![Wordle Blue](assets/images/wordle-blue.png)

#### ad 4) RED LETTER

Finally, if a letter is not in the randomly selected word they are highlighted in <span style="color:red">Red</span>. 


![Wordle Red](assets/images/wordle-red.png)

[Back to top](#contents)

### Winning message

When the user manages to guess the application randomly selected word.

The user is congratulated and informed of the number of attempts they had remaining.

![Wordle Win](assets/images/wordle-win.png)

At the end, the user gets a choice to play again 'Y' or to quit the game 'N'. 

When the user types 'Y' and presses Enter, the game is reset to the intial settings and allows them to enter their first guess.

If the user chooses 'N' and presses Enter, a goodbye message is displayed.

![Wordle Goodbye](assets/images/wordle-goodbye.png)

[Back to top](#contents)

### Future Features

- In the future, I could also implement a user name input at the start of the game and a scoreboard to track user scores using Google Sheets.

- ASCII word art for the game title and for the feedback.

- Further checking of user guess validation. The text file works well as a source of validation but I am aware its not perfect. It is missing some valid five letter words and may contain words that are not actually valid. But with 5,757 words I hope it will provide the user hours of learning and fun.

[Back to top](#contents)

# Technologies Used
- [Github](https://github.com/) - Used for hosting the repository.
- [Heroku](https://heroku.com/) - Used for deploying the application.
- [Visual Studio Code](https://code.visualstudio.com/) - Used for developing the application.
- [Github Desktop](https://desktop.github.com/) - Used to track and commit changes to github.
- [Git for Windows](https://gitforwindows.org/) - To push changes to github.
- [Python](https://www.python.org/) - Used for adding functionality to the application.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation of python code.

[Back to top](#contents)

# Python Packages

* [Colorama](https://pypi.org/project/colorama/) - Used to add colours to the terminal.
* [Random](https://docs.python.org/3/library/random.html) - Used to select a random word for each game.

# Testing

For testing the application, I used manual testing and external validators.

## Validation

The <i>word_five.txt</i> text file is a key file for the application as well as being the source for the five-letter words for the game. It is also used to validate to ensure exactly five-letter words are inputted by the user. If there are more or less letters (or non letters ie integers) in their guess they are told to try again. Basically, if the word does not appear in the text file it is considered to be invalid. 

I used manual testing throughout the whole development phase of the project and created a smaller text file with five letter words for testing and validation purposes and for the screenshots for this file.


Testing to ensure user guess is five letters in length:

* If guess is less than five letters: 

![Less than five](assets/images/test-less-than.png)

* If guess is greater than five letters:

![Greater than five](assets/images/test-greater-than.png)

* If guess is invalid and contains illegal characters.

![Invalid word](assets/images/test-invalid-word.png)

[Back to top](#contents)

## Lighthouse testing

The application has been tested in Lighthouse. Here are the results:

![Lighthouse testing](assets/images/lighthouse-test.png)

# Validation

Code Institution's Python Linter was used to test Python code for semantic and stylistic problems. 

All issues were fixed within linter application. The most common error I had was trailing whitespaces and having too much content on a single line. Once I had fixed all errors I copied over the previous version of the file (after saving first).

![Pylint Run](assets/images/linter-run.py.png)

The same test was also performed on the play.py file which is used by the application to check the states of the letter guesses for the game.

![Pylint Run](assets/images/linter-play.py.png)

# Bugs

As mentioned earlier the wordle_five.txt text file is not perfect but it performs its main purpose and acts as a good validation point despite its limitation such as possibly missing some five letter words.

The issue of dealing with duplicate letter is a common issue when coding Wordle application. This occurs when two identical letters are in a guess but only one occurence of the letter is in the word. This issue was resolve in this commit bc24dde.

# Deployment to Heroku

## Before deployment

<b>Requirements.txt</b> is used in Heroku to look for libraries/packages installed (ie Coloroma) that are required to run the application.

To get a list of all packages installed, the following command is run from the terminal (in Windows). <b>></b> redirects the output of the command to the file (requirements.txt).

<i>py -m pip freeze > requirements.txt</i>


## Project Deployment

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the button "New" in the top right corner, below the header and choose "Create new app".
   

  ![Create new app](assets/images/heroku-new-app.png)
   
3. Choose a unique name for the application and select your region. When done, click "Create app".
   
![Create app](assets/images/heroku-create-new-app.png)

4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button on the right.


   ![Heroku Settings](assets/images/heroku-settings.png)

  <b>Please note:</b> If you have used Google sheets your credential details must also be saved into the settings section. Using 'CREDS' in the key field and copying and pasting the details from the creds.json file used for the application into the 'value' input field opposite.)

  ![Heroku Settings](assets/images/heroku-creds.png)


5. Afterwards, scroll down to the "Buildpacks" section of the settings page and click the button "Add buildpack".

   
   ![Heroku Settings](assets/images/heroku-add-buildpacks.png)

6. First add "Python" package and then "node.js". Please ensure Python is listed first if not drag it upwards using your mouse above "node.js"
   
  
8. Scroll back to the top of the page and choose the "Deploy" tab. Then choose "GitHub" as Deployment method.
   


9. Go to "Connect to GitHub" section, search for your repository and then click "Connect".
   

10. In the "Automatic Deploys" section, choose your preferred method for deployment. At first, I used the manual deployment option, and later I changed it to automatic deploys. Afterwards, click "Deploy Branch".
 

The link to the the live application can be found here - 
The link to the GitHub repository can be found here - 


[Back to top](#contents)

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changed without affecting the original repository. Take the following steps to fork the repository:

1. Log in to **GitHub** and locate the repository you wish to fork.
2. On the top right hand side of the page is a button called **'Fork'**. Click on the button to create a copy of the original repository in your GitHub Account.


[Back to top](#contents)

## To create a local clone of a project

Take the following steps to create a clone of a project:

1. Click on the **Code** button in the right top corner.
3. In the **HTTPS** section, click on the clipboard icon to copy the displayed URL.
4. In your IDE of choice, open **Git Bash**.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **git clone**, and then paste the URL copied from GitHub.
7. Press **enter** and the local clone will be created.

[Back to top](#contents)

# Credits

## Content
The inspiration for this application is thanks to this version of the [game](https://www.wordle.ie/).

The framework for the Readme file is thanks to this [Readme](https://github.com/lucia2007/towers-of-hanoi/blob/main/README.md).

The rectangular box used to store the user's guesses are thanks to this [website](https://en.wikipedia.org/wiki/Box-drawing_character) for box drawing characters.

## Acknowledgements
- Thanks to this [Youtube tutorial](https://www.youtube.com/watch?v=SyWeex-S6d0) which greatly helped me as a newbie to Python programming.
- Thanks to help and guidance from my mentor Precious Ijege and for sending on the readme file which I used as a template.
- Thanks to this [Github repository](https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt) which was used as a source for the 5-letter words for the game.
- Finally, thanks to all at the Code Institute, particularly our course facilitator Kamil Wojciechowski. 

[Back to top](#contents)

