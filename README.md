# GAN-Based-Image-Denoising-for-Car-Driving-Assistance

A car driving assistance system that involves segmenting pedestrians, vehicles (cars, bikes, etc.), and lane detection. 
Before performing segmentation and traffic sign detection, you will first apply a GAN-based denoising model to enhance images captured in adverse weather conditions.
For denoising, you will use the IDD dataset, which contains separate folders for low light, rain, snow, and fog conditions. Since these conditions are provided separately, 
you aim to tackle the challenge of combining multiple adverse weather effects (e.g., foggy and rainy) by leveraging a latent space arithmetic approach inspired by the DCGAN paper. 

This method, analogous to:
"Man with glasses" - "Man without glasses" + "Women without glasses" = "Women with glasses",
will be applied as:
"Foggy Image" - "Normal Image" + "Rainy Image" = "Foggy and Rainy Image"
to create new mixed-weather datasets.
