import time
import run


def run_and_time_1_image_per():
    start_time = time.time()

    for _ in range(10):
        run.main("testing/dreamshaper_1.yml")

    end_time = time.time()

    print(
        f"Time taken to generate 10 images (1 image per): {end_time - start_time} seconds"
    )
    return end_time - start_time


def run_and_time_2_image_per():
    start_time = time.time()

    for _ in range(5):
        run.main("testing/dreamshaper_2.yml")

    end_time = time.time()

    print(
        f"Time taken to generate 10 images (2 images per): {end_time - start_time} seconds"
    )
    return end_time - start_time


def run_and_time_5_image_per():
    start_time = time.time()

    for _ in range(2):
        run.main("testing/dreamshaper_5.yml")

    end_time = time.time()

    print(
        f"Time taken to generate 10 images (5 images per): {end_time - start_time} seconds"
    )
    return end_time - start_time


def main():
    time_1 = run_and_time_1_image_per()
    time_2 = run_and_time_2_image_per()
    time_5 = run_and_time_5_image_per()

    print(f"time 1: {time_1}, time 2: {time_2}, time 5: {time_5}")


if __name__ == "__main__":
    main()
