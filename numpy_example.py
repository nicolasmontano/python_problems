import numpy_example as np


a=[[1,1,1],[2,2,2],[3,3,np.nan]]
np_a=np.array(a)

np_a[2,1] # slice like matrix
np_a[1,:] # 1 row
np_a[:,1] # 1 column
np.squeeze(np_a)


np_a[::2,:] # fetch every 2 rows
np_a[[1,2]] # mask as filter

# Mask
index=np.where(np_a>1)
np_a[index] # exgtract the value, loses the dim
np.delete(np_a,index) # delete the values, loses the dim
np_a[np.isnan(np_a)]  # nan values, loses dim
np.isnan(np_a).any()
np_a[np.isnan(np_a)[:,2],2]

# Sum, product, div (Element by element)
np_a+np.array([1,2,3]) # broadcast by col   mulitply by 1 ,2 ,3 each column
np_a+np_a # each [i,j] is doubled

# arithmetic methods
np_a=np.array([[1,1,1],[2,2,2],[3,3,3]])
np_a[:,1].sum()  # add by column
np_a.sum(axis=0) # add all by col
np_a.sum(axis=1) # add all by row

# matrix multiplication
np_a.dot(np_a[0]) 

#transpose
np.transpose(x.reshape(1,3))  #require an adeq dim

#nulls
np_a[~np.isnan(a)] # remove nulls

# sort 
np_a=np.array([[3,5,1],[6,2,4],[9,8,7]])
np.sort(np_a) # sort by row is not inplace
np.sort(np_a[:,1]) # sort a column or np_a[:,1].sort() inplace

# search
np.count_nonzero(np.where(np_a<=1,a,100))
np.count_nonzero()

# max
np.max(np_a)

