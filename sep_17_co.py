# linked list


# class LUCY:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# current1 = Node(10)

# while current1 is not None:
#     print(current1.data)
#     current1 = current1.next
    
    
class Node:
        def __init__(self,  data, next=None): 
            # init se functio run automatic
            # self kivalue khud ko refer 
            # data uske andar stored value
            # next --> none 
            self.data = data
            self.next = next
            #input the node
            # 
a = Node(10)
b = Node(20)
c = Node(30)
            
            #now connect the node fully pledge
a.next = b
b.next = c
            
current = a 
            #isko store karbe ke liye variable
while current is not None:
                print(current.data)
                
                current = current.next
            
            
#now new node add karna hai. 
class Natsu_DRAGNEEL:
    def __init__(self,  data, next=None) -> None:
            self.value = data
            self.next = None
            
            
            #node ko define karo
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
            

a.next = b
b.next = c
c.next = d


while a is not None:
    print(a.data)
    
    a = a.next

# ab do lists ko ek saath traverse karna hai
#toh hume kya karna hai sabse pehle:
class GRAY_FULLBUSTER:
    def __init__(self, data, next=None):
           self.value = data
           self.next = None
           
    a = Node(16)
    b = Node(26)
    c = Node(36)
    d = Node(46)
    x1 = Node(29)
    x2 = Node(39)
    x3 = Node(49)
    x4 = Node(59)
    a.next = b
    b.next = c
    c.next = d
    x1.next = x2
    x2.next = x3
    x3.next = x4
    current1 = a
    current2 = x1
    
    carry = 0 
    dummy = Node(0)
    tail = dummy 
    while current1 is not None and current2 is not None:
        
        print(current1.data, "+" ,current2.data)
        sum = current1.data + current2.data + carry
        result_digit = sum % 10
        carry = sum // 10
        
        
        
        print(sum)
        print("RESULT_DIGIT: ", result_digit)
        print("CARRY:  ", carry)
                
        new_node = Node(result_digit)
        tail.next = new_node
        tail = new_node
        current1 = current1.next
        current2 = current2.next
        
    current = dummy.next
        
    while current is not None:
            print(current.data)
            current = current.next
        
        
        # mein carry ka concept seekh raha tha kaise linked list mein caary and digit alakh rakhni hai . 
        # result_digit = current//10
        # result_digit1 = current%10
        # logic
        # result_digit1 = sum % 10
        # result_carry1 = sum // 10
        
        # print(result_digit1)
        
        
    #     #leetcode final question
    # class solution(object):
    #     def addTwoNumbers(self,l1, l2):
    #         data = l1
    #         l2 = None
            
    #         self.value = l1
    #         self.next = l2
    #         current1 = 0
    #         current2 = 0
    #         #write a newnode for sure
            
    #         object = Node
    #         a = object(2)
    #         b = object(4)
    #         c = object(3)
            
    #         a.next = b
    #         b.next = c
            
    #         s = object(5)
    #         v = object(6)
    #         j = object(4)
            
    #         s.next = v
    #         v.next = j
            
    #         a = current1
    #         s = current2
            
    #         print(current1)
    #         print(current2)
            
    #         carry = 0
    #         while current1 is not l1 and current2 is not l2:
    #             sum = current1 + current2 + carry
                
    #             result_digit = sum % 10 
    #             carry_digit = sum / 10
                
    #             print("\nnum_sum: ", sum)
    #             print("\nresult_digit: ", result_digit)
    #             print("\ncarry_digit: ", carry_digit)
                
    #         # we have to print the sum of node now
    #         dummy = Node(sum)
    #         tail = dummy
    #         tail.next = 
    
    # class solution(object):
    #     def addTwoNumbers(self, l1, l2):
    #         self.value = l1
    #         self.next = l2

    #         a = Node(2)
    #         b = Node(4)
    #         c = Node(3)

    #         a.next = b
    #         b.next = c

    #         current1 = a

    #         w = Node(5)
    #         x = Node(6)
    #         y = Node(4)

    #         w.next = x
    #         x.next = y

    #         current2 = w

    #         carry = 0
    #         while current1 is not None and current2 is not None:
    #             total = current1.data + current2.data + carry
    #             result_digit = total % 10
    #             carry = total // 10

    #             print(result_digit, carry)

    #             current1 = current1.next
    #             current2 = current2.next
                
    #             print(total)
                
    #             dummy = ListNode[0]
    #             tail = dummy
    #             tail.next = NewNode[0]\
    #             print(dummy)
    
    
    # class structure(object):
    #     def addTwoNumbers(self, l1, l2):
    #         self.l1 = l1
    #         self.l2 = l2
            
    #         a = Node[2]
    #         b = Node[5]
    #         c = Node[3]
            
    #         a.next = b
    #         b.next = c
    #         current1 = a
            
    #         x1 = Node[5]
    #         x2 = Node[6]
    #         x3 = Node[4]
    #         x1.l2 = x2
    #         x2.l2 = x3
            
    #         current2 = x1
    #         carry = 0
    #         while current1 is not None and current2 is not None:
    #             total + a.l1 + b.l2  
                
    #             result_digit = sum % 10
    #             carry_digit = sum // 10
                
    #             print("carry_digit":,  carry_digit)
    #             print("result_digit":, result_digit)
    #             print(total)
                
    #             dummy = NewNode[result_digit]
    #             tail = dummy
    #             tail.next = NewNode
    #             print(dummy)
            
                
                
                
                
            
            
                
            
            
            
        
        
        
        
        
        
        
    

      

            
        