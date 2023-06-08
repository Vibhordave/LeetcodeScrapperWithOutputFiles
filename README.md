# Leetcode Scrapper With Output Files

# Description
The main branch serves as the primary branch of the project and contains the setup details and the chromedriver.exe file. This branch provides the necessary resources and instructions for setting up the project.

# Setup Instructions
To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the requirements.txt file.
3. Download the chromedriver.exe file and place it in the project's root directory.


# Usage
After completing the setup, you can run the project by executing the run script (run.py). This script serves as the entry point for the application.
If any individual part is to be run then checkout the branch.

# Problems Experienced Along with their solutions

1. One of the major challenges encountered during the web scraping process was the issue of the page reloading. Despite the webdriver attempting to load page 2, it resulted in page 1 being reloaded, leading to the extraction of incorrect data.

  **Solution:** After extensive research and experimentation with different approaches, the most effective solution was to utilize a method where the webdriver     clicks the next button instead of directly loading the link. Despite thorough investigation, no specific cause for the issue could be identified.

2. The second most challenging aspect was grasping the usage of the os library. Opening a file directly by specifying a local address proved to be problematic and inefficient.

  **Solution:** At this stage, the os library proved to be invaluable. Utilizing the **cur_dir = os.path.dirname(os.path.abspath(__file__))** command enabled me      to determine the current path and use it to navigate to its parent directory using **os.path.join(current_dir, "..")**. This functionality facilitated            accessing any other sibling directories within the project.

3. I encountered significant challenges while implementing the **TF-IDF (Term Frequency-Inverse Document Frequency) algorithm**.

  **Solution:** I used the [link](https://medium.com/nlplanet/two-minutes-nlp-learn-tf-idf-with-easy-examples-7c15957b4cb3) to read about the same.


  **The Above project has been created for education purposes only.**
