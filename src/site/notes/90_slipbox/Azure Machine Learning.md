---
{"dg-publish":true,"permalink":"/90-slipbox/azure-machine-learning/","tags":["notes"]}
---


Azure Machine Learning is a cloud-based platform for creating, managing, and publishing machine learning models. It has the following capability:

- Automated machine learning - This feature enables non experts to quickly create an effective machine learning model from data.
- Azure Machine Learning Designer - A graphical interface enabling no-code development of machine learning solutions.
- Data and compute management - Cloud-based data storage and compute resources that professional data scientists can use to run data experiment code at scale
- Pipelines - Data scientists, software engineers, and IT operations professionals can define pipelines to orchestrate model training, deployment, and management tasks.

## Automated ML

Automated Machine Learning automatically tries multiple pre-processing techniques and model-training algorithms in parallel. Automated machine learning allows you to train models without extensive data science or programming knowledge. For people with a data science or programming background. it provides a way to save time and resources by automating algorithm selection and hyperparameter tuning.

In Azure Machine Learning, operations that you run are called *jobs*. The job configuration provides the information needed to specify your training script, compute target, and Azure ML environment in your run configuration and run a training job.

## Azure Machine Learning Studio

Azure Machine Learning Studio is a web portal for machine learning solutions in Azure. It includes a wide range of features and capabilities that help data scientists prepare data, train models, publish predictive services, and monitor their usage.

AMLS is used to manage the compute used by Azure Machine Learning, to which there are 4 kinds of compute you can create.

**Compute Instances**: Development workstations that data scientists can use to work with data and models.  
**Compute Clusters**: Scalable clusters of virtual machines for on-demand processing of experiment code.  
**Inference Clusters**: Deployment targets for predictive services that use your trained models.  
**Attached Compute**: Links to existing Azure compute resources, such as Virtual Machines or Azure Databricks clusters.
