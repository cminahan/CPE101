# CPE 101 Lab 4
# Name: Claire Minahan

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment = get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
#int --> int
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while (size) < 0:
      print ("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user
# int --> int
def get_first():
   first = int(input("Enter the value of the first number in the table: "))

   while (first) < 0:
      print ("First number must be non-negative")
      first = int(input("Enter the value of the first number in the table:"))
   return first;

# Display the table of power4
# table
def show_table(size, first, increment):
   print ("A power4 table of size %d will appear here starting with %d." % (size, first))
   print ("Number  Power4")
   
   # Insert Loop Here
   i = 0
   power4 = 0
   while i < size:
      print ("%-6d  %d" % (first, first**4))
      power4 += first**4
      first += increment
      i += 1
   print ("The sum of power4 is: ", power4)

#Obtain the increment between rows
#int --> int
def get_increment():
   inc = int(input("Enter the increment between rows: "))

   while inc < 0:
      print("Increment must be non-negative.")
      inc = int(input("Enter the increment between rows: "))
   return inc

if __name__ == "__main__":
   main()