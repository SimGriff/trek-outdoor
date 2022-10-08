# Trek Outdoor
![Screenshot of mockup](static/images/screenshots/mockup.png)
View the deployed site [here:](https://simgriff-trek-outdoor.herokuapp.com/)
## User Experience (UX)

---

## Introduction
Trek Outdoor is a fictional e-commerce website that I created for my Milestone Project 4. The main goal of this project is to sell outdoor pursuits clothing and equipment, the site is for educational purposes only, however, it is fully functional as an e-commerce website.

The checkout functionality is set up to accept stripe payments. **Please don't enter your personal card details.**
To process a test stripe payment, please use the following details.
* Card number : 4242 4242 4242 4242
* Date: Any future date
* CVC: Any 3 numbers

---

## User Stories
- As an unregistered user, I want to
    1. View a list of products
    2. View details of individual products
    3. View any deals or offers
    4. See the total value of my purchases at any time
    5. Sort the list of available products
    6. Sort a specific category of product
    7. Search a product by name or description
    8. See my search results
    9. Register for an account
    10. Select the size and quantity of a product when purchasing
    11. View items in my shopping cart
    12. Change the quantity of items or remove items from my cart
    13. Enter my payment information
    14. Feel that my personal details and payment information are secure
    15. View order confirmation after checkout

* As a registered user, I want to
    1. Have the same access to functionality as the unregistered user
    2. Be able to Sign In or logout
    3. Reset my password if I forget it
    4. Receive a confirmation email once registered
    5. Have my own personalised user profile
    6. Save my personal information and be able to edit if needed
    7. Review products that I have purchased
    8. Edit and delete my reviews
    9. Add items to my wishlist
    10. Put Wishlist items into my shopping cart
    11. Receive an email confirmation after successfully completing an order at checkout

- As a Site owner/Admin, I want to
    1. Have the same access to functionality as the registered user
    2. Add a product.
    3. Edit a product.
    4. Delete a product.
       
---

## Features
### Home Page

* General
  - The Hero image covers the home page completely except for the Navigation section at the top of the page. The image draws the user in and invites the user into the site with a beautiful picture of the great outdoors.
  - The site Logo appears on the top left of the page within the navbar and appears on all pages, when a user clicks on the logo they are taken back to the home page.

![Home Page](docs/screenshots/home.png)

* Navigation
  - The Navbar appears on all pages throughout the site. The site logo appears on the left and is read by the user first, reading left to right, top to bottom. 
  - Navigation links are also displayed for each product category with drop-down menus displaying all the available subcategories. 

![Site navigation menu](docs/screenshots/site-nav.png)

Categories and sub-categories
  * All Products
     - By Price
     - By Category
     - By Rating
     - All Products
  * Clothing
     - Jackets
     - Tops
     - Trousers
     - All clothing
  * Footwear
     - Shoes
     - Boots
     - Sandals
     - Accessories
     - All Footwear
  * Equipment
     - Hiking
     - Climbing
     - Cycling
     - Swimming
     - Camping
     - Skiing
     - All Equipment
  * Sale
     - New offers
     - Clearance
     - All Sale items


* Search feature
  - The search bar is centred at the top of the page allowing the user to search for products by entering a keyword.

  - The search results are displayed on the main page in the same format as the main products page with cards representing each item that matches the search criteria.

![Search Results](docs/screenshots/user-stories-search.png)


* Main Site Icons
  - Fontawesome icons are shown at the top of the page representing ‘My Account’, ‘Wishlist’ and the Shopping Cart. There is a further drop-down option under ‘My Account’ for ‘Sign In’ and ‘Register’.

![Main Page Icons](docs/screenshots/user-stories-register-sign-in.png)
 
* Shop Now button
  - This button is presented on the main page and takes the user directly into the ‘All Products’ section.

![Shop now button](docs/screenshots/shopnow.png)

### Products Page

* The Products page displays relevant products displayed on individual cards. The number of products is displayed in the top left of the section with a link to the home page next to this.
* Products can be sorted by Price, Rating, Name and Category with a drop-down selector on the right side of the page. 
* Admin also have access to two further buttons to delete or update a product.

![Products Page](docs/screenshots/user-stories-sort.png)

### Product Details Page

* Features the product image on the left.
* Product details displayed on right side of image, including product name, description, price, category and rating.
* When user signed in, a white heart icon is displayed on bottom right of image that enables signed add product to their wishlist. The heart icon changes to green once selected, it can be removed by selected once again.
* Quantity selector allows user to select required number of products.
* Add to Cart button adds product to users shopping cart, shopping cart icon at top of page is updated with the relevant amount. 
* Feedback provided to shopper via a popup from Bootstrap toasts, informing the user that item has been added with a link to the shopping cart page.

![Product Details Page](docs/screenshots/user-stories-product-details.png)

![Shopping Cart Success](docs/screenshots/cart-success.png)

* Admin also have access to two further buttons to delete or update a product.
* Reviews - Any product reviews are listed underneath the product card. A signed in user has the option to edit or delete any reviews they have added via the two buttons beneath the review that are only available to the user that created the review, or admin.

![Edit Review Buttons](docs/screenshots/edit-review-btn.png)

### Add/Edit Review Page

* Edit – User is taken to the Edit Review form and asked to confirm any changes, they layout of the add review form is identical.

![Edit Review Form](docs/screenshots/edit-review-form.png)

* Delete – Once selected, a Delete confirmation modal is displayed to safeguard against accidental deletion.
* If the user has not added a review yet, the Add Review button is displayed and the user is taken to the Add Review Form.

![Edit Review Modal](docs/screenshots/review-modal-btn.png)

### Wishlist

* The logged in user can add any item to their wishlist via the add to wishlist button within the product details page.

![Add to wishlist button](docs/screenshots/user-stories-register-wishlist-btn.png)

* The page displays all products added to the users wishlist. Products are displayed in the same format as the main products page with the same functionality. 

![Wishlist Page](docs/screenshots/user-stories-wishlist-page.png)

* Once selected, each product in the wishlist also has the same functionality as the product details page, with an additional remove from wishlist button.

* Shopping Cart Success Pop up

![Wishlist Page](docs/screenshots/cart-success.png)

### Shopping Cart

*  Each product selected by the shopper is listed along with an image, Name of product, size (if applicable), SKU code and price.
*  The shopper can adjust the quantity of an individual product in the cart or remove it completely.
*  At the bottom of the listed products in the cart is a Cart Total, Delivery Charge (if applicable) and Grand total.
*  The shopper is given two option buttons under the grand total, to Keep Shopping or go to the Secure Checkout.

![Shopping Cart Page](docs/screenshots/user-stories-shopping-cart.png)

### Checkout Page

* Shipping and payment information form is shown on the left.
* Allows user to save information if signed in. If not signed in, Create an account or Sign in to save this information message is presented with the appropriate link.
* Order summary is shown on the right, with delivery charges, if applicable and a grand total.

![Checkout Page](docs/screenshots/checkout-page.png)

* Once order submitted success message displayed with order summary, email order confirmation is also sent to user’s email address.


![Order Confirmation Email](docs/screenshots/user-stories-email.png)

* The page shows details of the products purchased along with the delivery information, order time, order number, order date and a link at the bottom taking the user back to the products page. 
* Under the listed products is an Order Total, Delivery Charge (if applicable) and Grand total.

![Order Success Page](docs/screenshots/user-stories-confirmation.png)

### Admin Product Management

* Admin have access to an additional menu selection ‘Product Management’.

![Admin Menu](docs/screenshots/user-stories-admin-menu.png)

* Here they can add a new product by completing the form.

![Add Product Form](docs/screenshots/user-stories-admin-page.png)

* Admin also have additional access to edit and delete products via links on the product cards on the main and product detail pages.

![admin edit](docs/screenshots/user-stories-admin-edit.png)


### Allauth features

* The sign in, register, password reset, email confirmation pages etc, have all been provided by Django allauth and formatted to meet the needs of the site.


---


### Future features
* Adding stock management for the products.
* Add more payment options, Paypal, Apple Pay etc.
* Allow the site to recommend products to the shopper based on their order history.

---
## Database Design
### Database Schema
The Database Schema below was produced using [Lucidchart]( https://www.lucidchart.com/)

![Database Schema](docs/screenshots/database-schema.png)

### Models
* User model
  - Created with django allauth and contains the customer username, email and password.
* User Profile model
  - Holds users default delivery information and order history.
* Category model
  - Holds all main category names for a product.
* Subcategory model
  - Holds subcategory names for a product.
* Products model
  - Holds detailed information for each individual product.
* Wishlist model
  - Signed in user can select any items they wish to place into a wishlist. 
  - Items can be easily removed from the wishlist.
  - Items can be added to the shopping cart directly from the wishlist
* Order model
  - Holds all information relating to a customer’s completed order.
  - Allows the user to view their previous orders.
* OrderLineItem model
  - Holds information of an individual product that has been purchased.
* Review model
  - Holds reviews added for a specified product. Displays username that left the review along with time/date.

---

## Design
### Colour Scheme
I used [Coolors](https://coolors.co/) to generate a colour scheme from my chosen hero image. I selected four colours from the palette that complement each other. The colours represent the earthly natural colours of the great outdoors. The Colour palette includes Light Blue #B9DEED background on the home page with overlayed text in Charleston Green #142126, this  ensure excellent readability. The Charleston Green #142126 text was used throughout the site and stood out well against the white background. Steel Blue #587D9U and Army Green #50542A, were also used for some of the buttons. Bootstrap standard class colours were also used throughout the site.

![palette used for Project 4](docs/screenshots/colours.png)

---

### Typography
I used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site. 
I chose the 'Cabin' font as it is a very clear and legible typeface. I felt that this font gave off a friendly vibe and worked well with my e-commerce site.

![font used for Project 4](docs/screenshots/font.png)

---

### Imagery
The main hero image on the landing page is taken from pixabay [pixabay.com]( https://pixabay.com/) with a Free to use license. 
The eye catching outdoor image draws the user in and helps convey the purpose of the e-commerce site.
The mountains logo from [Font Awesome](https://fontawesome.com/) was used to give the site name more of a visual impact. 
Fontawesome icons were also used throughout the site, the icons help inform the user of the purpose of a particular section and lead to a more enjoyable user experience. 
Include screenshots of logo and

![logo-screenshot](docs/screenshots/logo.png)

![main-icons-screenshot](docs/screenshots/main-icons.png)

All product images have been downloaded from [sportpersuit.com](https://www.sportpursuit.com/) e-commerce store.

---

## Wireframes

The wireframes for the site were produced using [Balsamiq:](https://balsamiq.com/) 

* Mobile Wireframes:
  - [Home](docs/wireframes/home-mobile.png)
  - [Products](docs/wireframes/products-mobile.png)
  - [Product Details](docs/wireframes/product-detail-mobile.png)
  - [Add Review](docs/wireframes/add-review-mobile.png)
  - [Wishlist](docs/wireframes/wishlist-mobile.png)
  - [Shopping Cart](docs/wireframes/shopping-cart-mobile.png)
  - [Checkout](docs/wireframes/checkout-mobile.png)
  - [My Account](docs/wireframes/my-account-mobile.png)
  - [Sign In](docs/wireframes/sign-in-mobile.png)
  - [Register](docs/wireframes/register-mobile.png)
  - [Add Products](docs/wireframes/add-products-mobile.png)
  
* Desktop Wireframes:
  - [Home](docs/wireframes/home-desktop.png)
  - [Products](docs/wireframes/products-desktop.png)
  - [Product Details](docs/wireframes/product-details-desktop.png)
  - [Add Review](docs/wireframes/add-review-desktop.png)
  - [Wishlist](docs/wireframes/wishlist-desktop.png)
  - [Shopping Cart](docs/wireframes/shopping-cart-desktop.png)
  - [Checkout](docs/wireframes/checkout-desktop.png)
  - [My Account](docs/wireframes/my-account-desktop.png)
  - [Sign In](docs/wireframes/sign-in-desktop.png)
  - [Register](docs/wireframes/register-desktop.png)
  - [Add Products](docs/wireframes/add-products-desktop.png)


---

## Technologies Used

### Languages Used

* [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
---
### Frameworks, Libraries & Programs Used

* [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.
* [Coolors](https://coolors.co/) was used to generate a colour scheme.
* [Google Fonts](https://fonts.google.com/) was used to import the fonts used in this project.
* [Font Awesome](https://fontawesome.com) was used throughout the website to add icons for aesthetic and UX purposes.   
* [Adobe Color](https://color.adobe.com/create/color-contrast-analyzer) contrast checker used for this project.
* [pixlr.com](https://pixlr.com/e) was used to resize images and editing photos for this project.
* [Techsini](https://techsini.com/multi-mockup/index.php) was used to produce mockup image across multiple devices.
* [Django]( https://www.djangoproject.com/) made it easier to build my site more quickly and with far less code.  
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used to assist with the responsiveness and styling throughout the site. 
* [jQuery](https://jquery.com/) was used as a JavaScript library to help write less JavaScript and do more. 
* [Stripe](https://stripe.com/gb) is an online payment processing and credit card processing platform that was used to handle payments made on the site. Stripes webhooks were also used to offer payment backup in the event of payment failure. 
* [AWS(Amazon Web Services)](https://aws.amazon.com/) was used to host the static files and media files used by the site.
* [Gitpod:](https://gitpod.io/projects) was the code editor used throughout the project.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [Heroku](https://id.heroku.com/) was used to deploy the application.

---
