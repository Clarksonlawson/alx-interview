#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    
    for byte in data:
        # Get the 8 least significant bits of the integer
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Check how many bytes the current UTF-8 character has
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
                
            # 1-byte character
            if num_bytes == 0:
                continue
                
            # Invalid scenarios: if num_bytes is 1 or more than 4
            if num_bytes == 1 or num_bytes > 4:
                return False
                
        else:
            # Check that the byte is a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
                
        # Decrement the number of bytes remaining
        num_bytes -= 1
        
    return num_bytes == 0

# Example Usage:
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False

