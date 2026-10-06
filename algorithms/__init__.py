from .fedavg import FedAvgTrainer
from .fedprox import FedProxTrainer
from .fedavgm import FedAvgMTrainer

TRAINER_REGISTRY = {
    "fedavg": FedAvgTrainer,
    "fedprox": FedProxTrainer,
    "fedavgm": FedAvgMTrainer,
}


def get_trainer(algorithm: str, **kwargs):
    try:
        trainer_cls = TRAINER_REGISTRY[algorithm]
    except KeyError:
        raise ValueError(
            f"Unknown algorithm '{algorithm}'. Available: {list(TRAINER_REGISTRY)}"
        )
    return trainer_cls(**kwargs)