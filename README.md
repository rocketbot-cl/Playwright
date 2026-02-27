



# Playwright

Module with advanced functionalities for the browser that uses Playwright instead of Selenium

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.


## Overview


1. Open Browser
Open a new browser instance.

2. Open URL
Navigate to a URL and waiting until the selected event happens.

3. Close browser
Close browser and all tabs, and saves profile state. 

4. Wait For Object
Wait for an element to be in a certain state.

5. Click on object
Click an element.

6. Clean input and send Text
Deletes the contents of an input object and sends the text.

7. Extract Text Playwright
Get inner text of an element.

8. Take Screenshot
Take a screenshot of the page.

9. Download
Allows clicking a button to download an item.

10. Select Option
Select one or multiple options in a dropdown element.

11. Send key combination
Command to send key combination to the active element. Shortcuts that are not part of the web page but are browser or system shortcuts are not supported.

12. Check / Uncheck
Check or Uncheck a check.

13. Get Attribute
Get an Attribute's value.

14. Wait for load state
Wait until page reaches a required load state.

15. Get tab titles
Returns a list with the titles of all open tabs in the browser.

16. Switch tab by title
Switch to a tab by its title in the current context.

17. Evaluate JS
Evaluates JS code in the context of the page. Returns the result of the execution.

18. Count elements
Count how many times an element appears on the page.

19. Change to IFRAME
Change to IFRAME and set its content as default.

20. Change to body content
Leave the body of the page as the default content.




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**playwright**](https://pypi.org/project/playwright/)
### License

![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)
[MIT](https://opensource.org/license/mit)