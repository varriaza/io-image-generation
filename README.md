# io-image-generation

Have you wanted to generate your own AI images without rate limits or website constraints? 
Or maybe your GPU is being used by an AI Compute DePIN project?
If so, this is the guide for you!

*A Step-by-Step Guide To Running Stable-Diffusion Based Models using IO.net*
Made for people with with little to no coding experience!

What you will need BEFORE you start
- A computer with a web browser


Ray Cluster Creation Steps
1. Create an IO.net Ray cluster    
2. Hover over the top left and click on "Cloud" from the drop down
3. Click on the "Deploy" button for a Ray cluster (NOT a Mega-Ray!)
4. You will be taken to a "Create New Cluster" page
5. For "Cluster type" select "General"
6. Scroll down to "Supplier" and click IO
7. For GPU, you have some choices here
    - For your first time I would recommend an RTX 3050 (Ti or regular) or RTX 3060 (Ti or regular)
    - If you need more power you can always create a new cluster later. Thats the beauty of IO.net!
8. For Location, select the country nearest you that is available
9. Scroll down to speed and choose Low or Medium
    - This will only really matter for when the code downloads the models (which can be a few GB) or when you want to download your created images
10. The Cluster name is not important, you can leave it as is
11. For the Summary we have a few options
    - GPU Quantity
        - I would recommend 1 for now
        - Some GPUs will make you buy multiple at a time which can cause your final price to skyrocket very quickly
            - If you don't see "1" as an option for your first time I would try a different GPU
    - For duration, I would recommend 1-2 hours
        - That should be plenty of time to install everything and mess around
        - You can always extend this later (or make a new cluster) but if you purchase, for example, 10 hours now, there is no refund for unused time!
12. Double check the "Cluster Options" match what you want and hit the "Deploy" button right below them
13. Wait for your cluster to be deployed
    - This can take 3-5 minutes
    - If the cluster fails to be created (you get a bunch of red "x"s) you'll just have to re-make it from step 3
14. Once that is done, click "View Cluster"


Access and Setup Your Cluster
1. Click on the "Password" in "Your Dev Environment" to copy it to your clipboard
2. From the cluster page, log into your new cluster by clicking the "Visual Studio" button
    - If you click the button and get a page that says "tunnel not found. create one at tunnels.io.systems", you'll have to create a support ticket.
3. Paste in the password you copied earlier
4. Click the hamburger menu at the top left (the three bars), go to "terminal" -> "new terminal"
5. This will open a linux terminal at the bottom of your screen
    - No need to worry, I will walk you through everything you need to do with it 
6. Clone the following repo (I need to figure out how to link this without it being an issue)
    - Provide part of url or ask admin to post link 
    - Run:
        - git clone https://github.com/varriaza/io-image-generation.git
            - This copies the code I made to your cluster 
        - NOTE: To run something in the terminal, copy/paste the text (WITHOUT the bullet point) and press enter
7. Click on the two pages/documents icon on the top left
8. Click the "Open Folder" button
9. A menu will open up with the text "/home/ray", add "io-image-generation" so it looks like "/home/ray/io-image-generation" and click the "OK" button
    - If you accidentally forget to add "io-image-generation" you'll see a bunch of other files, you'll just have to ignore those
10. Your screen will refresh and you will see some files on the left
11. If you see a message saying "Do you trust the authors of the files in this folder?" click on either answer. Both will work.
12. Follow the instructions to open your terminal again (step 4)
13. If you DID NOT add "io-image-generation" in step 9, in the terminal run: 
    - cd io-image-generation
        - Your terminal should show:
            - (base) root@virtualgpu30:~/io-image-generation#
        - This command opens the "io-image-generation" folder in the terminal (this is the code you just downloaded)
14. Run:
    - python -m venv image-generation 
        - This creates a "virtual environment", that we called "image-generation", where you can install code 
15. Run:
    - source image-generation/bin/activate
        - Your terminal should show:
            - (image-generation) (base) root@virtualgpu30:~/io-image-generation#
        - This activates the "virtual environment" we just created
16. Run:
    - pip install -r requirements.txt 
        - This installs the code requirements


Everything is now installed!


Create Image Steps
1. You are ready to start making images!
2. To change prompt text, image quality and the number of images generated per prompt, open the "config_files" folder on the left
3. Each file in this folder represents the input to the model with the same name
4. For specific details and examples of some images, follow the link to the huggingface page included in the "yaml" (aka yml) files
5. Edit the values as you see fit
    - Don't forget to save the files!!!
    - I would recommend leaving quality on "low" or "medium" until you see how long it takes to generate an image with the GPU you selected
    - Depending on quality settings and GPU, it could take ~10 seconds to more than 1 minute
        - With my own 4080, I got the following times to make 10 images, with dreamshaper, at medium settings
            - num_images = 1 - 8 minutes and 37 seconds
            - num_images = 2 - 8 minutes and 5 seconds
            - num_images = 5 - 20 minutes and 56 seconds (this was probably too many images for my GPU to create at once)
    - For now, your quality options have been simplified into "low", "medium" and "high"
        - I might add an advanced option later that will allow people to manually set values themselves
6. Once you're done editing the yaml file, save it
7. In your terminal run:
    - python run.py (your config file name here)
        - Examples:
            - python run.py dreamshaper.yml
            - python run.py lightning.yml
            - python run.py ssd_1b.yml 
8. The script will handle downloading the models and generating the images!
9. Images will be generated in the "image_results" folder
    - To see them, click on them
        - It may take a second to load them
10. Go back to the yaml file and refine your prompt and rerun step 7
11. To download an image, or multiple, select them, right click and hit download
12. If you get a "torch.cuda.OutOfMemoryError: CUDA out of memory." error just reduce the "num_images" you are telling the GPU to generate






