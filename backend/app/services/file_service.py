"""
File Service
"""

from sqlalchemy.orm import Session

from app.models.file import File


class FileService:
    """
    File Service
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def update(
        self,
        file: File,
    ) -> File:
        """
        File 정보를 저장한다.
        """

        self.db.add(file)
        self.db.commit()
        self.db.refresh(file)

        return file

    def set_indexed(
        self,
        file: File,
        indexed: bool = True,
    ) -> File:
        """
        파일의 인덱싱 상태를 변경한다.
        """

        file.indexed = indexed

        return self.update(file)

    def delete(
        self,
        file: File,
    ) -> None:
        """
        파일을 삭제한다.
        """

        self.db.delete(file)
        self.db.commit()