# Review of Artificial Intelligence in Brain Tumor Radiogenomic Classification

Jiawei Zhao  
zhaojw@bu.edu  
Department of Electrical and Computer Engineering, College of Engineering, Boston University, Boston, MA, US

Glioblastoma, known as a malignant tumor in the brain, is a common cancer with median survival being less than a year. People found that a specific genetic sequence, MGMT promoter methylation, is a favorable prognostic factor of brain tumor. If the genetics of cancer can be predicted through imaging (i.e., MRI, magnetic resonance imaging), it will minimize the number of surgeries, refine the type of therapy and improve the survival of patients. Recently, artificial intelligence has great potential applications in the field of medical imaging analysis, which not only can provide accurate treatment plans in brain cancer, but also optimize the existing medical resources in other medical fields.  
Keywords: Brain cancer, artificial intelligence, neural network, transfer learning

### INTRODUCTION
A brain tumor is growth of abnormal cells in human brain, such as glioblastoma. It is an aggressive type of cancer that can be very difficult to cure. In order to classify the genetic characterization of tumor, patients require surgery to extract a tissue sample which can take several weeks. It can reduce the life quality and survival rate and time. Nowadays, imaging tests can help doctors determine the size and location of patients’ brain tumor. MRI (magnetic resonance imaging) and some other imaging tests are often used to diagnose brain tumors(Iv et al., 2018). 

Some of the studies proved that a combination of traditional artificial intelligence can assist to classification accurately of benign and malignant tumors in images. However, the accuracy of classification needs to be improved. Other reports show that convolutional neural network is also capable of abstract features. But it requires sufficient high-quality medical images for hyper-parameter optimization which is infeasible currently(Greenspan et al., 2016). Deep learning with transferred high-level features can solve this problem, making precise diagnosis possible and medical resource be full use of.

### REVIEW

In order to improve diagnosis and treatment planning for patients with cancer, artificial intelligence-assisted diagnosis model was paid more attention these years. This kind of models consist of two parts, feature extraction and machine classification. The most common classifiers conclude Support Vector Machines, Naive Bayesian, Decision Tree and Random Forest. Moura et al. evaluated the performance of SVM in breast classification based on 12 features (Moura and Guevara López, 2013). Convolutional Neural Network (CNN) is also applied in tumor classification.

CNN is a kind of digitally driven self-supervision model and consists of an input layer, hidden layers and an output layer. It currently inspired by using in biological processes. In order to classify instances accurately, deep convolutional neural network need sufficient data sample to optimize millions of parameters(Greenspan et al., 2016).

Except for receiving more imaging instances, transfer learning (TL) can also assist improving performance of AI diagnosis(Valverde et al., 2021). TL stores knowledge while solving one problem and applies it to another related field(Day and Khoshgoftaar, 2017). For instance, a model trained for brain extraction could also be used in recognizing tumor segmentation. A literature search showed that, a majority of articles applied CNNs (Convolutional neural networks) and transfer learning to MR brain imaging tasks (Figure 1) (Valverde et al., 2021).  

<img src="https://github.com/zhaojiawei86/ec601/blob/main/Project1/Figure1.png" width = "450" height = "350"/>

Figure 1. Number of articles applied transfer learning to MR brain imaging task based on Machine Learning (Valverde et al., 2021)


Among these articles, some researchers had applied transfer learning strategies to brain imaging. Moradi et al. demonstrates the method by predicting the symptom severity in ASD based on MRI (Moradi et al., 2017). This method comes from another surveyed feature-based strategies that sought a single domain-invariant feature space for all the available input features (Moradi et al., 2017).

Aside from the suitable strategies, people should also pay attention to the collection of features, image pretreatment, model training and parameters adjustment as well as the valuation of prediction performance. In general, brain tumor classification based on CNN and transfer learning require appropriate professional background and sufficient time to create and improve.

### CONCLUSION

As mentioned above, this review shows that researchers considered Machine Learning, such as deep learning, and Transfer Learning as useful approaches to solve cancer classification problems in recent years. CNNs are the most popular machine learning method utilized in brain MRI. Also, the growing number of transfer learning approaches for limited training data signals the importance of this field.

This review aims to introduce the possibilities on recognizing brain tumor based on brain MRI in researches. No attempt will be made to show the preference of specific solution. Additionally, due to the limited knowledge, this review does not supply more detailed strategy, the comparison among different approaches as well as applications, which should be discussed in the future.

### REFERENCES

DAY, O. & KHOSHGOFTAAR, T. M. 2017. A survey on heterogeneous transfer learning. Journal of Big Data, 4, 29.  

GREENSPAN, H., GINNEKEN, B. V. & SUMMERS, R. M. 2016. Guest Editorial Deep Learning in Medical Imaging: Overview and Future Promise of an Exciting New Technique. IEEE Transactions on Medical Imaging, 35, 1153-1159.  

IV, M., YOON, B. C., HEIT, J. J., FISCHBEIN, N. & WINTERMARK, M. 2018. Current Clinical State of Advanced Magnetic Resonance Imaging for Brain Tumor Diagnosis and Follow Up. Semin Roentgenol, 53, 45-61.  

MORADI, E., KHUNDRAKPAM, B., LEWIS, J. D., EVANS, A. C. & TOHKA, J. 2017. Predicting symptom severity in autism spectrum disorder based on cortical thickness measures in agglomerative data. NeuroImage, 144, 128-141.  

MOURA, D. C. & GUEVARA LÓPEZ, M. A. 2013. An evaluation of image descriptors combined with clinical data for breast cancer diagnosis. International Journal of Computer Assisted Radiology and Surgery, 8, 561-574.  

VALVERDE, J. M., IMANI, V., ABDOLLAHZADEH, A., DE FEO, R., PRAKASH, M., CISZEK, R. & TOHKA, J. 2021. Transfer Learning in Magnetic Resonance Brain Imaging: A Systematic Review. J Imaging, 7.  
