#!/usr/bin/python3

def canUnlockAll(boxes):
    # Total number of boxes
    n = len(boxes)
    
    # Set of unlocked boxes
    unlocked = set()
    # Queue for BFS (we can also use a stack for DFS)
    queue = [0]
    
    while queue:
        # Get the current box index
        current_box = queue.pop(0)
        if current_box not in unlocked:
            # Mark the current box as unlocked
            unlocked.add(current_box)
            # Add all boxes we can open with the keys from the current box
            for key in boxes[current_box]:
                if key < n and key not in unlocked:
                    queue.append(key)
    
    # Check if we have unlocked all the boxes
    return len(unlocked) == n

