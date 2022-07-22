import sys
import array


def mergesort(a, arr_type):
  def perform_merge(a, arr_type, start, mid, end):
    # Merges two previously sorted arrays
    # a[start:mid] and a[mid:end]
    tmp = array.array(arr_type, [i for i in a])
    def compare(tmp, i, j):
      if tmp[i] <= tmp[j]:
        i += 1
        return tmp[i-1]
      else:
        j += 1
        return tmp[j-1]
    i = start
    j = mid + 1
    curr = start
    while i<=mid or j<=end:
      if i<=mid and j<=end:
        if tmp[i] <= tmp[j]:
          a[curr] = tmp[i]
          i += 1
        else:
          a[curr] = tmp[j]
          j += 1
      elif i==mid+1 and j<=end:
        a[curr] = tmp[j]
        j += 1
      elif j == end+1 and i<=mid:
        a[curr] = tmp[i]
        i += 1
      elif i > mid and j > end:
        break
      curr += 1

    def mergesort_helper(a, arr_type, start, end):
      # Divides the array into two parts
      # recursively and merges the subarrays
      # in a bottom up fashion, sorting them
      # via Divide and Conquer
      if start < end:
        mergesort_helper(a, arr_type, start, (end + start)//2)
        mergesort_helper(a, arr_type, (end + start)//2 + 1, end)
        perform_merge(a, arr_type, start, (start + end)//2, end)

    # Sorts the array using mergesort_helper
    mergesort_helper(a, arr_type, 0, len(a)-1)


sys.modules[__name__] = mergesort