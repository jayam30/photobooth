import os
import numpy as np
import torch
import torchvision.transforms as transforms
from PIL import Image, ImageEnhance, ImageOps

class ImagePreprocessor:
    def __init__(self, target_size=(160, 160)):
        """
        Initialize image preprocessor with configurable settings
        
        Args:
            target_size (tuple): Desired image size for resizing (width, height)
        """
        self.target_size = target_size
        
        # Standard normalization transform for face recognition models
        self.normalize_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],  # ImageNet mean
                std=[0.229, 0.224, 0.225]    # ImageNet std
            )
        ])
    
    def resize_image(self, image, method=Image.LANCZOS):
        """
        Resize image to target dimensions
        
        Args:
            image (PIL.Image): Input image
            method (int): Resampling method
        
        Returns:
            PIL.Image: Resized image
        """
        return image.resize(self.target_size, method)
    
    def augment_image(self, image, augmentation_types=None):
        """
        Apply data augmentation techniques
        
        Args:
            image (PIL.Image): Input image
            augmentation_types (list): Types of augmentations to apply
        
        Returns:
            list of PIL.Image: Augmented images
        """
        if augmentation_types is None:
            augmentation_types = [
                'brightness', 
                'contrast', 
                'sharpness', 
                'horizontal_flip'
            ]
        
        augmented_images = [image]
        
        if 'brightness' in augmentation_types:
            brightness_factors = [0.8, 1.2]
            for factor in brightness_factors:
                enhancer = ImageEnhance.Brightness(image)
                augmented_images.append(enhancer.enhance(factor))
        
        if 'contrast' in augmentation_types:
            contrast_factors = [0.8, 1.2]
            for factor in contrast_factors:
                enhancer = ImageEnhance.Contrast(image)
                augmented_images.append(enhancer.enhance(factor))
        
        if 'sharpness' in augmentation_types:
            sharpness_factors = [0.8, 1.2]
            for factor in sharpness_factors:
                enhancer = ImageEnhance.Sharpness(image)
                augmented_images.append(enhancer.enhance(factor))
        
        if 'horizontal_flip' in augmentation_types:
            augmented_images.append(ImageOps.mirror(image))
        
        return augmented_images
    
    def preprocess(self, image, augment=False, augmentation_types=None):
        """
        Complete image preprocessing pipeline
        
        Args:
            image (PIL.Image): Input image
            augment (bool): Whether to perform data augmentation
            augmentation_types (list): Types of augmentations to apply
        
        Returns:
            list or torch.Tensor: Preprocessed images
        """
        # Ensure image is in RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize image
        resized_image = self.resize_image(image)
        
        # Perform augmentation if requested
        if augment:
            augmented_images = self.augment_image(resized_image, augmentation_types)
            return [self.normalize_transform(img) for img in augmented_images]
        
        # Return normalized single image
        return self.normalize_transform(resized_image)