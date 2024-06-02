# Input: book_stack and user_request
book_stack = [34, 67, 8, 98, 34, 2, 34, 65, 76]
user_request = [8, 25, 34, 98]

# Output: output
output = []

# Loop over the user requests
for book in user_request:
    # Check if the request is valid
    if book == -1:
        break
    # Check if the book is in the stack
    if book in book_stack:
        # Initialize a counter and a temporary stack
        count = 0
        temp = []
        # Pop out the books until the requested book is found
        while book_stack[-1] != book:
            temp.append(book_stack.pop())
            count += 1
        # Pop out the requested book and increment the counter
        book_stack.pop()
        count += 1
        # Push back the books in the same order
        while temp:
            book_stack.append(temp.pop())
        # Append the count to the output list
        output.append(count)
    else:
        # Append -1 to the output list
        output.append(-1)

# Print the output list
print(output)
