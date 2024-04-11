import cv2
import numpy as np

# Load the blurred image
BlurImg = cv2.imread(r'PythonFiles\BlurredImg.jpeg', cv2.IMREAD_GRAYSCALE)


def gaussian_psf(size, sigma=1):
    kernel = cv2.getGaussianKernel(size, sigma)
    return np.outer(kernel, kernel)


# Generate Gaussian PSF
psf = gaussian_psf(11, sigma=3)  # Adjust size and sigma as needed

# Pad the PSF to match the size of the blurred image FFT
psf_padded = np.zeros_like(BlurImg)
psf_padded[:psf.shape[0], :psf.shape[1]] = psf

# Perform Fourier Transform on the blurred image and padded PSF
blurred_img_fft = np.fft.fft2(BlurImg)
psf_fft = np.fft.fft2(psf_padded)

# Handle division by zero (avoid division by small values)
psf_fft[psf_fft < 1e-6] = 1  # Avoid division by zero
restored_img_fft = np.divide(blurred_img_fft, psf_fft)

# Perform inverse Fourier Transform to get the deblurred image
restored_img = np.fft.ifft2(restored_img_fft).real

# Normalize the image to 0-255 range
restored_img_norm = cv2.normalize(restored_img, None, 0, 255, cv2.NORM_MINMAX)
restored_img_norm = np.uint8(restored_img_norm)

# Display the deblurred image
cv2.imshow('Deblurred Image', restored_img_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the deblurred image
cv2.imwrite(r'PythonFiles\restored_image.jpg', restored_img_norm)
