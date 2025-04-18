# GAN-Based-Image-Denoising-for-Car-Driving-Assistance

A car driving assistance system is being developed, incorporating segmentation of pedestrians, vehicles (cars, bikes, etc.), traffic signs and lane detection. 
Before performing segmentation and detection, a GAN-based denoising model will be applied to enhance images captured in adverse weather conditions.

For denoising, the IDD dataset is utilized, which contains separate folders for low light, rain, snow, and fog conditions. Since these conditions are provided separately, the challenge of combining multiple adverse weather effects (e.g., foggy and rainy) is addressed using a latent space arithmetic approach inspired by the DCGAN paper.

This method, analogous to:
#### "Man with glasses" - "Man without glasses" + "Women without glasses" = "Women with glasses",
will be applied as:
#### "Foggy Image" - "Normal Image" + "Rainy Image" = "Foggy and Rainy Image"
to create new mixed-weather datasets.

## Dataset Links:
1. CULane Detection Dataset: https://xingangpan.github.io/projects/CULane.html
2. IDD Segmentation Dataset: IDD Segmentation (IDD 20k Part I) (18.5 GB)
3. IDD Traffic Sign Detection: Dataset: MissingTSMini (2.2 GB)
4. IDD Adverse Weather Dataset: IDD-AW (19 GB)
