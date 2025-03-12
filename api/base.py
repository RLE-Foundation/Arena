from abc import ABC, abstractmethod
from typing import Any

class BaseEvaluator(ABC):
    """
    Base class for all evaluators.

    Args:
        benchmark: str, the name of the benchmark
        version: str, the version of the benchmark
        environment: str, the environment of the benchmark
    """
    def __init__(self,
                 benchmark: str,
                 version: str,
                 environment: str,
                 ) -> None:
        super().__init__()
        self.benchmark = benchmark
        self.version = version
        self.environment = environment
        self.env = self.build(benchmark, version, environment)

    @abstractmethod
    def build(self, benchmark: str, version: str, environment: str) -> None:
        """
        Build the evaluation environment.
        """
        pass

    @abstractmethod
    def evaluate(self, model: Any) -> float:
        """
        Evaluate the model.
        """
        pass
    
    @abstractmethod
    def encrypt(self) -> Any:
        """
        Encrypt the evaluation result.
        """
        pass

    @abstractmethod
    def decrypt(self) -> Any:
        """
        Decrypt the evaluation result.
        """
        pass

    @abstractmethod
    def get_params_size(self) -> int:
        """
        Get the size of the model parameters.
        """
        pass
    
    
    