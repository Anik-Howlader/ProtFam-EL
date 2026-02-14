<table width="100%">
 <tr>

<h1 style="margin-bottom: 10px;" >ProtFam-EL</h1>

<p style="margin-top: 0;">
Protein Functional Family Classification using Ensemble Machine Learning
</p>
<td width="25%" valign="top" align="right">
     <img src="ProtFam_EL.png" width="160" alt="ProtFam-EL Logo">
</td>

 <table>
  <tr>
    <td><b>Dataset</b></td>
    <td>:</td>
    <td>Kaggle Bioinformatics Protein Dataset (Simulated)</td>
  </tr>
  <tr>
    <td><b>Link</b></td>
    <td>:</td>
    <td>
      <a href="https://www.kaggle.com/datasets/gallo33henrique/bioinformatics-protein-dataset-simulated/data">
        View Dataset
      </a>
    </td>
  </tr>
  <tr>
    <td><b>Target</b></td>
    <td>:</td>
    <td>Achieve &gt;80% classification accuracy with interactive web application</td>
  </tr>
 </table>
 </td>



<p style="margin-bottom: 10px;"><i>---Organized as follows:</i></p>

```text
ProtFam-EL/
├── data/
│   ├── raw/                           # Original dataset
│   └── processed/                     # Cleaned and processed data
├── notebooks/
│   ├── 01_EDA_Analysis.ipynb          # Week 1: Exploratory Data Analysis
│   ├── 02_Feature_Selection.ipynb     # Week 2: Feature Engineering
│   ├── 03_Model_Training.ipynb        # Week 2: Model Development
│   └── 04_Model_Evaluation.ipynb      # Week 2: Performance Analysis
├── models/                            # Trained model files
├── app/                               # Streamlit web application
│   ├── app.py                         # Main app file
│   └── pages/                         # Multi-page components
├── src/                               # Source code modules
├── reports/
│   └── figures/                       # Generated visualizations
└── README.md
```

<p style="margin-bottom: 10px;"><i>---What the EDA Will Show You</i></p>

<small><table>
  <thead>
    <tr>
      <th>EDA Section</th>
      <th>What It Will Show</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Dataset Overview</strong></td>
      <td>
        Number of samples and features, Data types and missing values, Basic statistics
      </td>
    </tr>
    <tr>
      <td><strong>Protein Family Analysis</strong></td>
      <td>
        Distribution of protein classes, Class imbalance assessment, Family characteristics
      </td>
    </tr>
    <tr>
      <td><strong>Feature Analysis</strong></td>
      <td>
        Feature distributions, Correlation patterns, Outlier detection, Zero-variance features
      </td>
    </tr>
    <tr>
      <td><strong>Data Quality Report</strong></td>
      <td>
        Missing data summary, Duplicate detection, Recommendations for preprocessing
      </td>
    </tr>
  </tbody>
</table></small>


