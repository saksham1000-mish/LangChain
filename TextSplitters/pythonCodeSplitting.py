from langchain_classic.text_splitter import PythonCodeTextSplitter

code = """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
 def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

"""
splitter = PythonCodeTextSplitter(
    chunk_size=150,
    chunk_overlap=20,
 )

chunks = splitter.split_text(code)
print(len(chunks))
print(chunks[0])