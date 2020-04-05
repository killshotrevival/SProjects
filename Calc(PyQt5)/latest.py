def main_list(string):
	op = ['*', '/', '+', '-' ]
	final_list = []
	#item in final_list = 'operator', first operand, position, second operand, position 
	i=0
	try:

		while(i<len(string)):
			if string[i] in op:
				temp = []
				temp.append(string[i])

				#for first operand
				j=i-1
				temp_ope = ''
				while(j>=0):
					if string[j] in op:
						break
					temp_ope+=string[j]
					j-=1
				temp.append(int(temp_ope[::-1]))
				temp.append(j+1)

				#for second operand
				j=i+1
				temp_ope = ''
				while(j<len(string)):
					if string[j] in op:
						break
					temp_ope+=string[j]
					j+=1
				temp.append(int(temp_ope))
				temp.append(i+1)
				final_list.append(temp)
			i+=1
		return final_list

	except:
		return False

def compute(l):
	if l[0]=='*':
		return l[1]*l[3]
	elif l[0]=='/':
		return l[1]/l[3]
	elif l[0]=='+':
		return l[1]+l[3]
	elif l[0]=='-':
		return l[1]-l[3]

def main_producer(s):
	m_l = main_list(s)
	#print(m_l)
	if not m_l:
		return 'Invalid Expression'
	else:

		op = ['*', '/', '+', '-' ]
		m_l.sort(key= lambda i: op.index(i[0]) )
		res=0
		i=0
		addr_changed = [m_l[0][2],m_l[0][4]]
		while(i<len(m_l)):
			#print('m_l')
			#print(m_l)
			res = compute(m_l[i])
			#print('res'+str(res))
			for j in m_l:
				if j!=i:
					if j[2]>=addr_changed[0] and j[2]<=addr_changed[1]:
						j[1]=res
					elif  j[4]>=addr_changed[0] and j[4]<=addr_changed[1]:
						j[3]=res
			if (m_l[i][2]<addr_changed[0]):
				addr_changed[0]=m_l[i][2]
			elif m_l[i][4]>addr_changed[1]:
				addr_changed[1]=m_l[i][4]
			m_l.remove(m_l[i])
		return(str(res))

