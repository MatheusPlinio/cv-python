from cv.repositories.contracts.collaborator_repository_interface import CollaboratorRepositoryInterface
from django.core.files.uploadedfile import UploadedFile
from typing import Dict, Union
from cv.models import Collaborator


class CollaboratorRepository(CollaboratorRepositoryInterface):
    def validate_file_type(self, file: UploadedFile) -> bool:
        allowed_types = ['application/pdf',
                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
        return file.content_type in allowed_types

    def create_collaborator(
        self,
        name: str,
        phone: str,
        email: str,
        file: UploadedFile
    ) -> Dict[str, Union[str, bool]]:

        if not self.validate_file_type(file):
            return {'error': False, 'message': 'Invalid file type'}

        try:
            collaborator = Collaborator.objects.create(
                name=name,
                phone=phone,
                email=email,
                curriculum=file
            )

            return {'success': True, 'message': 'Collaborator created successfully'}

        except Exception as e:
            return {'error': False, 'message': str(e)}
