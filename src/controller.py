import os
import imageio
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from html import escape


def resize_image(input_path, size):
    with Image.open(input_path) as img:
        img_resized = img.resize(size)
        img_resized.save(input_path)

def compare_images(image1_path, image2_path):
    target_size = (300, 200)
    resize_image(image1_path, target_size)
    resize_image(image2_path, target_size)

    # Load images
    img1 = imageio.imread(image1_path)
    img2 = imageio.imread(image2_path)

    # Convert images to grayscale
    img1_gray = np.mean(img1, axis=-1)
    img2_gray = np.mean(img2, axis=-1)

    # Compute structural similarity index
    similarity_index, _ = ssim(img1_gray, img2_gray, data_range=img2_gray.max() - img2_gray.min(), full=True)

    return similarity_index

def generate_html_report(image_folder1, image_folder2, output_file='report.html'):
    # Get the list of image files in the folders
    images1 = [f for f in os.listdir(image_folder1) if f.endswith('.png') or f.endswith('.jpg')]
    images2 = [f for f in os.listdir(image_folder2) if f.endswith('.png') or f.endswith('.jpg')]

    # Generate HTML report
    html_content = "<html><head><title>Image Comparison Report</title></head><body>"
    html_content += "<h1>Image Comparison Report</h1>"

    for image1 in images1:
        for image2 in images2:
            image1_path = os.path.join(image_folder1, image1)
            image2_path = os.path.join(image_folder2, image2)

            # Compare images
            similarity_index = compare_images(image1_path, image2_path)

            # Add information to HTML report
            if image1 == image2 :
                html_content += f"<h2>{escape(image1)} vs {escape(image2)}</h2>"
                html_content += f"<p>Structural Similarity Index: {similarity_index:.4f}</p>"
                html_content += f"<img src='data:image/png;base64,{imageio.imread(image1_path).tolist()}' alt='Image 1'><br>"
                html_content += f"<img src='data:image/png;base64,{imageio.imread(image2_path).tolist()}' alt='Image 2'><br>"
                html_content += "<hr>"
            
         

    html_content += "</body></html>"

    # Save HTML report to file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    print(f"HTML report generated: {output_file}")

# Example usage
generate_html_report('data/version_a', 'data/version_b', 'comparison_report.html')