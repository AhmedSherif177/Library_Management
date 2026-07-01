#task 7
import numpy as np
import pandas as pd 

books=pd.read_csv(r"C:\D\New folder\ieee\week7 (rev)\data\books.csv")
members=pd.read_csv(r"C:\D\New folder\ieee\week7 (rev)\data\members.csv")
borrowings=pd.read_csv(r"C:\D\New folder\ieee\week7 (rev)\data\borrowings.csv")

halfmerged= pd.merge(books,borrowings,on="BookID")
df=pd.merge(halfmerged,members,on="MemberID")

genre=books.groupby("Genre")
memberships_type=members.groupby("MembershipType")
borrow_date=borrowings.groupby("BorrowDate")

TotalNumofBooks = books.shape[0]
TotalNumofMembers = members.shape[0]
TotalNumofBorrowings =borrowings.shape[0]
print(f"-Total Number of Books = {TotalNumofBooks}, Books Shape = {books.shape}\n-Total Number of Members = {TotalNumofMembers}, Members Shape = {members.shape}\n-Total Number of Borrowing Records = {TotalNumofBorrowings}, Borrowings Shape = {borrowings.shape}")


print(f"-Available Genres : {books["Genre"].unique().tolist()}")
sel_genre="Mystery"

def booksprop(genre_name):
    num_of_books_in_sel_genre = genre.get_group(genre_name).value_counts().sum()
    print(f"-Probability of Selecting a Borrowed Book from The {genre_name} Genre = {num_of_books_in_sel_genre/TotalNumofBooks}")
booksprop(sel_genre)


print(f"-Available Membership Types : {members["MembershipType"].unique().tolist()}")
sel_membership="Student"

def memberships_prop(type):
    num_of_members_with_sel_type = memberships_type.get_group(type).value_counts().sum()
    print(f"-Probability of Selecting a Member with {type} Membership = {num_of_members_with_sel_type/TotalNumofMembers}")
memberships_prop(sel_membership)


borrow_genre="History"
borrowdate= pd.Timestamp("2025-12-31")
genreid=genre.get_group(borrow_genre)["BookID"].tolist()

def borrowing_prob(borrowdate):   
   num_of_records = borrowings[
      (pd.to_datetime(borrowings["BorrowDate"]) > borrowdate) &
      (borrowings["BookID"].isin(genreid)) ]
   print(f"-Probability of Selecting a Record That Has a Borrowing Date After {borrowdate.date()} And The Genre of The Gorrowed Book is {borrow_genre} = {num_of_records.shape[0]/TotalNumofBorrowings}")
borrowing_prob(borrowdate)    


print(f"-Genre With The Most Borrowings is {(df['Genre'].value_counts()).idxmax()}, Number of Borrowings= {df['Genre'].value_counts().max()}")
print(f"-Genre With The Least Borrowings is {(df['Genre'].value_counts()).idxmin()}, Number of Borrowings= {df['Genre'].value_counts().min()}")
print(f"-Gender with The Most Borrowings is {(df['Gender'].value_counts().idxmax())}")

print(df['MembershipType'].value_counts())
print(f"-Membership Type with The Most Borrowings is {(df['MembershipType'].value_counts().idxmax())}")
print((df.loc[:,['Genre','MembershipType']]).value_counts())
print(df['PublicationYear'].value_counts())
print(df['Author'].value_counts())
print(f"-Author with The Most Borrowings is {(df['Author'].value_counts().idxmax())}")


bk= books['BookID'].tolist()
br= (df["BookID"].unique()).tolist()

never_borrowed=[]
for x in bk :
    if x not in br :
        never_borrowed.append(x)
print(f"Books That have Never Been Borrowed {never_borrowed}" )

df["BorrowingPeriod"]=pd.to_datetime(df["ReturnDate"]) - pd.to_datetime(df["BorrowDate"])
print(df.groupby("Genre")["BorrowingPeriod"].mean())

print(books["Genre"].value_counts())
df['BorrowDate']=pd.to_datetime(df['BorrowDate'])
print((df.groupby(df['BorrowDate'].dt.to_period('M')))["Genre"].value_counts())


print(df.groupby("Gender")["Genre"].value_counts())
print(df.groupby("Genre")["Age"].mean())
print(df["Publisher"].value_counts())


numeric = np.array(df['Age'])
print(numeric)

print(f"-Highest Borrower Age is {np.max(df["Age"])} Years")

filt = numeric[numeric<25 ]

filt = np.sort(filt)
print(filt)

numeric2 = numeric *2 
print(numeric2)

print(f"Summary :\nMost Borrowed Genre is {(df['Genre'].value_counts()).idxmax()}\nLeast Borrowed Genre is {(df['Genre'].value_counts()).idxmin()}\nAverage Borrower Age is {df['Age'].mean()} Years\nMembership Type with The Most Borrowings is {(df['MembershipType'].value_counts().idxmax())}\nMembership Type with The Least Borrowings is {(df['MembershipType'].value_counts().idxmin())}")