from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ['Test1', 'Test2', 'Test3'],
    # blur=2,
    # random_blur=True
)
generator = GeneratorFromWikipedia(count= 5)

for i, (img, lbl) in enumerate(generator):
    # Do something with the pillow images here.
    # import pdb; pdb.set_trace()
    img.save(f"sample_imgs/test_{i}.jpg")