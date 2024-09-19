from train import main
from configs.config import RunConfig

config = "configs/nerf_ship.json"
FLAGS = RunConfig.from_json(config)
main(FLAGS)