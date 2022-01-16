# Create JSONs from a CSV file using a Python script

## Overview

Our `Compiler.py` python script converts the traits in `Roster.csv` into a JSON file for each row.

While this logic can be used for a number of applications, our example creates JSONs for an NFT collection called ParkPics. Find the full repo for ParkPics [here](https://github.com/alxrnz2/ERC1155-with-EIP2981-for-OpenSea), which covers metadata pinning/upload, smart contracts, deployment, verification, and OpenSea import.

## Steps to update `Compiler.py`

First, adjust the image pin to reflect your images' CAR file. Learn more about CARs in our [ERC 1155 repo](https://github.com/alxrnz2/ERC1155-with-EIP2981-for-OpenSea#1-pinupload-token-metadata).

```
archive = "ipfs://bafybeiatmiig6ylhha5p7o7bxvqutfitv6k2n5ghche4r22tgkmoz6gu5u/"
```

Next, update the `Compiler.py` variables for your metadata fields and number of rows. For debugging purposes, we use descriptive labels for each variable.

```
filename = row[0]
name = row[1]
park = row[2]
type = row[3]
feature = row[4]
```

Finally, update `NFTjson = ...` for the desired fields in your JSONs. Learn more from the [NFT School](http://nftschool.dev.ipns.localhost:8080/reference/metadata-schemas/) about token metadata standards.

## Create your JSONs

Run the `Compiler.py` script in your IDE/CLI of choice. If you're new to Python scripts, check out this [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) from [VS Code](https://code.visualstudio.com/).

## Test the JSONs before upload

Before uploading your JSONs, we recommend opening a few in VS Code (or a similar IDE), right clicking anywhere in the JSON, and selecting `Format Document`. Then, the IDE should flag any formatting errors that you'd need to fix in your Python script.
