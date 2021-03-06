..
   Copyright 2021 AI Singapore. All rights reserved.

   Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
   the License. You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
   an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
   specific language governing permissions and limitations under the License.


.. image:: imgs/rarity_logo.png
   :width: 200px
   :height: 100px
   :alt: rarity
   :align: center

.. raw:: html

   <p align="center">
      <img alt="Python" src="https://img.shields.io/badge/python-3.6%2B-blue"/>
      <a href="https://pypi.org/project/rarity/" target="_blank" rel="noopener noreferrer">
         <img alt="PyPI" src="https://img.shields.io/badge/pypi-v1.0-orange"/>
      </a>
      <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener noreferrer">
         <img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue"/>
      </a>
      <a href="https://github.com/aimakerspace/Rarity" target="_blank" rel="noopener noreferrer">
         <img alt="GitHub" src="https://img.shields.io/badge/GitHub-%20rarity%20-blueviolet"/>
      </a>
      <a href="https://community.aisingapore.org/groups/mlops-data-and-infra-engineering/" target="_blank" rel="noopener noreferrer">
         <img alt="Community" src="https://img.shields.io/badge/community-AISG%20Forum-brightgreen"/>
      </a>
   </p> 

**Rarity** is a diagnostic library for tabular data with minimal setup to enable deep dive into datasets identifying features 
that could have potentially influenced the model prediction performance. It is meant to be used at post model training phase to ease the understanding on
miss predictions and carry out systematic analysis to identify the gap between actual values versus prediction values. The auto-generated gap analysis 
is presented as a dash web application with flexible parameters at several feature components.

The inputs needed to auto-generate gap analysis report with **Rarity** are solely depending on features, yTrue and yPred values. Rarity is therefore a model anogstic 
package and can be used to inspect miss predictions on tabular data generated by any model framework.


Supported Analysis Type
-----------------------
Rarity currently supports tasks related to

- **Regression**
- **Binary Classifciation**
- **Multiclass Classification**

It can also be used to conduct **bimodal analysis**.
As it is used to inspect miss predictions in details down to the granularity at each data index level, multiple modal analysis won't be ideal for repetition at 
individual data index for each model. Therefore, the package supports upto 2 model miss prediction gap analysis for side-by-side comparison benefiting more during
the post model training and final phase of model fine-tuning stage.


Core Feature Components
-----------------------
There are five core feature components covered in the auto-generated gap analysis report by **Rarity**:

- **General Metrics** : covers general metrics used to evaluate model performance.
- **Miss Predictions** : presents miss predictions scatter plot by index number
- **Loss Clusters** : covers clustering info on offset values (regression) and logloss values (classification)
- **xFeature Distribution** : distribution plots ranked by kl-divergence score
- **Similarities** : tabulated info listing top-n data points based on similarities in features with reference to data index specified by user

**Counter-Factuals** is also included under **Similarities** component tab for classification task to better compare data points with most similar features but show different prediction outcomes. 
For futher details on how the feature components are displayed in the web application, please checkout the examples under section :doc:`Features Introduction </features_introduction>`

.. raw:: html

   <p align="center">
      <video controls width='85%'>
         <source src='_static/rarity-full-demo-reg.mp4' type="video/mp4">
      </video>
   </p>


.. toctree::
   :hidden:
   :caption: Overview

   Installation <installation>
   Quick Start <quick_start>
   Features Introduction <features_introduction>

.. toctree::
   :hidden:
   :caption: Core Components

   Dataloaders <dataloaders>
   Interpreters <interpreters>
   Visualizers <visualizers>
   Features <features>
   Analyzer <analyzer>

.. toctree::
   :hidden:
   :caption: Acknowledgement

   Program <acknowledgement>
