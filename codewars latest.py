def main_list(string):
	op = ['*', '/', '+', '-' ]
	final_list = []
	#item in final_list = 'operator', first operand, position, second operand, position 
	i=0
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
			temp.append(int(temp_ope))
			temp.append(j)

			#for second operand
			j=i+1
			temp_ope = ''
			while(j<len(string)):
				if string[j] in op:
					break
				temp_ope+=string[j]
				j+=1
			temp.append(int())
			temp.append(i)
			final_list.append(temp)
		i+=1
	return final_list

def main():
	print("Input the string")
	s = input()
	print(main_list(s))
