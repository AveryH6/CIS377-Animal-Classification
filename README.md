<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<h3 align="center">Animal Species Predictor</h3>

  <p align="center">
    This project involves the implementation of three different CNN models for animal classification. The goal is to determine which model performs best at predicting the animal type based on an image, using a dataset obtained from Kaggle for training and validation. In addition to testing various models, we also explore the use of image augmentation to assess its impact on the results.
    <br />
    <a href="https://github.com/kayleeodom/CIS377-Animal-Classification">
    <br />
    <br />
<!--     <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#model">Model</a></li>
    <li><a href="#evaluation">Evaluation</a></li>
    <li><a href="#Results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* Visual Studio

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AveryH6/CIS377-Animal-Classification.git
   cd CIS377-Animal-Classification
   ```
2. Set up a Python Virtual Environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install Dependencies
   ```js
     pip install -r requirements.txt
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin AveryH6/CIS377-Animal-Classification
   git remote -v # confirm the changes
   ```

Dependencies
* scikit-learn
* seaborn
* matplotlib
* numpy
* transformer
* pandas
* Python 3.10+
* tensorflow

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usuage
### Running the Model
<p>This section describes how to train, evaluate, or use the model.</p> <p>Each model can be run from its respective Jupyter notebook. You can use the Jupyter Extension in VS Code to run and manage notebooks directly within the editor.</p> <p>There is a folder titled `keras` which contains a notebook for each model, where it trains and evaluates on the dataset without any image augmentation. The "image augmentation" folder contains a notebook for each model, where it trains and evaluates its metrics on the dataset with image augmentation.</p>

1. Install the Jupyter Extension
   Go to the Extensions view
   Search for "Jupyter" and install the extension
3. Open a notebook
   Open any .ipynb file in the editor, and the Jupyter environment will load automatically
4. Run Cells within VS Code
   You can execute notebook cells directly in the editor using the "Run Cell" button or keyboard shortcuts
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Data -->
## Dataset

The dataset used for training and validation checks of the model is available in csv/raw-img.

<p>The dataset used in this project is Animals-10, an image dataset that consists of about 28k medium quality animal images. They are separated into folders, one for each category, with an image count varying from 2k to 5k units. There are different categories: dog, horse, spider, elephant, butterfly, chicken, cat, cow, sheep, and squirrel. These images have been collected from "google images" and checked by humans. The dataset was initially collected in Italian and includes a translation file. </p>

Load the dataset: Run this file
   ```sh
   python animal-classification.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Model -->
## Model

<p>For this project, our main focus was not on improving one model to classify the species, but rather on determining which CNN (image classification) model was the most effective. All three models used in this project are Convolutional Neural Networks pre-trained on the ImageNet dataset. The three models we focused on were VGG-16, ResNet50, and InceptionV3, all of which were loaded using the Keras API. Keras is a Python-based, open-source API for deep learning that is used to create and test neural networks. Each model is housed in its own Jupyter notebook, where it was trained and evaluated on the Animal-10 dataset. After training the model, we display the training and validation metrics in a line graph. We then run a test to evaluate the model’s performance across different classes in the validation dataset and display the results using a confusion matrix.</p>

Train: Refer to the usuage section

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Evaluation -->
## Evaluation

<p>The model's performance was evaluated using accuracy, precision, loss, and recall metrics. To determine which model performed the best, we tried to maintain consistency. One such measure was the number of epochs the models were trained for. To save time while allowing sufficient training, we settled on 5 epochs.

In the Keras Final folder, you can see the models evaluated on the dataset without any adjustments. In the Image Augmentation folder, the models were evaluated on a dataset that included some image augmentation.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Results -->
## Results
![inception-keras-graph](https://github.com/user-attachments/assets/d3a85c7b-7f59-4866-b048-8ae64c4bf1b7)


<h2>Keras Folder Results</h2>
<h3>Training and Validation Metric Graphs /h3>
  
![inception-keras-graph](https://github.com/user-attachments/assets/d3a85c7b-7f59-4866-b048-8ae64c4bf1b7)
![resnet-keras-graph](https://github.com/user-attachments/assets/cbb2629a-84ce-4826-b6a0-6be4cc987da8)
![vgg-keras-graph](https://github.com/user-attachments/assets/cc5a8478-ad16-4df0-b1bc-33e918dad6ba)

<h3>Confusion Matrix</h3>

![inception-confusion](https://github.com/user-attachments/assets/bb5a1ca2-236d-4b85-9b2e-e815ec9ba9c0)
![resnet-confusion](https://github.com/user-attachments/assets/857e0eec-1260-4636-b42a-c9d005ffc0eb)
![vgg-confusion](https://github.com/user-attachments/assets/a3088c03-290e-49f2-afa4-946a37b7274e)


<h2>Image-Augmentation Folder Results</h2>
<h3>Training and Validation Metric Graphs</h3>

![inception-ig-graph](https://github.com/user-attachments/assets/5fa35d70-ee05-4926-b5e1-d45572daf3ac)
![resnet-ia-graph](https://github.com/user-attachments/assets/6859a2fd-7af2-4f95-ba9d-305337f4e97f)
![vgg-ia-graph](https://github.com/user-attachments/assets/c55a2137-09ea-4801-83a2-94ca7ef43348)

<h3>Confusion Matrix</h3>

![inception-ia-confusion](https://github.com/user-attachments/assets/516e2b98-5d71-482d-b564-6dd619762dd0)
![resnet-ia-confusion](https://github.com/user-attachments/assets/2accdbd6-6d94-4470-9406-067773a88b35)
![vgg-ia-confusion](https://github.com/user-attachments/assets/c20af165-a64a-4b61-b1df-560ddf87ef03)

<pBy examining these graphs, we can get an idea of which model was the most effective at classifying the animals in this dataset. In addition to looking at the graphs, after you train each model, you will see the loss, accuracy, and precision of each epoch.

After examining the results in just the Keras folder (no image augmentation), we see that the InceptionV3 model performed the best and the ResNet model performed the worst. You can also see a similar outcome in the image-augmentation folder. I think this outcome is due to the architectural and design differences between the models and the type of dataset it's being used for.p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
