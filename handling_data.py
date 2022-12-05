# Handling Data
import pandas as pd

# items = pd.Series(['chairs', 'labels', 'tables'])
#
# print(items)


# Creating a series by passing in a List without key

# names = pd.Series(["James", "Tom", "Jane"])
# items = pd.Series(['chairs', 'labels', 'tables'])
#
# d_frame = {'Name': ["Joe", 'Tom', 'Jane'],
#            'Items':['tables', 'chairs', 'labels']}
#
# purchases = pd.DataFrame(d_frame)
#
# print(purchases)

# mdata = pd.read_csv("Marketing.csv");
# m_data = mdata.head(10)
# minfo = mdata.info
# print(minfo)

# authors = pd.Series(['E.L. James', 'Suzanne Collins', 'J.K. Rowling', 'Dan Brown'])
# reviews = pd.Series([410, 211, 314, 178])
#
# print(authors, reviews)

# d_frame = {"Authors": ['E.L. James','Suzanne Collins', 'J.K. Rowling', 'Dan Brown'],
#            "Reviews": [410, 211, 314, 178]}
# df = pd.DataFrame(d_frame)
# print(df)

best = pd.read_csv('bestsellers.csv')
b_1 = best.head()

print(b_1)
