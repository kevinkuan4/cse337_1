# CSE337
# Kevin Kuan
# 109645104

# I used the algorithm map from below to implement it
# https://4.bp.blogspot.com/-tfW9kZlhTzg/VvYbIaACxfI/AAAAAAAAA-M/dVc_sn3iZTA05mENL1W2gW1uoPbnVkFow/s1600/print-all-interleavings-of-string-recursion-stack.png
def interleave(list1, list2):
	(interleave_helper(list1,list2,[]))

def interleave_helper(list1,list2,list3):
	## BASE CASE
	if len(list1) == 0 and len(list2) == 0:
		print(list3)
		
	# ### 2nd case
	if len(list1) != 0:
		list1_temp=list1[:]
		x = list1_temp[0]
		del list1_temp[0]
		interleave_helper(list1_temp,list2,list3+[x])


	## 3rd case 
	if len(list2) != 0:
		list2_temp=list2[:]
		x = list2_temp[0]
		del list2_temp[0]
		interleave_helper(list1,list2_temp,list3+[x])


interleave([1,2],[3,4])

