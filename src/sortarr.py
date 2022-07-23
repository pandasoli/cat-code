import sys


def quicksort(a):
  def do_partition(a, start, end):
    pivot_idx = end
    pivot = a[pivot_idx]
    idx = start - 1

    def increment_and_swap(j):
      nonlocal idx
      idx += 1
      a[idx], a[j] = a[j], a[idx]

    [increment_and_swap(j) for j in range(start, end) if a[j] < pivot]

    a[idx + 1], a[end] = a[end], a[idx+1]

    return idx + 1

  def quicksort_helper(a, start, end):
    if start < end:
      pivot_idx = do_partition(a, start, end)
      quicksort_helper(a, start, pivot_idx - 1)
      quicksort_helper(a, pivot_idx + 1, end)

  quicksort_helper(a, 0, len(a) - 1)


sys.modules[__name__] = quicksort