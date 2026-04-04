# Checking Unique characters:

def has_unique_chars(s):
    
   duplicate_found = False
   
   character01 =[]

   for i in range (len(s)):
      
      to_check = s[i]
      
      for j in range (i+1,len(s)):
         
         if to_check == s[j]:

            duplicate_found = True

            if to_check not in character01:
                character01.append(to_check)
            
      
   return duplicate_found, character01
       

         
      

data =input("Enter the data: ")

s= data.lower()


d_found,char_check = has_unique_chars(s)

if d_found:
   print("The data given has duplicate characters")
   print(f"The duplicate characters are: {char_check}")

else:
   print("The data has only unique characters")