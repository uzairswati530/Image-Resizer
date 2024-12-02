import cv2

# Configurable Parameters
source = "download.jpg"  # Source image
destination = "newImage.png"  # Destination for the resized image
scale_percent = 50  # Scale by which the image will be resized (50%)

# Read the source image
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Check if the image was loaded successfully
if src is None:
    print("Error: Image not found!")
else:
    # Calculate the new dimensions based on the scale percentage
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resize the image to the new dimensions
    output = cv2.resize(src, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(destination, output)

    # Display the resized image (optional)
    cv2.imshow("Resized Image", output)

    # Wait for a key press indefinitely or for 0 milliseconds
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
