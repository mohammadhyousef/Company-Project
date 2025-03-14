from modeltranslation.translator import translator, TranslationOptions
from projects.models import Project

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Project, ProjectTranslationOptions)