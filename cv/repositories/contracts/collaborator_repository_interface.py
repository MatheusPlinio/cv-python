from abc import ABC, abstractmethod
from typing import Dict, Union
from django.core.files.uploadedfile import UploadedFile


class CollaboratorRepositoryInterface(ABC):
    @abstractmethod
    def create_collaborator(
        self,
        name: str,
        phone: str,
        email: str,
        file: UploadedFile
    ) -> Dict[str, Union[str, bool]]:
        pass

    @abstractmethod
    def validate_file_type(self, file: UploadedFile) -> bool:
        pass