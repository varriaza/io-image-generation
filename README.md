# io-image-generation

Have you recently wanted to generate your own AI images but found your GPU in use by a certain IO.net project?
This is the guide for you!

*A Step-by-Step Guide To Running Stable-Diffusion Based Models using IO.net*
Made for people with with little to no coding experience!

What you will need BEFORE you start
- Huggingface account???


Ray Cluster Creation Steps
1. Create an IO.net Ray cluster(?)
    - You should use a small GPU, like a 3050 or 3050 Ti to start out with
    - If you need more power you can always create a new cluster later. Thats the beauty of IO.net!
2. Hover over the top left and click on "Cloud" from the drop down
3. Click on the "Deploy" button for a Ray cluster (NOT a Mega-Ray!)
4. You will be taken to a "Create New Cluster" page
5. For "Cluster type" select "General"
6. Scroll down to "Supplier" and click IO
7. For GPU, you have some choices here
    - For your first time I would recommend an RTX 3050 or RTX 3060
    - Again, you can always create a better cluster later
8. For Location, select the country nearest you that is available
9. Scroll down to speed and choose Low or Medium
    - This will only really matter for when the code downloads the models (which can be a few GB) or when you want to download your created images
10. The Cluster name is not important, you can leave it as is
11. For the Summary we have a few options
    - GPU Quantity
        - I would recommend 1 for now
        - Some GPUs will make you buy multiple at a time which can cause your final price to skyrocket very quickly
    - For duration, just leave it at 1 hour
        - That should be plenty of time to install everything and mess around
        - You can always extend this later but if you purchase, for example, 10 hours now, there is no refund for unused time!
12. Double check the "Cluster Options" match what you want and hit the "Deploy" button right below them
13. Wait for your cluster to be deployed
    - This may take a few minutes
    - It took 3 minutes for me
14. Once that is done, click "View Cluster"

Access Your Cluster
1. Click on the "Password" in "Your Dev Environment" to copy it to your clipboard
2. From the cluster page, log into your new cluster by clicking the "Visual Studio" button
    - If you click the button and get a page that says "tunnel not found. create one at tunnels.io.systems", you'll have to create a support ticket.
2. Paste in the password you copied earlier
3. Click the hamburger menu at the top left (the three bars), go to view -> terminal
4. This will open a linux terminal at the bottom of your screen
5. Clone the following repo (I need to figure out how to link this without it being a link)
    - Provide part of url or ask admin to post link 
    - Run:
        - git clone https://github.com/varriaza/io-image-generation.git
7. Open a terminal and run: 
    - cd io-image-generation
    - Your terminal should show:
        - (base) root@virtualgpu30:~/io-image-generation#
6. Next run:
    - python -m venv image-generation 
7. source image-generation/bin/activate
    - Your terminal should show:
        - (image-generation) (base) root@virtualgpu30:~/io-image-generation#
8. pip install requirements.txt 
9. Click on the two pages/documents on the top left
10. Click the "Open Folder" button
11. A menu will open up with the text "/home/ray", add "io-image-generation" so it looks like "/home/ray/io-image-generation" and click the "OK" button
12. Your screen will refresh and you will see some files on the left
13. Follow the instructions to open your terminal again (step 3 and run step 7)
14. If you see a message saying "Do you trust the authors of the files in this folder?" click on "Yes, I trust the authors"

Everything is now installed!

Run Steps
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
        - num_images = 1 - 8 minutes and 5 seconds
        - num_images = 1 - 20 minutes and 56 seconds (this was probably too many images for my GPU to create at once)
- For now, your quality options have been simplified into "low", "medium" and "high"
    - I plan to add an advanced option later that will allow people to manually set values themselves
6. Once you're done editing the yaml file, save it

8. Run
- python run.py (your config file name here)
    - Examples:
        - python run.py dreamshaper.yml
        - python run.py lightning.yml
        - python run.py ssd_1b.yml 
8. The script will handle downloading the models and generating the images!
9. Images will be generated in the "image_results" folder
10. Go back to the yaml file and refine your prompt






