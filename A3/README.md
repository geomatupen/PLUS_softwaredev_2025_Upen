# Geospatial Jupyter Environment Setup (`geoenv`)

This README provides step-by-step instructions to set up a Conda environment named `geoenv` with geospatial libraries like GDAL and Rasterio, and configure it for use in Jupyter Notebook.

---

## Step 1: Create and Activate the Conda Environment

Open Anaconda Prompt and run the following commands to create the environment:

```
conda create -n geoenv python=3.11 jupyter gdal rasterio -y
conda activate geoenv
```

> **Note**: You only need to create the environment once. From next time onward, just run:

```
conda activate geoenv
```

---

## Step 2: Export the Conda Environment to `environment.yml`

After activating the environment and installing the required libraries, export the environment configuration:

```
conda env export --from-history > environment.yml
```

This will generate a file called `environment.yml` that lists the environment configuration. It can be used to recreate the environment later.

---

## Step 3: Register `geoenv` Environment as a Jupyter Kernel

With the `geoenv` environment activated, register it as a kernel for Jupyter:

```
python -m ipykernel install --user --name=geoenv --display-name "Python (geoenv)"
```

After this, you will see "Python (geoenv)" as an option under **Kernel > Change kernel** in the Jupyter Notebook interface.

---

## Step 4: Activate the Environment (if not already activated)

(Optional)

```
conda activate geoenv
```

---

## Step 5: Open Jupyter Notebook

With the environment activated, launch Jupyter Notebook:

```
jupyter notebook
```

This will open the Jupyter interface in your web browser.

---

## Step 6: Choose the `geoenv` Kernel in Jupyter

In the Jupyter Notebook interface:

1. Open your notebook.  
2. Go to the top menu: **Kernel > Change Kernel**.  
3. Select **Python (geoenv)**.  

Your notebook will now run using the `geoenv` environment.

---

## How to Use This Environment in Your Notebook

To reuse this environment on a different machine or share it with others, follow these steps:

1. Make sure you have the `environment.yml` file in your project directory.  
2. Open Anaconda Prompt and run the following command to create the environment from the file:

```
conda env create -f environment.yml
```

3. Activate the environment:

```
conda activate geoenv
```

4. Register the environment as a Jupyter kernel (if not already registered):

```
python -m ipykernel install --user --name=geoenv --display-name "Python (geoenv)"
```

5. Launch Jupyter Notebook and select the Python (geoenv) kernel.

---

## Useful Links

- Anaconda: https://docs.anaconda.com/  
- Rasterio: https://rasterio.readthedocs.io/  
- GDAL Python Bindings: https://gdal.org/api/python.html  
- Jupyter Notebook: https://jupyter-notebook.readthedocs.io/
