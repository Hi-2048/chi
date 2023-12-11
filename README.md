# README
# Partiality and Misconception: Investigating Cultural Representativeness in Text-To-Image Models

Text-to-image (T2I) models enable users worldwide to create high-definition and realistic images through text prompts, where the
underrepresentation and potential misinformation of images have raised growing concerns. However, few existing works examine
cultural representativeness, especially involving whether the generated content can fairly and accurately reflect global cultures.
Combining automated and human methods, we investigate this issue in multiple dimensions quantificationally and conduct a set
of evaluations on three prevailing T2I models (DALL-E v2, Stable Diffusion v1.5 and v2.1). Introducing attributes of cultural cluster
and subject, we provide a fresh interdisciplinary perspective to bias analysis. The benchmark dataset UCOGC is presented, which
encompasses authentic images of unique cultural objects from global clusters. Our results reveal that the culture of a disadvantaged
country is prone to be neglected, some specified subjects often present a stereotype or a simple patchwork of elements, and nearly half
of cultural objects are mispresented.

We conduct feature extraction from generated images using prompts specifying cultural subjects and country
names (expanded prompts). By employing these features to categorize images whose prompts have no ·regional
constraints(neutral prompts), we can analyze their distribution by default. Observing these images generated with
neutral prompts, we find that there are problems of uneven diversity and the patchwork of elements, thus they
are further assessed in quantitative manners. To measure whether each specific cultural object can be accurately
portrayed, the Unique Cultural Objects from Global Clusters (UCOGC) dataset is established, serving as a benchmark
to test the similarity between generated images and authentic images namely, fidelity. In the quantitative evaluation
procedure, we particularly note the problems that previous works investigating T2I models exist, where the metrics are
inconsistent with human perceptions and lack of interpretation and the human evaluation is unreliable
and unrepeatable, thus devising a hybrid machine-human evaluation methodology to ensure the reliability of our
results.

In this work, we propose a set of quantitative methods to scrutinize whether the generated content can fairly and
accurately reflect global cultures. The complete experimental procedure and methodology are illustrated in Figure 1.
Given the multidimensional nature of culture, our study is closely aligned with previous global cross-cultural studies.
We select three countries as representatives from each of the ten cultural clusters defined in the previous GLOBE study
and nine cultural subjects, including both material and non-material culture. By using three prevailing T2I models:
DALL-E v2, Stable Diffusion v1.5 and v2.1, a large number of images are generated for cultural representativeness
analysis by inputting three types of prompts, neutral, extended, and cultural object prompts.

The contributions of our research can be summarized as follows:
(1) Introducing Attributes of cultural clusters and subjects for analyzing cultural representativeness, providing a
fresh perspective and interdisciplinary approach to multimodal bias analysis in cultural representativeness.
(2) Analyzing 193,800 generated images and 37,600 authentic images, our research uncovers representativeness
biases of global cultures in T2I models systematically and robustly, including distribution, diversity, patchwork,
and fidelity. To our knowledge, this is the first comprehensive work to examine the performance of T2I models
on cultural representativeness.
(3) The UCOGC dataset, proposed by us, encompasses diverse cultural subjects from 30 countries, gathering
authentic images that align with the respective cultural objects. Not only does it provide a standard for
appraising all T2I models, but it can also be used to train other visual models to accurately perceive and
articulate cultural objects worldwide.
 
All of the generated images we investigated and completed for UCOGC are available there.

Hope to help you!


