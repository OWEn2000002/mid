1、Recursive Solution for Tower of Hanoi：

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from peg {source} to peg {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from peg {source} to peg {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

# Example usage
tower_of_hanoi(3, 'A', 'C', 'B')

2、Iterative approach  for Tower of Hanoi：

def tower_of_hanoi_iterative(n, source, target, auxiliary):
    stack = [(n, source, target, auxiliary)]
    while stack:
        disks, source, target, auxiliary = stack.pop()
        if disks == 1:
            print(f"Move disk 1 from peg {source} to peg {target}")
        else:
            stack.append((disks - 1, auxiliary, target, source))
            stack.append((1, source, target, auxiliary))
            stack.append((disks - 1, source, auxiliary, target))

# Example usage
tower_of_hanoi_iterative(3, 'A', 'C', 'B')

3、answers：
  1）Time Complexity:
  Both the recursive and iterative solutions for the Tower of Hanoi problem have the same time complexity, which is O(2^n), where n is the number of disks. 
  This is because the number of moves required to solve the Tower of Hanoi problem 
  for n disks grows exponentially with the number of disks.

  2）Space Complexity:
    i) [Recursive Solution]:
    The recursive solution has a space complexity of O(n) due to the function call stack. 
    As the function makes recursive calls, memory is allocated on the call stack for each call until the base case is reached.

    ii) [Iterative Solution]:
    The iterative solution has a space complexity of O(n) due to the stack data structure used to simulate the recursive calls.
    In this approach, we use an explicit stack to keep track of the state instead of relying on the function call stack.

  3）Explain the Differences：
    The main difference in space complexity arises from the use of the function call stack in the recursive solution versus an explicit stack in the iterative solution.
    The iterative solution avoids the overhead of recursive function calls, 
    potentially leading to better performance for large values of n due to reduced memory usage and avoiding potential stack overflow issues.
    Both solutions have the same time complexity, but the iterative solution can be more efficient in terms of space utilization for large inputs.

    In summary, 
    while both solutions have the same time complexity, 
    the iterative solution offers an advantage in space efficiency by using an explicit stack rather than relying on the function call stack,
    especially for larger input sizes.
