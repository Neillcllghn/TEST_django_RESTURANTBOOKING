# TableFor2 - Django Resturant Booking System.
Tablefor2 is a responsive website allowing visitors to view on a range of devices. It allows users to view times and a menu (consisting of Starter, Main course and Dessert) and make a booking/reservation while signed in.

### IMAGE HERE
---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Tablefor2 is an online booking system that allows users of the site to register online to make/edit or cancel bookings.

The client would like users of the site to register with the site to allow for user identifcation, select times that are listed on the site so to avoid selecting out of hour periods, provide an unique email to all bookings so that the client can make contact with the user if need be (future updates to the system), plus to provide each booking as unique to avoid double booking.

#### Key information for the site:
- What is on the Menu.
- What Times are availble for booking.
- Register/Sign in page.
- How to make a booking.
- View bookings already made.
- Which bookings are pending approval (which can be edited or deleted) and approved (which can only be deleted by the user).

### User Stories

#### Client Goals:
- To be able to view the site on a range of device sizes.
- To make it easy for potential customers (the user) to find out what is on offer (menu) and how to make a booking.
- To make it clear to the user what times are available for bookings.
- To allow users to view the bookings made and prevent double bookings.
- Approve bookings.

#### User/Customer Goals:
- I want to know what Tablefor2 offers in terms of a menu etc.
- I want to register an account so that I can make a booking/reservation.
- I want to make a booking by selecting a time and date for my reservation.
- I want to be able to view a list of my bookings so that I know what has been booked etc.
- I want to be able to edit a booking so that I can make changes if needed and prior to approval.
- I want to be able to cancel/delete a booking (whether it is pending approval or approved).


## Design

### Typography

The Font used is lato & Merriweather which is easy to read and easy on the eye.

I also like to include an image of the fonts chosen as a reference.

## Features

The website is comprised of a home page, login, register and sign out pages, a booking page, an update bookings page and a Your Bookings page.

All Pages on the website are responsive and have:

- The title of the site at the top of every page. This title also acts as a link back to the home page.
![image](https://user-images.githubusercontent.com/109948740/234081436-51b304c9-8f15-40bb-a40c-e52def0e926d.png)

- The Buttons will highlight when the cursor is hovering over them, This is to indicate to the user that this button is the one that is being selected:

When Button is not highlighted:

![image](https://user-images.githubusercontent.com/109948740/234083160-55a69603-b4bb-4f03-bd84-e797d6f93c4f.png)

When Button is highlighted:

![image](https://user-images.githubusercontent.com/109948740/234083620-b09e5077-ac13-4d97-b97c-aac9d73fa55d.png)

### General features on each page

### The Home Page

The home page of TableFor2 displays the sites name as a title and then a container which holds some welcome text, the times and menu. The Welcome Text will change for the user, from indicating that the user will need to sign in to make a booking to providing links to make a booking when signed in:

- When the user is not registered or signed in:
  ![image](https://user-images.githubusercontent.com/109948740/234085541-666f3c25-b19f-49c7-ab91-0d5935b15c17.png)


- When the user is signed in:
  ![image](https://user-images.githubusercontent.com/109948740/234085691-572b8c89-130c-45ae-bb7b-2a0b537843c3.png)


Another feature to notify that the user is signed in or not is the Nav-bar will change from providing links to the Register/Login pages to Make a Booking, Your Bookings and Logout pages:

- When the user is not registered or signed in:

  ![image](https://user-images.githubusercontent.com/109948740/234086164-c78ad6b0-7a59-46ca-b78d-15ef42c049d4.png)


- When the user is signed in:

  ![image](https://user-images.githubusercontent.com/109948740/234086102-31519ca7-2e85-4294-81de-64774032ab85.png)


The Times portion of the home page (this is displayed to the user, whether they are logged in or not):

![image](https://user-images.githubusercontent.com/109948740/234086515-004fe18f-fe1a-48d4-91af-799e131a23fa.png)

The Menu is also displayed to the user regardless of login/Registeration and is a collapsible list when clicked on consisting of Starter, Main Course and Dessert selections:

![image](https://user-images.githubusercontent.com/109948740/234087251-2952bee7-0da9-4b7f-aa53-c531c2172238.png)

![image](https://user-images.githubusercontent.com/109948740/234087288-096b30da-d1b6-483d-a379-b4eb1a8a870e.png)


# Registeration Page

This consist of a title, a link to login if you are already have an account, a means to type in a username, and email (optional) and a password.

![image](https://user-images.githubusercontent.com/109948740/234365245-18ba1fd9-f18b-41fd-8415-f60263dac061.png)


# Sign in page

This consist of a title, a link to register if you do not have an account, a means to type in your username and password. Furthermore, it has a remember me checkbox just so the user's details will be saved on the system.

![image](https://user-images.githubusercontent.com/109948740/234366047-97a1815b-1afc-4f73-bf4d-5d9669d469a7.png)

# Sign out page

This consist of a title, and a signout button:

![image](https://user-images.githubusercontent.com/109948740/234367296-b3b65089-0f1e-4d30-9602-7b03d3d68902.png)

# Make a Booking Page:

This consists short sentences outlining what the user can and cannot do such as how many guests the user can have, a link to the home page for the user to be reminded of the available times and an additional note that each booking must have an email which will give a booking its uniqueness and so if the user wishes to book on behalf of a friend on the same day as a booking they made, a different email will allow the user to proceed with the booking.

The user will be notifed by error message if the following happens:
- Double booking - as mentioned above, if the user inputs the same email and selects the same day as a booking that is already made, it will be rejected.
- Day in the past - if the user selects a day in the past, an error message will appear preventing the user from booking.
- Time in the past - if the user selects a time in the past, an error message will appear preventing the user from booking.
- Number of guests - if the user selects more than 6 and less than 1, an error message will appear preventing the user from booking.

![image](https://user-images.githubusercontent.com/109948740/234372929-2c1a2e5a-9591-4fe6-b0a3-699dffc5e865.png)


