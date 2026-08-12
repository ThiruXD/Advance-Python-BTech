import cv2

# Load the image
image = cv2.imread('iwmages.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not read the image. Check the file path.")
else:
    # 1. Image Dimensions (Returns a tuple: Height, Width, and Channels)
    dimensions = image.shape
    height = image.shape[0]
    width = image.shape[1]
    
    # Handle grayscale images which do not have a 3rd element in the shape tuple
    channels = image.shape[2] if len(image.shape) == 3 else 1

    # 2. Total Number of Pixels (Height x Width x Channels)
    total_pixels = image.size

    # 3. Image Data Type (e.g., uint8, float32)
    data_type = image.dtype

    # Print all retrieved properties
    print("--- OpenCV Image Properties ---")
    print(f"Shape (H, W, C): {dimensions}")
    print(f"Image Height:    {height} pixels")
    print(f"Image Width:     {width} pixels")
    print(f"Number of Channels: {channels}")
    print(f"Total Pixels:    {total_pixels}")
    print(f"Data Type:       {data_type}")


