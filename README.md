# <p style="text-align: center; font-size: 40px;">**Bookmark-It**</p>

![Place am I responsive image here](documentation/testing/)

[View the Bookmark-It live website here]()


# UX/UI

## Strategy

### Project Goals
Bookmark-It is a platform that combines the functionalities of an e-commerce bookstore with the book-tracking features similar to Goodreads. In addition to offering books for purchase, users can conveniently bookmark titles they are currently reading, plan to read, or have already completed.

For avid readers, Bookmark-It offers added convenience by integrating purchasing capabilities directly. This means users can seamlessly transition from browsing and bookmarking books to purchasing them, all within the same interface.

User profiles on Bookmark-It include a dedicated section that provides insights into the reader's reading habits. This feature allows users to track the number of books they've read over a specified period, whether it's monthly or yearly.

## Scope

### Feature Plan
| User                   | Feature                     | Importance | Viability | MVP | Complete |
| ---------------------- | --------------------------- | ---------- | --------- | --- | -------- |
| Site Visitor           | Register for an account     | 5          | 5         | MVP |          |
| Account Holder         | Password recovery           | 5          | 5         | MVP |          |
| Account Holder         | User Profile                | 4          | 5         | MVP |          |
| Account Holder         | Order history               | 4          | 5         |     |          |
| Account Holder         | Reading list                | 5          | 4         |     |          |
| Account Holder         | Reading goals               | 2          | 1         |     |          |
| Account Holder         | Reading tracker             | 4          | 4         |     |          |
| Account Holder         | Read book reviews           | 3          | 3         |     |          |
| Account Holder         | Leave book reviews          | 3          | 3         |     |          |
| Admin                  | Add books                   | 5          | 5         | MVP |          |
| Admin                  | Edit/update books           | 5          | 5         | MVP |          |
| Admin                  | Delete books                | 5          | 5         | MVP |          |
| Account Holder & Admin | Checkout                    | 5          | 5         | MVP |          |
| Account Holder & Admin | Stripe payments             | 5          | 5         | MVP |          |
| Account Holder & Admin | Order confirmation by email | 5          | 5         | MVP |          |
| All                    | Search & filter books       | 5          | 5         | MVP |          |
|                        | User Roles                  | 5          | 5         | MVP |          |
|                        |                             | 75         | 75        |     |          |


## Structure
### User Stories
| No: | As a...                          | I want to be able to                                         | so that I can                                                                         | Progress                |
| :-: | -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------- | ----------------------- |
|     | **Viewing & Navigation**         |                                                              |                                                                                       |                         |
|  1  | site visitor / account holder    | navigate the website easily                                  | find books to purchase or bookmark.                                                   | Build <br>Test <br>Done |
|  2  | site visitor / account holder    | view different categories of books                           | find books that best suit my reading taste                                            | Build<br>Test<br>Done   |
|  3  | site visitor / account holder    | view individual book summaries                               | have an idea of what each book is about                                               | Build<br>Test<br>Done   |
|  4  | account holder                   | easily see books that I have selected to buy                 | amend my order                                                                        | Build<br>Test<br>Done   |
|  5  | account holder                   | easily see the total cost of books in my basket              | track my spending                                                                     | Build<br>Test<br>Done   |
|     | **Registration & User Accounts** |                                                              |                                                                                       |                         |
|  6  | site visitor                     | register for an account                                      | use the bookmark feature and use my saved details at checkout                         | Build<br>Test<br>Done   |
|  7  | account holder                   | receive confirmation email of account registration           | verify my account was created successfully                                            | Build<br>Test<br>Done   |
|  8  | account holder / admin           | log in and out of my account                                 | keep my account private and secure                                                    | Build<br>Test<br>Done   |
|  9  | account holder                   | view my profile                                              | amend my account details such as delivery address, password etc                       | Build<br>Test<br>Done   |
| 10  | account holder / admin           | reset my account password                                    | recover account                                                                       | Build<br>Test<br>Done   |
|     | **Searching & Filtering books**  |                                                              |                                                                                       |                         |
| 11  | site visitor / account holder    | sort books by category or price (low - high) / (high - low)  | easily identify books at a lower price and categories of books that I prefer          | Build<br>Test<br>Done   |
| 12  | site visitor / account holder    | search for a book by title, author or series (if applicable) | find a specific book, books by a specific author or a specific series                 | -Build<br>Test<br>Done  |
| 13  | site visitor / account holder    | easily see what I've searched for and the number or results  | quickly identify whether the book I'm looking for is available                        | Build<br>Test<br>Done   |
|     | Buying books & checkout          |                                                              |                                                                                       |                         |
| 14  | account holder                   | adjust quantity of books to add to basket                    | add more than one of the same book to my basket                                       | Build<br>Test<br>Done   |
| 15  | account holder                   | amend the quantity of a book when viewing my basket          | add another or remove one from the basket page itself                                 | Build<br>Test<br>Done   |
| 16  | account holder                   | easily identify where to remove books from my basket         | remove books if I change my mind                                                      | Build<br>Test<br>Done   |
| 17  | account holder                   | see cost breakdown and totals of books in basket             | review my spending                                                                    | Build<br>Test<br>Done   |
| 18  | account holder                   | see cost of delivery                                         | be aware of extra charges before payment                                              | Build<br>Test<br>Done   |
| 19  | account holder                   | see grand total or delivery + books                          | know the final amount that will be charged to my card                                 | Build<br>Test<br>Done   |
| 20  | account holder                   | easily enter my personal & payment information               | make the checkout process as convenient as possible                                   | Build<br>Test<br>Done   |
| 21  | account holder                   | receive email confirmation following successful checkout     | have a record of what I purchased                                                     | Build<br>Test<br>Done   |
|     | **Admin & Store Management**         |                                                              |                                                                                       |                         |
| 22  | admin                            | add new books                                                | upload new stock to the website                                                       | Build<br>Test<br>Done   |
| 23  | admin                            | edit book details                                            | make changes to the price, description, cover etc                                     | Build<br>Test<br>Done   |
| 24  | admin                            | delete books                                                 | remove books that are no longer for sale to ensure they're not accidentally purchased | Build<br>Test<br>Done   |
|     | **Bookmark**                         |                                                              |                                                                                       |                         |
| 25  | account holder                   | bookmark books                                               | keep track of books that I want to read                                               | Build<br>Test<br>Done   |
| 26  | account holder                   | update the progress of bookmarked books                      | easily differentiate between books I have read, I am reading or have yet to read      | Build<br>Test<br>Done   |
| 27  | account holder                   | set reading goals                                            | challenge myself to read more                                                         | Build<br>Test<br>Done   |
|     | **Book Ratings / reviews**           |                                                              |                                                                                       |                         |
| 28  | account holder                   | rate books that I have read  / bought                        | help others choose the best books to buy                                              | Build<br>Test<br>Done   |
| 29  | account holder                   | view reviews written by other users                          | make decisions on my own purchases                                                    | Build<br>Test<br>Done   |