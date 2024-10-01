# Brain MRI Metastasis Segmentation

This project implements and compares two deep learning architectures, Nested U-Net and Attention U-Net, for brain MRI metastasis segmentation.

## Architecture
- **Nested U-Net (U-Net++)**: Extends the original U-Net architecture by adding nested layers with dense skip connections.
- **Attention U-Net**: Incorporates attention mechanisms to focus on important areas of the MRI image.

## Dataset Preprocessing
- Applied CLAHE to enhance MRI image contrast.
- Augmented the dataset with rotations, shifts, and zooms.

## Results
- Nested U-Net DICE Score: XX.XX
- Attention U-Net DICE Score: XX.XX
