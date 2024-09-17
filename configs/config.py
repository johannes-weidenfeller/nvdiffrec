import torch
import json
import os

import torch
import json
import os

import json

class Config:
    def to_dict(self):
        """Recursively convert all attributes to a dictionary, including lists of Configs."""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Config):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [v.to_dict() if isinstance(v, Config) else v for v in value]
            else:
                result[key] = value
        return result

    def update_from_dict(self, update_dict):
        """Recursively update the config from a dictionary, including lists of Configs."""
        for key, value in update_dict.items():
            if hasattr(self, key):
                current_value = getattr(self, key)
                if isinstance(current_value, Config) and isinstance(value, dict):
                    current_value.update_from_dict(value)
                elif isinstance(current_value, list) and isinstance(value, list):
                    # Update list elements if they are Config instances
                    for i, (cur_item, new_item) in enumerate(zip(current_value, value)):
                        if isinstance(cur_item, Config) and isinstance(new_item, dict):
                            cur_item.update_from_dict(new_item)
                        else:
                            current_value[i] = new_item
                else:
                    setattr(self, key, value)

    @classmethod
    def from_json(cls, json_file):
        """Create an instance of the config class, updating defaults from a JSON file."""
        with open(json_file, 'r') as f:
            data = json.load(f)

        instance = cls()
        instance.update_from_dict(data)
        return instance
class GPUConfig(Config):
    def __init__(self):
        self.local_rank = 0
        self.multi_gpu = False

class RenderConfig:
    def __init__(self):
        self.background = "checker"
        self.spp = 1
        self.display_res = [512, 512]

class LoggingConfig(Config):
    def __init__(self):
        self.log_interval = 100
        self.log_dir = 'logs'
        self.save_interval = 100
        self.display_interval = 0
        self.display = [{"latlong" : True}, {"bsdf" : "kd"}, {"bsdf" : "ks"}, {"bsdf" : "normal"}]
        self.out_dir = None
class DataConfig(Config):
    def __init__(self):
        self.ref_mesh = None
        self.mtl_override = None
        self.pre_load = True
        self.train_res = [512,512]
class GeometryConfig(Config):
    def __init__(self):
        self.isosurface = "dmtet"
        self.dmtet_grid = 64
        self.mesh_scale = 2.1
        self.base_mesh = None

class OptimizationPassConfig(Config):
    def __init__(self):
        self.num_iter = 5000
        self.batch = 8
        self.warmup_iter = 100
        self.learning_rate = 0.01
        self.save_interval = 100
        self.display_interval = 0
        self.optimize_geometry = True
        self.optimize_material = True
        self.optimize_light = True

class MaterialConfig(Config):
    def __init__(self):
        self.layers = 1
        self.random_textures = True
        self.custom_mip = False
        self.texture_res = [1024, 1024]
        self.kd_min = [0.0, 0.0, 0.0, 0.0]
        self.kd_max = [1.0, 1.0, 1.0, 1.0]
        self.ks_min = [0.0, 0.08, 0.0]
        self.ks_max = [1.0, 1.0, 1.0]
        self.nrm_min = [-1.0, -1.0, 0.0]
        self.nrm_max = [1.0, 1.0, 1.0]

class CameraConfig(Config):
    def __init__(self):
        self.cam_near_far = [0.1, 1000.0]

class LightConfig(Config):
    def __init__(self):
        self.env_scale = 1.0
        self.envmap = None
        self.camera_space_light = False
        self.initial_light = "random"

class LossConfig(Config):
    def __init__(self):
        self.loss = "logl1"
        self.sdf_regularizer = 0.2
        self.sdf_consistency = 0.03
        self.laplace = "relative"
        self.laplace_weight = 0.1


class RunConfig(Config):
    def __init__(self):
        # Validate option
        self.validate = True

        # DataConfig
        self.ref_mesh = None
        self.mtl_override = None
        self.pre_load = True
        self.train_res = [512, 512]

        # GeometryConfig
        self.isosurface = "dmtet"
        self.dmtet_grid = 64
        self.mesh_scale = 2.1
        self.base_mesh = None

        # OptimizationPassConfig
        self.optimization_passes = [OptimizationPassConfig()]
        self.texture_optimization_passes = [OptimizationPassConfig()]

        # MaterialConfig
        self.layers = 1
        self.random_textures = True
        self.custom_mip = False
        self.texture_res = [1024, 1024]
        self.kd_min = [0.0, 0.0, 0.0, 0.0]
        self.kd_max = [1.0, 1.0, 1.0, 1.0]
        self.ks_min = [0.0, 0.08, 0.0]
        self.ks_max = [1.0, 1.0, 1.0]
        self.nrm_min = [-1.0, -1.0, 0.0]
        self.nrm_max = [1.0, 1.0, 1.0]

        # RenderConfig
        self.background = "checker"
        self.spp = 1
        self.display_res = [512, 512]

        # LoggingConfig
        self.log_interval = 100
        self.log_dir = 'logs'
        self.save_interval = 100
        self.display_interval = 0
        self.display = [{"latlong": True}, {"bsdf": "kd"}, {"bsdf": "ks"}, {"bsdf": "normal"}]
        self.out_dir = None

        # CameraConfig
        self.cam_near_far = [0.1, 1000.0]

        # LightConfig
        self.env_scale = 1.0
        self.envmap = None
        self.camera_space_light = False
        self.initial_light = "random"

        # LossConfig
        self.loss = "logl1"
        self.sdf_regularizer = 0.2
        self.sdf_consistency = 0.03
        self.laplace = "relative"
        self.laplace_weight = 0.1

        # GPUConfig
        self.local_rank = 0
        self.multi_gpu = False

