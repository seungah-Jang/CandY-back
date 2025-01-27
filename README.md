# Team HoT - CandY (Concentration and You !)

## Project Title

**Establishing the Correlation Between Bio-Data and Concentration Levels Utilizing EEG Data**

## Project Period
 Sep/20/2023 ~ Dec/20/2023 

## Project Content
1. [Team Members](#collaborator)
2. [Project Overview](#project-overview) 
3. [Research problem statements](#research-problem-statements)
4. [Research novelty](#research-novelty)
5. [Environment Setting](#environment-setting)
6. [Experiment](#experiment)
   <!--   - [File Structure](#file-structure)
    - [Dataset](#dataset)
    - [Requirments](#requirments) -->
   <!--
    - [Result](#result)     
    - [Model Architecture](#mode-architecture) -->

## Team Members

| Name         | University               | Department                                   | Email               | Git                        |
| :------------- | :------------------------: | :--------------------------------------------: | :-------------------: | :------------------------------: |
| Seojeong Park    | Hallym University        | Computer Science                    | diditjwjd@gmail.com | https://github.com/seojeongP     |
| Seungah Jang  | Jeju National University        | Computer Science and Statistics                    | wkdtmddk6733@gmail.com   | https://github.com/seungah-Jang     |
| Jeongmin Seo | Kyunghee University     | Software Convergence               | balljm@naver.com | https://github.com/jeongmin1217       |
| Yunhui Lim | Kyunghee University     | Computer Science and Engineering                | lyhhh0320@gmail.com   | https://github.com/YunheeLim    |
| Byeongsoo Min  | Kyunghee University | Computer Science and Engineering       | qud9783@gmail.com   | https://github.com/Byeongsoo-Min  |
| Martin Kim | Purdue University        | Computer and Information Technology | 19alswprla@gmail.com    | https://github.com/19alswprla |

## Research Problem Statements 

Modern day society has bore witness to a phenomenon of diminished concentration levels and attention spans as a result of dependency and increased usage of smart phones. The usage rate of smartphones is more than 70% of adults in the United States and nearly 50% of adults worldwide. The decline in cognitive ability in daily life due to the increase in smartphone use can be observed. Therefore, the need for methods to facilitate and assist users in maintaining high levels of concentration in their daily lives has increased significantly.

## Research Novelty 
1. This study adopted a wearable device in daily life to measure the concentration level instead of using a specialized EEG sensor.<br>
2. This study set the experimental background as a everyday life.<br>
3. Extracted brainwaves were used as a direct indicator of concentration without Fourier transform.<br>
4. A quantified figure was utilized to analyze a concentration score instead of subjective self-assessment.<br>
5. The correlation between bio-data and concentration is provided with importance and proportionality.

## Project Overview
<p align="center">
<img width="1000" alt="architecture" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/9032607c-dc88-4661-8c5c-600f3c55e6b4">   
</p>

>### Machine Learning Process
<p align="center">
<img width="700" alt="architecture" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/dd04f249-a38f-4e9f-88ce-a8f5615ad139">   
</p>

>### Service Architecture
<p align="center">
<img width="500" alt="architecture" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/940893d5-319f-4e06-b7a2-1deb2c91f46e">   
</p>
   
## Environment Setting
>### Machine Learning
1. Go to https://www.python.org/downloads/ and install Python version 3.11
2. Install packages
```bash
pip install numpy pandas matplotlib shap lime xgboost 
```
3. Set the environment variables for each OS
4. git clone
5. Open Jupyter Lab or Colab
7. Set the dataset path like File Structure
8. Run the code

>### Service
1. Go to https://nodejs.org/en and download Node.js
2. Download the Expo Go app on your phone in App Store or Google Play Store.
3. Follow the command below in your bash.
```bash
npm install --g expo-cli
```
```bash
git clone https://github.com/KSW-IITP/f23-healthcare-of-things.git
```
```bash
cd code/fontend
```
```bash
npm start
```
4. Scan the QR code that can be shown in the console with your phone.
<p align="center">
<img width="200" alt="app_screen1" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/7922116d-d626-4ee6-8557-abb10b9c63b6"> 
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img width="200" alt="app_screen2" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/435d4f48-ec10-4fb7-82b8-cb929072e45b">
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img width="200" alt="app_screen3" src="https://github.com/Healthcare-of-Things/CandY-front/assets/92131041/dfa05cae-f907-47e8-950d-d0d672b6820d">    
</p>

#### Requirements
```
- npm version 8.1.0
- expo-cli version 6.3.10
- Python version 3.11.5
```

## File Structure
    📦2023-ksw-fall-program-final-team-hot/
     └📂data
      └📜1_Real_Original.csv
      └📜2_Augmentation.csv
      └📜3_Removing_errors.csv
      └📜4_Feature_Engineering.csv
      └📜4+5_Feature_Scaling.csv
      └📜4+5_Feature_Scaling+6_Imputation.csv
      └📜4+6_Imputation.csv
      └📜4+6_Imputation+5_Feature_Scaling(final_dataset).csv
     └📂presentation
      └📜mid_presentation.pptx
      └📜final_presentation.pptx
      └📜demo.mp4
     └📂paper
      └📜paper.pdf
     └📂code
       └📂Machine_Learning
        └📜Dataset_selection_Model_selection.ipynb
        └📜Model_Optimization.ipynb
        └📜Model_Training_Result_Analysis.ipynb
       └📂frontend
         └📂assets
         └📂components
           └📜CircleProgress.js
           └📜CircularProgress.js
         └📂screens
           └📂Home
             └📜Bluetooth.js
             └📜Home.js
           └📂Main
             └📜Main.js
           └📂OnBoarding
             └📜LaunchScreen.js
             └📜SignInScreen.js
             └📜SignUpScreen.js
           └📂Profile
             └📜Profile.js
           └📂Recommendation
             └📜Recommendation.js
           └📂Record
             └📜Record.js
           └📂Statistics
             └📜DailyStatistics.js
             └📜SessionStatistics.js
             └📜Statistics.js
         └📜App.js
         └📜package.json
       └📂backend
         └📂CandY_Server
           └📜views.py
         └📂models
     └📜README.md
     └ ...
       

## Experiment
>### Dataset
The pre-processed dataset is in data folder. You can see the raw dataset in this link: https://drive.google.com/drive/folders/1i6HLH5zdqJvw2UVocrSX6AfheRVAwdkn?usp=sharing

>### Result

>#### 5-Fold Cross-Validation

|   |R2|RMSE|MAE|
|---|:-:|:-:|:-:
|**Extra Tree Regressor**|0.8600|0.0902|0.0609|
|**Optimized ETR**|0.8610|0.0899|0.0608|
|**RandomForest Regressor**|0.8286|0.0998|0.0680|
|**Optimized RFR**|0.8316|0.0989|0.0674|
|**XGBoost Regressor**|0.7979|0.1084|0.0780|
|**Optimized XGBR**|0.8270|0.1003|0.0701|

>#### 10-Fold Cross-Validation
>
|   |R2|RMSE|MAE|
|---|:-:|:-:|:-:
|**Extra Tree Regressor**|0.8745|0.0854|0.0579|
|**Optimized ETR**|<span style="color:red">0.8763</span>|0.0848|0.0576|
|**RandomForest Regressor**|0.8430|0.0955|0.0652|
|**Optimized RFR**|0.8444|0.0951|0.0649|
|**XGBoost Regressor**|0.7993|0.1084|0.0774|
|**Optimized XGBR**|0.8314|0.0990|0.0689|
