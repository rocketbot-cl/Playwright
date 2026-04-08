



# Playwright

Module with advanced functionalities for the browser that uses Playwright instead of Selenium

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.


## Overview


1. Open Chrome
Open a new chrome instance.

2. Check Libraries
Checks if the necessary libraries exist for the current OS and allows forcing their download.

3. Close browser
Close browser and all tabs, and saves profile state. 

4. Open URL
Navigate to a URL and waiting until the selected event happens.

5. Wait For Object
Wait for an element to be in a certain state.

6. Click on object
Click an element.

7. Clean input and send Text
Deletes the contents of an input object and sends the text.

8. Extract Text Playwright
Get inner text of an element.

9. Take Screenshot
Take a screenshot of the page.

10. Download
Allows clicking a button to download an item.

11. Select Option
Select one or multiple options in a dropdown element.

12. Send key combination
Command to send key combination to the active element. Shortcuts that are not part of the web page but are browser or system shortcuts are not supported.

13. Check / Uncheck
Check or Uncheck a check.

14. Get Attribute
Get an Attribute's value.

15. Wait for load state
Wait until page reaches a required load state.

16. Get tab titles
Returns a list with the titles of all open tabs in the browser.

17. Switch tab by title
Switch to a tab by its title in the current context.

18. Evaluate JS
Evaluates JS code in the context of the page. Returns the result of the execution.

19. Count elements
Count how many times an element appears on the page.

20. Change to IFRAME
Change to IFRAME and set its content as default.

21. Change to body content
Leave the body of the page as the default content.

22. Click link to new tab
Clicks an element that would open a new tab.

23. Upload files
Command to upload one or more files to an input of type file. Just complete a single value depending on how many files you want to upload.




----
### OS

- windows
- mac

### Dependencies
- [**playwright**](https://pypi.org/project/playwright/)
### License

![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)
[MIT](https://opensource.org/license/mit)