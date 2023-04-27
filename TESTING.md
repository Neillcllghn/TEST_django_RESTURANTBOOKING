# TABLEFOR2
## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Python Validator](#python-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

Testing was ongoing throughout the entire build. During development I made use of Google Chrome Developer Tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome Developer Tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. I have checked the HTML via direct input and also by inspecting the page source and running this through the validator.

* [Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2F) - No errors or warnings.

- - -

### W3C CSS Validator

No errors were found when passing through the official (jigsaw) validator. Link can be found [here](https://jigsaw.w3.org/css-validator/#validate_by_input).

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

![image](https://user-images.githubusercontent.com/109948740/234950008-3ffaa5b3-192b-4dfd-98b1-8d4300edd346.png)

- - -

### Python Validator

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python files. Please see below the results from the python files in which I had to input 

* bookings app.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234952613-5513be5c-fbba-4728-90d7-a8c7f538d6bc.png)

* tablefor2 app.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234954589-4e932e47-f12d-4f5c-931a-8f28da38d6da.png)

* forms.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234952920-aca96315-3052-41a0-b5f9-6ef3a1ecb239.png)

* models.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953170-4e1cd007-724f-4194-b037-5ebda304cf3a.png)

* urls.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953459-aecf26e8-ef1c-45cf-8272-b75ebe56ad2a.png)

* views.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953636-e56121cf-ec03-4dee-ab08-7c858638745a.png)

- - -

### Lighthouse

We used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

Overall, the lighthouse scores are very good, with one or two things that could be improved. A future implementation would be to convert all images to the webp format.

### Desktop Results

Home Page:

![image](https://user-images.githubusercontent.com/109948740/234960792-30d716a7-75a1-40cb-a622-8920887e3107.png)

Make a Booking Page:

![image](https://user-images.githubusercontent.com/109948740/234961740-0106a242-3676-4bd9-ac0e-206b8a4cfc35.png)

Your Bookings Page:

![image](https://user-images.githubusercontent.com/109948740/234961984-13a55ca2-9409-4426-87e0-6a7936c79050.png)

Register Page:

![image](https://user-images.githubusercontent.com/109948740/234961081-41f21993-c6d0-4493-b0d1-ec288d1c94d2.png)

Sign In Page:

![image](https://user-images.githubusercontent.com/109948740/234961308-51a68725-0558-46c3-a979-08e12b0e2612.png)

Sign Out page:

![image](https://user-images.githubusercontent.com/109948740/234962162-c9638a7f-83ad-45c1-8375-c812a9ab0bb2.png)


### Mobile Results

Home Page:

![image](https://user-images.githubusercontent.com/109948740/234962665-e2d1b808-66a8-475d-aa1e-789aad7be14d.png)

Make a Booking Page:

![image](https://user-images.githubusercontent.com/109948740/234963051-eecd4522-5c5e-426a-bee4-e84523c5baf5.png)

Your Bookings Page:

![image](https://user-images.githubusercontent.com/109948740/234963156-f5547468-7b91-4c29-8e12-587bc3a463a1.png)

Register Page:

![image](https://user-images.githubusercontent.com/109948740/234963313-faf9d9cc-b75e-42ec-83e2-c6fefa7f4fd6.png)

Sign In Page:

![image](https://user-images.githubusercontent.com/109948740/234963435-9900b7d5-72d6-4624-ace4-375c995229f8.png)

Sign Out page:

![image](https://user-images.githubusercontent.com/109948740/234962503-92b60410-b836-4f1d-8c92-aeae13a7c9d2.png)

- - -

## MANUAL TESTING

### Testing User Stories

`User/Customers visting the site`

| Goals | How are they achieved? |
| :--- | :--- | 
| Provide a menu that the user can view. | Created a standard menu list that is collapsible thanks to JS and gives three of each of starter, main course and dessert. |


### Full Testing

Full testing was performed on the following devices, and additional testing for other devices was carried out using developer tools:

iMac 2021, MacBook Pro 14 inch 2021, iPhone 13 Pro, Samsung S20, 25 inch monitor, windows laptop

Each device tested the site using the following browsers:

Google Chrome on Mac and Windows, Safari

`Index/Base Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **NAVBAR** |  |  |  |  |
|  |  |  |  |  |
| Logo image link | When clicked you are redirected to the home page | Clicked Logo | Redirected to home page | Pass|
| Navbar home link | When clicked you are redirected to the home page | Clicked link | Redirected to home page | Pass|
| Navbar Register link | When clicked you are redirected to the Register page | Clicked link | Redirected to Register page | Pass|
| Navbar Login link | When clicked you are redirected to the Sign in page | Clicked link | Redirected to Sign in page | Pass|
| Navbar Make a Booking link | When clicked you are redirected to the Make a booking page | Clicked link | Redirected to Make a booking page | Pass|
| Navbar Your Booking link | When clicked you are redirected to the Your Booking page | Clicked link | Redirected to Your Booking page | Pass|
| Navbar Logout link | When clicked you are redirected to the Sign out page | Clicked link | Redirected to Sign out page | Pass|
| Navbar link - Hover | When hovered over a shading of the area will occur to indicate that the cursor is over link | Hovered over link | Shading appears | Pass|
| **Menu** |  |  |  |  |
|  |  |  |  |  |
| Menu list | When click on, the menu will open to reveal the menu list and clicked again it will collapsible | Clicked collapsible list | List of menu appears and collapsibles when clicked on again | Pass|

`Make a booking Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **NAVBAR** |  |  |  |  |





