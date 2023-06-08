# Leetcode Scrapper With Output Files

# Description
The main branch serves as the primary branch of the project and contains the setup details and the chromedriver.exe file. This branch provides the necessary resources and instructions for setting up the project.

# Setup Instructions
To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the requirements.txt file.
3. Download the chromedriver.exe file and place it in the project's root directory.


# Usage
After completing the setup, you can run the project by executing the main script (main.py). This script serves as the entry point for the application.

# Problems Experienced Along with their solutions

1. For the Scrapping part the most difficult problem faced was reloading of page 1 even though webdriver was trying to load page 2 which caused wrong data to be scrapped.
**Solution:** After a lot of research and trying of various methods, the best method was to rather make the webdriver click the next button rather that directly loading the link. I tried to find any possible cause however nothing came up.

2. The second most problematic portion was to understand the os library. As opening directly a file was causing problem as I was forced to write local address which wasn't efficient at all.
**Solution:** At this point os was the library that came handy. **cur_dir = os.path.dirname(os.path.abspath(__file__))** command allowed me to find the current path and use it to go to its parent using **os.path.join(current_dir, "..")** which can be used to go to any other sibling directories.

3. I also found implementation of **TF-IDF Algorithm** very tough.
**Solution:** I used the following [link]([https://example.com](https://medium.com/nlplanet/two-minutes-nlp-learn-tf-idf-with-easy-examples-7c15957b4cb3)) to read about the same.


**The Above project has been created for education purposes only.**
