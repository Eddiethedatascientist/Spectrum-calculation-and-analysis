# Spectrum-signal-analysis-toolkit
<img width="520" height="639" alt="5" src="https://github.com/user-attachments/assets/a0352ac8-0a0e-49b1-a2bc-db015d511a4e" />

A Python application for processing, analyzing, and visualizing spectrum measurement data collected from multiple measurement files. The application provides an interactive graphical interface for loading measurement datasets, performing spectrum processing, reducing measurement noise, calculating peak areas, and exporting the resulting figures.

---

# Project Overview

This project was developed as part of the **Elementary Programming** course at the **University of Oulu**.

The objective of the project is to automate the complete workflow of spectrum data analysis, from raw measurement files to processed visualization.

The application processes a folder containing **20 measurement files** (`measurement*.txt`). Each measurement file contains **500 rows**, where every row consists of two floating-point values:

| Column | Description |
|---------|-------------|
| Column 1 | Energy value |
| Column 2 | Measured intensity (deviation) |
<img width="517" height="640" alt="3" src="https://github.com/user-attachments/assets/6d45f176-81a4-46e2-90a5-d6542da766b4" />

The energy values remain identical across all measurement files, while the intensity values differ between measurements.

After loading the dataset, the application performs data validation, extracts the measurement values, generates the original spectrum, applies noise reduction, calculates the peak area using **NumPy's trapezoidal numerical integration**, and saves the processed spectrum as image files.

---

# Features

- Interactive GUI built with Tkinter
- Automatic loading of multiple measurement files
- Validation of measurement data
- Extraction of energy and intensity values
- Visualization of the original spectrum
- Noise reduction for smoother spectrum analysis
- Numerical peak area calculation using `numpy.trapezoid()`
- Automatic export of generated figures
- Modular project structure separating GUI and data processing

---

# Processing Pipeline

<img width="1536" height="1024" alt="13f26701-b1e9-4c24-992f-33d675912312" src="https://github.com/user-attachments/assets/79ce1ac3-e6f6-421a-91eb-058fde8dfbc6" />


The processing workflow consists of the following stages:

1. Select the measurement folder.
2. Read all measurement files.
3. Validate the input data.
4. Extract energy and intensity values.
5. Generate the original spectrum.
6. Apply noise reduction.
7. Generate the processed spectrum.
8. Calculate the spectrum peak area using `numpy.trapezoid()`.
9. Save the processed figures as image files.

---

# Project Structure

```text
Spectrum-Data-Processing/
│
├── main.py                 # Program entry point
├── guilib.py               # Graphical User Interface
├── data_processing.py      # Data processing functions
├── README.md
├── requirements.txt
│
├── measurement/
│   ├── measurement01.txt
│   ├── measurement02.txt
│   ├── ...
│   └── measurement20.txt
│
└── images/
    ├── workflow.png
    ├── gui.png
    ├── original_spectrum.png
    └── processed_spectrum.png
```

---

# Technologies Used

- Python
- Tkinter
- NumPy
- Matplotlib
- File I/O
- Modular Programming

---

# Learning Outcomes

This project strengthened practical experience in:

- Scientific data processing
- Data visualization
- Numerical analysis
- File parsing and validation
- GUI development with Tkinter
- Modular software architecture
- Exception handling
- Scientific computing using NumPy
<img width="600" height="500" alt="f1" src="https://github.com/user-attachments/assets/8ba7b133-2d92-4ad9-b5b0-1f3a48259ecc" />

---

# Future Improvements

Potential future enhancements include:

- Automatic peak detection
- Baseline correction
- Multiple noise filtering algorithms
- Interactive spectrum exploration
- CSV export of processed data
- Support for additional measurement formats

---

# Author

**Eddie Nguyen**

Bachelor's Programme in Computer Science and Engineering

University of Oulu
