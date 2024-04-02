# Tower of Hanoi

Towers of Hanoi is a Python command line interface (CLI) application which allows the user to play a well-know game of <a href="https://en.wikipedia.org/wiki/Tower_of_Hanoi" target="_blank" rel="noopener">Tower of Hanoi</a>. The user has an option to choose the difficulty level. The easy level can be played in a minute, the more difficult levels will take some time, but will help the user develop and improve their logical thinking. 

This game can be played both by adults and children. In fact, the inspiration for replicating this game for my project came from seeing my daughter enjoy playing this game.

You can play the Towers of Hanoi here:
[Towers of Hanoi](https://towers-of-hanoi-game.herokuapp.com/)

[Back to top](#contents)

# Contents

- [Tower of Hanoi](#tower-of-hanoi)
- [Contents](#contents)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [Primary Goal](#primary-goal)
    - [Visitor Goals](#visitor-goals)
      - [First Time Visitor](#first-time-visitor)
      - [Returning Visitor](#returning-visitor)
      - [Frequent Visitor](#frequent-visitor)
  - [Creation Process](#creation-process)
    - [Planning](#planning)
    - [Projects Tool](#projects-tool)
    - [Dependency diagram](#dependency-diagram)
    - [App Structure](#app-structure)
    - [Python Logic](#python-logic)
  - [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color Scheme](#color-scheme)
- [Features](#features)
    - [ASCII Art](#ascii-art)
    - [Welcome message](#welcome-message)
    - [Slow Print](#slow-print)
    - [Difficulty Level](#difficulty-level)
    - [Initial Picture](#initial-picture)
    - [Mechanism of the Game](#mechanism-of-the-game)
      - [ad 1) FROM BASE](#ad-1-from-base)
      - [ad 2) TO BASE](#ad-2-to-base)
    - [Scores](#scores)
    - [Winning message](#winning-message)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Python Packages](#python-packages)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [External Testing](#external-testing)
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

The primary goal of this CLI application is to provide a simple game for children and adults to help them develop critical logical skills, but at the same time to teach them patience and perseverence, especially when playing the more difficult levels.

### Visitor Goals
Towers of Hanoi game has been designed to be straightforward, with minimalist design due to using CLI. The current version is aimed at people who enjoy puzzles and challenges so they can put their logical skills to test. The user can choose a level of difficulty and can challenge themselves the beat the minimum number of moves needed.

#### First Time Visitor
  - A user can read the welcome message.
  - A user can find the game rules on the opening screen.
  - A user can choose the level of difficulty by indicating a number of disks they want to play with.
  - A user can expect a visual feedback for warnings, but also for winning the game.
  - A user can expect the number of moves to be displayed in the winning message.
  - A user can compare their number of moves with the minimum number of moves needed.
  - A user can choose to Play again after they have won, or choose to leave the game.
#### Returning Visitor
  - A user is familiar with the rules and can start the game by clicking the Run button.
  - A user can choose the level of difficulty. The more disks they choose, the more difficult the game.

#### Frequent Visitor
  - A user can try to use the minimum number of moves which according to [Wikipeadia](https://en.wikipedia.org/wiki/Tower_of_Hanoi) is 2**n - 1.


[Back to top](#contents)
## Creation Process
### Planning

Before I started working on the actual application, I created a flow chart (see below) which helped me organize dependencies and provided me with a blueprint to follow when developing the app. This was extremely useful especially in moments when it was not clear where a certain function or a feature belonged, what the dependencies were or what should be tackled next. 

I tried to break each step into a managable bite-size function so the code would be easy to read and understand. I started by figuring out the dimensions of my disks and the maximum number of disks the user would be able to use for choosing difficulty levels. Afterwards, I focused on being able to move the disks from one base to another. At first I was printing the pyramids below each other for simplicity, but later I changed the layout to parallel for better readability and to go back to the original layout. Towards the end of the development process, I started adding some nice-to-have features, like clearing the screen for a less messy output or shortening and rephrasing the rules and prompts for better comprehension. As I went, I refactored the code wherever possible to make it easily comprehensible.

For this project, I did not create any wireframes, as the application is rather simple in layout and is mainly intended to be played on the desktop. But, I was inspired by this [picture](readme-images/tower-of-hanoi.png) and this [version in terminal](/readme-images/towers_of_hanoi_terminal.gif).

My main goal was for the content to fit within the restricted size of the window. The width of the window also predetermined the highest level of difficulty, as the largest disks needed to fit three times next to each other on the screen of 80 characters. I used the clear function to keep the CLI neat and easily readable.

Example of requirements taken into account:
  - The game will use simple and clear representation of the towers of Hanoi.
  - The user will be able to choose the level of difficulty.
  - The screen will be cleared periodically, so the user is not overwhelmed or confussed by a large number of print statements.
  - The game will show the scores in the winning message and compare them to minimum required moves.
  - The user will have a choice to play again or stop playing the game.
  
[Back to top](#contents)

### Projects Tool

I used Projects tool inbuilt in GitHub, [GitHub's Projects](https://github.com/lucia2007?tab=projects), to help me manage the scope of the project, to track my progress and record bugs, but also to jot down any ideas that were relevant for the application development. These ideas were either later applied in the code or dismissed if they did not seem to enhance the user's experience or improve the development process.

Whenever I had an idea related to the project, I would jot it down in the "To Do" section. Later, I would choose 2, max 3 things that were currently being worked on and I placed them in the "In Progress" section. If I became stuck on a task for whatever reason or depended on external input, I moved it to "Blocked". At last, when a task was completed, I would move it to the "Done" section.

This tool has been very benefitial for my development process, especially, because I could rely on having all the information there. I would write down the sources to be credited, or bugs to be fixed or ideas on how to improve some part of the application, so I did not have to worry about having forgotten something crucial. 

In the future, for a bigger project, I would focus on a more detailed description of the tasks and adding next steps or a deadline for each of the entries.

[GitHub Projects](readme-images/projects_tool.png)

[Back to top](#contents)
### Dependency diagram

  This is the original flow chart where I broke the program into managable clear steps. 

  [Dependency Diagram](dependency.drawio.svg)

[Back to top](#contents)
### App Structure
The app structure is very simple and uniform as it is a CLI application and its dimensions are restricted by the display window of 80 characters per line on max 24 lines.

[Back to top](#contents)
### Python Logic
  The logic of the game itself is not very difficult: The goal is to move all the disks from the first base to the last base. The main restriction is that the user may not place a bigger disk on a smaller one. The game can become quite long and tedius if the user is just randomly moving the disks and is not trying to optimize the number of moves. On the other hand, it can be quite motivating to try to achieve the minumum number of moves.

  I had to frequently manually validate the user's input to make sure that the correct type of input was returned. In case of a number input I had to check if a number was entered, and if it was within the required range. For a string, I had to check if the correct string was returned.
  
  Anytime the user does not provide the correct input, they are informed about their mistake and asked to correct their choice. All warning messages are displayed in red, so the user is alerted about the mistake. 
  
  I also had to check for logical catches like preventing the user from taking a disk from an empty pyramid, or placing a bigger disk on a smaller one.

  I used (Object oriented programming) OOP in some parts of the application for better manipulation with the objects. This proved helpful especially when moving the disks from one stack to the other, or for drawing the pyramids.

[Back to top](#contents)

## Design Choices

I tried to keep the game design very simple and easily legible. However, I used ASCII art to make the welcome and good-bye screens a bit more interesting. I also used the ASCII Art to inform the user of their win. The winning message is in yellow color to make it stand out more.

[Back to top](#contents)
### Typography

I have not altered the type of script, as the original one is well suited for this app. 

[Back to top](#contents)

### Color Scheme

As regards the color scheme, I mostly went along with the original setting, but I did install [Colorama](https://pypi.org/project/colorama/) in order to be able to use red color of font for warnings and yellow color for the winning display.

[Back to top](#contents)

# Features
### ASCII Art

I choose to use ASCII Art on the welcome page to improve the user experience and to get the user interested.

![ACSII Art](./readme-images/towers_of_hanoi_ascii.png)

### Welcome message

![Welcome message](./readme-images/welcome_message.png)

As soon as the page is loaded, the ASCII Art is displayed and a welcome message is gradually printed out. In the welcome message the rules and mechanism of the game are explained. 
### Slow Print

The welcome message and the rules are printed slowly so the user is not overwhelmed by the long text they would have to read when opening the app. 

The first few user options are displayed with a slight delay so the user has time to make a choice.

[Back to top](#contents)

### Difficulty Level

After the welcome message, the user is promted to choose a number of disks they want to play with. The more disks the user chooses, the more difficult and longer the game.

![Difficulty level](/readme-images/difficulty_level_input.png)

The user is expected to enter a number between 3 and 6. If they choose a number smaller or bigger than the given range, they are informed of their mistake and prompted to choose a number from the indicated range. Also, they are alerted if they choose a string instead of a number.

### Initial Picture

After the user chooses a number of disks, a "playground" with the correct number of disks is displayed.

![Initial Picture](readme-images/intial_picture.png)

[Back to top](#contents)
### Mechanism of the Game
A move consists of two steps:
1. The user has to choose FROM WHICH base they want to take the top disk.
2. The user has to indicate ON WHICH base they want to place the chosen disk.
#### ad 1) FROM BASE

The user must indicate from which base they want to move the disk. They may not take a disk from an empty base. They must choose a number between 1 and 3. If a mistake is made, the user is alerted by a message printed in red and they are prompted to correct their choice.

#### ad 2) TO BASE

The user must indicate on which base they want to place the disk. They must choose a number between 1 and 3. If a mistake is made, the user is alerted by a message printed in red and they are prompted to correct their choice. They may not place a disk on a base where the top disk is smaller than the chosen one.

[How to play video](/readme-images/mechanism_of_the_game.webm)

[Back to top](#contents)
### Scores

Each time the user moves a disk from one stack/pyramid to another, the number of moves is increased. The moves are displayed when the user has accomplished moving all the disks from the first base to the third base in the winning message, see below.

[Back to top](#contents)

### Winning message

When the user manages to move all the disks from the 1st base to the last one, they are informed of successfully finishing the game. 

![The Winning message](/readme-images/congratulations.png)

Within the winning message, the user is informed of the number of moves they used. This number is compared to the minimum number of moves which is 2**n -1. This can motivate the user to decrease the number of moves they use next time, or the user is congratulated on the use of minimum number of moves if that's what they achieved.

At the end, the user gets a choice to play again or to quit the game. 

When the user chooses the Play again option, the game is reset to the intial settings and the user can newly choose the level of difficulty.

When the user chooses to quit, a good bye message is displayed.

![Good-bye message](readme-images/good_bye.png)

[Back to top](#contents)
### Future Features
- I would like to improve the visualization of the disk being moved for the user to clearly see the moved disk. This is mainly because of a confusing situation when the user is trying to move a disk which is bigger than top disks on all the other stacks and thus has to return the disk to its original position. 

- In the future, I could also implement the user name usage and score tracking functionality.

[Back to top](#contents)

# Technologies Used
- [Github](https://github.com/) - Used for hosting the repository.
- [Heroku](https://heroku.com/) - Used for deploying the application.
- [Gitpod](https://www.gitpod.io/#get-started) - Used for developing the application.
- [Python](https://www.python.org/) - Used for adding functionality to the application.
- [Projects in GitHub](https://github.com/lucia2007?tab=projects) - Used for project managament.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation python code.
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - Used to generate tables in Markdown.
- [Draw.io](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) - Used for creating the dependency diagram.

[Back to top](#contents)

# Python Packages

* [Colorama](https://pypi.org/project/colorama/) - Used to add colours to the terminal.
* [Time](https://docs.python.org/3/library/time.html) - Used for the slow print functionality and for delaying print statements.
* [Sys](https://docs.python.org/3/library/sys.html) - Used to provide access to some variables used or maintained by the interpreter.
* [Random](https://docs.python.org/3/library/random.html) - Used within the slow print functionality.
* [OS](https://docs.python.org/3/library/os.html) - Used to clear the screen in the terminal.

# Testing

For testing the application, I used manual testing and external validators. Both manual and external testing are a part of a separate testing [file](/TESTING.md).

### Manual testing
  - I used manual testing throughout the whole development phase of the project. Mainly:
    - I frequently checked if all the inputs were valid, namely if my validation functions were catching all errors and exceptions. (Details are in the [Testing file](TESTING.md).)
    - I played the game repeatedly to see if the correct winning message was displaying when the user finished the game.
    - I made sure that when the user chose to play again, they would be taken to the choice of a difficulty level and the moves counter was cleared (setting of the initial state).
    - I checked if a good-bye message displayed after the user chose not to play again.

### External Testing
  All external testing is a part of a separate testing [file](/TESTING.md).

[Back to top](#contents)

# Deployment to Heroku

## Project Deployment

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the button "New" in the top right corner, below the header and choose "Create new app".
   <details><summary><b>Create new app</b></summary>

   ![Create new app](/readme-images/create_new_app.png)
   </details><br />

3. Choose a unique name for the application and select your region. When done, click "Create app".
   <details><summary><b>Create app</b></summary>

   ![Create app](/readme-images/create_app.png)
   </details><br />


4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button on the right.

   <details><summary><b>Config Vars</b></summary>

   ![Config Vars](/readme-images/config_vars.png)
   </details><br />

5. Afterwards, scroll down to the "Buildpacks" section of the settings page and click the button "Add buildpack".

   <details><summary><b>Buildpacks</b></summary>

   ![Buildpacks](/readme-images/buildpacks.png)
   </details><br />

6. First add "Python" package and then "node.js". 
   
   <details><summary><b>Choose Buildpacks</b></summary>

   ![Choose Buildpacks](/readme-images/packages_order.png)
   </details><br />

7. If you exchanged the order of the packages, just drag the Python package above.
   
   <details><summary><b>Buildpacks' Order</b></summary>
   
   ![Buildpacks's Order](/readme-images/buildpacks_correct_order.png)
   </details><br />

8. Scroll back to the top of the page and choose the "Deploy" tab. Then choose "GitHub" as Deployment method.
   
   <details><summary><b>Deployment method</b></summary>
   
   ![Deployment method](/readme-images/deploy.png)
   </details><br />

9. Go to "Connect to GiHub" section, search for the repository and then click "Connect".
   
   <details><summary><b>Connect to GitHub</b></summary>
   
   ![Connect to GitHub](/readme-images/connect_repository.png)
   </details><br />

10. In the "Automatic Deploys" section, choose your preferred method for deployment. At first, I used the manual deployment option, and later I changed it to automatic deploys. Afterwards, click "Deploy Branch".
   
    <details><summary><b>Automatic Deploys</b></summary>
   
    ![Automatic Deploys](/readme-images/automatic_deploys.png)
    </details><br />

The link to the the live site can be found here - https://towers-of-hanoi-game.herokuapp.com/.
The link to the GitHub repository can be found here - https://github.com/lucia2007/towers-of-hanoi.


[Back to top](#contents)

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changed without affecting the original repository. Take the following steps to fork the repository:

1. Log in to **GitHub** and locate the [repository](https://github.com/lucia2007/towers-of-hanoi).
2. On the top right hand side of the page is a button called **'Fork'**. Click on the button to create a copy of the original repository in your GitHub Account.

[GitHub forking process image](/readme-images/forking_process.png)

[Back to top](#contents)

## To create a local clone of a project

Take the following steps to create a clone of a project:

1. Click on the **Code** button in the left top corner.
2. Next to the green **GitPod** button, click on **Code** drop-down menu.
3. In the **HTTPS** section, click on the clipboard icon to copy the displayed URL.
4. In your IDE of choice, open **Git Bash**.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **git clone**, and then paste the URL copied from GitHub.
7. Press **enter** and the local clone will be created.

[Github cloning process image](/readme-images/cloning_process.png)

[Back to top](#contents)


# Credits

## Content
- The overall inspiration came from the well-known game called <a href="https://www.amazon.co.uk/Tower-Hanoi-9-disc-version/dp/B0006A3JZC/ref=asc_df_B0006A3JZC/?tag=googshopuk-21&linkCode=df0&hvadid=310869104636&hvpos=&hvnetw=g&hvrand=15866353930159951919&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007850&hvtargid=pla-439214070867&psc=1" target="_blank" rel="noopener">Tower of Hanoi</a> which my children recently discovered and fell in love with.
- [Draw.io](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) was used to create the dependency diagram.
- The framework for the Readme file was originally inspired by [Wawas Wood](https://github.com/EwanColquhoun/wawaswoods/blob/master/README.md), [Scoops](https://github.com/amylour/scoops_pp1/blob/main/README.md#testing) and [CI_Project-Protfolio-3](https://github.com/MikeR94/CI-Project-Portfolio-3#python-logic)

## Media
- I was inspired by <a href="https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/" target="_blank" rel="noopener">Towers of Hanoi illustrative picture</a>. 
- When looking for inspiration as how to approach the visualization of the game in CLI, I came accross this version: <a href="https://unix.stackexchange.com/questions/382585/animation-inside-terminal-with-escape-codes" target="_blank" rel="noopener">Towers of Hanoi in CLI</a>.

## Acknowledgements
- Extra help and guidance was received from my mentor Precious Ijege, from my husband Sam and fellow colleagues from the Code Institute.
- My husband Sam encouraged me to use OOP and guided me through it. He also encouraged me to use annotation for functions which helped me during the debugging process. Lastly, he showed my how to disable pylint statements.
- Other sources of inspiration and help:
  - [Clear Screen in Python](https://www.geeksforgeeks.org/clear-screen-python/)
  - [Convert range into list](https://pythonexamples.org/python-convert-range-into-a-list/)
  - [Slow print](https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python)
  - [Sleep function](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python's%20sleep,pauses%20between%20words%20or%20graphics.)
  - [While Do Loop in Python](https://www.freecodecamp.org/news/python-do-while-loop-example/)
  - [ASCII ART Generator](https://patorjk.com/software/taag/#p=display&h=2&f=Big&t=Towers%20of%20Hanoi)
  - [Use and installation of COLORAMA](https://dev.to/muhimen123/colored-text-in-terminal-using-python-1nmd#:~:text=In%20colorama%2C%20the%20font%20color,start%20by%20importing%20the%20module.&text=Then%2C%20in%20the%20print%20statement,Just%20like%20this.)
  - [Print multiple lines of text in Python](https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python)
  - [Create raw string in Python](https://www.digitalocean.com/community/tutorials/python-raw-string)

Thank you all for your support and encouragement. I couldn't have done it without you.

[Back to top](#contents)

