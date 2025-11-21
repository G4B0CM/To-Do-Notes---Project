'''Crea una nota nueva en la base de datos'''
#Esta es una implementacion simplificada para crear notas dentro del repositorio
class CreateNoteUseCase:
    def __init__(self, note_repository):
        self.note_repository = note_repository

    def execute(self, note_create):
        return self.note_repository.create_note(note_create)