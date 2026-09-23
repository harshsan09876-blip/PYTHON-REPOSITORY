# 1. Input string lo
# 2. String ko check karo
# 3. Characters repeat ho rahe hain ya nahi, check karo
# 4. Non-repeating substring identify karo
# 5. Uski length nikalo
# 6. Sabse badi length ko result mein rakho
# # 7. Result print karo


string = input("Enter the string: ")

max_length = 0
  
  
for i in range(len(string)):
    current = ""
    
    for j in range(0, len(string)):
        if string[j] in current:
            break
        
        else:
            current += string[j]
            
            if len(current) > max_length:
                max_length = len(current)
                
print(max_length)






class Solution(object):
    def LengthOfLongestSubstring(self, s):
        max_length = 0
        
        s