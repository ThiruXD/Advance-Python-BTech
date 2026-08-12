# 📚 Advanced Python (5th sem - BTech)

This repository serves as a centralized hub for university study notes, core curriculum breakdowns, and hands-on laboratory code implementations for the course **Advanced Python (Course Code: 10ABTCE24513)**.

---

## 🔍 Course Overview
The primary objective of this course is to develop proficient skills in foundational Computer Vision, Image/Video Manipulation using OpenCV, advanced Python backend scripting, and data analytics/visualization.

### 🎯 Expected Course Outcomes (COs)
* **CO1**: Explain the fundamentals of Computer Vision, OpenCV, image representation, and processing techniques.
* **CO2**: Demonstrate real-time video processing including video capture, object tracking, and motion detection.
* **CO3**: Apply modules, file handling, JSON data serialization, regex pattern matching, and exceptions.
* **CO4**: Analyze and visualize structured data via NumPy, Pandas, Matplotlib, and web scraping tools.

---

---

## 📂 Repository File Tree

```text
.
├── module-1/                          # Unit I: Computer Vision Foundations
│   ├── asset/
│   │   └── iwmages.jpg                # Sample asset image
│   ├── cv2_modules_1.py
│   ├── cv2_modules_2.py
│   ├── display_img.py
│   ├── flip_img.py
│   ├── geometrical_shapes.py
│   ├── image_properties.py
│   └── img_on_panel.py
├── module-2/                          # Unit II: Video Processing Implementations
│   ├── VidOutput/                     # Generated frame outputs
│   ├── capture_cam_vid_geo.py
│   ├── capture_cam_vid.py
│   ├── sample_vid.mp4                 # Sample test footage
│   ├── vid_capture.py
│   └── vid_processing.py
├── module-3/                          # Unit III: Python Modules & Systems
│   ├── db/
│   │   └── students.json              # Local JSON database storage
│   ├── modules/                       # Custom imported modular logic
│   │   ├── basic_var.py
│   │   ├── calc.py
│   │   ├── json.py
│   │   └── qroot.py
│   ├── main.py
│   └── temp.py
├── module-4/                          # Unit IV: Data Science (Coming Soon)
│   └── comming-soon.txt
├── README.md                          # Main project documentation
└── requirements.txt                   # Project dependency manifest
```

---


## 🗂️ Course Syllabus Breakdown

### 🔹 [Unit I: Introduction to Computer Vision and Video Processing](./module-1)
* **Foundations**: Overview, features, capabilities, and applications of the OpenCV Library.
* **Image Representation**: Pixels, resolution, color space models, and internal layout properties.
* **Operations**: Reading, displaying, writing, manipulating, and cropping static images.
* **Core Scripts**:
  * `display_img.py` / `img_on_panel.py` — Methods to open and project windows.
  * `image_properties.py` — Extracts color space dimensions, array types, and pixel counts.
  * `flip_img.py` — Simple spatial matrix axis rotation flips.
  * `geometrical_shapes.py` — Superimposing matrix bounding zones onto static canvasses.


### 🔹 [Unit II: Video Processing using OpenCV](./module-2)
* **Video Handling**: Working with video formats, extracting frames, reading file paths, and camera streaming.
* **Overlays**: Drawing dynamic elements (lines, rectangles, circles) and embedding text overlays with date/time stamps.
* **Analytics**: Configuring custom video properties, real-time object tracking, and frame-differencing motion detection.
* **Core Scripts**:
  * `vid_capture.py` / `capture_cam_vid.py` — Camera hardware interface controllers.
  * `capture_cam_vid_geo.py` — Overlays annotations onto continuous streaming frames.
  * `vid_processing.py` — Framework processing routines mapping to sequential files inside `/VidOutput`.


### 🔹 [Unit III: Python Modules and File Handling](./module-3)
* **Modular Code**: Creating, naming/renaming, variables scoping, and importing components using `dir()`.
* **Data Interchange**: Parsing, converting, and serializing unstructured structured JSON strings.
* **Text & Reliability**: Complex string pattern analysis with Regular Expressions (RegEx) and Exception Handling patterns.
* **Core Scripts**:
  * `main.py` — Execution orchestrator file calling localized scripts.

### 🔹 [Unit IV: Pandas, NumPy, and Matplotlib](./module-4)
* **Status**: ⏳ *Coming Soon (Tracked inside `comming-soon.txt`)*
* **Topics**: Matrix algebra manipulation via NumPy arrays, building analytical Pandas dataframes, web text extraction, and generating performance visualization charts using Matplotlib.

* **Data Wrangling**: Multi-dimensional NumPy array layout (`ndarray`), indexing structures, splitting, and filtering.
* **Structured Records**: Constructing Pandas Series/DataFrames, appending streams, and parsing standard CSV datasets.
* **Visualization & Collection**: Live automated Web Scraping and plotting performance metrics with Matplotlib charts.

---


## 💻 Environment Setup

### 1. Repository Setup
```bash
git clone https://github.com/ThiruXD/Advance-Python-BTech.git
cd Advance-Python-BTech
```

### 2. Dependency Installation
Initialize your software environment by fetching the standard package modules using `pip`:
```bash
pip install -r requirements.txt
```

---

## 👥 Credits & Contributors

Acknowledgment to the core student contributor who compiled, structured, and implemented these course resources:

* **Thiruselvan (ThiruXD)**
  * 🌐 GitHub: [@ThiruXD](https://github.com/ThiruXD)
  * 🎓 Course: Advanced Python (10ABTCE24513)

---

## 📚 Reference Materials

### Core Text Books
* *Learning OpenCV 4: Computer Vision with Python* — Gary Bradski & Adrian Kaehler
* *OpenCV 4 for Secret Agents* — Joseph Howse et al.
* *Automate the Boring Stuff with Python (2nd Edition)* — Al Sweigart
* *Python for Data Analysis (3rd Edition)* — Wes McKinney

### Documentation Web Portals
* [OpenCV Docs](https://opencv.org) | [Python Manuals](https://python.org) | [NumPy Guide](https://numpy.org) | [Pandas API](https://pydata.org)


