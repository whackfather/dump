# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 12
# References: Jesse Paulsen
# Time: 30 minutes

from helper_library import *

def block_average(grid:list, x:int, y:int, width:int, height:int) -> list:
    sum_r = sum_g = sum_b = 0
    for i in range(y, y + height):
        for j in range(x, x + width):
            pixel = grid[i][j]
            sum_r += pixel[0]
            sum_g += pixel[1]
            sum_b += pixel[2]
    num_pixels = width * height
    avg_r = sum_r // num_pixels
    avg_g = sum_g // num_pixels
    avg_b = sum_b // num_pixels
    
    return [avg_r, avg_g, avg_b]

def create_compressed_block(avg_color:list, width:int, height:int) -> list:
    return [[avg_color] * width for _ in range(height)]

def merge_lists(lst1:list, lst2:list) -> list:
    merged = []
    for row1, row2 in zip(lst1, lst2):
        merged.append(row1 + row2)
    
    return merged

def compress_image(grid:list, x:int, y:int, width:int, height:int, threshold:int) -> list:
    if width <= threshold or height <= threshold:
        avg_color = block_average(grid, x, y, width, height)
        return create_compressed_block(avg_color, width, height)
    
    mid_width = width // 2
    mid_height = height // 2
    
    top_left = compress_image(grid, x, y, mid_width, mid_height, threshold)
    top_right = compress_image(grid, x + mid_width, y, width - mid_width, mid_height, threshold)
    bottom_left = compress_image(grid, x, y + mid_height, mid_width, height - mid_height, threshold)
    bottom_right = compress_image(grid, x + mid_width, y + mid_height, width - mid_width, height - mid_height, threshold)
    
    top_half = merge_lists(top_left, top_right)
    bottom_half = merge_lists(bottom_left, bottom_right)

    return top_half + bottom_half

if __name__ == "__main__":
    image_filename = input("IMAGE_FILENAME> ")
    compression_threshold = int(input("COMPRESSION_THRESHOLD> "))
    
    grid = image_to_list(image_filename)
    height = len(grid)
    width = len(grid[0])
    
    print(f"OUTPUT Width: {width}")
    print(f"OUTPUT Height: {height}")
    print(f"OUTPUT Threshold: {compression_threshold}")
    
    compressed_grid = compress_image(grid, 0, 0, width, height, compression_threshold)
    output_filename = f"compressed_{image_filename}"
    output_image(compressed_grid, output_filename)
