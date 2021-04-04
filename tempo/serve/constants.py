from typing import Dict, List, Optional, Type, Union

SKLEARN_MODEL = "sklearn"
XGBOOST_MODEL = "xgboost"
TENSORFLOW_MODEL = "tensorflow"
PYTORCH_MODEL = "pytorch"
ONNX_MODEL = "onnx"

# PyDantic issue doesn't support raw Tuple : https://github.com/samuelcolvin/pydantic/issues/2132
# ModelDataType = Optional[Union[Type,Tuple,Dict[str,Type]]]
ModelDataType = Optional[Union[Type, List, Dict[str, Type]]]

DefaultModelFilename = "model.pickle"
DefaultRemoteFilename = "remote.pickle"
DefaultEnvFilename = "environment.tar.gz"

# TODO: Update once tempo is published
MLServerEnvDeps = ["mlserver==0.3.1.dev7"]
DefaultCondaFile = "conda.yaml"

ENV_K8S_SERVICE_HOST = "KUBERNETES_SERVICE_HOST"