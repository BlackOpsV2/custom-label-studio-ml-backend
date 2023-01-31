## Overview 
This is the Label Studio ML Backend for Custom Model Deployed at Url . 

## Quickstart

Build and start Machine Learning backend on `http://localhost:9090`

```bash
docker-compose up
```

Check if it works:

```bash
$ curl http://localhost:9090/health
{"status":"UP"}
```

## Then connect running backend to Label Studio:

### How it works

1. Get your model code
2. Wrap it with the Label Studio SDK
3. Create a running server script
4. Launch the script
5. Connect Label Studio to ML backend on the UI


0. Clone the repo
   ```bash
   git clone https://github.com/heartexlabs/label-studio-ml-backend  
   ```
   
1. Setup environment
    
    It is highly recommended to use `venv`, `virtualenv` or `conda` python environments. You can use the same environment as Label Studio does. [Read more](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) about creating virtual environments via `venv`.
   ```bash
   cd label-studio-ml-backend
   
   # Install label-studio-ml and its dependencies
   pip install -U -e .
   
   # Install example dependencies
   pip install -r label_studio_ml/examples/requirements.txt
   ```
2. Copy above repo to `label_studio_ml/examples/`

3. Initialize an ML backend based on an example script:
   ```bash
   label-studio-ml init my_ml_backend --script label_studio_ml/examples/custom-label-studio-ml-backend/custom_image_classifier.py
   ```
   This ML backend is an example provided by Label Studio. See [how to create your own ML backend](#create-your-own-ml-backend).

4. Start ML backend server
   ```bash
   label-studio-ml start my_ml_backend
   ```
   
5. Start Label Studio and connect it to the running ML backend on the project settings page.


```bash
label-studio start --init new_project --ml-backends http://localhost:9090 --template image_classification
```

## License

This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.com/). 2022

<img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
