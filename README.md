# Library_Management
A python program to better understand how library's books are borrowed to help the library improve its services using Pandas and Numpy. The program analyzes 3 given datasets containing info about books,members and borrowings to obtain useful insights. All Three datasets are merged into one dataset named df to facilitate analysis.
# Features :
1-Caluclates the probaiblity of randomly selecting a book from any available genre.You can Replace the genre between the quotation marks in line 23 with desired genre.
2-Caluclates the probaiblity of randomly selecting a member from any available membership type. You can Replace the type between the quotation marks in line 32 with desired type.
3-Caluclates the probaiblity of randomly selecting a borrowing record that has a borrowing date that is after any specific date and the borrowed book is of a specific genre. You can Replace the genre between the quotation marks in line 40 with desired genre and the date between the quotation marks in line 41 with desired date in a this format (YYYY-MM-DD).
4-Finds the genre with the highest and lowest number of borrowings and their number of borrowings.
5-Determines which gender borrow books most frequently.
6-Compares borrowing activity between different membership types.
7-Finds number of borrowings per Membership type and the type with most borrowings.
8-Compares number of borrowings between different publication years.
9-Compares number of borrowings per author.
10-Identifies the most popular authors.
11-Finds the ID of books that have never been borrowed by adding book IDs that are in df dataset and not in books dataset to an empty list never_borrowed and then displays the full list. New lists bk and br are first created to hold the entire books IDs and borrowed books IDs respectively. 
12-Compares the average borrowing duration across genres by creating and adding a new column BorrowingPeriod to df dataset that holds the borrowing period of each borrowing by subtracting return and borrowing dates then calculating its mean for each genre.
13-Shows the distribution of books across genres.
14-Analyzes monthly borrowing trends.
15-Compares borrowing genres per gender
16-Calculates average borrower age per genre
17-Compares number of borrowings per publisher
