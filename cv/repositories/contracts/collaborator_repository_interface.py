from abc import ABC, abstractmethod
from typing import Dict, Union
from django.core.files.uploadedfile import UploadedFile


class CollaboratorRepositoryInterface(ABC):
    @abstractmethod
    def create(self, collaborator_data: Dict[str, Union[str, UploadedFile]]) -> 'Colaborador':
        """
        Cria um novo colaborador no repositório

        Args:
            collaborator_data: Dicionário contendo:
               - 'name': str
               - 'email': str
               - 'phone': str
               - 'curriculum': UploadedFile

        Returns:
           Instância do Colaborador criado
        """
        pass
