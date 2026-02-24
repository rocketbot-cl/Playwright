



# Playwright

Module with advanced functionalities for the browser that uses Playwright instead of Selenium

*Read this in other languages: [English](Manual_Playwright.md), [Português](Manual_Playwright.pr.md), [Español](Manual_Playwright.es.md)*

![banner](imgs/Playwright.jpg)
## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.


## Description of the commands

### Open Browser

Open a new browser instance.
|Parameters|Description|example|
| --- | --- | --- |
|Browser |Browser to open|Google Chrome|
|URL|URL that will be automatically opened once the browser and page are initialized.|https://rocketbot.com/en/|
|Proxy Server|Proxy server address (e.g., http//myproxy8080)|http://myproxy:8080|
|Proxy User|Username for proxy authentication|username|
|Proxy Password|Password for proxy authentication|password|
|Download folder|Default download path where the Download Command will save files|C:/Users/user/Desktop|
|Profile file|Profile file to open the opened browser|C:/folder/profile.json|
|Timeout (sec)|Maximum wait time (in seconds) for the initial URL to load.|30|
|Headless Mode|Run browser in headless mode (without GUI)||
|Session ID|Unique ID for this Playwright session. Allows running multiple browsers or bots in parallel without interference.|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Open URL

Navigate to a URL and waiting until the selected event happens.
|Parameters|Description|example|
| --- | --- | --- |
|URL|||
|Wait Until|Loaded Waits for the entire page, including images and styles, to finish loading.
DOMContentLoaded Waits for the HTML/Text to appear, without waiting for images.
Network Idle consider navigation to be finished when there are no network connections for at least 500 ms.
Commit consider navigation to be finished when the network response is received and the document started loading.||
|Open in New Tab|If checked, opens the URL in a new tab instead of the current one.||
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Close browser

Close browser and all tabs, and saves profile state. 
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Wait For Object

Wait for an element to be in a certain state.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|State|Visible wait for the element to be visible.
 Hidden wait for the element to be hidden.
 Attached wait for the element to be present in the DOM.
 Detached wait for the element to be removed from the DOM.||
|Timeout (sec)|Maximum wait time (in seconds) until the object is in the selected state.|30|
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Click on object

Click an element.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Timeout (sec)|Maximum wait time (in seconds) until the element can be clicked.|30|
|Force Click|Whether to force the click action, even if the element is not visible or interactable.||
|Session ID|Unique ID for this Playwright session|1|

### Clean input and send Text

Deletes the contents of an input object and sends the text.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Text to Fill|||
|Special Key|Select a special key to press after the text. (Optional)|SPACE|
|Timeout (sec)|Maximum wait time (in seconds) until the element can be written on.|30|
|Session ID|Unique ID for this Playwright session|1|

### Extract Text Playwright

Get inner text of an element.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Timeout (sec)|Maximum wait time (in seconds) until element's text can be extracted.|30|
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Take Screenshot

Take a screenshot of the page.
|Parameters|Description|example|
| --- | --- | --- |
|Folder path||C:/Users/User/Downloads/|
|File Name|File name and extension|screenshot.jpg|
|Full Page|Check to capture the full scrollable page intead of just the viewport.||
|Session ID|Unique ID for this Playwright session|1|

### Download

Allows clicking a button to download an item.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to click.|Data|
|Selector Type|||
|Save Directory|Folder where file will be saved. Optional.|C:/Users/User/Downloads/|
|File Name Override|Optional. If empty, uses original name.|file_name|
|Timeout (sec)|Maximum wait time (in seconds) until the element can be downloaded.|60|
|Saved File Path|Var to store the final file path||
|Saved Filename Variable|Var to store the filename||
|Session ID|Unique ID for this Playwright session|1|

### Select Option

Select one or multiple options in a dropdown element.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Option|Select the labels, values, or indexes of the options to choose. If multiple, send a list ex [option1, option2].|option1|
|Select the option by|Select to choose the option by it's value, label, or index.|Select by|
|Session ID|Unique ID for this Playwright session|1|
|Timeout (sec)|Maximum wait time (in seconds) until an option from the element can be selected.|30|

### Send key combination

Command to send key combination
|Parameters|Description|example|
| --- | --- | --- |
|First special Key|First special key to combine with a letter/number and/or with a second special key|SPACE|
|Second special key|Second special key to combine with the first key if necessary.|SPACE|
|Letter or number|Letter or number to combine with the special keys if necessary.|a|
|Session ID|Unique ID for this Playwright session|4|

### Check / Uncheck

Check or Uncheck a check.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Check or uncheck|Check or uncheck the check.||
|Timeout (sec)|Maximum wait time (in seconds) until the element can be checked / unchecked.|30|
|Session ID|Unique ID for this Playwright session|1|

### Get Attribute

Get an Attribute's value.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Selector Type|||
|Attribute name|Attribute name whose value is to be obtained.|value|
|Timeout (sec)|Maximum wait time (in seconds) until the attribute of the element can be obtained.|30|
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Wait for load state

Wait until page reaches a required load state.
|Parameters|Description|example|
| --- | --- | --- |
|Load state|Loaded Waits for the entire page, including images and styles, to finish loading.
DOMContentLoaded Waits for the HTML/Text to appear, without waiting for images.
 Network Idle consider navigation to be finished when there are no network connections for at least 500 ms.|Load|
|Timeout (sec)|Maximum wait time (in seconds) until the page reaches the required load state.|30|
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Get tab titles

Returns a list with the titles of all open tabs in the browser.
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the command will be stored|Variable|

### Switch tab by title

Switch to a tab by its title in the current context.
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|Unique ID for this Playwright session|1|
|Title|Title of the tab you want to switch to|Variable|

### Evaluate JS

Evaluates JS code in the context of the page. Returns the result of the execution.
|Parameters|Description|example|
| --- | --- | --- |
|JS code|JS code to evaluate in the context of the page. Returns the result of the execution.|function(data) {
	return param1 * param2;
}|
|Function parameters|List of values of the parameters to be passed to the function. The values of the list are passed as strings.|[value1, value2, ...]|
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the JS code will be stored|Variable|

### Count elements

Count how many times an element appears on the page.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the elements to select.|Data|
|Selector Type|||
|Session ID|Unique ID for this Playwright session|1|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Change to IFRAME

Change to IFRAME and set its content as default.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the iframe.|Data|
|Selector Type|||
|Session ID|Unique ID for this Playwright session|1|

### Change to body content

Leave the body of the page as the default content.
|Parameters|Description|example|
| --- | --- | --- |
|Session ID|Unique ID for this Playwright session|1|
